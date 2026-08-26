# TAGLINE

BIND 的 DNS 服务器守护进程

# TLDR

以默认配置**启动** DNS 服务器

```named```

使用**自定义配置**文件

```named -c [path/to/named.conf]```

只使用 **IPv4**

```named -4```

只使用 **IPv6**

```named -6```

在 53 以外的**指定端口**监听

```named -p [port]```

在**前台运行**（不守护进程化）

```named -f```

# SYNOPSIS

**named** [**-4**|**-6**] [**-c** _config-file_] [**-p** _port_] [**-f**] [**-g**] [**-u** _user_]

# PARAMETERS

**-4**
> 只使用 IPv4，即使 IPv6 可用

**-6**
> 只使用 IPv6，即使 IPv4 可用

**-c _config-file_**
> 使用指定的配置文件而非 /etc/named.conf

**-p _port_**
> 在指定端口监听，而非默认的 53

**-f**
> 在前台运行；不守护进程化

**-g**
> 在前台运行并将日志输出到 stderr

**-u _user_**
> 绑定特权端口后以指定用户身份运行

**-t _directory_**
> 启动后 chroot 到指定目录

**-n _cpus_**
> 用于工作线程的 CPU 数量

**-d _debug-level_**
> 设置调试级别（越高越详细）

# DESCRIPTION

**named** 是 BIND（Berkeley Internet Name Domain）的 DNS（域名系统）服务器守护进程。它将域名解析为 IP 地址以及反向解析，响应客户端的 DNS 查询。

该服务器默认从 /etc/named.conf 读取区域文件和配置。它可以充当域名的权威服务器、递归解析器，或两者兼有。该守护进程通常作为由 systemd 管理的系统服务运行。

# CAVEATS

绑定 53 端口需要 root 权限。出于安全考虑，启动后应以非特权用户身份运行（-u）。配置不当的 DNS 服务器可能被利用发起放大攻击。区域文件语法错误会导致无法启动。

# HISTORY

**BIND**（Berkeley Internet Name Domain）最初于 20 世纪 80 年代初由加州大学伯克利分校开发。它是互联网上使用最广泛的 DNS 服务器软件。目前 BIND 由互联网系统协会（ISC）维护。

# INSTALL

```apt: sudo apt install bind9```

```dnf: sudo dnf install bind```

```pacman: sudo pacman -S bind```

```apk: sudo apk add bind```

```zypper: sudo zypper install bind```

```brew: brew install bind```

```nix: nix profile install nixpkgs#bind```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rndc](/man/rndc)(8), [dig](/man/dig)(1), [nslookup](/man/nslookup)(1), [named.conf](/man/named.conf)(5)
