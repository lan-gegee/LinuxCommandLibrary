# TAGLINE

面向故障硬盘的数据恢复工具

# TLDR

使用映射文件对设备制作**镜像**

```sudo ddrescue [/dev/sdb] [path/to/image.dd] [path/to/mapfile]```

磁盘对磁盘**克隆**的第一遍（跳过刮擦阶段）

```sudo ddrescue -f -n [/dev/sdX] [/dev/sdY] [path/to/mapfile]```

以直接磁盘访问方式**重试坏扇区** 3 次

```sudo ddrescue -d -f -r3 [/dev/sdX] [/dev/sdY] [path/to/mapfile]```

# SYNOPSIS

**ddrescue** [_options_] _infile_ _outfile_ [_mapfile_]

# DESCRIPTION

**ddrescue** 是一款数据恢复工具，可将数据从一个块设备复制到另一个块设备，并以智能方式处理读取错误。与遇到第一个读取错误就停止的 dd 不同，ddrescue 会跳过坏扇区继续复制完好的数据，之后再返回问题区域反复重试。

映射文件（旧版本称为 logfile）记录哪些块已成功复制、哪些失败、哪些尚未尝试。因此操作可以中断并在之后恢复而无需从头开始，使得跨越数天或数周的多遍处理成为现实。第一遍通常用 -n 快速复制所有可读数据并跳过错误；后续各遍则以不同策略集中处理坏扇区。

ddrescue 采用精密算法来最大限度地从故障硬盘中抢救数据。它可以反向读取、尝试不同的块大小，并在重试之间加入延迟进行多次尝试——因为故障硬盘有时会暂时变得"配合"一些。对于从物理受损介质恢复数据而言，这款工具不可或缺，能应对传统复制工具完全失败的场景。务必将数据恢复到备用磁盘上，而不是尝试原地恢复。

# PARAMETERS

**-f, --force**
> 覆盖输出设备

**-n, --no-scrape**
> 跳过刮擦阶段（加快第一遍速度）

**-r, --retry-passes** _n_
> 坏扇区的最大重试遍数

**-d, --direct**
> 使用直接 I/O

**-R, --reverse**
> 反向读取输入

# CAVEATS

始终使用映射文件以便断点续传。写入设备时必须加 -f 标志。最佳做法是先用 -n 快速跑一遍，再对坏扇区进行重试遍。不要把 GNU ddrescue 与目标相似但不同的 dd_rescue 混淆。

# HISTORY

**GNU ddrescue** 由 Antonio Diaz Diaz 编写，首次发布于 **2004 年**。它的诞生是为了解决 dd 遇到读取错误无法继续的问题，现已成为从故障硬盘抢救数据的标准自由软件工具。

# INSTALL

```apt: sudo apt install gddrescue```

```dnf: sudo dnf install ddrescue```

```pacman: sudo pacman -S ddrescue```

```apk: sudo apk add ddrescue```

```brew: brew install ddrescue```

```nix: nix profile install nixpkgs#ddrescue```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dd](/man/dd)(1), [testdisk](/man/testdisk)(8), [photorec](/man/photorec)(1)

# RESOURCES

```[Homepage](https://www.gnu.org/software/ddrescue/)```

```[Documentation](https://www.gnu.org/software/ddrescue/manual/ddrescue_manual.html)```

<!-- verified: 2026-07-11 -->
