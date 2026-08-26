# TAGLINE

收集 SteamOS 系统诊断信息

# TLDR

**转储全部系统信息**

```sudo steamos-dump-info```

**列出可用的分区段**

```steamos-dump-info --list-sections```

**以详细输出转储**

```sudo steamos-dump-info --verbose```

**不压缩输出地转储**

```sudo steamos-dump-info --no-compress```

**仅转储指定的分区段**

```sudo steamos-dump-info --section [network]```

# SYNOPSIS

**steamos-dump-info** [_options_]

# PARAMETERS

**-h**, **--help**
> 显示帮助消息。

**-L**, **--list-sections**
> 列出所有可以单独转储的可用分区段。

**--section** _NAME_
> 仅转储指定的分区段。可多次使用。

**-V**, **--version**
> 显示版本信息。

**-v**, **--verbose**
> 启用详细输出，提供收集过程的更多信息。

**-q**, **--quiet**
> 抑制大部分输出，只显示关键消息。

**--no-compress**
> 创建未压缩的目录而不是压缩归档。

# DESCRIPTION

**steamos-dump-info** 将 SteamOS 系统的综合诊断信息收集到压缩归档中。输出内容包括系统日志（journalctl、/var/log）、硬件信息（lspci、lsusb、/proc 条目）、网络配置、Steam 客户端日志、Xorg 日志以及系统配置文件。

Valve 支持团队在排查 Steam Deck 和 SteamOS 问题时通常会要求提供生成的归档，也可以将其上传到错误跟踪器或支持工单。

# CAVEATS

获取完整系统信息需要 root 权限。仅适用于 SteamOS（Steam Deck 及其他 Valve 设备）。输出的归档可能包含敏感的系统信息。

# HISTORY

**steamos-dump-info** 属于 **Valve** 为 Steam Deck 及其他基于 SteamOS 的设备开发的系统工具。

# SEE ALSO

[uname](/man/uname)(1), [lshw](/man/lshw)(1), [dmidecode](/man/dmidecode)(8), [steamos-finalize-install](/man/steamos-finalize-install)(1)
