#!/usr/bin/env python3
"""系统性修复：原文全大写的 H1 section 键被误译的文件。
用法: python3 tools/repair_caps.py   （在仓库根目录运行）
"""
import re
import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
count = 0
for f in sorted((REPO / "assets" / "commands").glob("*.md")):
    rel = str(f.relative_to(REPO))
    orig = subprocess.run(
        ["git", "show", f"upstream/master:{rel}"],
        cwd=REPO, capture_output=True, text=True,
    ).stdout
    if not orig:
        continue
    new_t = f.read_text()
    o1 = [m.group(1).strip() for m in re.finditer(r"^# (.+)$", orig, re.M)]
    n1 = [m.group(1).strip() for m in re.finditer(r"^# (.+)$", new_t, re.M)]
    if len(o1) != len(n1):
        continue
    changed = False
    for o, n in zip(o1, n1):
        if o != n and o.upper() == o and any(c.isalpha() for c in o):
            t2 = re.sub(rf"^# {re.escape(n)}$", f"# {o}", new_t, count=1, flags=re.M)
            if t2 != new_t:
                new_t = t2
                changed = True
                count += 1
    if changed:
        f.write_text(new_t)
print(f"fixed {count}")
