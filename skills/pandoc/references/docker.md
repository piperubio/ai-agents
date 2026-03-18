# Pandoc Docker Reference

The official `pandoc/extra` image is the recommended way to run Pandoc — it bundles LaTeX, the Eisvogel template, Lua filters, and open-source fonts, so you avoid managing a TeX distribution locally.

## Table of Contents
1. [Available Images](#1-available-images)
2. [Quick Usage](#2-quick-usage)
3. [Shell Alias](#3-shell-alias)
4. [Stacks (OS variants)](#4-stacks-os-variants)
5. [CI/CD Integration](#5-cicd-integration)
6. [Bundled Components](#6-bundled-components)
7. [Custom Dockerfile](#7-custom-dockerfile)

---

## 1. Available Images

| Image | Contents | When to use |
|---|---|---|
| `pandoc/core` | Pandoc only | Markdown↔HTML/DOCX/TeX, no PDF |
| `pandoc/latex` | Pandoc + TeX Live (BasicTeX) | PDF output, minimal footprint |
| `pandoc/extra` | Pandoc + LaTeX + Eisvogel + filters + fonts | Polished PDFs, presentations, citations |

All images are on [Docker Hub](https://hub.docker.com/r/pandoc/extra).

### Tags

```bash
pandoc/extra          # latest stable
pandoc/extra:3        # major version pinned
pandoc/extra:3.6      # minor version pinned
pandoc/extra:latest-ubuntu   # Ubuntu-based
pandoc/extra:latest-alpine   # Alpine-based (default, smaller)
```

---

## 2. Quick Usage

```bash
# Basic PDF conversion (run from document directory)
docker run --rm \
  --volume "$(pwd):/data" \
  --user $(id -u):$(id -g) \
  pandoc/extra input.md -o output.pdf

# PDF with Eisvogel template
docker run --rm \
  --volume "$(pwd):/data" \
  --user $(id -u):$(id -g) \
  pandoc/extra input.md -o output.pdf \
    --template eisvogel \
    --syntax-highlighting idiomatic

# DOCX
docker run --rm \
  --volume "$(pwd):/data" \
  --user $(id -u):$(id -g) \
  pandoc/extra input.md -o output.docx

# Beamer presentation
docker run --rm \
  --volume "$(pwd):/data" \
  --user $(id -u):$(id -g) \
  pandoc/extra slides.md -o slides.pdf --to beamer
```

> **Windows:** Omit `--user $(id -u):$(id -g)` or replace with your UID. In PowerShell use `${PWD}` instead of `$(pwd)`.

---

## 3. Shell Alias

Add to `~/.bashrc` or `~/.zshrc` for a drop-in `pandoc` replacement:

```bash
alias pandock='docker run --rm -v "$(pwd):/data" -u $(id -u):$(id -g) pandoc/extra'
```

Usage:
```bash
pandock input.md -o output.pdf --template eisvogel
pandock --version
pandock --list-highlight-styles
```

---

## 4. Stacks (OS variants)

All images support Alpine and Ubuntu stacks:

```bash
pandoc/extra:latest           # Alpine (default, ~smaller)
pandoc/extra:latest-alpine    # explicitly Alpine
pandoc/extra:latest-ubuntu    # Ubuntu (larger, more compatible)
```

---

## 5. CI/CD Integration

### GitHub Actions

```yaml
# .github/workflows/build-docs.yml
name: Build PDF

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    container:
      image: pandoc/extra:latest

    steps:
      - uses: actions/checkout@v4

      - name: Build PDF
        run: |
          pandoc docs/report.md -o output/report.pdf \
            --template eisvogel \
            --citeproc \
            --number-sections \
            --toc

      - uses: actions/upload-artifact@v4
        with:
          name: report
          path: output/report.pdf
```

### GitLab CI

```yaml
build-docs:
  image: pandoc/extra:latest
  script:
    - pandoc docs/report.md -o output/report.pdf --template eisvogel --toc
  artifacts:
    paths:
      - output/report.pdf
```

### Makefile

```makefile
PANDOCK = docker run --rm -v "$(PWD):/data" -u $(shell id -u):$(shell id -g) pandoc/extra

%.pdf: %.md
	$(PANDOCK) $< -o $@ --template eisvogel --toc --number-sections

%.docx: %.md
	$(PANDOCK) $< -o $@
```

---

## 6. Bundled Components

`pandoc/extra` includes:

| Component | Description |
|---|---|
| **Pandoc** | Latest stable release |
| **Tectonic** | Fast PDF engine (alternative to pdflatex/xelatex) |
| **Eisvogel** | `--template eisvogel` — polished LaTeX template |
| **Metropolis (Beamer)** | `--template metropolis` — modern beamer theme |
| **pandoc-latex-environment** | Custom div environments in LaTeX |
| **Lua filters** | Official pandoc Lua filters collection |
| **pandoc-include** | `!include` directive for splitting documents |
| **Font Awesome** | Icon font |
| **Source Code Pro** | Monospace font |
| **Source Sans Pro** | Sans-serif font |

---

## 7. Custom Dockerfile

If you need additional LaTeX packages or tools:

```dockerfile
FROM pandoc/extra:latest

# Install additional LaTeX packages via tlmgr
RUN tlmgr install pgf tikz-network

# Or install system packages (Ubuntu variant)
# FROM pandoc/extra:latest-ubuntu
# RUN apt-get update && apt-get install -y python3-pip
```

Build and use:
```bash
docker build -t my-pandoc .
docker run --rm -v "$(pwd):/data" -u $(id -u):$(id -g) my-pandoc input.md -o output.pdf
```
