# TAGLINE

Samba 网络工具

# TLDR

**列出服务器上的共享**

```net share```

**列出会话**

```net session```

**查看用户信息**

```net user [username]```

**加入域**

```net ads join -U [admin]```

**映射网络驱动器**

```net use [Z:] [\\\\server\\share]```

**显示工作组成员**

```net rpc group members "[group]" -S [server]```

# SYNOPSIS

**net** [_command_] [_options_]

# PARAMETERS

_COMMAND_
> Net 子命令。

**share**
> 管理共享。

**session**
> 查看会话。

**user**
> 用户管理。

**ads**
> Active Directory 操作。

**rpc**
> RPC 命令。

**--help**
> 显示帮助信息。

# DESCRIPTION

**net** 是一款 Samba 网络工具。它在 Linux 上提供 Windows 网络功能。

该工具管理共享、用户和域。属于 Samba 套件。

# CAVEATS

属于 Samba。面向 Windows 网络。需要正确的配置。

# HISTORY

net 是 **Samba** 的一部分，在 Unix 系统上提供与 Windows 兼容的网络操作。

# INSTALL

```apt: sudo apt install samba-common-bin```

```dnf: sudo dnf install samba-common-tools```

```apk: sudo apk add samba-common-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[smbclient](/man/smbclient)(1), [samba](/man/samba)(1), [wbinfo](/man/wbinfo)(1)
