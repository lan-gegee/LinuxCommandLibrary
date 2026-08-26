# TAGLINE

用于 groff 文档的图表语言预处理器

# TLDR

**将 grap 脚本经 groff 处理为 PostScript**

```grap [script.grap] | groff -Tps > [output.ps]```

**将 grap 输出通过 pic 和 groff 管道处理**

```grap [script.grap] | pic | troff -Tps > [output.ps]```

**从命令行定义变量**

```grap -d "[x=100]" [script.grap] | groff -Tps > [output.ps]```

**从标准输入读取**

```cat [script.grap] | grap | groff -Tps > [output.ps]```

# SYNOPSIS

**grap** [_options_] [_file_]

# PARAMETERS

_FILE_
> grap 输入文件。若省略，则从标准输入读取。

**-d** _VAR=VALUE_
> 在处理前定义变量及其值。

**-l**
> 使用图形默认的线条粗细。

**-R**
> 不加载默认的宏启动文件。

**--help**
> 显示帮助信息。

# DESCRIPTION

**grap** 是一个预处理器，用于在 groff/troff 文档中创建图表。输入以简单的声明式语言编写，置于 .G1 和 .G2 宏之间；输出是 pic(1) 代码，可进一步交由 pic 和 troff/groff 处理。

该工具为技术文档创建出版级质量的图表，支持坐标轴标注、多数据集、对数刻度和坐标系等特性。它与 troff 文档处理管道无缝集成。

# CAVEATS

属于 groff 生态系统的一部分。输出 pic 格式，必须再由 pic(1) 和 troff/groff 进一步处理。大多数发行版默认不安装它，通常作为独立软件包提供。

# HISTORY

grap 由 **贝尔实验室（Bell Labs）** 开发，是 Unix 文档准备工具的一部分，由 Kernighan 和 Bentley 撰文描述。

# INSTALL

```apt: sudo apt install grap```

```brew: brew install grap```

```nix: nix profile install nixpkgs#grap```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[groff](/man/groff)(1), [pic](/man/pic)(1), [troff](/man/troff)(1), [tbl](/man/tbl)(1), [eqn](/man/eqn)(1), [gnuplot](/man/gnuplot)(1)
