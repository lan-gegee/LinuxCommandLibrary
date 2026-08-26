# TAGLINE

分页并格式化文本以供打印

# TLDR

**格式化文件以供打印**

```pr [file]```

**添加页眉**

```pr -h "[Header Text]" [file]```

**多栏输出**

```pr -[3] [file]```

**双倍行距输出**

```pr -d [file]```

**为行编号**

```pr -n [file]```

# SYNOPSIS

**pr** [_options_] [_files_]

# PARAMETERS

_FILES_
> 输入文件。

**-h** _HEADER_
> 页眉文本。

**-NUM**
> 栏数。

**-d**
> 双倍行距。

**-n**
> 为行编号。

**-l** _LINES_
> 页长。

**-w** _WIDTH_
> 页宽。

**-m**
> 并排合并多个文件。

**-t**
> 省略页眉和页脚。

**-s** _CHAR_
> 用指定字符分隔各栏。

# DESCRIPTION

**pr** 通过添加页眉（含文件名和日期）、页脚、分页符和行号来格式化文本文件以供打印。它可以将文本排成多栏，并控制页面尺寸，包括长度、宽度和边距。

这个传统 Unix 工具适用于准备要打印的纯文本文档，或将单栏输入转换为格式化的多栏布局。它从文件或 stdin 读取，写入 stdout。

# CAVEATS

默认页长为 66 行（针对 11 英寸纸张）。页眉默认包含文件名和日期。输入必须是文本；二进制文件会产生不可预测的输出。

# HISTORY

pr 自 **20 世纪 70 年代初**起就是 Bell Labs Unix 的组成部分，最初用于为行式打印机准备文本文件。它被纳入 **POSIX** 规范，并包含在 GNU coreutils 中。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```apk: sudo apk add coreutils```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fmt](/man/fmt)(1), [fold](/man/fold)(1), [column](/man/column)(1)
