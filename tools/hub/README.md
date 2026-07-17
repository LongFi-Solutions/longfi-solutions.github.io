# LongFi Documentation Hub (docs.longfisolutions.com)

This folder generates the branded, password-gated documentation hub at
**docs.longfisolutions.com** from the same Markdown that powers the public
MkDocs site (longfi-solutions.github.io). `build.py` reads `mkdocs.yml` and
`docs/**/*.md` and renders every page in the LongFi brief design.

Vercel builds this automatically: **every push to `main` re-runs the build and
redeploys.** There is nothing to run or upload by hand.

## Adding a new implementation guide

1. **Create the Markdown file**, e.g. `docs/deployment/aruba.md`. Follow the same
   structure as the existing guides: a single `# Title`, then `##` section
   headings. Put any screenshots in `docs/assets/images/` and reference them
   with `![](/assets/images/your-image.png)`.
2. **Add it to the nav** in `mkdocs.yml` under `Deployment Guides` (placeholder
   lines are already there — just uncomment the one you need):

   ```yaml
   - Deployment Guides:
       - UniFi: deployment/unifi.md
       - Omada: deployment/omada-networks.md
       - Meraki: deployment/meraki.md
       - Mist: deployment/mist.md
       - Aruba: deployment/aruba.md   # <- new
   ```
3. **Commit to `main`.** Both the public site and docs.longfisolutions.com
   rebuild on their own. The new guide appears in the top nav, the left
   sidebar, and the search index automatically.

Optional: add a bullet for it on the landing page (`docs/deployment/index.md`)
so it also shows in the "Available Guides" list.

## Editing existing content

Just edit the `.md` file and push to `main`. No other steps.

## Good to know

- **The nav entry (step 2) is required for the hub.** A `.md` file that isn't in
  `mkdocs.yml` will render on the public MkDocs site but **not** on the hub — the
  hub only builds pages listed in the nav (plus a section's `index.md` landing
  page, which it picks up automatically).
- **A malformed page won't take the site down.** If a new page can't be parsed,
  the Vercel build fails and docs.longfisolutions.com simply stays on the last
  good version until it's fixed.
- **The password gate is automatic** — it applies to every page, no per-page
  setup. (It is a courtesy screen, not real security; the same content is public
  on longfi-solutions.github.io, so don't put anything confidential behind it.)
- **Inter-guide links** use normal relative Markdown (e.g. `[Mist](mist.md)`);
  the build rewrites them to the correct hub URLs.

## Local preview (optional)

```bash
pip install markdown pyyaml
python tools/hub/build.py --docs-dir . --out hub_site
python -m http.server -d hub_site 8000
# open http://localhost:8000  (password: longficonnect)
```
