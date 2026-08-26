# TAGLINE

在终端中绘制图表

# TLDR

**从文件创建柱状图**

```termgraph [data.txt]```

**用自定义标题创建图表**

```termgraph --title "[Monthly Sales]" [data.txt]```

**创建彩色图表**

```termgraph --color [red] [data.txt]```

**创建垂直柱状图**

```termgraph --vertical [data.txt]```

**创建堆叠柱状图**

```termgraph --stacked [data.txt]```

**创建直方图**

```termgraph --histogram --bins [10] [data.txt]```

**自定义图表宽度**

```termgraph --width [80] [data.txt]```

**从 stdin 创建图表**

```cat [data.txt] | termgraph```

# SYNOPSIS

**termgraph** [_options_] [_filename_]

# PARAMETERS

**--title** _title_
> 显示在图表上方的标题。

**--width** _n_
> 图表宽度（以字符计，默认为 50）。

**--format** _format_
> 数值的格式说明符。

**--suffix** _suffix_
> 追加到所有数据点之后的字符串。

**--no-labels**
> 隐藏标签列。

**--no-values**
> 隐藏条形末端的数值。

**--space-between**
> 每行之后打印一个换行。

**--color** _color_
> 条形颜色：red、blue、green、magenta、yellow、black、cyan。

**--vertical**
> 垂直显示条形。

**--stacked**
> 显示堆叠柱状图。

**--histogram**
> 从原始数据生成直方图。

**--bins** _n_
> 直方图的分组数量。

**--different-scale**
> 每个类别使用不同的比例。

**--calendar**
> 显示日历热力图。

**--start-dt** _date_
> 日历图表的起始日期。

**--custom-tick** _char_
> 自定义刻度字符（支持 emoji）。

**--delim** _char_
> 自定义分隔符（默认为逗号或空格）。

**--verbose**
> 启用详细输出。

# DESCRIPTION

**termgraph** 是一个 Python 命令行工具，用于在终端中绘制基础图表。它支持柱状图、堆叠图、直方图和日历热力图，并且可以水平或垂直显示。

数据采用简单的格式：第一列为标签，后续列为数值，以逗号或空格分隔。多个数值列会生成分组或堆叠图表。

该工具支持将 emoji 字符用作刻度标记，可以实现富有创意的可视化。它还可以作为 Python 库以编程方式生成图表。

通过 pip 安装：`pip install termgraph`

# CAVEATS

需要 Python 3。终端宽度限制图表尺寸。颜色支持取决于终端能力。复杂图表在狭窄的终端中可能无法正确渲染。

# HISTORY

**termgraph** 由 Marcus Kazmierczak 创建，旨在提供一种直接在终端中可视化数据的简单方式。对于命令行工作流和脚本而言，它是图形化图表工具的快速替代品。

# SEE ALSO

[gnuplot](/man/gnuplot)(1), [spark](/man/spark)(1)
