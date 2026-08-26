# TAGLINE

FreeRADIUS 认证与计费服务器

# TLDR

**启动 RADIUS 服务器**

```radiusd```

**以调试模式启动**

```radiusd -X```

**检查配置**

```radiusd -C```

**以前台模式加调试运行**

```radiusd -f -X```

**指定配置文件目录**

```radiusd -d [/etc/raddb]```

# SYNOPSIS

**radiusd** [_options_]

# PARAMETERS

**-X**
> 调试模式（详细输出）。

**-C**
> 仅检查配置。

**-f**
> 以前台方式运行。

**-d** _dir_
> 配置目录。

**-n** _name_
> 服务器名称。

**-l** _file_
> 日志文件。

# DESCRIPTION

**radiusd** 是 FreeRADIUS 服务器守护进程，实现 RADIUS（Remote Authentication Dial-In User Service，远程认证拨入用户服务）协议，用于网络访问的集中式认证、授权和计费。它处理来自 VPN 网关、无线接入点和交换机等网络设备的登录请求，并根据 LDAP、SQL 数据库或本地文件等后端验证凭据。

该服务器支持多种认证方法，包括 PAP、CHAP、MS-CHAP、EAP-TLS 和 PEAP。它处理授权策略以确定已认证用户可以访问哪些网络资源，并记录计费数据用于会话跟踪和计费。**-X** 调试模式提供详细的请求处理输出，对排查认证流程至关重要；**-C** 则在不启动服务器的情况下验证配置语法。

# EXAMPLES

```bash
# Start daemon
radiusd

# Debug mode (very verbose)
radiusd -X

# Check config syntax
radiusd -C

# Foreground for systemd
radiusd -f

# Test authentication
radtest user password localhost 0 testing123
```

# CONFIGURATION

**/etc/raddb/radiusd.conf**
> 主服务器配置文件，控制日志、线程池、模块加载和虚拟服务器定义。在基于 Debian 的系统上位于 /etc/freeradius/radiusd.conf。

**/etc/raddb/clients.conf**
> 定义 RADIUS 客户端（网络设备）及其 IP 地址和共享密钥，用于验证请求。

**/etc/raddb/users**
> 本地用户定义和授权规则，适用于没有外部认证后端的简单部署。

**/etc/raddb/mods-enabled/**
> 指向已启用模块配置的符号链接，控制认证后端、LDAP 连接、SQL 数据库和策略处理。

# PORTS

```
1812 - Authentication
1813 - Accounting
```

# CAVEATS

配置复杂。需要仔细进行安全设置。调试模式会输出密钥——仅用于测试。

# HISTORY

FreeRADIUS 是部署最广泛的 RADIUS 服务器，由 **Alan DeKok** 和 **Miquel van Smoorenburg** 于 1999 年发起。

# INSTALL

```dnf: sudo dnf install freeradius```

```pacman: sudo pacman -S freeradius```

```apk: sudo apk add freeradius```

```nix: nix profile install nixpkgs#freeradius```

<!-- packages: 2026-07-22 -->

# SEE ALSO
