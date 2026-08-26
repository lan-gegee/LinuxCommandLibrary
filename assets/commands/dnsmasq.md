# TAGLINE

轻量级 DNS 转发器和 DHCP 服务器

# TLDR

**启动 dnsmasq** 作为 DNS 转发器

```dnsmasq```

**使用指定的配置文件启动**

```dnsmasq -C [/etc/dnsmasq.conf]```

**以前台模式运行**并输出调试信息

```dnsmasq -d```

**测试配置**语法

```dnsmasq --test```

为子网**启用 DHCP 启动**

```dnsmasq --dhcp-range=[192.168.1.50,192.168.1.150,12h]```

**指定上游 DNS 服务器**

```dnsmasq --server=[8.8.8.8]```

**作为本地域名的权威服务器**启动

```dnsmasq --local=/[mydomain.local]/```

利用 hosts 文件**屏蔽广告**

```dnsmasq --addn-hosts=[/etc/hosts.ads]```

# SYNOPSIS

**dnsmasq** [_options_]

# DESCRIPTION

**dnsmasq** 是面向小型网络的轻量级 DNS 转发器和 DHCP 服务器。它在一个高效的单体软件包中提供 DNS 缓存、DHCP、TFTP 和 PXE 网络启动服务。

作为 DNS 服务器时，dnsmasq 将查询转发给上游服务器并缓存响应，降低延迟并节省带宽。它读取 /etc/hosts 进行本地名称解析，支持自定义本地域名，还可以基于 DNS 实现广告屏蔽。

DHCP 服务器支持动态和静态地址分配，并通过 BOOTP、PXE 和 TFTP 支持网络启动。dnsmasq 常用于路由器、嵌入式系统，以及作为本地开发的 DNS/DHCP 方案。

# PARAMETERS

**-d**
> 调试模式：前台运行，日志输出到 stderr。

**-k**
> 保持前台运行，不转为守护进程。

**-C** _file_
> 使用指定的配置文件。

**--test**
> 检查配置语法。

**-p** _port_
> 监听指定的 DNS 端口。

**-a** _address_
> 监听指定的地址。

**--dhcp-range=** _range_
> 启用 DHCP 并设置地址范围。

**--dhcp-host=** _config_
> 静态 DHCP 分配。

**-h**, **--no-hosts**
> 不读取 /etc/hosts。

**-H**, **--addn-hosts=** _file_
> 额外的 hosts 文件。

**--local=** _domain_
> 对指定域名作权威应答。

**--server=** _address_
> 上游 DNS 服务器。

**-R**, **--no-resolv**
> 不从 /etc/resolv.conf 读取上游服务器。

**-r**, **--resolv-file=** _file_
> 从指定文件而非 /etc/resolv.conf 读取上游域名服务器。

**--cache-size=** _n_
> DNS 缓存条数（默认 150）。

**--address=** _/domain/address_
> 为某域名下的所有主机返回指定地址。可用于屏蔽或重定向。

**--log-queries**
> 记录 DNS 查询日志。

# CONFIGURATION

**/etc/dnsmasq.conf**
> 主配置文件。包含 DNS 和 DHCP 设置、上游服务器、域名配置以及 DHCP 地址范围。

**/etc/hosts**
> 本地主机名到 IP 的映射。除非指定 --no-hosts，dnsmasq 会读取它进行本地 DNS 解析。

**/etc/dnsmasq.d/**
> 存放额外配置片段的目录。其中的文件会被自动并入主配置。

# CAVEATS

每个网络接口上只能运行一个 DNS/DHCP 服务器。在某些系统上与 systemd-resolved 冲突（需禁用或配置共存）。DHCP 需要适当的网络权限。大型网络可能需要功能完整的 DHCP 服务器。

# HISTORY

**dnsmasq** 由 **Simon Kelley** 于 **2000 年**创建，最初是拨号连接用的简易 DNS 转发器。后来加入了 DHCP 功能，并在嵌入式 Linux 系统、路由器（OpenWrt、DD-WRT）和开发环境中广受欢迎。该项目至今仍在活跃维护，并被大多数 Linux 发行版收录。

# INSTALL

```apt: sudo apt install dnsmasq-base```

```dnf: sudo dnf install dnsmasq```

```pacman: sudo pacman -S dnsmasq```

```apk: sudo apk add dnsmasq```

```zypper: sudo zypper install dnsmasq```

```brew: brew install dnsmasq```

```nix: nix profile install nixpkgs#dnsmasq```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[named](/man/named)(8), [dhcpd](/man/dhcpd)(8)
