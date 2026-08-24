# Site Architecture

Personal academic website for C.M. Downey. Almost entirely hand-coded HTML with Bootstrap. A
thin Jekyll layer renders the blog and the Markdown guides under `guides/`; everything else is
static HTML with no build step. See `site/jekyll.md` for that layer.

Served by GitHub Pages from the `cmdowney88/cmdowney88.github.io` repository, at the custom
domain **cmdowney.io** (set by the `CNAME` file at the repo root). The old
`cmdowney88.github.io` address still resolves, via GitHub's redirect. Prefer relative links
internally; if an absolute URL is genuinely needed, use the custom domain.

## Design Approach

- Minimal complexity; prefer understanding the code over pulling in libraries
- Readability over elegance
- Only add features with clear value

## Stack

- HTML5, hand-coded
- Bootstrap 4.4.1 via CDN (always with SRI hashes)
- `main.css` for custom styles, on top of Bootstrap defaults
- JavaScript: Bootstrap's jQuery + scrollspy only
- No build process — edit files directly

## Layout

```
cmdowney88.github.io/
├── CNAME                       # custom domain for GitHub Pages (cmdowney.io)
├── index.html                  # homepage (single-page CV)
├── main.css                    # global styles, applies to every page
├── .gitattributes              # enforces LF line endings repo-wide
├── cv/                         # CV source and build (see the update-cv skill)
├── blog/
├── guides/                     # Markdown guides rendered by Jekyll (see site/jekyll.md)
├── _config.yml                 # Jekyll config
├── Gemfile                     # local preview only; GitHub Pages ignores it
├── _layouts/                   # Jekyll layouts: default, post, guide
└── teaching/
    ├── index.html              # complete course listing
    ├── dscc251/spring26/
    ├── ling250/spring25/, spring26/
    ├── ling282/fall24/, fall25/, fall26/
    └── uw_574/
```

## Page Types

**Homepage** (`index.html`) — single-page CV with smooth scrolling. Sections: About, Education,
Employment, Honors & Awards, Publications, Talks, Teaching, Service. Each is a `<section>` with
an `id`; uses `data-spy="scroll"` for Bootstrap scrollspy.

**Course pages** (`teaching/<course>/<term>/index.html`) — three sections: Information,
Policies, Schedule. Fixed navbar carrying the course title, "Home" link back to the main site,
`class="course-page"` on `<body>` for targeted styling. See `courses/conventions.md`.

**Course listing** (`teaching/index.html`) — minimal directory of every course site ever taught,
grouped by institution (UR, then UW), courses alphabetical by code, semesters newest-first.

**Guides** (`guides/*.md`) — long-form reference documents shared across courses and the lab,
authored in Markdown and rendered by Jekyll. See `site/jekyll.md`.

## Navigation

The homepage navbar dropdown links the **most recent offering of each UR course**, regardless of
whether that course is running in the current semester, plus a link to `/teaching/` for the full
list. Archived offerings are not in the dropdown.

## Colors

UR brand colors — source: https://brand.rochester.edu/visual-identity/color-system/

| Use | Value |
|---|---|
| Navbar background (site-wide) | `#00205b` |
| Links | `#0066FD` (Arpeggio Azure) |
| Link hover | `#003EFF` (Quantum Cobalt) |
| Body text | `#646464` |

`#00205b` is the *pre-rebrand* official navy. UR's current primary is `#001E5F`; the two are
indistinguishable in practice and the old value is kept deliberately. Don't "correct" it.

### Per-course navbar colors

Each course site carries its own navbar color for visual identity. The homepage,
`teaching/index.html`, and the guide layout stay navy — they are not any one course.

| Course | Color | Text | Resting link |
|---|---|---|---|
| LING 282/482 | `#00205b` navy | white (`navbar-dark`) | n/a (`navbar-dark`) |
| DSCC 251/451 | `#66A2FF` Connective Cornflower | navy (`navbar-light`) | `#123166` |
| LING 250/450 | `#FFE95F` Bright Lemon | navy (`navbar-light`) | `#2C4B85` (default) |

Set as an inline `style="background-color: …"` on the `<nav>`, never a Bootstrap `bg-*` class.

**A course's color applies to its archived offerings too**, so every term of a course looks like
that course. `ling250/spring25` and `ling282/fall24` were updated retroactively for this reason.
The only page still on Bootstrap's `bg-dark` is `uw_574`, a UW course that should not take UR
colors at all — leave it.

#### Choosing one

1. Pick from the UR system above. Check contrast against **white**.
2. **≥ 4.5:1** — keep `navbar-dark`. Nothing else to do; Bootstrap's white text is fine.
3. **< 4.5:1** — switch that `<nav>` to `navbar-light`. Bootstrap would then render near-black
   text, so `main.css` pins it to UR navy for `body.course-page .navbar-light`.
4. For a `navbar-light` bar, check `#2C4B85` (the default resting-link tint) against the new
   background. If it misses 4.5:1, darken it and set `--nav-ink-muted` inline next to
   `background-color`. Two custom properties drive the whole block: `--nav-ink` (brand,
   hover, scrollspy-active) and `--nav-ink-muted` (resting links, toggler).
5. Update the table above.

```python
def contrast(a, b):
    def lum(h):
        h = h.lstrip("#")
        c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
        c = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
        return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]
    hi, lo = max(lum(a), lum(b)), min(lum(a), lum(b))
    return (hi + 0.05) / (lo + 0.05)
```

#### Two traps

**Use solid navy tints, never navy at reduced alpha.** Translucent navy composites toward
whatever is behind it, and over a yellow navbar that lands on olive — `#00205b` at 65% over
`#FFD82B` is `#59604a`, which is not a navy at all. This applies to the toggler border and the
icon's SVG stroke too. The icon's stroke is baked into a data URI and cannot read a custom
property; it stays at the default tint, which is acceptable because a non-text UI component
needs only 3:1.

**A light or blue bar collapses the muted/active distinction, and that was accepted.** The
resting link must clear 4.5:1 against the bar, so the lighter the bar, the darker that tint has
to be — until it is indistinguishable from the brand. On Cornflower the usable tint is `#123166`,
only 1.22:1 from the `#00205b` brand, so brand, nav links, and the active-section highlight all
read as roughly one navy. **This is a known, accepted trade-off of choosing Cornflower, not a
bug.** Do not "fix" it by lightening the tint — that breaks contrast. The only real fix is a
darker bar.

The yellow UR accent was formerly reserved entirely for the UR2NLP lab site (`ur2nlp.github.io`,
a different repo; do not conflate the two). LING 250's Bright Lemon navbar now also uses it,
which was a deliberate call. It stays off the homepage.

## CSS Conventions

`main.css` applies to all pages:

```css
html { scroll-behavior: smooth; }
a { color: #0066FD; }
a:hover { color: #003EFF; }
section { scroll-margin-top: 80px; }   /* fixed-navbar overlap */
body.course-page section { padding-top: 40px; padding-bottom: 40px; }
body.course-page section:first-of-type { padding-top: 80px; }  /* navbar clearance */
```

Use `.itemTitle` as a **class**, never an id — it repeats ~70 times on the homepage, and
repeated ids are invalid HTML.

Scrolling is Bootstrap's native scrollspy plus CSS `scroll-behavior`. Custom jQuery scrolling
with easing was removed deliberately; don't reintroduce it.

## Paths

- Homepage links down: `href="teaching/ling282/fall26/index.html"`
- Course pages link up: `href="../../../main.css"`
- CDN assets: full URLs with SRI hashes

All internal links are relative — there are no absolute self-links to either domain.

Relative paths throughout, because HTML pages are sometimes opened directly by double-clicking
(`file://`) rather than served. **Jekyll-rendered pages are the exception** — they only exist
once built, so `guides/*.md` and anything linking *to* a guide's permalink require a served site.

## Line Endings

`.gitattributes` sets `* text=auto eol=lf` for the whole repo, with `.pdf`/`.png`/`.zip` marked
binary. All text files are LF. If a diff ever shows an entire file as rewritten, check whether
something reintroduced CRLF before committing.

## What Not to Change

1. **No alternating section backgrounds on the homepage** — explicitly rejected. (Course pages
   do use `bg-light` on the Policies section; that is intentional and separate.)
2. **No web fonts** — system/Bootstrap defaults preferred.
3. **No SEO/social meta tags** — considered and declined as low value.
4. **Don't convert the hand-coded pages to Jekyll.** The homepage and the course pages are
   hand-written HTML and stay that way. Jekyll exists here to render Markdown content that is
   genuinely authored in Markdown (the blog, the guides), and new Markdown content may use it —
   but that is not a reason to migrate the existing HTML. Don't propose it.
5. **Keep the yellow accent off the homepage** — it is LING 250's navbar color and the lab
   site's differentiator, not a general accent for this site.
6. **Never use `id` for repeated elements.**

## Git Workflow

See `.claude/git-workflow.md`.
