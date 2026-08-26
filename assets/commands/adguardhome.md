# TAGLINE

全网范围的广告与跟踪器拦截 DNS 服务器

# TLDR

**启动** AdGuard Home

```sudo adguardhome -s start```

**安装**为系统服务

```sudo adguardhome -s install```

**卸载**系统服务

```sudo adguardhome -s uninstall```

检查服务**状态**

```sudo adguardhome -s status```

以**自定义配置**启动

```adguardhome -c [/path/to/config.yaml]```

# SYNOPSIS

**adguardhome** [_-c config_] [_-w workdir_] [_-h host_] [_-p port_] [_-s command_]

# DESCRIPTION

**AdGuard Home** 是一款全网范围的广告、跟踪与恶意域名拦截软件。它以 DNS 服务器的形式运行，先根据拦截列表和自定义规则过滤请求，再把合法查询转发到上游。

该应用提供用于配置和统计数据的 Web 界面，支持 DNS-over-HTTPS、DNS-over-TLS 和 DNS-over-QUIC，并且可以取代路由器的 DHCP 服务器。

# PARAMETERS

**-s** _command_
> 服务控制：start、stop、restart、status、install、uninstall

**-c** _path_
> 配置文件的路径

**-w** _path_
> 工作目录的路径

**-h** _host_
> Web 界面绑定的主机

**-p** _port_
> Web 界面绑定的端口

**--no-check-update**
> 不检查更新

**--pidfile** _path_
> PID 文件的路径

**--verbose**
> 启用详细日志输出

# CONFIGURATION

**AdGuardHome.yaml**
> 主配置文件，通常位于工作目录（例如 /opt/AdGuardHome/）中。控制 DNS 设置、上游服务器、过滤规则、DHCP、客户端以及 Web 界面选项。

# CAVEATS

作为 DNS 服务器运行需要占用端口 53，这可能与 systemd-resolved 或其他 DNS 服务冲突。首次设置需要访问 Web 界面来完成配置。

# HISTORY

**AdGuard Home** 由 AdGuard Software Limited 开发，于 **2018** 年首次发布，是一款开源的全网广告拦截器。它被设计为可自托管的 Pi-hole 替代方案，并额外提供加密 DNS 协议等特性。

# INSTALL

```pacman: sudo pacman -S adguardhome```

```apk: sudo apk add adguardhome```

```nix: nix profile install nixpkgs#adguardhome```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[pihole](/man/pihole)(1), [dnsmasq](/man/dnsmasq)(1), [unbound](/man/unbound)(1)
