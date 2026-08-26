# TAGLINE

注册 mDNS/DNS-SD 服务和地址映射

# TLDR

在本地网络上**注册**一项服务

```avahi-publish -s "[service_name]" [service_type] [port]```

带 TXT 记录**注册**服务

```avahi-publish -s "[service_name]" _http._tcp [port] "path=/index.html"```

**注册**主机名到 IP 地址的映射

```avahi-publish -a [hostname] [ip_address]```

以详细模式**注册**服务

```avahi-publish -s -v "[service_name]" [service_type] [port]```

在特定域中**注册**服务

```avahi-publish -s --domain=[domain] "[service_name]" [service_type] [port]```

带子类型**注册**

```avahi-publish -s --subtype=[subtype] "[service_name]" [service_type] [port]```

# SYNOPSIS

**avahi-publish** **-s** [_options_] _name_ _service-type_ _port_ [_TXT data ..._]

**avahi-publish** **-a** [_options_] _hostname_ _address_

# PARAMETERS

**-s, --service**
> 注册一项服务（需要名称、服务类型和端口）

**-a, --address**
> 注册主机名到地址的映射

**-v, --verbose**
> 启用包含详细信息的详细输出

**-H, --host=**_HOSTNAME_
> 为服务指定远程主机名

**-d, --domain=**_DOMAIN_
> 在指定域中发布（默认：.local）

**--subtype=**_SUBTYPE_
> 为主服务类型添加子类型注册（可重复）

**-R, --no-reverse**
> 跳过发布反向（地址到名称）条目

**-f, --no-fail**
> 守护进程不可用时继续等待并重连

**-h, --help**
> 显示帮助信息

**-V, --version**
> 显示版本信息

# DESCRIPTION

**avahi-publish** 是一个命令行工具，用于通过 Avahi 守护进程注册 mDNS/DNS-SD 服务或主机名到地址的映射。它借助 **mDNS**（多播 DNS）和 **DNS-SD**（DNS 服务发现）协议，在本地网络上实现网络服务通告和主机名解析。

该工具有两种主要工作模式：

> **服务注册模式**（**-s**）：通过指定 DNS-SD 服务名称（如 "Web Server"）、服务类型（如 _http._tcp）和 IP 端口号来注册网络服务。可以追加可选的 TXT 记录字符串，提供路径、版本或配置参数等附加服务元数据。

> **地址/主机名注册模式**（**-a**）：注册完全限定主机名与 IPv4 或 IPv6 地址之间的映射，从而支持基于 mDNS 的名称解析。

启动后，**avahi-publish** 连接到 Avahi 守护进程并维持注册状态，直到进程被终止。进程退出时注册会自动撤销。

服务类型遵循 DNS-SD 命名约定：**_service._proto**，其中 service 标识应用层协议（http、ssh、ftp），proto 为 _tcp 或 _udp。例如 HTTP 服务用 **_http._tcp**，SSH 用 **_ssh._tcp**。

默认情况下，服务发布在 **.local** 域中，但可以通过 **--domain** 选项更改。该工具还通过 **--subtype** 支持服务子类型，实现额外的服务分类。

# CAVEATS

需要 **avahi-daemon** 正在运行。注册仅在 **avahi-publish** 进程存活期间有效；终止进程即撤销服务通告。如需持久的服务注册，请使用 **/etc/avahi/services/** 中的服务定义文件。

# INSTALL

```apt: sudo apt install avahi-utils```

```dnf: sudo dnf install avahi-tools```

```apk: sudo apk add avahi-tools```

```zypper: sudo zypper install avahi-utils```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[avahi-publish-service](/man/avahi-publish-service)(1), [avahi-publish-address](/man/avahi-publish-address)(1), [avahi-resolve](/man/avahi-resolve)(1), [avahi-browse](/man/avahi-browse)(1), [avahi-daemon](/man/avahi-daemon)(8)

# RESOURCES

```[Homepage](https://avahi.org/)```

```[Source code](https://github.com/avahi/avahi)```

<!-- verified: 2026-06-17 -->
