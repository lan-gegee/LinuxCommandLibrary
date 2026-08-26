# TAGLINE

用于绘制图表的 troff 预处理器

# TLDR

**将 pic 处理为 troff**

```pic [diagram.pic] | troff```

**生成输出文件**

```pic [diagram.pic] > [output.troff]```

**安全模式**

```pic -S [diagram.pic]```

**仅检查语法**

```pic -n [diagram.pic]```

**显示版本**

```pic --version```

# SYNOPSIS

**pic** [_-S_] [_-n_] [_-C_] [_options_] [_files_]

# PARAMETERS

**-S**
> 安全模式（不允许 shell 命令）。

**-n**
> 抑制输出，只检查语法。

**-C**
> 兼容模式。

**-D**
> 定义宏。

**-T** _DEVICE_
> 输出设备。

**-z**
> 将不可见的线条和方框绘制为零尺寸对象（GNU 扩展）。

**--help**
> 显示用法信息。

**--version**
> 打印版本信息。

# DESCRIPTION

**pic** 是用于绘制图表的 troff 预处理器。它将文本描述转换为 troff 绘图命令。

图表使用几何图元：方框、圆、线、箭头。定位方式支持相对或绝对。

对象之间用线和箭头连接。标签和文本用于标注元素。

该语言支持宏和变量。复杂图表可由可复用的组件构建。

输出可与 groff/troff 文档处理流程集成。Pic 图表可以嵌入技术文档中。

# EXAMPLE

```
.PS
box "Start"
arrow
circle "Process"
arrow
box "End"
.PE
```

# CAVEATS

与现代绘图工具相比功能有限。只能输出 troff。学习曲线陡峭。

# HISTORY

**pic** 由 **Brian Kernighan** 于 **20 世纪 80 年代**在 **贝尔实验室** 创建。它是 troff/groff 文档准备系统的一部分，并影响了后来的图表语言。

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

[groff](/man/groff)(1), [troff](/man/troff)(1), [tbl](/man/tbl)(1), [eqn](/man/eqn)(1)
