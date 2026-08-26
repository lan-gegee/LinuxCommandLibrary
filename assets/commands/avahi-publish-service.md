# TAGLINE

在本地网络上注册 mDNS/DNS-SD 服务

# TLDR

**发布** mDNS 服务

```avahi-publish-service [MyService] [_http._tcp] [80]```

带**服务文本记录**发布

```avahi-publish-service [MyService] [_http._tcp] [80] ["path=/api"]```

在**特定主机**上发布

```avahi-publish-service -H [myhost.local] [MyService] [_http._tcp] [80]```

带**子类型**发布

```avahi-publish-service --subtype=[_printer._sub._http._tcp] [MyPrinter] [_http._tcp] [631]```

# SYNOPSIS

**avahi-publish-service** [_options_] _name_ _service-type_ _port_ [_txt-record_...]

# DESCRIPTION

**avahi-publish-service** 通过 Avahi 守护进程在本地网络上注册 mDNS/DNS-SD 服务，让其他使用 Avahi 或 Bonjour 兼容服务发现的设备可以发现这些服务。此命令等同于 **avahi-publish -s**，是专门用于服务注册的便捷快捷方式。

该工具需要服务名称、DNS-SD 服务类型（如 **_http._tcp**）和端口号。可选的 TXT 记录字符串可提供关于服务的附加元数据。还可以注册服务子类型以实现更细的分类。

注册仅在进程运行期间有效。进程终止时，服务通告会自动从网络中撤销。

# PARAMETERS

**-H**, **--host=**_HOSTNAME_
> 若服务不在本机上，为其指定主机名。必须是完全限定名，且可通过 mDNS 或单播 DNS 解析。

**-d**, **--domain=**_DOMAIN_
> 在指定域中发布。若省略，Avahi 守护进程将在其默认域（通常为 .local）中发布。

**--subtype=**_SUBTYPE_
> 为服务注册一个附加子类型。可多次传入。

**-f**, **--no-fail**
> 守护进程未运行时不失败。等待其出现，断开时自动重连。

**-v**, **--verbose**
> 启用详细模式。

**-V**, **--version**
> 显示版本信息。

**-h**, **--help**
> 显示帮助。

# CAVEATS

需要 avahi-daemon 正在运行。服务仅在命令运行期间存在。防火墙必须放行 mDNS（UDP 端口 5353）。服务名称在网络中必须唯一。

# HISTORY

**avahi-publish-service** 是 Avahi 项目的一部分，由 Lennart Poettering 创建，作为 Apple Bonjour/Zeroconf 协议的自由实现，于 **2005 年**前后首次发布。

# INSTALL

```apt: sudo apt install avahi-utils```

```dnf: sudo dnf install avahi-tools```

```apk: sudo apk add avahi-tools```

```zypper: sudo zypper install avahi-utils```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[avahi-publish](/man/avahi-publish)(1), [avahi-browse](/man/avahi-browse)(1), [avahi-daemon](/man/avahi-daemon)(8)
