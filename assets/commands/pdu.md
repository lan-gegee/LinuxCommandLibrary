# TAGLINE

高度并行、快速的目录树磁盘用量分析器

# TLDR

**显示当前目录的磁盘用量**

```pdu```

**显示指定目录的磁盘用量**

```pdu [path/to/directory]```

**比较多个目录**

```pdu [dir1] [dir2]```

**显示表观大小而非块大小**

```pdu --quantity=apparent-size [path/to/directory]```

**显示所有条目而不限大小**

```pdu --min-ratio=0 [path/to/directory]```

**以 JSON 输出**

```pdu --json-output [path/to/directory]```

**可视化之前保存的 JSON 文件**

```pdu --json-input < [disk-usage.json]```

**使用二进制单位显示磁盘用量（1K = 1024 B）**

```pdu --bytes-format=binary [path/to/directory]```

**计算大小时对硬链接去重**

```pdu --deduplicate-hardlinks [path/to/directory]```

# SYNOPSIS

**pdu** [_options_] [_files_...]

# DESCRIPTION

**pdu**（Parallel Disk Usage）是一个高度并行、快速的目录树分析器，可在终端中绘制磁盘用量的图形化条形图。它可以作为 dust 和 dutree 的替代品，并支持 JSON 输出与多目录比较。

默认情况下，**pdu** 按块大小计量、按大小对条目排序（从大到小）、显示深度限制为 10 层、隐藏小于总量 1% 的条目，并以公制单位（1K = 1000 B）显示大小。

# OPTIONS

**--bytes-format**, **-b** _FORMAT_
> 字节值的显示方式。可选值：**plain**（原始字节数）、**metric**（1K = 1000 B，默认）、**binary**（1K = 1024 B）。

**--quantity**, **-q** _MEASURE_
> 要度量的对象。可选值：**block-size**（默认）、**apparent-size**、**block-count**。

**--max-depth**, **-d** _N_
> 显示树的最大深度。用 **inf** 表示不限制。默认：**10**。

**--min-ratio**, **-m** _RATIO_
> 条目显示所需的最小大小占比（0–1）。默认：**0.01**（1%）。

**--total-width**, **-w** _N_
> 整个可视化图形的字符宽度。

**--top-down**
> 自上而下而不是自下而上打印树。

**--align-right**
> 把条形图的根端置于右侧。

**--no-sort**
> 不对分支排序；保持文件系统的顺序。

**--deduplicate-hardlinks**, **-H**
> 检测硬链接并从父节点中扣除其大小，避免重复计数。

**--progress**, **-p**
> 报告扫描进度。会有一定的性能开销。

**--silent-errors**, **-s**
> 抑制 stderr 上的文件系统错误消息。

**--threads** _N_
> 使用的线程数。接受正整数、**auto**（默认）或 **max**。

**--json-output**
> 以 JSON 形式打印磁盘用量数据，而不是渲染图表。

**--json-input**
> 从 stdin 读取先前导出的 JSON 并渲染成图表。

**-h**, **--help**
> 显示帮助信息。

**-V**, **--version**
> 显示版本信息。

# HISTORY

**pdu** 由 **Hoang Van Khai**（KSXGitHub）创建，使用 **Rust** 编写。

# SEE ALSO

[du](/man/du)(1), [dust](/man/dust)(1), [ncdu](/man/ncdu)(1), [gdu](/man/gdu)(1)
