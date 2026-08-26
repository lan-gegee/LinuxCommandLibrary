# TAGLINE

从命令行绘制 ASCII 折线图

# TLDR

对来自 stdin 的逗号分隔数字**绘图**

```echo "[1,2,5,4,3,8,7]" | asciigraph```

以指定高度和宽度**绘图**

```seq 1 20 | asciigraph -h [10] -w [40]```

**添加标题说明**

```echo "[3,4,9,6,2,4,5,8]" | asciigraph -c "CPU load"```

从数据流生成**实时图表**

```[your-metrics-command] | asciigraph -r -w [60] -h [15]```

带图例的**多序列**图

```asciigraph -sn [2] -sl "a,b" -sc "blue,red"```

为超过/低于阈值的点**着色**

```echo "[1,2,5,9,3]" | asciigraph -ca "red,4" -cb "green,2"```

# SYNOPSIS

**asciigraph** [*options*]

# DESCRIPTION

**asciigraph** 是一个小型命令行工具（源自 Go 的 **asciigraph** 软件包），可在终端中渲染轻量级的 ASCII 折线图。它从标准输入读取数值数据点（可拆分为多个序列），打印出文本形式的图形，支持自定义尺寸、标题、坐标轴范围、颜色、图例，并能为流式数据实时刷新。

可通过 **go install github.com/guptarohit/asciigraph/cmd/asciigraph@latest** 安装，也可使用发布页的二进制文件或已发布的容器镜像。

# PARAMETERS

**-w** *width*

> 图表宽度，单位为列。

**-h** *height*

> 图表高度，单位为文本行（0 表示自动缩放）。

**-c** *caption*

> 显示在图表下方的说明文字。

**-d** *delimiter*

> 在输入流中切分数据点的分隔符（默认 **,**）。

**-sn** *n*

> 输入数据中的序列（列）数（默认 1）。

**-sl** *legends*

> 逗号分隔的各序列图例。

**-sc** *colors*

> 逗号分隔的各序列颜色。

**-r**

> 为流式输入启用实时绘图。

**-f** *fps*

> 启用实时模式时的每秒帧数（默认 24）。

**-b** *buffer*

> 实时模式的数据点缓冲区大小（默认等于宽度）。

**-lb** / **-ub** *value*

> 垂直轴的下界/上界。

**-p** *precision*

> Y 轴标签的精度（默认 2）。

**-o** *offset*

> 标签的列偏移量（默认 3）。

**-ca** / **-cb** *color,value*

> 为高于/低于阈值的数据点着色（例如 **red,4**）。

**-g** *palette*

> 渐变着色（**spectrum** 或逗号分隔的颜色节点）。

**-ac** / **-lc** / **-cc** *color*

> 坐标轴、标签和标题的颜色。

运行 **asciigraph --help** 可查看你的构建版本支持的完整选项列表。

# CAVEATS

需要能够良好显示等宽 ASCII/Unicode 制表字符的终端。颜色选项需要支持颜色的终端。实时模式面向连续数据流；通过管道传入的有限输入通常只绘制一次。

# INSTALL

```dnf: sudo dnf install asciigraph```

```aur: yay -S asciigraph```

```nix: nix profile install nixpkgs#asciigraph```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[gnuplot](/man/gnuplot)(1), [termgraph](/man/termgraph)(1), [youplot](/man/youplot)(1)

# RESOURCES

```[Source code](https://github.com/guptarohit/asciigraph)```

<!-- verified: 2026-07-19 -->
