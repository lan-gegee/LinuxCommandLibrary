# TAGLINE

启用 **/etc/network/interfaces** 中配置的网络接口

# TLDR

**启用**指定接口

```ifup [eth0]```

启用标记为 auto 的**所有**接口

```ifup -a```

# SYNOPSIS

**ifup** [_options_] _interface_

# PARAMETERS

**-a**, **--all**
> 启用 /etc/network/interfaces 中标记为 auto 的所有接口

**-v**, **--verbose**
> 打印详细信息

**--force**
> 即使接口看似已启用也强制配置

**--no-scripts**
> 不运行任何前置/后置脚本

# DESCRIPTION

**ifup** 启用 **/etc/network/interfaces** 中配置的网络接口。它读取接口定义并执行相应的命令和脚本来配置接口，包括设置 IP 地址、运行 DHCP 客户端以及执行用户定义的脚本。

该命令处理完整的接口初始化流程，包括配置文件中定义的所有依赖或前置条件。

# CAVEATS

属于 ifupdown 软件包，主要用于基于 Debian 的系统。现代系统通常改用 NetworkManager 或 systemd-networkd。要求接口已在 /etc/network/interfaces 中定义。

# HISTORY

ifup 属于 ifupdown 软件包——Debian 及其衍生版传统的网络接口配置系统。虽然仍在广泛使用，但在桌面系统上正逐渐被 NetworkManager 取代，在服务器上则被 systemd-networkd 取代。

# INSTALL

```apt: sudo apt install ifupdown```

```apk: sudo apk add ifupdown-ng```

```nix: nix profile install nixpkgs#ifupdown-ng```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ifdown](/man/ifdown)(8), [ip](/man/ip)(8)
