# TAGLINE

为 groff 和 troff 格式化表格

# TLDR

**处理包含表格的文件**并经 tbl 和 groff 输出

```groff -t [file.roff] | [less]```

**在支持公式的情况下处理表格**

```tbl [file.roff] | eqn | troff```

**从标准输入处理**

```cat [file.roff] | tbl```

**处理包含表格的 man page**

```tbl [page.man] | nroff -man | less```

**启用 AT&T 兼容模式**

```tbl -C [file.roff]```

# SYNOPSIS

**tbl** [**-Cv**] [_file_...]

# PARAMETERS

**-C**
> 启用 AT&T 兼容模式；即使在 .TS 和 .TE 后面跟的不是空格或换行符时也能识别它们。

**-v**, **--version**
> 打印版本信息并退出

**--help**
> 显示用法信息并退出

# DESCRIPTION

**tbl** 是 groff/troff 文档排版系统中的预处理器，用于格式化表格。它将嵌入在 **.TS**（表格开始）和 **.TE**（表格结束）宏之间的表格描述翻译成 troff 排版命令。

表格由两部分定义：指定列对齐方式的格式部分和包含内容的数据部分。列分类符包括 **L**（左对齐）、**R**（右对齐）、**C**（居中）、**N**（数字对齐）和 **A**（字母对齐）。还可以对列应用修饰符，如 **b**（粗体）和 **i**（斜体）。

区域选项控制表格外观：**box** 绘制边框，**center** 使表格水平居中，**expand** 将其拉伸至行宽，**tab(c)** 设置列分隔字符。

tbl 通常通过 **groff -t** 调用而非直接运行。当使用多个预处理器时，tbl 应在 **eqn**（公式）之前运行。groff 命令会自动处理调用顺序。

# TABLE SYNTAX

```
.TS
box center;
c c c
l l n.
Header1	Header2	Value
Data1	Data2	100
Data3	Data4	200
.TE
```

> **c/l/r/n** = 居中/左/右/数字对齐
> 以 **.** 结尾的行用于分隔格式与数据
> 默认以制表符分隔各列

# CAVEATS

GNU tbl 的输出需要 GNU troff 才能处理，无法由 AT&T troff 处理。包含大量跨列或嵌套元素的复杂表格难以调试。制表符是默认分隔符；可用 **tab(;)** 更改。

# HISTORY

**tbl** 由贝尔实验室的 **M.E. Lesk** 编写，最早于 **1976 年**在论文 "TBL -- A Program to Format Tables" 中记载。GNU 版本由 **James Clark** 作为 groff 的一部分编写。它在原版基础上扩展了无限列数等特性并改进了兼容性。

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

[groff](/man/groff)(1), [troff](/man/troff)(1), [nroff](/man/nroff)(1), [eqn](/man/eqn)(1), [pic](/man/pic)(1), [refer](/man/refer)(1), [col](/man/col)(1)
