# TAGLINE

OpenSSH SSH 守护进程

# TLDR

**启动 SSH 守护进程**

```sshd```

**测试配置文件**是否存在语法错误

```sshd -t```

**在前台运行**（对容器很有用）

```sshd -D```

**使用其他配置**文件

```sshd -f [/etc/ssh/sshd_config]```

**调试模式**（单连接，详细输出）

```sshd -d```

**扩展调试**（最大详细程度）

```sshd -ddd```

**指定监听端口**

```sshd -p [2222]```

**带匹配条件的扩展测试模式**

```sshd -T -C user=[testuser],host=[example.com]```

# SYNOPSIS

**sshd** [**-46DdeGiqTtV**] [**-C** _connection_spec_] [**-f** _config_file_] [**-g** _login_grace_time_] [**-h** _host_key_file_] [**-o** _option_] [**-p** _port_] [**-u** _len_]

# PARAMETERS

**-D**
> 在前台运行，不转为守护进程

**-d**
> 调试模式；以详细输出处理一个连接。多个 -d 可提高详细程度（最多 3 个）。

**-t**
> 测试模式；校验配置文件的语法

**-T**
> 扩展测试模式；将生效的配置输出到标准输出

**-C** _connection_spec_
> 为 -T 匹配测试指定连接参数（user、host、addr、laddr、lport、rdomain）

**-f** _file_
> 指定配置文件（默认：/etc/ssh/sshd_config）

**-h** _host_key_file_
> 指定主机密钥文件（可为不同密钥类型多次指定）

**-g** _login_grace_time_
> 客户端认证的宽限时间（默认：120 秒）

**-p** _port_
> 监听端口（可多次指定）

**-o** _option_
> 以 key=value 格式指定配置选项

**-E** _log_file_
> 将调试日志追加到 log_file 而不是系统日志

**-e**
> 将调试日志写入标准错误而不是系统日志

**-q**
> 安静模式；抑制非致命的日志消息

**-4**
> 仅强制使用 IPv4 地址

**-6**
> 仅强制使用 IPv6 地址

# DESCRIPTION

**sshd** 是 OpenSSH 的服务器守护进程，它监听传入的 SSH 连接，对用户进行身份验证，并提供加密的远程 Shell 访问、文件传输和端口转发服务。它是 **ssh** 客户端的服务器端对应程序。

该守护进程支持多种身份验证方式，包括公钥、密码、keyboard-interactive 以及 GSSAPI/Kerberos。可以通过配置指令按用户、组和来源地址限制访问。X11 转发、代理转发和 TCP 端口转发等功能均可单独控制。

调试模式（**-d**）在前台以详细输出运行单个连接以便排查问题，而 **-t** 用于在重启服务前检查配置文件是否有语法错误。前台模式（**-D**）常用于容器环境，此时守护进程不应脱离控制进程。

# CONFIGURATION

**/etc/ssh/sshd_config**
> 主配置文件，控制身份验证方式、访问限制、端口、协议选项、转发权限和日志记录。

**/etc/ssh/ssh_host_*_key**
> 主机密钥文件（RSA、Ed25519、ECDSA），用于向连接的客户端表明服务器身份。

**/etc/ssh/sshd_config.d/**
> 用于模块化配置片段的 drop-in 配置目录（通过 Include 指令引入）。

# CAVEATS

绑定特权端口（低于 1024）需要 root 权限。配置错误可能导致你被锁在系统之外。重启服务前务必用 **-t** 测试配置更改，并在修改期间保持一个活动会话不断开。

# HISTORY

**sshd** 属于 **OpenSSH**，由 OpenBSD 项目自 **1999 年**起开发。它取代了 telnet 和 rsh 等不安全的协议。

# INSTALL

```apt: sudo apt install openssh-server```

```dnf: sudo dnf install openssh-server```

```apk: sudo apk add openssh-server```

```zypper: sudo zypper install openssh-server```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ssh](/man/ssh)(1), [ssh-keygen](/man/ssh-keygen)(1)
