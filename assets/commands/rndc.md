# TAGLINE

远程控制 BIND DNS 服务器

# TLDR

**重新加载 BIND 配置**

```rndc reload```

**重新加载指定区域**

```rndc reload [example.com]```

**显示服务器状态**

```rndc status```

**清空缓存**

```rndc flush```

**停止服务器**

```rndc stop```

# SYNOPSIS

**rndc** [_options_] _command_ [_args_]

# PARAMETERS

**-s** _server_
> 服务器地址。

**-p** _port_
> 端口号。

**-k** _keyfile_
> 密钥文件。

**-c** _config_
> 配置文件。

# COMMANDS

**reload** [_zone_]
> 重新加载配置/区域。

**status**
> 服务器状态。

**flush** [_view_]
> 清空缓存。

**stop**
> 停止服务器。

**reconfig**
> 仅重新加载配置。

**zonestatus** _zone_
> 区域状态。

# DESCRIPTION

**rndc**（Remote Name Daemon Control）用于管理 BIND DNS 服务器。它向 named 发送命令来重新加载区域、清空缓存以及执行其他管理任务。

# EXAMPLES

```bash
# Check status
rndc status

# Reload all
rndc reload

# Reload specific zone
rndc reload example.com

# Flush DNS cache
rndc flush

# Flush specific name
rndc flushname example.com

# Reload configuration only
rndc reconfig

# Check zone status
rndc zonestatus example.com
```

# CONFIGURATION

**/etc/rndc.conf**
> 主配置文件，定义用于连接 named 的认证密钥、默认服务器地址和端口。

**/etc/rndc.key**
> 共享的 HMAC 密钥文件，用于向 BIND 服务器认证 rndc 命令。由 **rndc-confgen** 生成。

**/etc/named.conf**
> BIND 服务器配置必须包含一个匹配的 **controls** 块并使用相同的密钥，才能接受 rndc 连接。

# CAVEATS

需要与 named 共享密钥。默认端口为 953。可使用 rndc-confgen 生成密钥。

# HISTORY

rndc 是 **ISC**（Internet Systems Consortium）开发的 **BIND**（Berkeley Internet Name Domain）的组成部分。

# INSTALL

```apt: sudo apt install bind9-utils```

```dnf: sudo dnf install bind```

```pacman: sudo pacman -S bind```

```apk: sudo apk add bind```

```zypper: sudo zypper install bind```

```brew: brew install bind```

```nix: nix profile install nixpkgs#bind```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[named](/man/named)(8), [named.conf](/man/named.conf)(5)
