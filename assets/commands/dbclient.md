# TAGLINE

Dropbear 套件中的轻量级 SSH 客户端

# TLDR

**连接**远程主机

```dbclient [user]@[host]```

在**指定端口**连接

```dbclient [user]@[host] -p 2222```

使用**身份密钥**连接

```dbclient -i [path/to/key_file] [user]@[host]```

分配 TTY 运行**命令**

```dbclient [user]@[host] -t [command] [arguments]```

**转发代理**连接

```dbclient -A [user]@[host]```

# SYNOPSIS

**dbclient** [_options_] [_user_@]_host_ [_command_]

# DESCRIPTION

**dbclient** 是 Dropbear 套件中的 SSH 客户端。Dropbear 是一个面向嵌入式系统和资源受限环境的轻量级 SSH 实现。它提供标准 SSH 功能，包括远程 shell 访问、命令执行、端口转发和代理转发，而二进制体积和内存占用都显著小于 OpenSSH。

Dropbear 常见于路由器、IoT 设备、嵌入式 Linux 系统和其他资源受限环境。整套工具（服务器加客户端）压缩后通常不足 110KB，而 OpenSSH 需要数 MB。

dbclient 支持 SSH 协议的核心特性：公钥认证、密码认证、本地与远程端口转发，以及交互式会话的 TTY 分配。不过为了保持体积小巧，它省略了一些高级的 OpenSSH 特性。

一个显著区别是密钥格式：dbclient 使用 Dropbear 自己的密钥格式而非 OpenSSH 的格式。需要时可用 **dropbearconvert** 工具在两种格式之间转换。

# PARAMETERS

**-p** _port_
> 连接到指定端口（默认：22）

**-i** _keyfile_
> 身份密钥文件（Dropbear 格式）；可指定多个

**-l** _user_
> 以指定用户登录远程主机

**-t**
> 分配 PTY

**-T**
> 不分配 PTY

**-A**
> 转发认证代理连接

**-L** _listenport:host:port_
> 本地端口转发

**-R** _listenport:host:port_
> 远程端口转发

**-g**
> 允许非本地主机连接到转发的端口

**-N**
> 不请求远程 shell

**-f**
> 认证完成后 fork 到后台

**-y**
> 总是接受未知主机密钥而不提示

**-W** _windowsize_
> 每通道接收窗口缓冲区大小

**-K** _seconds_
> 保活间隔（秒）

**-s**
> 将远程命令作为子系统请求（用于 sftp）。

**-o** _option_
> 以 OpenSSH 配置文件格式指定选项（例如 **-o** "StrictHostKeyChecking=no"）。

**-c** _cipherlist_
> 要启用的加密算法列表（逗号分隔）。

**-m** _MAClist_
> 要启用的 MAC 算法列表（逗号分隔）。

# CAVEATS

使用 Dropbear 密钥格式而非 OpenSSH 格式。可用 **dropbearconvert** 在两种格式间转换密钥。不支持所有通过 **-o** 传入的 OpenSSH 配置项。属于 Dropbear SSH 套件，常见于嵌入式 Linux 系统。

# HISTORY

**dbclient** 是 **Matt Johnston** 创建的 **Dropbear** SSH 套件的一部分。Dropbear 为嵌入式系统设计——完整 OpenSSH 套件在这些场景下过于庞大——其服务器与客户端整体压缩后通常不足 110KB。

# INSTALL

```apt: sudo apt install dropbear-bin```

```apk: sudo apk add dropbear-dbclient```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ssh](/man/ssh)(1), [scp](/man/scp)(1), [dropbear](/man/dropbear)(8), [dropbearkey](/man/dropbearkey)(1), [dropbearconvert](/man/dropbearconvert)(1)
