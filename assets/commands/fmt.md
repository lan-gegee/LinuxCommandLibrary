# TAGLINE

对段落进行重排的简易文本格式化工具

# TLDR

将文本文件**重新格式化**为 75 列（默认）

```fmt [path/to/file.txt]```

**按指定宽度重新格式化**

```fmt -w [60] [path/to/file.txt]```

**从标准输入重新格式化文本**

```echo "[long text here]" | fmt```

**保留段落缩进**

```fmt -p [prefix] [file.txt]```

**只拆分过长的行**（不合并短行）

```fmt -s [file.txt]```

**设置目标宽度和最大宽度**

```fmt -g [70] -w [80] [file.txt]```

**统一空格间距**（词间一个空格，句后两个空格）

```fmt -u [file.txt]```

**格式化多个文件**

```fmt [file1.txt] [file2.txt]```

# SYNOPSIS

**fmt** [_-csuw_] [_-g goal_] [_-p prefix_] [_-w width_] [_file ..._]

# PARAMETERS

**-w**, **--width** _n_
> 最大行宽（默认：75）。

**-g**, **--goal** _n_
> 目标宽度（最佳行长度，默认为宽度的 93%）。

**-s**, **--split-only**
> 只拆分长行，不合并短行。

**-u**, **--uniform-spacing**
> 词间一个空格，句后两个空格。

**-c**, **--crown-margin**
> 保留前两行的缩进。

**-p**, **--prefix** _string_
> 只对以指定前缀开头的行重新排版。

**-t**, **--tagged-paragraph**
> 保留第一行的缩进。

**--help**
> 显示帮助并退出。

**--version**
> 显示版本并退出。

# DESCRIPTION

**fmt** 是一款简易的文本格式化工具，将段落重排到指定的行宽以内。它从文件或标准输入读取文本、重新排版并输出到标准输出。

该工具能智能处理段落：连续的非空行被视为一个段落并一起重排。空行、缩进变化以及其他排版标记则表示段落边界。

排版算法在不超过最大宽度的前提下尽量接近目标宽度。这比简单地在最大宽度处断行产生的外观更自然。单词永远不会被连字符断开或截断。

常见用途包括为电子邮件、文档和代码注释排版文本，以及提高文本文件的可读性。当你只想折断过长的行而不影响已正确排版的文本时，**-s** 选项很有用。

与更复杂的格式化工具不同，fmt 只处理纯文本。它不理解标记语言、代码块或特殊排版格式，专为简单的散文段落设计。

# CAVEATS

不会精确保留原有的空格和排版。可能会破坏代码或表格等有意排版的文本。不支持标记语言。超过行宽的超长单词不会被断开。不同实现的行为可能略有差异。

# HISTORY

**fmt** 起源于 **1979 年**前后的 BSD Unix，基于更早的一个工具。它被设计为用于准备文档和电子邮件的简易文本格式化工具。该命令后来被纳入 GNU coreutils，至今仍是类 Unix 系统的标准组成部分。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```apk: sudo apk add coreutils-fmt```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fold](/man/fold)(1), [pr](/man/pr)(1), [nroff](/man/nroff)(1), [groff](/man/groff)(1)
