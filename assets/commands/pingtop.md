# TAGLINE

ping 多台服务器并以类 top 的终端界面显示结果

# TLDR

**ping 多台主机**

```pingtop [host1] [host2] [host3]```

以指定的数据包大小 **ping 主机**

```pingtop -s [64] [host1] [host2]```

**ping 主机并将结果记录**到文件

```pingtop -l [results.log] [host1] [host2]```

# SYNOPSIS

**pingtop** [_options_] _hosts_...

# PARAMETERS

**-s**, **--packetsize** _BYTES_
> 要发送的数据字节数（默认：56）。

**-l**, **--logto** _FILE_
> 将输出记录到文件。

# DESCRIPTION

**pingtop** 同时 ping 多台服务器，并在类 top 的终端用户界面中显示结果。它在一个视图中实时监控所有指定主机的延迟和丢包情况。

# CAVEATS

发送 ICMP 数据包需要 root 或 CAP_NET_RAW 能力。通过 `pip install pingtop` 安装。

# HISTORY

**pingtop** 由 **laixintao** 创建，用 **Python** 编写。

# INSTALL

```aur: yay -S pingtop```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ping](/man/ping)(1), [mtr](/man/mtr)(8), [gping](/man/gping)(1), [fping](/man/fping)(1), [hping3](/man/hping3)(1)
