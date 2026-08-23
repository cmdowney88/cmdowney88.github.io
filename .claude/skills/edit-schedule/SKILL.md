---
name: edit-schedule
description: Restructure a published course schedule — cancel a session, add or drop an in-class activity, shift content, move a deadline — while keeping quizzes, slot counts, and readings consistent
allowed-tools: Read, Glob, Grep, Edit, Write, Bash
---

# Edit Schedule

For changing a course schedule that already exists, mid-semester or while planning. Distinct from
`new-course-page`, which builds one from scratch, and from `publish-slides`, which only wraps a
Topics cell in a link.

Typical triggers: the instructor will be away, an activity is added or dropped, a milestone moves,
a topic needs more or less time.

## The Invariant That Actually Bites

**Content and its assessment move together.** Quizzes are keyed to material, not to dates. If a
lecture shifts one session later, a quiz that tested it may now fall *before* it is taught. This
is silent — the page still looks fine — and it is the single most common way an edit goes wrong.

After any content shift, re-derive every quiz label from what precedes it. LING 282 quizzes run at
the start of most Mondays and cover material through the previous week; check each one against the
rows above it.

The same applies to readings: they belong to the topic, so they move with it, not with the date.

## Steps

1. **Read the schedule first.** It is the **last** `<tbody>` in the file; earlier tables hold
   meeting times and staff. Dump it as text before changing anything — date, topic, events per
   row — so you can diff against it afterwards:

   ```bash
   python3 - <<'PY'
   import re
   h = open('teaching/<course>/<term>/index.html').read()
   tb = h[h.rfind('<tbody>'):].split('</tbody>')[0]
   for r in re.findall(r'<tr>(.*?)</tr>', tb, re.S):
       c = [re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',x)).strip()
            for x in re.findall(r'<td[^>]*>(.*?)</td>', r, re.S)]
       print(f"{c[0]:10} | {(c[1] if len(c)>1 else '')[:48]:48} | {c[-1][:56]}")
   PY
   ```

2. **Count the slots.** Teaching sessions = meeting dates − holidays − cancellations. Content rows
   + activity rows must equal that. Report the arithmetic to the user *before* editing:

   - Cancelling a session removes a slot; something must give.
   - Dropping an activity frees one.
   - These often cancel out. Say so rather than reshuffling more than necessary.

   Never silently pad or compress to make the numbers work.

3. **Apply the shift programmatically.** Rebuild the affected rows from a script rather than
   editing cells by hand — a shift touches every row in a range and hand-editing drifts. Extract
   the four `<td>` cells per row, reassign topics and readings, keep date cells in place, and
   decide events per row explicitly.

   Course pages are indented with **tabs**. Rebuild rows as
   `'<tr>\n' + ''.join('\t'*8 + cell + '\n' for cell in cells) + '\t'*7 + '</tr>'`.

4. **Re-derive the quizzes** as described above.

5. **Check deadlines for collisions.** Milestones fall on Fridays; homework is due on class days.
   A shift can move a topic onto a deadline row or strand a deadline on a cancelled day. Confirm
   no milestone shares a date with a homework due date unless the user wants that.

6. **Update the prose too.** Milestone dates, presentation dates, and the final writeup date
   usually appear in the Term Project section as well as the schedule. Grep for every date string
   you changed.

7. **Verify**: re-dump the schedule and compare against step 1; check tag balance with
   `html.parser`; confirm local `href`s resolve; confirm `grep -c 'slides/\|hw/'` has not changed
   unexpectedly.

## Row Forms

Regular session, holiday, cancellation, and activity:

```html
<td>Oct 21</td>
<td colspan="3" align="center">No class: instructor traveling</td>
```

```html
<td><em>In-class activity: peer-review workshop</em></td>
```

Cancellations use the same `colspan="3"` form as holidays. Activities are italicised and never
linked — `publish-slides` must not wrap them.

**Leave Topics cells as plain text** when the slides are unreleased. If a guide or reading needs
linking on that row, put it in the **Readings** column so the Topics cell stays available for
`publish-slides`.

## Reference

- Schedule conventions and the milestone sequence: `.claude/courses/conventions.md`
- Per-course meeting days, quiz cadence, and grading: `.claude/courses/<course>.md`
- Academic calendar retrieval (registrar PDFs need `pdftotext`, not WebFetch): the
  `new-course-page` skill
