#!/usr/bin/env python3
"""
LongFi branded documentation hub generator.

Reads the docs repo's mkdocs.yml (nav, markdown_extensions, site_name) and
docs/**/*.md, renders every page in the LongFi *brief* design (indigo hero, gold
eyebrow, card sections, right-hand TOC), with a shared top nav, our own
client-side search, dark/light toggle, and a whole-site courtesy password gate.
Outputs a self-contained static site (assets self-hosted, not hotlinked).

Usage:  python tools/hub/build.py [--docs-dir .] [--out hub_site]
"""
import argparse, hashlib, html as htmllib, json, os, re, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_PASSWORD = "longficonnect"
GATE_SALT = "longfi-docs"

def die(m): print("ERROR: " + m, file=sys.stderr); sys.exit(1)
def warn(m): print("WARNING: " + m, file=sys.stderr)

def load_yaml(path):
    import yaml
    return yaml.safe_load(open(path, encoding="utf-8"))

def ext_config(mkdocs):
    exts, cfgs = [], {}
    for item in (mkdocs or {}).get("markdown_extensions", []) or []:
        if isinstance(item, str): exts.append(item)
        elif isinstance(item, dict):
            for k, v in item.items():
                exts.append(k)
                if isinstance(v, dict) and v: cfgs[k] = v
    for need in ("toc", "attr_list", "admonition", "tables"):
        if need not in exts: exts.append(need)
    return exts, cfgs

def strip_front_matter(t):
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", t, re.S)
    if not m: return t, {}
    try:
        import yaml; meta = yaml.safe_load(m.group(1)) or {}
    except Exception: meta = {}
    return t[m.end():], meta

def clean(inner): return re.sub(r'<a class="headerlink".*?</a>', '', inner, flags=re.S).strip()
def strip_hr(s): return re.sub(r'<hr\s*/?>', '', s)
def strip_tags(s): return re.sub(r'<[^>]+>', '', s)
def flatten(toks):
    for t in toks:
        yield t
        for c in flatten(t.get("children", [])): yield c

def demote(content, primary):
    shift = primary - 2
    if shift <= 0: return content
    for L in range(primary + 1, 7):
        content = content.replace('<h%d' % L, '<h%d' % (L - shift)).replace('</h%d>' % L, '</h%d>' % (L - shift))
    return content

def fill(template, mapping):
    pat = re.compile("|".join(re.escape(k) for k in sorted(mapping, key=len, reverse=True)))
    return pat.sub(lambda m: mapping[m.group(0)], template)

def url_and_out(mdpath):
    p = mdpath.replace("\\", "/")
    if p == "index.md": return "/", "index.html"
    if p.endswith("/index.md"): d = p[:-len("index.md")]; return "/" + d, d + "index.html"
    stem = p[:-3]
    return "/" + stem + "/", stem + "/index.html"

def rewrite_md_links(html, page_src):
    """Rewrite relative *.md links in rendered HTML to clean directory URLs.

    MkDocs resolves inter-page links relative to the current source file; the
    hub uses use_directory_urls, so a source link like ``deployment/index.md``
    must become ``/deployment/``. External (scheme:), absolute (/) and pure
    anchor (#) links are left untouched.
    """
    import posixpath
    base = posixpath.dirname(page_src.replace("\\", "/"))
    def repl(m):
        head, href, tail = m.group(1), m.group(2), m.group(3)
        if re.match(r'^(?:[a-z][a-z0-9+.\-]*:|#|//|/)', href, re.I):
            return m.group(0)
        path, sep, frag = href.partition("#")
        if not path.endswith(".md"):
            return m.group(0)
        target = posixpath.normpath(posixpath.join(base, path)) if base else path
        url, _ = url_and_out(target)
        return head + url + (sep + frag if sep else "") + tail
    return re.sub(r'(<a\b[^>]*?\shref=")([^"]+)("[^>]*>)', repl, html)

def render_markdown(md_text, extensions, configs):
    import markdown
    md = markdown.Markdown(extensions=extensions, extension_configs=configs)
    return md.convert(md_text), getattr(md, "toc_tokens", [])

def build_body(body, toc, fallback_title):
    """Return (hero_title, lead_html, article_html, toc_html, plain_text, headings_text)."""
    h1 = re.search(r'<h1[^>]*>(.*?)</h1>', body, re.S)
    if h1:
        hero_title = clean(h1.group(1)); after = body[h1.end():]
    else:
        hero_title = htmllib.escape(fallback_title); after = body

    levels = [t["level"] for t in flatten(toc) if t["level"] >= 2]
    if levels:
        primary = min(levels)
        ph = re.compile(r'<h%d\b' % primary)
        first = ph.search(after)
        lead = strip_hr(after[:first.start()]) if first else ""
        rest = after[first.start():] if first else ""
        sections = []
        for chunk in re.split(r'(?=<h%d\b)' % primary, rest):
            if not chunk.strip(): continue
            hm = re.search(r'<h%d\b[^>]*\sid="([^"]+)"[^>]*>(.*?)</h%d>' % (primary, primary), chunk, re.S)
            if not hm:
                die("could not parse an h%d heading near: %s" % (primary, chunk[:80]))
            sid, htext = hm.group(1), clean(hm.group(2))
            content = demote(strip_hr(chunk[hm.end():]), primary)
            sections.append((sid, htext, content))
        sec_ids = [s[0] for s in sections]
        prim_ids = [t["id"] for t in flatten(toc) if t["level"] == primary]
        if sec_ids != prim_ids:
            die("section/TOC mismatch: %s vs %s" % (sec_ids, prim_ids))
        article = "\n".join('<section class="card" id="%s"><h2 class="card-h">%s</h2>%s</section>' % s for s in sections)
        toc_lines = []
        for t in flatten(toc):
            if t["level"] == primary: toc_lines.append('<a href="#%s">%s</a>' % (t["id"], htmllib.escape(t["name"])))
            elif t["level"] == primary + 1: toc_lines.append('<a href="#%s" class="sub">%s</a>' % (t["id"], htmllib.escape(t["name"])))
        toc_html = ('<div class="toc-title">On this page</div>' + "".join(toc_lines)) if toc_lines else ""
    else:
        lead = ""
        article = '<section class="card">%s</section>' % strip_hr(after)
        toc_html = ""

    headings_text = " ".join(htmllib.unescape(t["name"]) for t in flatten(toc))
    plain = re.sub(r'\s+', ' ', htmllib.unescape(strip_tags(article))).strip()
    return hero_title, lead, article, toc_html, plain, headings_text

def add_link_targets(s):
    def repl(m):
        tag = m.group(0)
        return tag if "target=" in tag else tag[:-1] + ' target="_blank" rel="noopener noreferrer">'
    return re.sub(r'<a href="(?:https?://|mailto:)[^"]*"[^>]*>', repl, s)

def polish(s):
    s = s.replace('<img ', '<img loading="lazy" ')
    return add_link_targets(s)

def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--docs-dir", default=".")
    ap.add_argument("--out", default=os.path.join(HERE, "..", "..", "hub_site"))
    args = ap.parse_args(argv)

    docs = args.docs_dir
    mkdocs = load_yaml(os.path.join(docs, "mkdocs.yml"))
    site_name = mkdocs.get("site_name", "LongFi Solutions Documentation")
    extensions, configs = ext_config(mkdocs)
    expected = hashlib.sha256((GATE_SALT + ":" + DEFAULT_PASSWORD).encode()).hexdigest()
    template = open(os.path.join(HERE, "templates", "page.html"), encoding="utf-8").read()

    # ---- parse nav into sections ----
    import posixpath
    nav = mkdocs.get("nav") or []
    sections = []   # {label, url, pages:[{title,src,url,out}]}
    for entry in nav:
        (label, val), = entry.items()
        if isinstance(val, str):
            u, o = url_and_out(val)
            sections.append({"label": label, "url": u, "pages": [{"title": label, "src": val, "url": u, "out": o}]})
        elif isinstance(val, list):
            pages = []
            for child in val:
                (ctitle, cpath), = child.items()
                if not isinstance(cpath, str): continue
                u, o = url_and_out(cpath)
                pages.append({"title": ctitle, "src": cpath, "url": u, "out": o})
            if pages:
                # If the children share one directory and that directory has an
                # index.md on disk (a MkDocs section landing page that may be
                # omitted from nav), render it as the section's landing page so
                # /<dir>/ resolves instead of 404ing.
                child_dirs = {posixpath.dirname(p["src"].replace("\\", "/")) for p in pages}
                if len(child_dirs) == 1:
                    d = next(iter(child_dirs))
                    cand = (d + "/index.md") if d else "index.md"
                    have = any(p["src"].replace("\\", "/") == cand for p in pages)
                    if not have and os.path.exists(os.path.join(docs, "docs", cand)):
                        lu, lo = url_and_out(cand)
                        pages = [{"title": label, "src": cand, "url": lu, "out": lo}] + pages
                sections.append({"label": label, "url": pages[0]["url"], "pages": pages})

    # ---- top nav html ----
    def topnav_html(active_label):
        return "".join('<a href="%s"%s>%s</a>' % (s["url"], ' class="active"' if s["label"] == active_label else "", htmllib.escape(s["label"])) for s in sections)

    out = args.out
    if os.path.isdir(out): shutil.rmtree(out)
    os.makedirs(out, exist_ok=True)

    # ---- copy docs assets (self-host images/css) ----
    assets_src = os.path.join(docs, "docs", "assets")
    if os.path.isdir(assets_src):
        shutil.copytree(assets_src, os.path.join(out, "assets"))
    hub_out = os.path.join(out, "assets", "hub")
    os.makedirs(hub_out, exist_ok=True)
    for fn in ("hub.css", "search.js", "gate.js"):
        shutil.copyfile(os.path.join(HERE, "assets", fn), os.path.join(hub_out, fn))

    search_index = []
    count = 0
    for sec in sections:
        multi = len(sec["pages"]) > 1
        for page in sec["pages"]:
            src = os.path.join(docs, "docs", page["src"])
            if not os.path.exists(src): die("missing source: %s" % src)
            raw = open(src, encoding="utf-8").read()
            text, meta = strip_front_matter(raw)
            body, toc = render_markdown(text, extensions, configs)
            body = rewrite_md_links(body, page["src"])
            title = meta.get("title") or page["title"]
            hero_title, lead, article, toc_html, plain, headings = build_body(body, toc, title)

            eyebrow = "LongFi Connect Documentation" if sec["url"] == "/" else sec["label"]
            sidenav = ""
            if multi:
                links = "".join('<a href="%s"%s>%s</a>' % (p["url"], ' class="active"' if p["url"] == page["url"] else "", htmllib.escape(p["title"])) for p in sec["pages"])
                sidenav = '<nav class="sidenav" aria-label="%s"><div class="sidenav-title">%s</div>%s</nav>' % (htmllib.escape(sec["label"]), htmllib.escape(sec["label"]), links)

            html_out = fill(template, {
                "__PAGE_TITLE__": htmllib.escape("%s | %s" % (strip_tags(hero_title), site_name)),
                "__DESC__": htmllib.escape(mkdocs.get("site_description", site_name)),
                "__EXPECTED__": expected,
                "__TOPNAV__": topnav_html(sec["label"]),
                "__EYEBROW__": htmllib.escape(eyebrow),
                "__HERO_TITLE__": hero_title,
                "__HERO_LEAD__": lead,
                "__SIDENAV__": sidenav,
                "__TOC__": toc_html,
                "__ARTICLE__": article,
            })
            html_out = polish(html_out)
            dest = os.path.join(out, page["out"])
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            open(dest, "w", encoding="utf-8").write(html_out)
            search_index.append({"url": page["url"], "title": strip_tags(hero_title),
                                 "section": sec["label"], "headings": headings, "text": plain[:6000]})
            count += 1

    json.dump(search_index, open(os.path.join(hub_out, "search-index.json"), "w", encoding="utf-8"))
    open(os.path.join(out, "robots.txt"), "w").write("User-agent: *\nDisallow: /\n")
    print("Built %d pages -> %s" % (count, out))
    print("Sections: " + ", ".join(s["label"] for s in sections))

if __name__ == "__main__":
    main()
