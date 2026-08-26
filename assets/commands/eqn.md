# TAGLINE

troff 的数学公式预处理器

# TLDR

**处理 troff 输入中的公式**

```eqn [document.ms] | troff -ms```

**配合 groff 处理**

```groff -e -ms [document.ms]```

**处理后输出到标准输出**

```eqn [equations.eqn]```

# SYNOPSIS

**eqn** [_options_] [_files_...]

# PARAMETERS

_FILES_
> 包含公式的输入文件。

**-d** _XY_
> 设置行内公式的分隔符。

**-f** _FONT_
> 设置公式字体。

**-s** _SIZE_
> 设置磅值大小。

**-p** _N_
> 下标/上标的大小缩减量。

**-C**
> 即使在注释中也识别 .EQ 和 .EN。

# DESCRIPTION

**eqn** 是 troff 的预处理器，用于排版数学公式。它把高级公式描述语言转换为 troff 命令，产生排版输出。

公式写在 .EQ 与 .EN 宏之间，或用行内分隔符括起。该语言用 "over" 表示分数、"sup" 表示上标、"sqrt" 表示根号等单词。

eqn 通常与 troff/groff 组成管道，用于生成带数学符号的技术文档。

# CAVEATS

语法与 LaTeX 不同。输出需要经过 troff 处理。复杂公式需要仔细排版。相比 TeX 符号集较为有限。

# HISTORY

eqn 由 **Brian Kernighan** 和 **Lorinda Cherry** 于 20 世纪 70 年代在贝尔实验室编写。它是最早的数学排版工具之一，影响了后来的系统。

# INSTALL

```apt: sudo apt install groff-base```

```dnf: sudo dnf install groff-base```

```pacman: sudo pacman -S groff```

```apk: sudo apk add groff```

```zypper: sudo zypper install groff```

```brew: brew install groff```

```nix: nix profile install nixpkgs#groff```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[groff](/man/groff)(1), [troff](/man/troff)(1), [tbl](/man/tbl)(1), [pic](/man/pic)(1), [neqn](/man/neqn)(1)

# RESOURCES

```[Source code](https://cgit.git.savannah.gnu.org/cgit/groff.git)```

```[Homepage](https://www.gnu.org/software/groff/)```

```[Documentation](https://www.gnu.org/software/groff/manual/groff.html)```

<!-- verified: 2026-07-14 -->
