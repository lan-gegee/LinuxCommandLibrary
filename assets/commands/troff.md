# TAGLINE

GNU roff 排版处理器

# TLDR

使用 man 宏包排版文档

```troff -man [file.1]```

使用 ms 宏包排版

```troff -ms [file.ms]```

生成 ASCII 输出

```troff -a [file]```

打印版本信息

```troff -v```

启用所有警告

```troff -w all [file]```

以兼容模式排版

```troff -C [file]```

# SYNOPSIS

**troff** [_-abcivzCERU_] [_-d cs_] [_-f fam_] [_-F dir_] [_-m name_] [_-n num_] [_-o list_] [_-r cn_] [_-T name_] [_-w name_] [_file ..._]

# PARAMETERS

**-a**
> 生成排版结果的 ASCII 近似输出。

**-b**
> 在每条警告或错误消息中打印回溯信息。

**-c**
> 禁用彩色输出。

**-C**
> 启用与传统 troff 的兼容模式。

**-d** _cs_
> 将字符串 c 定义为 s。

**-f** _fam_
> 设置默认字族。

**-F** _dir_
> 在指定目录中搜索字体文件。

**-i**
> 处理完文件后继续读取标准输入。

**-m** _name_
> 包含宏包（例如 **man**、**ms**、**me**、**mom**）。

**-n** _num_
> 第一页的页码设为 num。

**-o** _list_
> 仅输出列表中的页。

**-r** _cn_
> 将寄存器 c 的值设置为 n。

**-T** _name_
> 为指定设备准备输出（默认：ps）。

**-U**
> 启用不安全模式（允许危险的请求）。

**-v**
> 打印版本号。

**-w** _name_
> 启用指定警告。使用 **-w all** 可启用大多数警告。

**-W** _name_
> 禁用指定警告。

# DESCRIPTION

**troff** 是 groff (GNU roff) 文本格式化系统中的排版处理器。它读取包含格式化命令的文本文件，并为 PostScript、PDF 和终端等多种设备生成格式化输出。

troff 通常通过 **groff** 调用，后者自动处理预处理器（tbl、eqn、pic）和后处理器。宏包提供高层的格式化能力：**man** 用于手册页，**ms** 用于一般文档，**mom** 用于复杂文档。

groff 实现扩展了传统 Unix troff，增加了颜色支持、额外的转义序列和改进的兼容特性，同时保持向后兼容。

# CAVEATS

直接使用 troff 并不常见；首选 **groff** 包装器来处理完整的处理管线。除非必要，应避免 **-U** 不安全模式，因为它允许潜在危险的文件操作。旧文档可能需要兼容模式 (**-C**)。

# HISTORY

最初的 troff 由 **Joe Ossanna** 于 **1973 年**在贝尔实验室作为 Unix 的一部分编写，由更早的 runoff 格式化程序演化而来。Ossanna 于 1977 年去世后，**Brian Kernighan** 重写并维护了 troff。GNU troff (groff) 由 **James Clark** 自 **1989 年**起开发，作为自由的软件替代品，如今由 groff 项目作为 GNU 系统的一部分维护。

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

[groff](/man/groff)(1), [nroff](/man/nroff)(1), [man](/man/man)(1), [tbl](/man/tbl)(1), [eqn](/man/eqn)(1)
