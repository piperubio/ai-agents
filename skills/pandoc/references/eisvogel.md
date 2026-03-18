# Eisvogel Template Reference

Eisvogel is a clean pandoc LaTeX template designed for lecture notes, technical documents, and academic papers. It is **bundled in the `pandoc/extra` Docker image** — no separate install is needed when using Docker.

## Table of Contents
1. [Quick Start](#1-quick-start)
2. [Installation (local)](#2-installation-local)
3. [Custom Variables](#3-custom-variables)
4. [Usage Examples](#4-usage-examples)
5. [Required LaTeX Packages (local)](#5-required-latex-packages-local)
6. [Common Errors](#6-common-errors)

---

## 1. Quick Start

```bash
# Via Docker (no install needed)
pandock document.md -o document.pdf \
  --template eisvogel \
  --syntax-highlighting idiomatic

# Minimal frontmatter
```yaml
---
title: "My Document"
author: [Author Name]
date: "2026-01-01"
titlepage: true
toc: true
---
```

---

## 2. Installation (local)

1. Download `eisvogel.latex` from the [release page](https://github.com/Wandmalfarbe/pandoc-latex-template/releases/latest).
2. Place in your pandoc templates folder:
   - **macOS/Linux:** `~/.local/share/pandoc/templates/` or `~/.pandoc/templates/`
   - **Windows:** `C:\Users\USERNAME\AppData\Roaming\pandoc\templates\`

---

## 3. Custom Variables

### Title Page

| Variable | Default | Description |
|---|---|---|
| `titlepage` | `false` | Show title page |
| `titlepage-color` | — | Title page background (HTML hex, e.g. `1E4B7A`) |
| `titlepage-text-color` | `5F5F5F` | Title page text color |
| `titlepage-rule-color` | `435488` | Top rule color |
| `titlepage-rule-height` | `4` | Top rule height (points) |
| `titlepage-logo` | — | Path to logo image (relative to execution dir) |
| `titlepage-background` | — | Path to full-page background image |

> **Underscore in filenames:** If the logo or background path contains `_`, wrap it: `` titlepage-background: "`bg_image.pdf`{=latex}" ``

### Page Layout

| Variable | Default | Description |
|---|---|---|
| `page-background` | — | Background image for all pages |
| `page-background-opacity` | `0.2` | Background image opacity |
| `toc-own-page` | `false` | Start new page after TOC |
| `book` | `false` | Book typesetting (chapters, two-sided) |
| `first-chapter` | `1` | Starting chapter number |

### Headers & Footers

| Variable | Default | Description |
|---|---|---|
| `disable-header-and-footer` | `false` | Disable on all pages |
| `header-left` | title | Left header text |
| `header-center` | — | Center header text |
| `header-right` | date | Right header text |
| `footer-left` | author | Left footer text |
| `footer-center` | — | Center footer text |
| `footer-right` | page number | Right footer text |

### Typography

| Variable | Default | Description |
|---|---|---|
| `logo-width` | `35mm` | Logo width (TeX unit required, e.g. `50mm`) |
| `code-block-font-size` | `\small` | Font size for code blocks (`\tiny` … `\Huge`) |
| `caption-justification` | `raggedright` | Caption alignment |
| `footnotes-pretty` | `false` | Prettier footnote formatting |
| `footnotes-disable-backlinks` | `false` | Disable footnote backlinks |

### Tables & Figures

| Variable | Default | Description |
|---|---|---|
| `table-use-row-colors` | `false` | Alternate row colors |
| `float-placement-figure` | `H` | Figure float placement (`h`, `t`, `b`, `p`, `H`) |
| `listings-disable-line-numbers` | `false` | No line numbers in listings |
| `listings-no-page-break` | `false` | Prevent page breaks inside listings |

### Other

| Variable | Default | Description |
|---|---|---|
| `watermark` | — | Watermark text on every page |

---

## 4. Usage Examples

### Numbered Sections
```bash
pandock document.md -o document.pdf --template eisvogel --number-sections
```

### Syntax Highlighting
```bash
# With listings (matches Eisvogel style)
pandock document.md -o document.pdf --template eisvogel --syntax-highlighting idiomatic

# Without listings
pandock document.md -o document.pdf --template eisvogel --syntax-highlighting tango
# Other styles: pygments | kate | espresso | zenburn | haddock | breezedark
```

### Book Typesetting
```bash
pandock book.md -o book.pdf \
  --template eisvogel \
  --top-level-division=chapter \
  -V book=true \
  -V classoption=oneside  # omit for two-sided (print)
```

### Different Language
```bash
pandock document.md -o document.pdf --template eisvogel -V lang=de
```

### Standalone LaTeX (for manual compilation)
```bash
pandock document.md -o document.tex --template eisvogel
```

### Full Academic Paper Frontmatter
```yaml
---
title: "Research Paper Title"
author: [Author Name, Second Author]
date: "February 2026"
lang: en-GB
titlepage: true
titlepage-color: "1E3A5F"
titlepage-text-color: "FFFFFF"
titlepage-rule-color: "CCCCCC"
titlepage-rule-height: 2
titlepage-logo: "logo.png"
logo-width: 40mm
toc: true
toc-own-page: true
toc-depth: 3
numbersections: true
header-left: "Research Paper"
header-right: "2026"
footer-center: "Confidential"
footnotes-pretty: true
bibliography: references.bib
csl: assets/csl/apa.csl
link-citations: true
---
```

---

## 5. Required LaTeX Packages (local)

With Docker (`pandoc/extra`) all packages are pre-installed.

For a local setup with a minimal texlive bundle (`texlive-latex-extra`), install missing packages via tlmgr:

```bash
tlmgr install soul adjustbox babel-german background bidi collectbox csquotes \
  everypage filehook footmisc footnotebackref framed fvextra letltxmacro ly1 \
  mdframed mweights needspace pagecolor sourcecodepro sourcesanspro titling \
  ucharcat unicode-math upquote xecjk xurl zref draftwatermark
```

For a complete install (simpler):
```bash
# Ubuntu/Debian
sudo apt-get install texlive-full

# macOS
brew install --cask mactex
```

---

## 6. Common Errors

### `Missing endcsname` / `File not found` with logo/background containing underscores

Fix: escape the path as LaTeX literal:
```yaml
titlepage-background: "`background_image.pdf`{=latex}"
logo: "`company_logo.png`{=latex}"
```

### `Missing \begin{document}`
You are using the wrong file as the template. Download the `.latex` file (not `.md`) from the [releases page](https://github.com/Wandmalfarbe/pandoc-latex-template/releases/latest).

### `auto expansion is only possible with scalable fonts` (MiKTeX/Windows)
Run `updmap.exe` from `C:\Program Files\MiKTeX\miktex\bin\x64\`.

### `cannot find image file`
Check all image paths are correct and relative to the directory where pandoc is run. Avoid spaces in filenames.
