---
name: publish-slides
description: Detect new slide PDFs via git, link them in the course schedule HTML, and commit
allowed-tools: Read, Glob, Grep, Edit, Bash
---

# Publish Slides

After the user has produced a slide PDF — exported from Keynote, or generated from a markdown
source as in DSCC 251 — and placed it in a course's `slides/` directory, this skill detects
which PDFs are new, links them in that course's schedule HTML, and commits.

The course and semester are **never hardcoded** — git tells you which they are. A PDF that is
untracked or modified is by definition the one being published, and its path names the course
and term.

## Steps

1. **Detect new slides.** From the repo root:

   ```bash
   git status --porcelain -- 'teaching/*/*/slides/*.pdf'
   ```

   Each result line is `XY path`, where `??` means untracked (a brand-new deck) and ` M` means
   modified (a re-export of a deck already published). Both count.

   - If there are no results, tell the user there are no new slides and stop.
   - Parse each path as `teaching/<course>/<term>/slides/<file>.pdf`. That gives you the course
     directory and the schedule file at `teaching/<course>/<term>/index.html`.
   - If results span multiple courses or terms, group them and handle each group separately.
     Do not assume they all belong to one course.

2. **Extract lecture info from the filename.** Slide filenames usually follow `N_topic.pdf`
   (e.g. `10_transfer_learning.pdf`). The number prefix indicates ordering, which helps you
   locate the right row, but **do not trust it as a row index** — lecture numbers skip, and
   holidays and activity days occupy rows without consuming a number.

   Some decks have no number (e.g. `pytorch.pdf`, `overview.pdf`). For these, match on topic
   text alone.

3. **Read the schedule HTML** at `teaching/<course>/<term>/index.html`. The schedule is the
   **last** `<tbody>` in the file — earlier tables hold meeting times and teaching staff. Find
   the row whose Topics cell matches this lecture. It will be plain text, not yet wrapped in an
   `<a>`.

   - If the topic is already inside an `<a>`, the deck appears to be published already. Ask
     whether to re-link before changing anything.
   - If no row plausibly matches, stop and ask rather than guessing. A wrong row is worse than
     no link.

4. **Replace plain text with a link.** Change the Topics cell content to:

   ```html
   <a href="slides/FILENAME.pdf" target="_blank">Topic Title</a>
   ```

   Preserve existing `<br>` tags and multi-line topic text — a single row often lists two
   topics, and only one of them may be the deck you're publishing. Match the surrounding
   indentation, which is **tabs** in these files.

5. **Handle any additional changes** the user mentioned (schedule adjustments, reading links,
   date changes).

6. **Verify before committing.** Two cheap checks that catch the failure modes that actually
   occur:

   ```bash
   # every local href in the page resolves to a real file
   python3 - "teaching/<course>/<term>/index.html" <<'PY'
   import os, re, sys
   page = sys.argv[1]; base = os.path.dirname(page)
   for href in re.findall(r'href="([^"#][^":]*?)"', open(page, encoding="utf-8").read()):
       target = os.path.normpath(os.path.join(base, href))
       if not os.path.exists(target):
           print("MISSING:", href)
   PY
   ```

   Then confirm the diff is as small as it should be:

   ```bash
   git diff --stat -- teaching/<course>/<term>/index.html
   ```

   A one- or two-line change per deck is expected. A full-file diff means something rewrote the
   whole file — investigate before committing.

7. **Commit.** Stage the new PDF(s) and the modified HTML:

   ```
   <coursecode>: add lecture N slides
   ```

   For multiple lectures: `dscc251: add lecture 10, 11 slides`. If there were additional
   changes, reflect them in the message. Do NOT push — the user handles that.

## HTML Patterns Reference

**Lecture with slides linked:**
```html
<td>
	<a href="slides/7_self-supervised.pdf" target="_blank">Self-supervised Learning</a>
</td>
```

**Lecture without slides (what you're replacing):**
```html
<td>Transfer learning</td>
```

**Two topics in one row** — link only the one you are publishing:
```html
<td>
	<a href="slides/8_ffnn-lm.pdf" target="_blank">Feed-forward Language Models</a>
	<br>Recurrent Neural Networks
</td>
```

**Student discussion, holidays, in-class activities (do NOT modify these):**
```html
<td><em>Student-led discussion: Transfer learning</em></td>
<td colspan="3" align="center">Fall Break: no class</td>
```

## Course-Specific Notes

- Schedule tables are 4 columns everywhere: Date, Topics, Readings, Events. The Topics header
  is titled slightly differently per course ("Topics", "Topics + Slides") — match on position,
  not on the header text.
- Lecture numbers may skip (e.g. no lecture 4). This is intentional, not a mistake to correct.
- **ling250** does not use local slide PDFs. Its Topics cells link out to notebooks in the
  `cmdowney88/ling250-materials` GitHub repo. If a PDF shows up under `teaching/ling250/*/slides/`,
  confirm with the user how they want it linked instead of assuming the local-PDF pattern.
- A course's `slides/` directory may not exist yet in a newly created term (see the
  `new-course-page` skill, which deliberately does not create one). Create it when the first
  deck is published.
