# TAGLINE

注册 mDNS 主机名到地址的映射

# TLDR

**注册**主机名到 IP 地址的映射

```avahi-publish-address [hostname] [ip_address]```

为主机名**注册**一个 IPv4 地址

```avahi-publish-address myserver.local 192.168.1.100```

为主机名**注册**一个 IPv6 地址

```avahi-publish-address myserver.local fe80::1```

以详细模式**注册**

```avahi-publish-address -v [hostname] [ip_address]```

在特定域中**注册**

```avahi-publish-address --domain=[domain] [hostname] [ip_address]```

**注册**时不发布反向 DNS 条目

```avahi-publish-address --no-reverse [hostname] [ip_address]```

# SYNOPSIS

**avahi-publish-address** [_options_] _hostname_ _address_

# PARAMETERS

**-v, --verbose**
> 启用包含详细信息的详细输出

**-d, --domain=**_DOMAIN_
> 指定要注册到的 mDNS 域名（默认为 .local）

**-R, --no-reverse**
> 不为该地址发布反向 DNS（PTR）条目

**-f, --no-fail**
> 守护进程不可用时继续等待并重连

**-h, --help**
> 显示帮助信息

**-V, --version**
> 显示版本信息

# DESCRIPTION

**avahi-publish-address** 是一个命令行工具，通过 Avahi 守护进程使用 mDNS（多播 DNS）注册主机名到地址的映射。此命令等同于 **avahi-publish -a**，是专门用于地址注册的便捷快捷方式。

该工具通过通告主机名及其关联的 IPv4 或 IPv6 地址来实现本地网络的名称解析。该主机名通常在本地网络中以 **hostname.local** 的形式解析，让其他设备能够按名称而非 IP 地址发现并连接到这台主机。

调用后，**avahi-publish-address** 连接到 Avahi 守护进程并持续维护该主机名到地址的映射，直到进程被终止。进程退出时映射会自动撤销。

默认情况下，该工具同时发布正向（名称到地址）和反向（地址到名称）DNS 条目。可以使用 **--no-reverse** 选项抑制反向条目。协议版本（IPv4 或 IPv6）会根据地址格式自动判断。

所发布的主机名可被本地网段上其他支持 mDNS 的设备发现，包括装有 Avahi 的 Linux 系统、带 Bonjour 的 macOS 系统，以及具备相应 mDNS 支持的 Windows 系统。

# CAVEATS

需要 **avahi-daemon** 正在运行。主机名注册仅在 **avahi-publish-address** 进程存活期间有效；终止进程即移除映射。如需持久的主机名注册，请在 **/etc/avahi/hosts** 中配置静态映射。

# INSTALL

```apt: sudo apt install avahi-utils```

```dnf: sudo dnf install avahi-tools```

```apk: sudo apk add avahi-tools```

```zypper: sudo zypper install avahi-utils```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[avahi-publish](/man/avahi-publish)(1), [avahi-publish-service](/man/avahi-publish-service)(1), [avahi-resolve](/man/avahi-resolve)(1), [avahi-browse](/man/avahi-browse)(1), [avahi-daemon](/man/avahi-daemon)(8)
