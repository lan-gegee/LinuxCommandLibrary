# TAGLINE

使用 BPF 的终端网络流量监控器

# TLDR

**监控所有网络流量**

```sudo netop```

**监控指定接口**

```sudo netop -n [eth0]```

# SYNOPSIS

**netop** [_options_]

# PARAMETERS

**-n** _INTERFACE_
> 指定要监控的网络接口。

# DESCRIPTION

**netop** 是一款基于终端的网络流量监控器，它使用 BPF（Berkeley Packet Filter）捕获并显示网络活动。它提供 TUI 界面，实时展示网络拓扑和流量统计，并支持自定义过滤规则。

# CAVEATS

捕获数据包需要 root 权限。系统必须支持 BPF。

# HISTORY

**netop** 由 **ZingerLittleBee** 创建，使用 **Rust** 编写。

# INSTALL

```nix: nix profile install nixpkgs#netop```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tcpdump](/man/tcpdump)(8), [iftop](/man/iftop)(8), [nethogs](/man/nethogs)(8)
