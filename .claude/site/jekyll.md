# The Jekyll Layer

Most of this site is hand-coded HTML served as-is. A thin Jekyll layer renders the two kinds of
content that are genuinely authored in Markdown:

- `blog/` and `_posts/` — the blog (currently empty, but live)
- `guides/*.md` — long-form reference documents shared across courses and the lab

GitHub Pages builds this automatically. **Do not migrate the hand-coded HTML pages into it** —
see the rule in `architecture.md`.

## Config

`_config.yml` is deliberately minimal: `markdown: kramdown`, a blog permalink pattern, the site
`url` (`https://cmdowney.io`), and an `exclude` list that keeps `vendor/`, `Gemfile`, and
`Gemfile.lock` out of the built site. Without that exclude, `bundle install --path vendor` causes
Jekyll to try to build every Markdown file inside the vendored gems.

## Guide Pages

A guide is a Markdown file with front matter:

```yaml
---
layout: guide
title: BlueHive Cluster Setup
subtitle: Getting started on the University of Rochester's computing cluster
permalink: /guides/cluster-setup/
---
```

The explicit `permalink` gives a clean URL; without it the page lands at
`/guides/cluster-setup.html`. Link to guides by permalink, relatively — from a course page that
is `../../../guides/cluster-setup/`.

`_layouts/guide.html` sets `layout: default`, renders the title/subtitle header, and appends a
small script that injects a **Copy** button into every `<pre>`. Styles live in `main.css`, all
scoped under `body.guide-page`.

### Table of Contents

Kramdown generates it server-side. Put this in the Markdown where the TOC should appear:

```markdown
* placeholder
{:toc}
```

It becomes a `<ul id="markdown-toc">` built from the headings, with no JavaScript. The literal
word "placeholder" is discarded — kramdown only needs a list item to attach to.

### Audience Callouts

Guides serve more than one reader (students in a course vs. lab members). The convention is
inline labelled boxes, always visible — not tabs, and not JS show/hide. Ctrl-F, printing, and
deep links all keep working, and nothing is hidden-but-present in the HTML, which matters because
the page is public regardless.

```html
<div class="audience for-lab" markdown="1">
<span class="audience-label">In the lab</span>

Body text, **with Markdown parsed normally** thanks to `markdown="1"`.
</div>
```

`for-course` is UR navy, `for-lab` is azure. Omitting `markdown="1"` leaves the body as literal
text — kramdown does not parse Markdown inside HTML blocks by default.

## Two Traps That Cost Real Time

**1. `body_class` in a layout is `layout.body_class`, not `page.body_class`.** `default.html`
resolves it with a fallback:

```liquid
{% assign body_class = page.body_class | default: layout.body_class %}
<body{% if body_class %} class="{{ body_class }}"{% endif %}>
```

Testing only `page.body_class` silently produced a bare `<body>`, which disabled every
`body.guide-page` rule in `main.css`. The page rendered fine structurally, so this was invisible
until the site was actually built and the output inspected.

**2. Kramdown wraps loose inline HTML in `<p>`.** The `<span class="audience-label">` inside a
callout comes out as `<p><span class="audience-label">…</span></p>`, so direct-child selectors
(`.audience > .audience-label`) miss it. Use descendant selectors for anything inside a
`markdown="1"` block.

The general lesson: **verify Jekyll changes by building and reading the generated HTML**, not by
reading the source. Both bugs above were invisible in the Markdown and the layout.

## Local Preview

Needed because a guide has no `file://` form — it only exists once built.

```bash
export PATH="/opt/homebrew/opt/ruby@3.3/bin:$PATH"
bundle exec jekyll serve --livereload
```

Serves at `http://localhost:4000`. `bundle config set --local path vendor/bundle` is already set;
`vendor/`, `.bundle/`, and `Gemfile.lock` are gitignored.

**Ruby version matters and the failure is confusing.** The `github-pages` gem requires
Ruby < 4.0 (its `commonmarker` dependency caps there), while Homebrew's `ruby` formula is now
4.x. On Ruby 4, Bundler silently resolves *backwards* to `github-pages 223` / Jekyll 3.9, whose
pinned Liquid 4.0.3 calls `String#tainted?` — removed in Ruby 3.2 — and the build dies with an
unrelated-looking `NoMethodError`. Install `ruby@3.3` and run under it; that resolves
`github-pages 232` / **Jekyll 3.10.0**, which is what GitHub Pages itself builds with, so local
output matches production.

Both Homebrew Rubies are keg-only, so `/usr/bin/ruby` is untouched and neither is on `PATH` by
default.

## Verifying a Build

```bash
bundle exec jekyll build

# body class actually applied
grep -o '<body[^>]*>' _site/guides/cluster-setup/index.html

# no unrendered Markdown leaked through
grep -c '```' _site/guides/cluster-setup/index.html      # expect 0
grep -c 'markdown="1"' _site/guides/cluster-setup/index.html  # expect 0
```

Also worth running a link check across the whole built site, resolving each local `href` against
`_site/` and accepting either the file or a directory containing `index.html`.
