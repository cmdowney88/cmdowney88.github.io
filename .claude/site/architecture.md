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
| Navbar background | `#00205b` |
| Links | `#0066FD` (Arpeggio Azure) |
| Link hover | `#003EFF` (Quantum Cobalt) |
| Body text | `#646464` |

The yellow UR accent is deliberately unused here — reserved for visual differentiation of the
separate UR2NLP lab site (`ur2nlp.github.io`, a different repo; do not conflate the two).

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
5. **Keep the yellow accent out** — reserved for the lab site.
6. **Never use `id` for repeated elements.**

## Git Workflow

See `.claude/git-workflow.md`.
