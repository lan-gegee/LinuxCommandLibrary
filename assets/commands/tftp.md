# TAGLINE

简单文件传输协议（TFTP）客户端

# TLDR

**连接**到服务器

```tftp [server_ip] [port]```

直接**执行命令**

```tftp [server_ip] -c [command]```

使用 **IPv6** 和端口范围连接

```tftp [server_ip] -6 -R [port:port]```

设置传输**模式**（交互式）

```mode [binary|ascii]```

**下载**文件（交互式）

```get [file]```

**上传**文件（交互式）

```put [file]```

**退出**（交互式）

```quit```

# SYNOPSIS

**tftp** [_OPTIONS_] [_HOST_ [_PORT_]]

# PARAMETERS

**-c** _COMMAND_
> 执行 TFTP 命令后退出

**-6**
> 使用 IPv6

**-R** _PORT:PORT_
> 强制指定源端口范围

**-4**
> 仅使用 IPv4

**-v**
> 详细输出

**-V**
> 打印版本和配置信息，然后退出

**-l**
> 默认使用字面模式（不特殊处理文件名中的 ':'）

# INTERACTIVE COMMANDS

**get** _file_
> 从服务器下载文件

**put** _file_
> 向服务器上传文件

**mode** _binary|ascii_
> 设置传输模式

**status**
> 显示当前状态

**ascii**
> "mode ascii" 的简写

**binary**
> "mode binary" 的简写

**timeout** _seconds_
> 设置每个数据包的重传超时时间

**quit**
> 退出客户端

# DESCRIPTION

**tftp** 是简单文件传输协议（Trivial File Transfer Protocol）的客户端，这是一种无需身份验证的简单文件传输协议。TFTP 基于 UDP 运行，常用于网络启动（PXE）和固件更新。

# CAVEATS

没有身份验证和加密。基于 UDP，在防火墙环境下可能有问题。与 FTP 相比错误处理能力有限。最大文件大小受协议限制。

# HISTORY

TFTP 由 **RFC 1350**（1992 年）定义，是最古老的文件传输协议之一。它的设计追求简洁，因此适合嵌入式系统和网络启动环境。

# INSTALL

```apt: sudo apt install tftp-hpa```

```dnf: sudo dnf install tftp```

```pacman: sudo pacman -S tftp-hpa```

```apk: sudo apk add tftp-hpa```

```zypper: sudo zypper install tftp```

```nix: nix profile install nixpkgs#tftp-hpa```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ftp](/man/ftp)(1), [curl](/man/curl)(1), [wget](/man/wget)(1)
