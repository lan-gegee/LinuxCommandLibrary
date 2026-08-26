# TAGLINE

面向 Ubuntu 及其他 Linux 发行版的网络配置工具

# TLDR

**应用**网络配置并永久生效

```sudo netplan apply```

**生成**后端配置文件

```sudo netplan generate```

将接口配置为使用 **DHCP**

```sudo netplan set ethernets.[interface].dhcp4=true```

在超时时间内**试用**配置更改

```sudo netplan try --timeout [120]```

以**调试**输出方式应用

```sudo netplan --debug apply```

显示**当前状态**

```netplan status```

**获取**当前配置的值

```netplan get [ethernets]```

# SYNOPSIS

**netplan** [**--debug**] _command_ [_options_]

# COMMANDS

**apply**
> 应用网络配置并使其持久化

**generate**
> 生成特定于后端的配置文件

**try**
> 试用配置更改，支持自动回滚

**get**
> 获取当前的配置值

**set**
> 设置配置值

**status**
> 显示当前网络状态

**info**
> 显示可用特性

**ip**
> 从系统中获取 IP 信息（如 DHCP 租约）

**rebind**
> 将 SR-IOV 虚拟函数重新绑定到其驱动程序

# PARAMETERS

**--debug**
> 启用调试输出

**--root-dir** _path_
> 使用替代的根目录。

**--timeout** _seconds_
> try 命令回滚前的超时时间 [默认：120]。

**--config-file** _path_
> 使用指定的配置文件。

# CONFIGURATION

配置文件保存在 **/etc/netplan/*.yaml**

YAML 示例：
```
network:
  version: 2
  ethernets:
    eth0:
      dhcp4: true
```

# DESCRIPTION

**netplan** 是一款面向 Ubuntu 及其他 Linux 发行版的网络配置工具。它使用 YAML 文件描述网络接口，并为 NetworkManager 或 systemd-networkd 等后端渲染器生成配置。

这一抽象层让同一份配置可以配合不同的网络管理后端工作，从而简化跨环境的网络设置。

# CAVEATS

YAML 语法错误会导致配置无法应用。try 命令默认在 120 秒内未确认则自动回滚。必须安装某个后端（NetworkManager 或 systemd-networkd）。修改配置文件后需要执行 **apply** 才能生效。

# HISTORY

**netplan** 由 **Canonical** 为 Ubuntu 开发，首次出现于 Ubuntu 17.10。它旨在提供一套统一且人类可读的网络配置系统，并能兼容不同的网络后端。

# INSTALL

```apt: sudo apt install netplan.io```

```dnf: sudo dnf install netplan```

```pacman: sudo pacman -S netplan```

```nix: nix profile install nixpkgs#netplan```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[networkctl](/man/networkctl)(1), [nmcli](/man/nmcli)(1), [ip](/man/ip)(8)
