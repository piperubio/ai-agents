#!/usr/bin/env python3
"""Convert Mermaid code blocks in Markdown to images using Mermaid CLI (mmdc).

Scans a Markdown file for fenced code blocks tagged `mermaid`, renders each
one with `mmdc` (https://github.com/mermaid-js/mermaid-cli), and replaces the
block with a Markdown image reference so Pandoc can embed it in PDF/DOCX/HTML.

Examples:
    # Basic: replace blocks with images in mermaid-assets/, write document.mermaid.md
    python3 mermaid.py document.md

    # In-place rewrite, PNG at 3x scale (crisper for PDF)
    python3 mermaid.py document.md -i -f png -s 3

    # SVG output for HTML, custom image directory
    python3 mermaid.py document.md -o rendered.md -d assets/diagrams -f svg

    # Keep original blocks as HTML comments, preview only
    python3 mermaid.py document.md --keep --dry-run

Exit code is non-zero if any diagram fails to render.
"""

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

MERMAID_BLOCK = re.compile(
    r"^```mermaid[ \t]*\n(.*?)^```[ \t]*$",
    re.MULTILINE | re.DOTALL,
)


def build_parser():
    parser = argparse.ArgumentParser(
        description="Render Mermaid code blocks in Markdown to images using mmdc."
    )
    parser.add_argument("markdown_file", help="Input Markdown file")
    parser.add_argument(
        "-o", "--output",
        help="Output Markdown file (default: <input>.mermaid.md)",
    )
    parser.add_argument(
        "-i", "--in-place",
        action="store_true",
        help="Rewrite the input file instead of writing a new one",
    )
    parser.add_argument(
        "-d", "--output-dir",
        default="mermaid-assets",
        help="Directory for generated images (default: mermaid-assets)",
    )
    parser.add_argument(
        "-f", "--format",
        choices=["png", "svg", "pdf"],
        default="png",
        help="Output image format (default: png; pdf requires -p latex)",
    )
    parser.add_argument(
        "-s", "--scale",
        type=float,
        default=2,
        help="Scale factor for PNG output (default: 2, recommended 3 for PDF)",
    )
    parser.add_argument(
        "-b", "--background",
        default="transparent",
        help="Background color (default: transparent; use 'white' if PDF shows black boxes)",
    )
    parser.add_argument(
        "-w", "--width",
        type=int,
        help="Width in pixels of the resulting diagram (mmdc -w)",
    )
    parser.add_argument(
        "-c", "--config",
        help="JSON file with Mermaid configuration (mmdc -c)",
    )
    parser.add_argument(
        "-p", "--puppeteer-config",
        help=(
            "JSON file with Puppeteer launch configuration (mmdc -p). "
            "Use the bundled assets/mermaid/puppeteer.json when Chrome fails "
            "with sandbox errors in Docker/CI."
        ),
    )
    parser.add_argument(
        "--mmdc",
        default="mmdc",
        help="Path or name of the mmdc binary (default: mmdc)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-render diagrams even if the image already exists",
    )
    parser.add_argument(
        "--keep",
        action="store_true",
        help="Keep original Mermaid source as an HTML comment above each image",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="List blocks and planned replacements without running mmdc",
    )
    return parser


def find_mmdc(binary):
    path = shutil.which(binary)
    if not path:
        print(
            "✗ mermaid CLI (mmdc) not found. Install it with:\n"
            "    npm install -g @mermaid-js/mermaid-cli\n\n"
            "If Chrome/Puppeteer fails to launch, install Chromium or pass\n"
            "`-p` with a puppeteer config containing {\"args\": [\"--no-sandbox\"]}.",
            file=sys.stderr,
        )
        sys.exit(2)
    return path


def slugify(text, max_len=40):
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug[:max_len].rstrip("-") or None


def render_block(mmd_path, block_text, index, args):
    """Render one Mermaid block with mmdc.

    Returns (image_relpath, error) where image_relpath is relative to the
    output Markdown file.
    """
    name = f"diagram-{index:02d}"
    ext = args.format
    out_file = args.output_dir / f"{name}.{ext}"

    if out_file.exists() and not args.force:
        return out_file, None

    command = [
        args.mmdc,
        "-i", str(mmd_path),
        "-o", str(out_file),
        "-b", args.background,
    ]
    if ext == "png":
        command += ["-s", str(args.scale)]
    if args.width:
        command += ["-w", str(args.width)]
    if args.config:
        command += ["-c", str(args.config)]
    if args.puppeteer_config:
        command += ["-p", str(args.puppeteer_config)]

    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        error = result.stderr.strip() or result.stdout.strip()
        return None, error
    return out_file, None


def main():
    args = build_parser().parse_args()

    input_path = Path(args.markdown_file)
    if not input_path.exists():
        print(f"✗ File not found: {input_path}", file=sys.stderr)
        sys.exit(2)

    if args.in_place:
        output_path = input_path
    elif args.output:
        output_path = Path(args.output)
    else:
        output_path = input_path.with_name(input_path.stem + ".mermaid.md")

    args.output_dir = Path(args.output_dir)
    args.output_dir.mkdir(parents=True, exist_ok=True)

    if not args.dry_run:
        mmdc = find_mmdc(args.mmdc)

    content = input_path.read_text(encoding="utf-8")
    blocks = list(MERMAID_BLOCK.finditer(content))

    if not blocks:
        print(f"ℹ No Mermaid blocks found in {input_path}")
        return

    print(f"Found {len(blocks)} Mermaid block(s) in {input_path}")

    rendered_paths = []
    failures = 0
    offset = 0

    for index, match in enumerate(blocks, start=1):
        block_text = match.group(1)
        replacement = None

        if not args.dry_run:
            with tempfile.NamedTemporaryFile(
                mode="w", suffix=".mmd", encoding="utf-8", delete=False
            ) as tmp:
                tmp.write(block_text)
                tmp_path = Path(tmp.name)

            try:
                image, error = render_block(tmp_path, block_text, index, args)
            finally:
                tmp_path.unlink(missing_ok=True)

            if image is None:
                failures += 1
                print(f"✗ Block {index}: render failed: {error}")
                continue

            rel_image = image.relative_to(output_path.parent) if output_path.parent else image
            replacement = f"![Diagram {index}]({rel_image.as_posix()})"
            rendered_paths.append(image)
            print(f"✓ Block {index}: {image}")

        else:
            preview = " ".join(block_text.strip().split())[:60]
            replacement = f"![Diagram {index}]({args.output_dir.as_posix()}/diagram-{index:02d}.{args.format})"
            print(f"• Block {index}: '{preview}…'  →  {replacement}")

        new_block = replacement
        if args.keep and replacement:
            new_block = f"<!-- Mermaid source (diagram {index}):\n{block_text.rstrip()}\n-->\n\n{replacement}"

        content = content[: match.start() + offset] + new_block + content[match.end() + offset :]
        offset += len(new_block) - len(match.group(0))

    if args.dry_run:
        print("\nDry run: no files written.")
        return

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content, encoding="utf-8")

    print(f"\nWrote: {output_path}")
    if failures:
        print(f"✗ {failures} diagram(s) failed and kept their original block. Fix the source and re-run.")
        sys.exit(1)
    print(f"✅ All diagrams rendered. Convert with: pandoc {output_path} -o output.pdf")


if __name__ == "__main__":
    main()
