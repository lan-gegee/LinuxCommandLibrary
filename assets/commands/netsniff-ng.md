# TAGLINE

高性能数据包嗅探器

# TLDR

**从接口捕获流量到 pcap 文件**

```netsniff-ng --in [eth0] --out [capture.pcap]```

**将 pcap 文件重放**到网络

```netsniff-ng --in [capture.pcap] --out [eth0]```

捕获时**应用 tcpdump/BPF 过滤器**

```netsniff-ng --in [eth0] --out [capture.pcap] "[tcp port 80]"```

**捕获并将数据包打印**到控制台（不写入文件）

```netsniff-ng --in [eth0] --out - --verbose```

**将输出轮转**到目录中，每个周期生成一个文件

```netsniff-ng --in [eth0] --out [dir/] --interval [60sec]```

为高速捕获**设置内核环形缓冲区大小**

```netsniff-ng --in [eth0] --out [capture.pcap] --ring-size [64MiB]```

# SYNOPSIS

**netsniff-ng** [_options_] [_filter-expression_]

# PARAMETERS

**-i**, **-d**, **--in**, **--dev** _INPUT_
> 输入来源：网络设备、pcap 文件，或表示 stdin 的 **-**。

**-o**, **--out** _OUTPUT_
> 输出目标：网络设备、pcap 文件、目录（配合 --interval），或表示 stdout 的 **-**。

**-f**, **--filter** _EXPR_
> 应用底层（BPF）或高层（tcpdump 风格）的数据包过滤器。命令行上的裸过滤表达式也会被接受。

**--ring-size** _SIZE_
> 设置 mmap 环形缓冲区大小，例如 **10MiB**、**1GiB**。

**-F**, **--interval** _NUM_
> 写入目录时，每 NUM 个数据包或按时间/大小（如 **60sec**、**100MiB**）开始一个新的 pcap 文件。

**-s**, **--silent**
> 不将捕获的数据包打印到控制台。

**-V**, **--verbose**
> 以详细形式打印/转储每个捕获的数据包。

**-T**, **--magic** _PCAP_MAGIC_
> 设置 pcap 文件格式的魔数（链路层/时间戳变体）。

**-b**, **--bind-cpu** _CPU_
> 将捕获进程绑定到指定的 CPU。

**-H**, **--prio-high**
> 以高调度优先级运行该进程。

**-V**, **--version**, **-h**, **--help**
> 显示版本或帮助信息。

# DESCRIPTION

**netsniff-ng** 是一款高性能、零拷贝的网络分析、数据包捕获与重放工具。它利用 Linux 内核的 **PACKET_MMAP** RX_RING/TX_RING 接口在内核态与用户态之间移动数据包而无需拷贝，从而实现接近线速的捕获和发送。

它可以将实时流量捕获到 pcap 文件、把 pcap 重放到接口上，并在长期采集中按周期轮转为多个文件。过滤器同时支持原始 BPF 表达式和 tcpdump 风格的表达式。

# CAVEATS

需要 root 权限（或 **CAP_NET_RAW** / **CAP_NET_ADMIN**）。它是 netsniff-ng 工具集的一员，该工具集还包括 trafgen、mausezahn、ifpps、flowtop 和 astraceroute。某些链路类型和时间戳格式取决于驱动程序与内核的支持情况。

# HISTORY

**netsniff-ng** 由 **Daniel Borkmann** 于 **2009 年**创建，是一款自由的 Linux 原生零拷贝数据包分析器，后来发展为更完整的 netsniff-ng 网络工具集。它采用 GPLv2 许可证发布。

# INSTALL

```apt: sudo apt install netsniff-ng```

```dnf: sudo dnf install netsniff-ng```

```pacman: sudo pacman -S netsniff-ng```

```zypper: sudo zypper install netsniff-ng```

```nix: nix profile install nixpkgs#netsniff-ng```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tcpdump](/man/tcpdump)(1), [wireshark](/man/wireshark)(1), [tshark](/man/tshark)(1)
