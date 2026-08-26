# TAGLINE

基于普通 SSH 连接的透明类 VPN 隧道

# TLDR

**隧道转发所有流量**

```sshuttle -r [user@host] 0/0```

**隧道转发指定网络**

```sshuttle -r [user@host] [192.168.0.0/24]```

**隧道转发多个网络**

```sshuttle -r [user@host] [10.0.0.0/8] [172.16.0.0/12]```

**排除地址**

```sshuttle -r [user@host] 0/0 -x [192.168.1.0/24]```

**隧道转发 DNS**

```sshuttle --dns -r [user@host] 0/0```

**自动检测网络**（来自服务器路由）

```sshuttle -r [user@host] --auto-nets```

**详细输出模式**

```sshuttle -v -r [user@host] [10.0.0.0/8]```

# SYNOPSIS

**sshuttle** [_-r server_] [_--dns_] [_-x exclude_] [_options_] _subnets_

# PARAMETERS

**-r** _SERVER_
> 远程服务器（user@host）。

**--dns**
> 对 DNS 查询建立隧道。

**-x** _SUBNET_
> 排除子网。

**-l** _ADDR_
> 监听地址。

**--auto-nets**
> 自动检测服务器网络。

**-H**, **--auto-hosts**
> 扫描远程的主机名，并在隧道存续期间将其添加到 `/etc/hosts`。

**-N**, **--auto-nets**
> 读取远程路由表，对远程可达的所有网络建立隧道（上面长选项的别名）。

**-e** _CMD_, **--ssh-cmd** _CMD_
> 要使用的 SSH 命令行（默认：`ssh`）。

**-v**
> 详细输出。

**--daemon**
> 以守护进程方式运行。

**--pidfile** _FILE_
> PID 文件。

**--method** _METHOD_
> NAT 方式（auto、nat、tproxy）。

# DESCRIPTION

**sshuttle** 通过 SSH 创建类 VPN 的隧道。它将流量透明地重定向到远程服务器，无需配置 VPN 软件。

与 VPN 不同，sshuttle 只需要 SSH 访问权限。除 Python 外无需在服务器端安装任何东西。在 VPN 端口被封的环境中也能工作。

子网规格决定哪些流量走隧道。0/0 表示转发所有流量。具体子网则只路由匹配的流量。

DNS 隧道可防止 DNS 泄漏。远程 DNS 解析能向本地网络隐藏查询模式。

该工具使用 iptables/pf 重定向流量。本地需要 root 权限来设置路由。远程端只需要 SSH 访问权限。

auto-nets 会读取远程路由表，对其所有可达网络建立隧道。

# CAVEATS

本地需要 root 权限。不是完整的 VPN（默认不支持 UDP）。SSH 会带来额外延迟。某些应用程序可能无法通过隧道工作。

# HISTORY

**sshuttle** 由 **Avery Pennarun** 于 **2010 年**前后创建。它被称为"穷人版 VPN"，只要 SSH 可用就能工作。

# INSTALL

```dnf: sudo dnf install sshuttle```

```pacman: sudo pacman -S sshuttle```

```zypper: sudo zypper install sshuttle```

```brew: brew install sshuttle```

```nix: nix profile install nixpkgs#sshuttle```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ssh](/man/ssh)(1), [openvpn](/man/openvpn)(8), [wg](/man/wg)(8), [proxychains](/man/proxychains)(1)
