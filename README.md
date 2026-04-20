# LongFi Solutions Documentation

Public documentation site for LongFi Solutions, built with MkDocs and the ReadTheDocs theme. Deployed automatically to https://longfi-solutions.github.io via GitHub Actions on every push to `main`.

---

## Editing Content

Content is edited via the Sveltia CMS admin panel at https://longfi-solutions.github.io/admin/ using a GitHub personal access token.

To generate a personal access token:
1. Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate a new token with the `repo` scope
3. Log in at the admin URL and paste the token when prompted

---

## Adding Images

1. Add image files to `docs/assets/images/`
2. Reference them in Markdown as `![description](/assets/images/filename.png)`

### Image Sizing

By default all images are constrained to the content column width. To control the size of a specific image, switch to **Markdown view** in the Sveltia editor and add a size class after the image reference:

```
![description](/assets/images/filename.png){ .img-sm }
```

| Class | Width |
|---|---|
| `.img-sm` | 25% — good for phone screenshots |
| `.img-md` | 50% — good for dashboard screenshots |
| `.img-lg` | 75% — good for wide diagrams |
| `.img-full` | 100% — full content width |

> **Note:** The Sveltia preview will show the raw `{ .img-sm }` text — this is expected. The class renders correctly on the live site.

---

## Adding New Pages

1. Create the page in Sveltia CMS or add a `.md` file to the appropriate folder under `docs/`
2. Add the page to the `nav:` section in `mkdocs.yml` so it appears in the sidebar

---

## Local Development

```bash
# Activate the Python virtual environment
source .venv/bin/activate

# Install dependencies (first time only)
pip install -r requirements.txt

# Live preview at http://127.0.0.1:8000
mkdocs serve
```

After editing locally, sync with any changes made via Sveltia:

```bash
git pull origin main
git push origin main
```
