# TAGLINE

用布尔运算组合两个文件的行

# TLDR

**输出同时出现在两个文件中的行**（交集）

```combine [file1] and [file2]```

**输出在 file1 中但不在 file2 中的行**（差集）

```combine [file1] not [file2]```

**输出任一文件中出现的行**（并集）

```combine [file1] or [file2]```

**输出恰好只出现在一个文件中的行**（对称差）

```combine [file1] xor [file2]```

**从标准输入读取其中一个输入**

```cat [file1] | combine - and [file2]```

# SYNOPSIS

**combine** _file1_ **and**|**not**|**or**|**xor** _file2_

# PARAMETERS

**and**
> 输出 _file1_ 中也存在于 _file2_ 的行（交集）。

**not**
> 输出 _file1_ 中不存在于 _file2_ 的行（集合差）。

**or**
> 输出 _file1_ 或 _file2_ 中的行（并集）；_file2_ 的行会被追加在后。

**xor**
> 输出恰好只出现在 _file1_ 或 _file2_ 其中之一的行（对称差）。

_file1_, _file2_
> 输入文件。使用 **-** 表示从标准输入读取。

# DESCRIPTION

**combine** 对两个文件的行执行布尔集合运算，将每个文件视为一个行的集合。输入无需排序；输出行按其在 _file1_ 中出现的顺序排列（使用 **or** 时 _file2_ 的行追加在后）。

该命令是 **moreutils** 实用工具集中的一员，无需经过 **sort**、**uniq** 和 **comm** 的多重管道，即可快速计算纯文本数据之间的集合关系。

# CAVEATS

这些运算不满足交换律：交换 _file1_ 和 _file2_ 可能改变输出顺序。文件内重复的行会在输出中原样保留；如需对称且去重的结果，可再经 **sort -u** 处理。在某些发行版上，该二进制程序作为 moreutils 的 **combine** 安装，但可能与 ImageMagick 旧版的 **combine** 工具冲突——请用 **which combine** 检查，或使用软件包的完整路径。

# HISTORY

**combine** 是 **moreutils** 的一部分，该工具集由 Joey Hess 自约 **2006 年**起维护。它提供的集合论运算原本需要 **sort** 和 **comm** 等多个管道阶段才能完成。

# INSTALL

```apt: sudo apt install moreutils```

```dnf: sudo dnf install moreutils```

```pacman: sudo pacman -S moreutils```

```apk: sudo apk add moreutils```

```zypper: sudo zypper install moreutils```

```brew: brew install moreutils```

```nix: nix profile install nixpkgs#moreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[comm](/man/comm)(1), [sort](/man/sort)(1), [uniq](/man/uniq)(1), [join](/man/join)(1), [diff](/man/diff)(1), [grep](/man/grep)(1)
