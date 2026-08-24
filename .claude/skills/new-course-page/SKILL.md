---
name: new-course-page
description: Port a course website to a new semester — rebuild the schedule from the registrar's academic calendar, strip last year's slide and homework links, and register the new page
allowed-tools: Read, Glob, Grep, Edit, Write, WebFetch, Bash
---

# New Course Page

Creates `teaching/<course>/<term>/index.html` for an upcoming semester, based on the most
recent prior offering. The prose carries over nearly unchanged; **the schedule is rebuilt from
scratch** against the new academic calendar, and every slide/homework link is stripped so the
user can release materials as the semester goes.

Term directories are named `fall26`, `spring26` — lowercase season plus two-digit year.

## Steps

1. **Establish the target.** Confirm the course, the new term, and the source offering (almost
   always the most recent existing term directory for that course). If the user has not said,
   ask rather than guessing.

2. **Get the academic calendar.** The University of Rochester registrar publishes it at:

   ```
   https://www.rochester.edu/registrar/assets/pdf/university-of-rochester-YYYY-YYYY-sas-and-hajim-academic-calendar.pdf
   ```

   **WebFetch cannot read these** — it returns binary garbage and a fabricated apology. Download
   and extract the text instead:

   ```bash
   curl -sL "<calendar-url>" -o /tmp/cal.pdf && pdftotext -layout /tmp/cal.pdf -
   ```

   If the user supplied a URL, use theirs. Record verbatim: first day of classes, every holiday
   and recess, last day of class, reading days, and the final exam period.

3. **Enumerate the meeting slots.** Get the meeting days from the source page's info table
   (Mon/Wed, Tue/Thu, etc.). Generate every meeting date from the first day of classes through
   the last day of class, then subtract the holidays.

   Traps that have actually bitten:
   - **Recesses are not always symmetric.** Fall Break 2026 is Mon *and* Tue (Oct 12-13), so a
     Mon/Wed course loses only the Monday. Read the date range, don't assume one day.
   - **A recess spanning a weekend** (Thanksgiving, Nov 25-29) may knock out only one meeting.
   - **The first day of classes may not be a meeting day**, and some terms insert an oddity like
     Spring 2027's "Rochester Monday" on Fri Jan 22, where Monday classes meet on a Friday.
   - Verify your date arithmetic with `python3 -c` and the `datetime` module. Do not do it in
     your head; off-by-one-week errors are easy and embarrassing on a published syllabus.

4. **Reconcile slots against content.** Count the teaching sessions (meeting slots minus
   holidays) and count the content rows in the source schedule. Report the difference to the
   user before writing anything:

   - **More slots than content** — propose what fills the surplus (project activities, a review
     day, an extra presentation day). Do not silently pad.
   - **Fewer slots than content** — propose what to cut or merge. Do not silently compress.

   Note that the source schedule may contain rows for sessions that were cancelled or
   repurposed mid-semester. Those are not content and should not carry over.

5. **Create the directory with the HTML only.**

   ```bash
   mkdir -p teaching/<course>/<term>
   cp teaching/<course>/<source-term>/index.html teaching/<course>/<term>/index.html
   ```

   **Copy nothing else.** No `slides/`, no `hw/`, no `.DS_Store`. The user re-exports these
   deliberately, and stale assets from last year are worse than absent ones. Do not create empty
   `slides/` or `hw/` directories either — `publish-slides` creates them on first use.

6. **Update the prose sections.**
   - Year strings in `<title>` and the `navbar-brand`.
   - **The daylight saving date in the Late Work section**, if present. It is the first Sunday
     in November and changes every year. This is easy to miss because the surrounding sentence
     reads fine with the wrong date.
   - Office hours, meeting time, and location — ask; do not assume they carry over.
   - Any deadline named in the prose (final writeup, milestone dates).

7. **Rebuild the schedule `<tbody>`.** This is the last `<tbody>` in the file. Write it fresh
   rather than editing rows in place — the dates all shift, so in-place editing is more
   error-prone than regeneration. Generating it from a small Python script with a `row()` helper
   keeps the tab indentation consistent.

   Every Topics cell must be **plain text**, with no `<a href="slides/...">` or
   `href="hw/...">`. Readings links to external sites (JM chapters, papers, blog posts) DO carry
   over — those are stable URLs, not course assets. Homework release/due markers stay as text
   with bracketed due dates; only the `[pdf, tex]` links are removed.

   Verify with:
   ```bash
   grep -c 'slides/\|hw/' teaching/<course>/<term>/index.html   # must print 0
   ```

8. **Register the new page in three places.** All three, or the page is orphaned:

   | Location | Rule |
   |---|---|
   | `index.html` nav dropdown | Points at the **most recent** offering of each course, regardless of whether it is the current semester. Replace the old link. |
   | `index.html` Teaching section | Prepend a new `<li>` above the prior term. Semesters run newest-first. |
   | `teaching/index.html` | Prepend a new `<li>` above the prior term, under the right course heading. |

   All three files are plain LF, enforced by `.gitattributes` (`* text=auto eol=lf`), so
   ordinary text-mode edits are safe. If a diff ever shows an entire file as rewritten, check
   whether something reintroduced CRLF before committing.

9. **Verify.** Three checks:

   ```bash
   # a. no asset links survived
   grep -c 'slides/\|hw/' teaching/<course>/<term>/index.html

   # b. diffs are proportionate to the change
   git diff --stat

   # c. tag balance on every page touched
   ```

   For (b), a modified page showing its full line count as changed means something rewrote the
   file wholesale — investigate before committing. For (c), use `html.parser` and compare
   against the source page: the prior year's page may itself have pre-existing tag bugs, so a
   finding is only yours if the source page is clean.

   Also confirm every local `href` resolves (see the check in the `publish-slides` skill).

10. **Do not commit** unless asked. Report what was created, the session-count reconciliation
    from step 4, and anything you deliberately left for the user to decide.

## Term Projects

If the course uses milestone-based term projects, see `.claude/courses/conventions.md` for the
shared milestone sequence. Spread the milestones across the new calendar rather than copying the
prior year's spacing, and put the due dates in the schedule's Events column.

Milestone specs are authored fresh per term and released as the semester progresses — step 5's
"copy nothing else" covers them. But the obvious way to write a new term's M1 is to copy the
prior term's and edit it, and where those specs are **Jekyll guide pages** (LING 282 from Fall
2026 on) that carries a term-specific absolute `permalink`:

```yaml
permalink: /teaching/ling282/fall26/project/m1/
```

**Rewrite the permalink to the new term, or the new page silently replaces the old one at the
old term's URL.** Jekyll emits no warning on a duplicate permalink — the build succeeds, and the
later file wins. The prior term's published spec is simply gone, replaced by next year's content
at last year's address. This is verified behavior, not a theoretical risk.

Also update the `title`/`subtitle` if they name the term, and the due dates in the body.

Check for collisions across the whole site:

```bash
grep -rh '^permalink:' teaching --include='*.md' | sort | uniq -d   # must print nothing
```

## Reference

- Schedule tables are 4 columns: Date, Topics, Readings, Events.
- Holiday and no-class rows use `<td colspan="3" align="center">Label</td>` after the date cell.
- Course pages are indented with **tabs**; `index.html` and `teaching/index.html` use spaces.
- Per-course facts live in `.claude/courses/<course>.md`; shared page conventions in
  `.claude/courses/conventions.md`; site-wide HTML/CSS rules in `.claude/site/architecture.md`.
