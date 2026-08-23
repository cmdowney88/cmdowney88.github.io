---
name: update-cv
description: After cv_data.yaml changes, rebuild the PDF and sync content outward to the personal website and lab site
allowed-tools: Read, Glob, Grep, Edit, Bash
---

# Update CV

After the user has edited `cv/cv_data.yaml`, this skill propagates changes outward: rebuild the PDF, update the personal website HTML, and sync relevant items to the lab website.

## Steps

1. **Identify what changed.** Run `git diff cv/cv_data.yaml` to see what was added or modified. Summarize the changes to the user.

2. **Rebuild the CV PDF.**
   ```bash
   cd cv/ && python build_cv.py && pdflatex cv_generated.tex
   ```
   Run pdflatex twice if there are citation/reference warnings. Report any build errors and stop.

3. **Update `index.html` if appropriate.** Check whether the YAML changes should appear on the personal website. Not everything does — the website intentionally shows fewer items than the PDF.

   Present the new/changed items and ask the user which (if any) should go on the website. When adding:
   - Publications: flat list, no year headers
   - Talk dates: month+year only (no day)
   - Match the existing HTML patterns in each section

4. **Sync to the lab website if appropriate.** Check whether any changes belong on the lab site at `~/ur2nlp.github.io/_data/`. Items appropriate for the lab site are a subset — typically:
   - Publications involving the lab (by the user or their students)
   - News items about the lab (paper acceptances, awards, grants)

   Present candidates and ask the user which to sync. When adding, write to the corresponding YAML data file (`publications.yml`, `news.yml`) following its existing format.

   Also flag any discrepancies found in the other direction (e.g., author order or venue name differences between the two sites).

5. **Commit if changes were made.** Stage changed files in this repo and commit with a descriptive message. If lab site files were changed, note that the user will need to commit and push separately in that repo. Do NOT push either repo.

## Architecture Reference

- **`cv/cv_data.yaml`** is the single source of truth for all CV content.
- **`cv/build_cv.py`** generates LaTeX (`cv_generated.tex`), compiled with `pdflatex`.
- **`index.html`** is maintained by hand — it is *not* generated from the YAML. The website
  intentionally shows fewer items than the PDF (less service, no dissertation).
- The CV PDF is linked from the homepage navbar as `cv/cv_generated.pdf`.

### Build Commands

```bash
cd cv/
python build_cv.py                                     # default: exclude internal-informal, archive
python build_cv.py --exclude-tags internal-informal archive undergrad
python build_cv.py --exclude-tags none                 # include everything
pdflatex cv_generated.tex
```

### Tag System

Items in the YAML may carry a `tags` list controlling filtering:

| Tag | Meaning | Default |
|---|---|---|
| `undergrad` | Undergraduate-era items | included |
| `internal-informal` | Lab meetings, reading groups, retreats | excluded |
| `internal-formal` | Department/university committees, internal grants | included |
| `archive` | No longer very relevant, worth keeping on record | excluded |

### LaTeX Template

Libertinus font. Section headers are small-caps with a rule underneath, colored via
`\sectioncolor`. Teaching uses a semester-grouped tabular layout (date left, courses right);
every other section uses `cvlist` (enumitem description list). `etoolbox` prevents page breaks
within `cvlist` items. Invited talks are auto-sorted most-recent-first, handling multi-instance
talks.

### Website vs PDF

- Website publications are a flat list with no year headers (avoids highlighting gaps)
- Website talk dates use month + year only
- "Supervised by" info is omitted from both
- `#publications li` carries extra margin in `main.css`

### Known Issues

- Author order on "Learning to Translate by Learning to Communicate" differs between the website
  and the LaTeX — check the ACL Anthology for the canonical order.
- Service dates in the generated CV render raw YAML strings (e.g. "2020 - 2021") rather than
  en-dash form.
