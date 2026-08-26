# TAGLINE

GNU 文档排版系统

# TLDR

**将文档排版为 PDF**

```groff -Tpdf [file.ms] > output.pdf```

**使用 man 宏排版**

```groff -man [file.1] > output.ps```

**使用 ms 宏排版为 PDF**

```groff -ms -Tpdf [file.ms] > output.pdf```

**在终端中预览**

```groff -Tutf8 [file.roff] | less```

**调用表格和公式预处理器处理**

```groff -t -e -ms [file.ms] > output.ps```

**将 man page 排版为纯文本**

```groff -Tutf8 -man [file.1]```

**显示将要执行的管道而不实际执行**

```groff -V -Tpdf [file.ms]```

# SYNOPSIS

**groff** [_options_] [_files_]

# PARAMETERS

_FILES_
> 要处理的输入文件。

**-T** _DEVICE_
> 输出设备（pdf、ps、html、utf8、ascii、latin1、dvi）。

**-m** _MACRO_
> 使用宏包（man、ms、me、mm）。

**-t**
> 运行 tbl 预处理器处理表格。

**-e**
> 运行 eqn 预处理器处理公式。

**-p**
> 运行 pic 预处理器处理图示。

**-R**
> 运行 refer 预处理器处理参考文献引用。

**-s**
> 运行 soelim 预处理器处理文件包含。

**-G**
> 运行 grap 预处理器处理图表。

**-S**
> 安全模式。禁用 .open、.opena、.pso、.sy 和 .pi 请求。

**-U**
> 不安全模式。恢复被 -S 禁用的不安全请求。

**-V**
> 将将要运行的管道打印到标准错误，但不执行。

**-Z**
> 禁用后处理。输出原始的 troff 中间输出。

**-a**
> 生成排版输出的纯文本近似版本。

**-b**
> 在每个错误或警告处打印回溯信息。

**-man**
> -m man 的简写形式。使用 man 宏。

**-ms**
> -m ms 的简写形式。使用 ms 宏。

**--help**
> 显示帮助信息。

# DESCRIPTION

**groff** 是 roff 文档排版系统的 GNU 实现。它是一个前端，负责在一条管道中调度预处理程序、troff 排版器和输出驱动的执行。它处理内嵌格式化命令的文本文件，生成多种格式的排版输出，包括 PDF、PostScript、HTML 和终端显示。

该系统包含处理表格（tbl）、公式（eqn）和图示（pic）的预处理器，并为不同的文档类型提供多个宏包。

# CONFIGURATION

**/usr/share/groff/current/tmac/**
> 系统级的宏文件以及 groff 输出设备的配置。

# CAVEATS

学习曲线陡峭。不同宏包有各自的约定。-man 和 -ms 简写是 groff 的扩展，传统 troff 中并不存在。除非用 -T 覆盖，默认输出设备为 ps（PostScript）。

# HISTORY

groff 由 **James Clark** 创建，是 AT&T troff 的自由实现。它目前作为 **GNU** 项目的一部分维护。

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

[troff](/man/troff)(1), [nroff](/man/nroff)(1), [man](/man/man)(1), [tbl](/man/tbl)(1), [eqn](/man/eqn)(1), [pic](/man/pic)(1), [refer](/man/refer)(1), [soelim](/man/soelim)(1)
