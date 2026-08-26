# TAGLINE

修复损坏的数据包捕获文件

# TLDR

**修复损坏的 pcap**

```pcapfix [corrupted.pcap]```

**修复并保存到新文件**

```pcapfix -o [fixed.pcap] [corrupted.pcap]```

**详细输出**

```pcapfix -v [corrupted.pcap]```

**深度扫描模式**

```pcapfix -d [corrupted.pcap]```

# SYNOPSIS

**pcapfix** [_options_] _file_

# PARAMETERS

_FILE_
> 损坏的 pcap 文件。

**-o** _OUTPUT_
> 输出文件。

**-v**
> 详细模式。

**-d**
> 深度扫描。

**-n**
> 修复 pcapng 文件。

# DESCRIPTION

**pcapfix** 修复损坏的数据包捕获文件。可修复 pcap 和 pcapng 文件。

该工具用于恢复网络抓包。可处理截断和损坏问题。

# CAVEATS

可能无法恢复全部数据。请备份原文件。支持 pcap 和 pcapng。

# HISTORY

pcapfix 是为**恢复损坏的**数据包捕获文件而创建的。

# INSTALL

```apt: sudo apt install pcapfix```

```nix: nix profile install nixpkgs#pcapfix```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tcpdump](/man/tcpdump)(1), [wireshark](/man/wireshark)(1), [editcap](/man/editcap)(1)
