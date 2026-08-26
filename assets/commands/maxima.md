# TAGLINE

用于符号数学的计算机代数系统

# TLDR

**启动 Maxima**

```maxima```

**求表达式的值**

```maxima --batch-string="[expand((x+1)^3)];"```

**运行脚本文件**

```maxima -b [script.mac]```

**使用安静模式**

```maxima -q```

**以 wxMaxima 界面启动**

```wxmaxima```

# SYNOPSIS

**maxima** [_options_]

# PARAMETERS

**-b**, **--batch** _file_
> 以批处理模式处理 maxima 文件。

**--batch-string** _string_
> 以批处理模式处理 maxima 命令。

**--batch-lisp** _file_
> 以批处理模式处理 Lisp 文件。

**-q**, **--quiet**
> 抑制 Maxima 启动消息。

**--very-quiet**
> 抑制表达式标签和启动消息。

**-l** _lisp_
> 指定 Lisp 实现（如 sbcl、clisp、gcl）。

**--init** _file_
> 初始化文件。

**-p** _file_
> 预加载 Lisp 文件。

**-d**, **--directories**
> 显示 Maxima 内部目录信息。

**-s** _port_, **--server** _port_
> 将 Maxima 连接到指定端口上的服务器。

**-v**, **--verbose**
> 在 maxima 包装脚本中显示 Lisp 调用。

**--version**
> 显示已安装的版本。

# DESCRIPTION

**Maxima** 是一个用于符号数学的计算机代数系统。它可以执行符号微分、积分、泰勒级数、变换、线性代数等运算。

Maxima 源自 Macsyma，那是最古老的计算机代数系统之一。
# CAVEATS

语法与其他计算机代数系统不同。输出格式可能较为复杂。交互式使用推荐使用 GUI（wxMaxima）。

# HISTORY

Maxima 源自 **1968 年**起于 **MIT** 开发的 **Macsyma**。DOE 版本于 **1998 年**开源发布，成为 Maxima。

# INSTALL

```apt: sudo apt install maxima```

```dnf: sudo dnf install maxima```

```pacman: sudo pacman -S maxima```

```zypper: sudo zypper install maxima```

```brew: brew install maxima```

```nix: nix profile install nixpkgs#maxima```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[octave](/man/octave)(1)
