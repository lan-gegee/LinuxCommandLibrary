# TAGLINE

数据包捕获文件编辑器和转换器

# TLDR

**按范围提取数据包**

```editcap -r [input.pcap] [output.pcap] [1-100]```

**移除重复数据包**

```editcap -d [input.pcap] [output.pcap]```

**按数据包数量分割**

```editcap -c [1000] [input.pcap] [output.pcap]```

**按时长分割**

```editcap -i [60] [input.pcap] [output.pcap]```

**转换格式**

```editcap -F [pcapng] [input.pcap] [output.pcapng]```

**更改快照长度**

```editcap -s [128] [input.pcap] [output.pcap]```

# SYNOPSIS

**editcap** [_options_] _infile_ _outfile_ [_packet_range_]

# PARAMETERS

**-r** _range_
> 只保留范围内的数据包。

**-d**
> 移除重复数据包。

**-D** _window_
> 去重窗口（默认 5）。

**-c** _count_
> 按每文件 count 个数据包分割。

**-i** _seconds_
> 按时间间隔分割。

**-F** _format_
> 输出文件格式。

**-s** _snaplen_
> 将数据包截断到指定长度。

**-t** _adjustment_
> 调整时间戳。

**-S** _offset_
> 设置起始时间。

**-A** _time_
> 只保留该时间之后的数据包。

**-B** _time_
> 只保留该时间之前的数据包。

**-T** _type_
> 设置封装类型。

# DESCRIPTION

**editcap** 是 Wireshark 套件中的数据包捕获文件编辑器。它读取捕获文件并将其中一部分或修改后的版本写入新文件，支持格式转换、数据包筛选和时间调整。

常见用途包括分割大型捕获文件、移除重复数据包、提取时间范围，以及在 pcap 和 pcapng 等捕获格式之间进行转换。

# CAVEATS

不会修改原始文件。某些操作会将整个文件加载到内存中。数据包范围从 1 开始计数。格式转换可能丢失元数据。属于 Wireshark 的一部分；需要 wireshark 或 tshark 软件包。

# HISTORY

editcap 是 **Wireshark** 项目的一部分，该项目最初名为 **Ethereal**，由 **Gerald Combs** 于 **1998 年**创建。editcap 提供命令行的捕获文件处理能力，与图形化的 Wireshark 分析器相辅相成。

# INSTALL

```apt: sudo apt install wireshark-common```

```apk: sudo apk add wireshark-common```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wireshark](/man/wireshark)(1), [tshark](/man/tshark)(1)
