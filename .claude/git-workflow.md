# Git Workflow

- Conceptually distinct changes go in separate commits
- Commit messages: concise but informative
- No AI co-authorship footer — commits are authored by the user
- **Never push**; the user handles that
- `.gitattributes` sets `* text=auto eol=lf`. If a diff shows a whole file rewritten, check for
  reintroduced CRLF before committing — writing files with Python `read_text`/`write_text` is a
  common cause

## Splitting Overlapping Edits Into Topical Commits

A session often edits one file several times for unrelated reasons. Hunk-level staging
(`git apply --cached`) fails here, because a single diff hunk routinely straddles two topics — a
list where one edit changed the dates and another added links, for instance.

The reliable method is to **replay the edits from the HEAD version in topical order**:

1. Copy the current file aside as `final`, and `git show HEAD:<path> > base`
2. In one script, start from `base` and apply the edits grouped by topic, snapshotting the file
   after each group
3. **Assert the last snapshot is byte-identical to `final`** — this is the whole safety
   guarantee; without it the commits may not sum to the work you actually did
4. Copy each snapshot over the real file in order, `git add` the specific paths, commit

Use exact-match string replacement with `assert h.count(old) == 1` for every edit, so a
non-matching or ambiguous pattern fails loudly instead of silently doing nothing.

## Traps

**`git rm` stages the deletion immediately.** A later `git commit` — even one where you carefully
`git add` only certain paths — sweeps that staged deletion into whatever commit comes next. If a
deletion belongs to a specific commit, either run `git rm` at that point in the sequence, or
delete the file and stage it with `git add -A <path>` when its turn arrives.

Relatedly, `git add <path>` **fails** on an already-deleted file (`pathspec did not match`), so a
script that assumes it will work stops in the middle. Print the staged file list before each
commit as a check:

```bash
git diff --cached --name-only
```

Nothing here is pushed automatically, so a bad sequence is always recoverable with
`git reset --mixed <sha>` followed by redoing the commits.
