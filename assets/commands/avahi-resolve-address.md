# TAGLINE

通过 mDNS 将 IP 地址解析为主机名

# TLDR

此命令是 **avahi-resolve --address** 的别名。

**将** IP 地址解析为主机名

```avahi-resolve-address [ip_address]```

一次**解析**多个地址

```avahi-resolve-address [ip1] [ip2]```

# SYNOPSIS

**avahi-resolve-address** [_OPTIONS_] _address_ ...

# DESCRIPTION

**avahi-resolve-address** 通过 Avahi 守护进程使用 mDNS/DNS-SD 将 IP 地址解析为主机名。它等同于带 **--address** 标志运行 **avahi-resolve**。

# INSTALL

```apt: sudo apt install avahi-utils```

```dnf: sudo dnf install avahi-tools```

```apk: sudo apk add avahi-tools```

```zypper: sudo zypper install avahi-utils```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[avahi-resolve](/man/avahi-resolve)(1), [avahi-resolve-host-name](/man/avahi-resolve-host-name)(1), [avahi-browse](/man/avahi-browse)(1), [avahi-daemon](/man/avahi-daemon)(8)

# RESOURCES

```[Homepage](https://avahi.org/)```

```[Source code](https://github.com/avahi/avahi)```

<!-- verified: 2026-06-17 -->
