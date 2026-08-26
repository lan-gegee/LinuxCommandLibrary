#!/usr/bin/env python3
"""批次清单生成器：将 assets/commands 下全部 man page 按字母序贪心装箱。

约束: 每批 ≤ MAX_WORDS 词 且 ≤ MAX_FILES 个文件。
输出: tools/l10n-batches/batch-XXX.txt（每行一个文件路径）+ manifest.json
已翻译的文件（与 upstream/master 相同则视为未译，未译才进批次）。
"""
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "tools" / "l10n-batches"
MAX_WORDS = 14000
MAX_FILES = 110


def word_count(text: str) -> int:
    return len(text.split())


def untranslated_files():
    files = sorted((REPO / "assets" / "commands").glob("*.md"))
    r = subprocess.run(
        ["git", "diff", "--name-only", "upstream/master", "--", "assets/commands"],
        cwd=REPO, capture_output=True, text=True,
    )
    translated = set(r.stdout.split())
    todo = []
    for p in files:
        rel = str(p.relative_to(REPO))
        if rel in translated:
            continue
        todo.append((rel, word_count(p.read_text())))
    return todo


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for old in OUT.glob("*"):
        old.unlink()
    todo = untranslated_files()
    batches, cur, cur_w = [], [], 0
    for rel, w in todo:
        if cur and (cur_w + w > MAX_WORDS or len(cur) >= MAX_FILES):
            batches.append(cur)
            cur, cur_w = [], 0
        cur.append(rel)
        cur_w += w
    if cur:
        batches.append(cur)

    manifest = []
    for i, b in enumerate(batches, 1):
        name = f"batch-{i:03d}.txt"
        (OUT / name).write_text("\n".join(b) + "\n")
        first = Path(b[0]).stem
        last = Path(b[-1]).stem
        manifest.append({
            "id": i, "file": name, "count": len(b),
            "range": f"{first}..{last}", "files": b,
        })
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=1))
    print(f"files={len(todo)} batches={len(batches)}")


if __name__ == "__main__":
    main()
