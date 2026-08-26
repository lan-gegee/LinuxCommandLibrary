# TAGLINE

Samba 的 Windows 事件日志管理器

# TLDR

**创建事件日志**数据库

```eventlogadm -o addsource [Application] [/var/lib/samba/eventlog]```

**转储事件日志**

```eventlogadm -o dump [Application]```

**向日志写入事件**

```eventlogadm -o write [Application] [message]```

# SYNOPSIS

**eventlogadm** [_options_] _operation_ [_args_]

# PARAMETERS

_OPERATION_
> 操作：addsource、dump、write。

**-o** _OP_
> 要执行的操作。

**-s** _CONF_
> Samba 配置文件。

**addsource** _NAME_ _PATH_
> 创建事件日志源。

**dump** _NAME_
> 转储日志内容。

**write** _NAME_ _MSG_
> 写入事件。

# DESCRIPTION

**eventlogadm** 是一个 Samba 工具，用于在 Unix 系统上管理兼容 Windows 的事件日志。它可以创建、读取和写入 Windows 客户端能够访问的事件日志数据库。

该工具与 Samba 对 Windows Event Log 服务的实现配合工作。事件日志以 TDB（Trivial Database）格式存储，可以在 Windows 事件查看器中查看。

eventlogadm 有助于将 Unix 日志与以 Windows 为中心的管理工具集成起来。

# CONFIGURATION

**/etc/samba/smb.conf**
> Samba 服务器配置，其中定义事件日志的路径和设置。

# CAVEATS

需要先配置好 Samba。事件日志格式专为 Windows 兼容性设计。存储位置取决于 Samba 配置。

# HISTORY

eventlogadm 是 **Samba** 的一部分，为 Windows 网络协议的 Unix 实现提供 Windows 事件日志兼容能力。

# INSTALL

```apt: sudo apt install samba```

```dnf: sudo dnf install samba```

```pacman: sudo pacman -S samba```

```apk: sudo apk add samba-server```

```zypper: sudo zypper install samba```

```brew: brew install samba```

```nix: nix profile install nixpkgs#samba```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[samba](/man/samba)(7)
