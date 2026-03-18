# Business Proposal Template Guide

Templates and best practices for creating professional business proposals using Pandoc and Eisvogel.

## Quick Start Template

Use this frontmatter for business proposals:

```yaml
---
title: "Proposal Title"
author:
  - Your Name
  - Company Name
  - https://company.com
date: "2026-01-01"
titlepage: true
titlepage-color: "1E4B7A"
titlepage-text-color: "FFFFFF"
titlepage-rule-color: "1E4B7A"
titlepage-rule-height: 4
toc: true
toc-own-page: true
toc-depth: 2
numbersections: true
classoption: oneside
---
```

## Proposal Structure

Recommended structure for consulting proposals:

```markdown
# Proposal Title

**Company Name**  
**Website**: https://company.com  
**Prepared by**: Your Name  
**Date**: 2026-01-01  
**Valid until**: 2026-02-01 (30 days)

## Executive Summary

Brief overview of the proposal...

## Understanding Their Situation

Current state and challenges...

## Proposed Solution

### Architecture

![Diagram](diagram.png)

### Phases

### Phase 1: Name

**Objective**: What we achieve

**Deliverables**:

* Item 1
* Item 2
* Item 3

### Phase 2: Name

**Objective**: What we achieve

**Deliverables**:

* Item 1
* Item 2

## Expected Results

| Result | Metric |
|--------|--------|
| Outcome 1 | Metric |
| Outcome 2 | Metric |

## Team

| Role | Responsibilities | Assignment |
|------|------------------|------------|
| Role 1 | Responsibilities | % |
| Role 2 | Responsibilities | % |

## Investment

### Pricing Model

| Phase | Description | Investment |
|-------|-------------|------------|
| Phase 1 | Description | Amount |
| Phase 2 | Description | Amount |
| **Total** | | **Amount** |

### Payment Terms

Payment milestones...

## Why Us

Experience, methodology, differentiators...

## Terms and Conditions

* Term 1
* Term 2
* Term 3
```

## Best Practices

### Formatting Tips

1. **Always add blank lines** before and after:
   - Lists
   - Tables
   - Blockquotes
   - Code blocks

2. **Avoid `---` separators** - they create large white spaces

3. **Use consistent heading levels** - don't skip from `#` to `####`

4. **Add page breaks** where needed:
   ```markdown
   \pagebreak
   ## New Section
   ```

### Including Diagrams

1. **Mermaid to PNG:**
   ```bash
   # Convert using Kroki
   curl -s -X POST https://kroki.io/mermaid/png \
     -H "Content-Type: text/plain" \
     -d 'flowchart LR
         A[Start] --> B[End]' > diagram.png
   ```

2. **Reference in markdown:**
   ```markdown
   ![Description](diagram.png)
   ```

### Company Branding

Customize the title page:

```yaml
titlepage-color: "1E4B7A"    # Your brand color
titlepage-text-color: "FFFFFF"
titlepage-rule-color: "1E4B7A"
titlepage-rule-height: 4
```

### Multi-Author Setup

```yaml
author:
  - Primary Author
  - Company Name
  - Website
```

## Common Issues

See `troubleshooting.md` for:
- List rendering problems
- Title hierarchy issues
- Image path problems
- Page break solutions
