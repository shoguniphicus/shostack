#!/usr/bin/env python3
"""Initialize a private idea-to-SaaS discovery workspace safely (standard library only)."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

FILES = {
    "PRODUCT.template.md": "PRODUCT.md",
    "DECISIONS.template.md": "DECISIONS.md",
    "NEXT.template.md": "NEXT.md",
    "AGENTS.addendum.md": "INTERVIEWER.md",
    "QUESTION-COVERAGE.md": "QUESTION-COVERAGE.md",
}


def bootstrap(workspace: Path, dry_run: bool = False) -> int:
    """Create missing discovery files only; never modify existing content."""
    if not workspace.exists() or not workspace.is_dir():
        print(f"Error: existing workspace directory required: {workspace}", file=sys.stderr)
        return 2

    source_dir = Path(__file__).resolve().parent
    destination_dir = workspace.resolve() / "discovery"
    if destination_dir.is_symlink():
        print("Error: discovery path must not be a symbolic link.", file=sys.stderr)
        return 2
    if destination_dir.exists() and not destination_dir.is_dir():
        print("Error: discovery path exists but is not a directory.", file=sys.stderr)
        return 2

    pending = []
    for source_name, dest_name in FILES.items():
        destination = destination_dir / dest_name
        if destination.exists() or destination.is_symlink():
            print(f"SKIP (exists): discovery/{dest_name}")
            continue
        pending.append((source_dir / source_name, destination))
        label = "WOULD CREATE" if dry_run else "CREATE"
        print(f"{label}: discovery/{dest_name}")

    if dry_run:
        print(f"Dry-run complete; {len(pending)} file(s) would be created.")
        return 0

    destination_dir.mkdir(parents=False, exist_ok=True)
    for source, destination in pending:
        # Exclusive creation means even a new concurrent file cannot be overwritten.
        try:
            with destination.open("x", encoding="utf-8") as handle:
                handle.write(source.read_text(encoding="utf-8"))
        except FileExistsError:
            print(f"SKIP (concurrent create): discovery/{destination.name}")

    print("Ready. Point your agent at discovery/INTERVIEWER.md and discovery/NEXT.md.")
    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Create the private ShoStack idea-to-SaaS discovery records without overwriting existing files."
    )
    parser.add_argument("workspace", nargs="?", default=".", help="An existing project directory (default: current directory)")
    parser.add_argument("--dry-run", action="store_true", help="Show which files would be created; write nothing")
    args = parser.parse_args(argv)
    return bootstrap(Path(args.workspace).expanduser(), args.dry_run)


if __name__ == "__main__":
    sys.exit(main())
