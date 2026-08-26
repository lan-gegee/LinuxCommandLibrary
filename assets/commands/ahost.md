# TAGLINE

查询 DNS 地址记录

# TLDR

打印与主机名关联的 **A 或 AAAA 记录**

```ahost [example.com]```

显示额外的**调试**输出

```ahost -d [example.com]```

显示具有**指定类型**的记录

```ahost -t [a|aaaa|u] [example.com]```

# SYNOPSIS

**ahost** [_-d_] [_-s server_] [_-t type_] [_-D domain_] _hostname_

# DESCRIPTION

**ahost** 是一个 DNS 查询工具，用于显示与主机名或 IP 地址关联的 A（IPv4）或 AAAA（IPv6）记录。它使用 c-ares 异步 DNS 库执行查询，因此是非阻塞且高效的。

与更常用的 **host** 或 **dig** 命令不同，ahost 是专门作为 c-ares 库的轻量级演示和实用工具而设计的。它支持反向查询（当给定 IP 地址时），并且可以查询特定的记录类型。

# PARAMETERS

**-d**
> 显示额外的调试输出

**-s server**
> 设置用于 DNS 查询的服务器列表

**-t type**
> 显示指定类型的记录：**a** 表示 A 记录，**aaaa** 表示 AAAA 记录，**u** 表示同时查找 AAAA 和 A 记录（默认）

**-D domain**
> 指定搜索域，而不是使用 /etc/resolv.conf 中的默认值（仅在使用 /etc/resolv.conf 的平台上可用）

# CAVEATS

c-ares 库工具的一部分。与更常用的 **host** 命令相比可能具有不同的功能。

# HISTORY

属于 **c-ares** 异步 DNS 解析库，最初从 ares 库分叉而来。

# INSTALL

```apk: sudo apk add c-ares-utils```

```zypper: sudo zypper install c-ares-utils```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[adig](/man/adig)(1), [acountry](/man/acountry)(1), [host](/man/host)(1), [dig](/man/dig)(1), [nslookup](/man/nslookup)(1)

# RESOURCES

```[Source code](https://github.com/c-ares/c-ares)```

```[Homepage](https://c-ares.org/)```

<!-- verified: 2026-06-11 -->
