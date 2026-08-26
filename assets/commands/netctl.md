# TAGLINE

Arch Linux 的网络配置文件管理器

# TLDR

**启动一个配置文件**

```sudo netctl start [profile]```

**停止一个配置文件**

```sudo netctl stop [profile]```

**开机时启用配置文件**

```sudo netctl enable [profile]```

**列出所有配置文件**

```netctl list```

**查看配置文件状态**

```netctl status [profile]```

**切换配置文件**

```sudo netctl switch-to [profile]```

# SYNOPSIS

**netctl** _command_ [_profile_]

# PARAMETERS

**start** _profile_
> 启动网络配置文件。

**stop** _profile_
> 停止网络配置文件。

**enable** _profile_
> 开机时启用。

**disable** _profile_
> 开机时不启用。

**list**
> 列出所有配置文件。

**status** _profile_
> 显示配置文件状态。

**switch-to** _profile_
> 切换到指定配置文件。

# DESCRIPTION

**netctl** 是 Arch Linux 的网络配置文件管理器。它通过配置文件管理网络配置，支持有线、无线、网桥、绑定（bond）和 VLAN。

netctl 基于 systemd，可以与 NetworkManager 共存（但通常不能同时运行）。

# PROFILE EXAMPLE

```
# /etc/netctl/ethernet-static
Interface=eth0
Connection=ethernet
IP=static
Address=('192.168.1.10/24')
Gateway='192.168.1.1'
DNS=('8.8.8.8')
```

# PROFILE LOCATION

```
/etc/netctl/
/etc/netctl/examples/
```

# CAVEATS

仅适用于 Arch Linux。每个接口只能对应一个配置文件。不要与 NetworkManager 同时使用。

# HISTORY

netctl 是为 **Arch Linux** 开发的 netcfg 替代品，利用 systemd 集成进行网络管理。

# INSTALL

```pacman: sudo pacman -S netctl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[networkctl](/man/networkctl)(1), [ip](/man/ip)(8), [NetworkManager](/man/NetworkManager)(8)
