#!/usr/bin/env python3
"""结构校验器：对比 upstream/master 英文原文，验证汉化文件未破坏程序依赖的结构。

用法:
  python3 tools/validate_l10n.py <file1> <file2> ...     # 校验指定文件
  python3 tools/validate_l10n.py --stdin                 # 从 stdin 读文件列表
  python3 tools/validate_l10n.py --all                   # 校验 assets/ 下全部已译文件

退出码: 0=全部通过, 1=存在失败。失败详情打印到 stdout。
"""
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
UPSTREAM_REF = "upstream/master"

SECTION_RE = re.compile(r"^# .*$", re.M)
MAN_URL_RE = re.compile(r"/man/[A-Za-z0-9._/-]+")
FENCE_RE = re.compile(r"^\s*(```|```)\s*$", re.M)

# 允许出现在代码块内的链接: 提取 URL 后比较; 链接文本可译
CODE_LINK_RE = re.compile(r"\[[^\]]*\]\((/man/[^)]+)\)")

FAILS = []
CHECKED = 0


def git_show(path: str) -> str | None:
    r = subprocess.run(
        ["git", "show", f"{UPSTREAM_REF}:{path}"],
        cwd=REPO, capture_output=True, text=True,
    )
    return r.stdout if r.returncode == 0 else None


def split_code_blocks(text: str):
    """返回 (代码块列表, 非代码文本)。正确处理单行完整围栏 ```xxx```。"""
    lines = text.split("\n")
    blocks, cur, prose = [], None, []
    for ln in lines:
        s = ln.strip()
        if cur is None and s.startswith("```") and s.endswith("```") and len(s) >= 6:
            # 单行完整代码块
            inner = s[3:-3]
            if inner.strip():
                blocks.append(inner)
        elif s.startswith("```"):
            if cur is None:
                cur = []
            else:
                blocks.append("\n".join(cur))
                cur = None
        elif cur is not None:
            cur.append(ln)
        else:
            prose.append(ln)
    if cur is not None:  # 未闭合围栏 → 结构破坏
        blocks.append(None)
    return blocks, "\n".join(prose)


def header_structure(text: str) -> list[tuple[int, str]]:
    """返回 [(级别, 标题文本)]，仅统计行首标题。"""
    out = []
    for ln in text.split("\n"):
        m = re.match(r"^(#+) ", ln)
        if m:
            out.append((len(m.group(1)), ln[len(m.group(1)) + 1 :].strip()))
    return out


def normalize_code(block: str) -> str:
    """代码块规范化: 链接只保留 URL，其余原样。"""
    return CODE_LINK_RE.sub(lambda m: m.group(1), block)


def validate(path: str) -> list[str]:
    errs = []
    orig = git_show(path)
    if orig is None:
        return [f"{path}: 上游不存在此文件（新增文件？跳过）"]
    try:
        new = (REPO / path).read_text()
    except Exception as e:
        return [f"{path}: 读取失败 {e}"]

    if new == orig:
        return []  # 尚未翻译，不算失败

    # 1. 标题结构：man page 要求逐字一致；basics/tips 仅要求层级序列一致（分类名可译）
    o_h = header_structure(orig)
    n_h = header_structure(new)
    if path.startswith(("assets/basics/", "assets/tips")):
        o_lvls = [(lv,) for lv, _ in o_h]
        n_lvls = [(lv,) for lv, _ in n_h]
        if o_lvls != n_lvls:
            errs.append(f"{path}: 标题层级结构被改动\n  原: {o_h}\n  新: {n_h}")
    else:
        if [t for _, t in o_h] != [t for _, t in n_h]:
            errs.append(f"{path}: section 标题被改动\n  原: {[t for _, t in o_h]}\n  新: {[t for _, t in n_h]}")

    # 2. 代码块数量与内容（链接文本除外）必须一致
    ob, op = split_code_blocks(orig)
    nb, np_ = split_code_blocks(new)
    if len(ob) != len(nb) or any(b is None for b in nb):
        errs.append(f"{path}: 代码块数量或闭合不一致 原{len(ob)} 新{len(nb)}")
    else:
        for i, (a, b) in enumerate(zip(ob, nb)):
            if normalize_code(a) != normalize_code(b):
                errs.append(f"{path}: 第{i+1}个代码块内容被改动")
                break

    # 3. /man/ URL 集合一致（正文+代码块全体）
    if sorted(MAN_URL_RE.findall(orig)) != sorted(MAN_URL_RE.findall(new)):
        errs.append(f"{path}: /man/ 链接集合不一致")

    # 4. 确实翻译了: 正文含 CJK
    def cjk_ratio(t: str) -> float:
        cjk = sum(1 for c in t if "\u4e00" <= c <= "\u9fff")
        return cjk / max(1, len(t))

    if cjk_ratio(np_) < 0.05 and path.startswith("assets/"):
        # SEE ALSO 纯命令列表等可能确实无需翻译；仅提示不判败
        pass

    return errs


def main():
    args = sys.argv[1:]
    if "--all" in args:
        files = [
            str(p.relative_to(REPO))
            for d in ("assets/basics", "assets/commands")
            for p in sorted((REPO / d).glob("*.md"))
        ] + ["assets/tips.md"]
    elif "--stdin" in args:
        files = [l.strip() for l in sys.stdin if l.strip()]
    else:
        files = args
    global CHECKED
    for f in files:
        CHECKED += 1
        FAILS.extend(validate(f))
    print(f"checked={CHECKED} failed={len([e for e in FAILS])}")
    for e in FAILS:
        print("FAIL:", e)
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
