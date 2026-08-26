# TAGLINE

处理颜色的命令行工具

# TLDR

**显示颜色信息**

```pastel color [red]```

**显示十六进制颜色**

```pastel color ["#ff5500"]```

**转换颜色格式**

```pastel format hsl ["#ff5500"]```

**列出颜色名称**

```pastel list```

**生成调色板**

```pastel gradient [blue] [red] --number [5]```

**交互式取色**

```pastel pick```

**调亮颜色**

```pastel lighten [0.2] [blue]```

**混合两种颜色**

```pastel mix [red] [blue]```

# SYNOPSIS

**pastel** _command_ [_options_] [_arguments_]

# PARAMETERS

**color** _COLOR_
> 显示颜色信息。

**list**
> 列出命名颜色。

**format** _FORMAT_ _COLOR_
> 将颜色转换为指定格式。

**pick**
> 交互式取色器。

**gradient** _COLOR1_ _COLOR2_
> 在两种颜色之间生成渐变。

**mix** _COLOR1_ _COLOR2_
> 混合两种颜色。

**lighten** _AMOUNT_ _COLOR_
> 调亮颜色（0.0-1.0）。

**darken** _AMOUNT_ _COLOR_
> 调暗颜色。

**saturate** _AMOUNT_ _COLOR_
> 提高饱和度。

**desaturate** _AMOUNT_ _COLOR_
> 降低饱和度。

**rotate** _DEGREES_ _COLOR_
> 旋转色相。

**complement** _COLOR_
> 获取互补色。

**distinct** _NUM_ [_COLORS_]
> 生成彼此差异最大的颜色。

**random**
> 生成随机颜色。

**paint** _COLOR_ _TEXT_
> 打印带颜色的文本。

**--number** _N_
> 要生成的颜色数量。

**--colorspace** _SPACE_
> 操作所用的色彩空间。

# DESCRIPTION

**pastel** 是一个处理颜色的命令行工具。它可以显示颜色信息、在不同格式之间转换、生成调色板，并以编程方式操作颜色。

颜色输入支持多种格式：名称（red、blue）、hex（#ff0000）、RGB（rgb(255,0,0)）、HSL（hsl(0,100%,50%)）等。该工具利用真彩色在终端中准确预览显示颜色块。

color 命令会显示全面的信息：RGB、HSL、CIELAB 值、最接近的命名颜色以及对比度信息。这对设计工作和无障碍检查很有帮助。

各种操作函数在感知均匀的色彩空间（CIELAB）中进行，效果自然。调亮、调暗和饱和度变化在整个色谱上表现一致。

调色板生成可创建和谐的配色方案。gradient 产生平滑的过渡。distinct 为可视化生成差异最大的颜色。random 创建美观的随机颜色。

paint 命令可在脚本中实现彩色终端输出。格式转换便于与 CSS、代码和设计工具集成。

# CAVEATS

需要真彩色终端才能准确显示。终端的颜色准确性各有差异。颜色感知取决于显示器校准。某些操作可能产生色域之外的结果。交互式取色器需要支持鼠标的终端。

# HISTORY

**pastel** 由 **David Peter**（sharkdp）于 **2019 年**前后创建。它使用 Rust 编写，是 fd、bat 等一系列现代 CLI 工具中的一员。该工具满足了终端工作流、设计和无障碍测试中操作颜色的需求，强调感知均匀的颜色运算。

# INSTALL

```dnf: sudo dnf install pastel```

```pacman: sudo pacman -S pastel```

```apk: sudo apk add pastel```

```zypper: sudo zypper install pastel```

```brew: brew install pastel```

```nix: nix profile install nixpkgs#pastel```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[color](/man/color)(1), [tput](/man/tput)(1), [convert](/man/convert)(1)
