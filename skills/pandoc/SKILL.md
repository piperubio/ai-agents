---
name: pandoc
description: Convert documents between 40+ formats using Pandoc. Prioritizes Docker via the pandoc/extra image (no local LaTeX required). Handles Markdown→PDF/DOCX/HTML/LaTeX, Beamer and reveal.js presentations, citations with BibTeX/CSL, Eisvogel template for polished PDFs, YAML frontmatter validation, and batch conversions. Use when user mentions pandoc, document conversion, PDF generation from Markdown, academic papers with citations, Word export, or slide presentations.
---

# Pandoc

Convert Markdown (and other formats) to PDF, DOCX, HTML, LaTeX, and 40+ others. **Always prefer Docker** over a local install to avoid LaTeX dependency hell.

## Docker Setup (Preferred)

The `pandoc/extra` image bundles pandoc + LaTeX (Tectonic) + Eisvogel template + Lua filters + open-source fonts. No local LaTeX required.

```bash
# One-shot conversion (run from the document directory)
docker run --rm \
  --volume "$(pwd):/data" \
  --user $(id -u):$(id -g) \
  pandoc/extra input.md -o output.pdf

# Convenient shell alias (add to ~/.bashrc or ~/.zshrc)
alias pandock='docker run --rm -v "$(pwd):/data" -u $(id -u):$(id -g) pandoc/extra'

# Then use as a drop-in replacement for pandoc
pandock input.md -o output.pdf --template eisvogel
```

> **Windows note:** Replace `$(id -u):$(id -g)` with your UID or omit `--user` on Windows.

## Core Conversion Patterns

### PDF (recommended defaults)
```bash
# Plain PDF
pandock document.md -o document.pdf

# With TOC + numbered sections (most documents)
pandock document.md -o document.pdf --toc --number-sections

# Unicode / custom fonts → use XeLaTeX
pandock document.md -o document.pdf --pdf-engine=xelatex

# Academic paper with citations
pandock paper.md -o paper.pdf \
  --pdf-engine=pdflatex \
  --citeproc \
  --number-sections \
  --toc
```

### DOCX (Word)
```bash
pandock document.md -o document.docx
pandock document.md -o document.docx --reference-doc=template.docx
```

### HTML
```bash
pandock document.md -o document.html --standalone --toc
pandock document.md -o document.html --standalone --self-contained  # embed all resources
```

### Presentations
```bash
# Beamer (PDF slides)
pandock slides.md -o slides.pdf --to beamer

# reveal.js (web slides)
pandock slides.md -o slides.html --to revealjs --standalone -V theme=black
```

## Eisvogel Template (Polished PDFs)

Eisvogel is already in `pandoc/extra` — no install needed with Docker.

```bash
pandock document.md -o document.pdf \
  --template eisvogel \
  --syntax-highlighting idiomatic
```

Minimal YAML frontmatter for Eisvogel:
```yaml
---
title: "Document Title"
author: [Author Name]
date: "2026-01-01"
titlepage: true
titlepage-color: "1E4B7A"
titlepage-text-color: "FFFFFF"
toc: true
toc-own-page: true
---
```

See `references/eisvogel.md` for the full list of Eisvogel variables.

## Citations (BibTeX / CSL)

1. Add to YAML frontmatter:
   ```yaml
   bibliography: references.bib
   csl: assets/csl/apa.csl   # or harvard.csl / ieee.csl
   link-citations: true
   ```

2. Cite in text: `[@citekey]` (parenthetical) or `@citekey` (in-text).

3. Add `# References` section at the end, or use `:::{#refs}:::`.

4. Convert with `--citeproc`:
   ```bash
   pandock paper.md -o paper.pdf --citeproc --number-sections
   ```

Bundled CSL files: `assets/csl/apa.csl`, `assets/csl/harvard.csl`, `assets/csl/ieee.csl`.

## Validation

Run the bundled validation script before converting to catch YAML and dependency errors early:

```bash
python3 scripts/validate.py document.md
```

## Defaults Files (Avoiding Long Commands)

For repeatable builds, define a `defaults.yaml`:

```yaml
from: markdown
to: pdf
pdf-engine: pdflatex
citeproc: true
number-sections: true
toc: true
metadata:
  fontsize: 12pt
  geometry: margin=1in
```

```bash
pandock document.md --defaults=defaults.yaml -o output.pdf
```

Starter defaults files are in `assets/templates/`.

## Batch Conversion

```bash
# Convert all .md files in a directory to PDF
for f in *.md; do
  pandock "$f" -o "${f%.md}.pdf" --pdf-engine=pdflatex
done
```

## Local Install (Fallback)

Use only when Docker is unavailable.

```bash
# macOS
brew install pandoc && brew install --cask mactex

# Ubuntu/Debian
sudo apt-get install pandoc texlive-xetex texlive-fonts-recommended texlive-latex-extra

# Windows (Chocolatey)
choco install pandoc miktex
```

Minimum: Pandoc ≥ 2.19 (3.x recommended) + a LaTeX distribution for PDF output.

## Bundled Resources

| Resource | Purpose |
|---|---|
| `scripts/validate.py` | Validates YAML frontmatter and checks bibliography/image dependencies |
| `assets/templates/` | Starter YAML defaults for academic, thesis, article, beamer, revealjs |
| `assets/csl/` | APA, Harvard, IEEE citation styles |

## Reference Files

Load these when you need detailed information:

- **`references/conversion_guide.md`** — Format-specific commands and advanced options (filters, resource paths, metadata overrides, batch patterns)
- **`references/yaml_reference.md`** — Complete YAML frontmatter variable reference (all PDF, HTML, DOCX settings)
- **`references/templates_guide.md`** — How to use and customize each bundled template
- **`references/eisvogel.md`** — All Eisvogel template variables and custom title-page options
- **`references/docker.md`** — Docker image variants (`pandoc/core`, `pandoc/latex`, `pandoc/extra`), tagging, and CI/CD usage
- **`references/troubleshooting.md`** — Common errors with fixes (YAML syntax, missing LaTeX packages, fonts, images, Unicode)
- **`references/snippets.md`** — Copy-paste commands for common workflows
