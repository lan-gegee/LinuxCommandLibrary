# TAGLINE

TELNET 协议客户端

# TLDR

**连接主机**的默认端口（23）

```telnet [host]```

**连接主机**的指定端口

```telnet [host] [port]```

**测试端口是否开放**

```telnet [host] [80]```

**以自动登录方式连接**

```telnet -a [host]```

**以指定用户身份连接**

```telnet -l [username] [host]```

**设置自定义转义字符**

```telnet -e [^X] [host]```

**强制 IPv4 连接**

```telnet -4 [host]```

# SYNOPSIS

**telnet** [_options_] [_host_] [_port_]

# PARAMETERS

**-4**
> 强制 IPv4 地址解析

**-6**
> 强制 IPv6 地址解析

**-8**
> 请求 8 位数据通路

**-a**
> 尝试用当前用户名自动登录

**-l** _USER_
> 指定用于自动登录的用户名

**-e** _CHAR_
> 设置转义字符（默认为 ^]）

**-E**
> 禁用转义字符

**-d**
> 启用调试模式

**-n** _FILE_
> 将跟踪信息记录到文件

**-K**
> 禁用自动登录

**-L**
> 仅在输出方向使用 8 位数据通路

**-7**
> 在输入和输出上去除第 8 位

# TELNET COMMANDS

在 telnet 命令模式下（按转义字符进入）：

**open** _host_ [_port_]
> 连接到主机

**close**
> 关闭当前连接

**quit**
> 退出 telnet

**status**
> 显示连接状态

**send** _chars_
> 发送特殊字符

**set** _variable_
> 设置 telnet 变量

**toggle** _option_
> 切换选项的开/关

**?**
> 显示帮助

# DESCRIPTION

**telnet** 是 TELNET 协议的用户界面，用于与远程主机通信。它可以连接任意 TCP 端口，因此除了传统的终端访问之外，还可用于测试网络服务。

不带参数时，telnet 进入以 **telnet>** 为提示符的命令模式。带有主机参数时则立即尝试连接。在连接过程中按转义字符（默认 **Ctrl+]**）可返回命令模式。

常见用途包括测试 Web 服务器（端口 80）、邮件服务器（端口 25），以及验证网络服务是否可访问。该协议以明文传输数据，没有加密。

# CAVEATS

Telnet 以明文传输包括密码在内的所有数据——切勿在不可信网络上用它进行敏感连接。安全的远程访问请使用 SSH。现代系统默认可能未安装 telnet。某些防火墙会封锁默认的 telnet 端口（23）。该协议已被认为不适合远程管理。

# HISTORY

TELNET 协议开发于 **1969 年**，是最早的互联网协议之一，定义于 RFC 15 以及后来的 RFC 854。它在互联网的前身 ARPANET 上提供远程终端访问。Telnet 曾是远程访问 Unix 的标准方式，直到 20 世纪 90 年代中期 **SSH** 作为安全替代方案出现。虽然在远程登录方面已弃用，但 telnet 在测试和调试网络服务方面仍然有用。

# INSTALL

```dnf: sudo dnf install telnet```

```apk: sudo apk add inetutils-telnet```

```zypper: sudo zypper install telnet```

```brew: brew install telnet```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ssh](/man/ssh)(1), [nc](/man/nc)(1), [netcat](/man/netcat)(1), [rlogin](/man/rlogin)(1)
