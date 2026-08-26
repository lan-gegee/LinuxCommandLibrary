# TAGLINE

通过 mDNS 将主机名解析为 IP 地址

# TLDR

此命令是 **avahi-resolve --name** 的别名。

**将**主机名解析为 IP 地址

```avahi-resolve-host-name [hostname.local]```

只**解析**为 IPv4 地址

```avahi-resolve-host-name -4 [hostname.local]```

只**解析**为 IPv6 地址

```avahi-resolve-host-name -6 [hostname.local]```

# SYNOPSIS

**avahi-resolve-host-name** [_OPTIONS_] _hostname_ ...

# DESCRIPTION

**avahi-resolve-host-name** 通过 Avahi 守护进程使用 mDNS/DNS-SD 将主机名解析为 IP 地址。它等同于带 **--name** 标志运行 **avahi-resolve**。

# INSTALL

```apt: sudo apt install avahi-utils```

```dnf: sudo dnf install avahi-tools```

```apk: sudo apk add avahi-tools```

```zypper: sudo zypper install avahi-utils```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[avahi-resolve](/man/avahi-resolve)(1), [avahi-resolve-address](/man/avahi-resolve-address)(1), [avahi-browse](/man/avahi-browse)(1), [avahi-daemon](/man/avahi-daemon)(8)

# RESOURCES

```[Homepage](https://avahi.org/)```

```[Source code](https://github.com/avahi/avahi)```

<!-- verified: 2026-06-17 -->
