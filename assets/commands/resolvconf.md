# TAGLINE

动态管理 DNS 解析器配置

# TLDR

**更新 DNS 配置**

```resolvconf -u```

**添加接口配置**

```echo "nameserver 8.8.8.8" | resolvconf -a [eth0]```

**删除接口配置**

```resolvconf -d [eth0]```

**列出接口**

```resolvconf -l```

**显示当前 resolv.conf**

```cat /etc/resolv.conf```

# SYNOPSIS

**resolvconf** [_-a interface_] [_-d interface_] [_-u_] [_options_]

# PARAMETERS

**-a** _INTERFACE_
> 添加/更新接口配置。

**-d** _INTERFACE_
> 删除接口配置。

**-u**
> 更新 resolv.conf。

**-l**
> 列出接口。

**-i** _PATTERN_
> 包含的接口。

**-x** _PATTERN_
> 排除的接口。

**-p**
> 将接口 resolv.conf 标记为私有。

**-m** _metric_
> 设置用于优先级排序的接口度量值。

**-f**
> 忽略不存在的接口。

# DESCRIPTION

**resolvconf** 是一个动态管理系统 DNS 解析器配置（**/etc/resolv.conf**）的框架。它不允许各个网络工具直接覆盖该文件，而是聚合来自 DHCP 客户端、VPN 连接和 NetworkManager 等多个来源的 DNS 信息，然后基于优先级排序生成统一的 resolv.conf。

每个网络接口通过 **-a** 标志向 resolvconf 注册其 DNS 服务器和搜索域，并在连接终止时使用 **-d** 移除。该框架通过合并所有已注册的输入来确定最终配置，较早注册的接口具有更高的优先级。静态条目可以通过 head 和 tail 配置文件添加，它们会被前置或追加到生成的输出中。

存在多种实现，包括 openresolv 和 Debian 的 resolvconf 软件包，各自的功能略有不同。在基于 systemd 的系统上，**systemd-resolved** 可能提供类似的功能，根据配置的不同，它可以与 resolvconf 共存或发生冲突。

# CONFIGURATION

**/etc/resolv.conf**
> 包含聚合后 DNS 解析器配置的生成文件。由 resolvconf 管理，不应手动编辑。

**/etc/resolvconf/resolv.conf.d/head**
> 前置到生成的 resolv.conf 的静态内容。

**/etc/resolvconf/resolv.conf.d/tail**
> 追加到生成的 resolv.conf 的静态内容。

**/etc/resolvconf/interface-order**
> 定义用于 DNS 解析的网络接口优先级排序。

# CAVEATS

可能与 systemd-resolved 冲突。各发行版的实现各不相同。有些使用 openresolv，有些使用 resolvconf。

# HISTORY

**resolvconf** 为处理来自多个网络来源的动态 DNS 配置而创建。存在多种实现，包括 openresolv 和 Debian 的 resolvconf 软件包。

# INSTALL

```apt: sudo apt install systemd-resolved```

```dnf: sudo dnf install systemd-resolved```

```pacman: sudo pacman -S openresolv```

```apk: sudo apk add openresolv```

```zypper: sudo zypper install systemd-resolved```

```nix: nix profile install nixpkgs#openresolv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemd-resolve](/man/systemd-resolve)(1), [resolvectl](/man/resolvectl)(1), [dhclient](/man/dhclient)(1), [nmcli](/man/nmcli)(1)
