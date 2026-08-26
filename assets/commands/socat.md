# TAGLINE

多用途双向数据中继工具

# TLDR

将 **TCP 端口转发**到另一台主机

```socat TCP-LISTEN:[8080],fork TCP:[remote.host]:[80]```

**创建简单的 TCP 服务器**

```socat TCP-LISTEN:[1234],reuseaddr,fork EXEC:[/bin/cat]```

**连接到 TCP 端口**

```socat - TCP:[host]:[port]```

将 **Unix 套接字转发**到 TCP

```socat TCP-LISTEN:[1234],fork UNIX-CONNECT:[/var/run/app.sock]```

在进程之间**创建双向管道**

```socat EXEC:'[command1]' EXEC:'[command2]'```

**创建简单的聊天服务器**

```socat TCP-LISTEN:[12345],fork,reuseaddr STDOUT```

**SSL/TLS 连接**

```socat - OPENSSL:[host]:[443],verify=0```

**串口转 TCP**

```socat TCP-LISTEN:[5000] /dev/ttyUSB0,b9600,raw,echo=0```

**创建虚拟终端对**

```socat -d -d pty,raw,echo=0 pty,raw,echo=0```

# SYNOPSIS

**socat** [_options_] _address1_ _address2_

# DESCRIPTION

**socat**（SOcket CAT）是一个多用途中继工具，它建立两个双向字节流并在其间传输数据。它就像一个更强大的 netcat，支持众多地址类型和协议。

地址类型包括 TCP、UDP、Unix 套接字、文件、管道、PTY、进程（EXEC）、SSL、串行设备等等。socat 可以在这些类型的任意组合之间进行连接、监听和中继。

常见用例包括端口转发、协议转换、调试网络服务、创建隧道以及连接不同的系统。它对系统管理和网络排障来说不可或缺。

# PARAMETERS

**TCP-LISTEN:** _port_
> 监听 TCP 端口。

**TCP:** _host_ **:** _port_
> 连接到 TCP host:port。

**UDP:** _host_ **:** _port_
> UDP 连接。

**UNIX-CONNECT:** _path_
> 连接到 Unix 套接字。

**UNIX-LISTEN:** _path_
> 监听 Unix 套接字。

**EXEC:** _command_
> 执行命令并连接到其输入输出。

**OPENSSL:** _host_ **:** _port_
> SSL/TLS 连接。

**PTY**
> 创建伪终端。

**STDIO** 或 **-**
> 标准输入/输出。

**FILE:** _path_
> 打开一个文件用于读写。

**PIPE:** _path_
> 创建或连接到命名管道。

**SOCKS4:** _host_ **:** _port_
> SOCKS4 代理连接。

**fork**
> 处理多个连接（地址选项）。

**reuseaddr**
> 允许地址重用（地址选项）。

**verify=** _0|1_
> SSL 证书验证（地址选项）。

**-d** **-d**
> 详细的调试输出（重复使用可获得更多细节，最多 -d -d -d -d）。

**-v**
> 详细记录数据传输。

**-t** _TIMEOUT_
> 总不活动超时时间，单位秒。

**-T** _TIMEOUT_
> 传输超时时间，单位秒。

**-u**
> 单向模式（仅从左到右）。

**-U**
> 单向模式（仅从右到左）。

# CAVEATS

复杂的地址规范需要仔细核对语法。处理多个连接需要 fork 选项。SSL 证书可能需要配置。某些功能需要提升的权限。

# HISTORY

**socat** 由 **Gerhard Rieger** 于 **1999 年**创建，作为 netcat 的扩展版本，支持更多地址类型。它满足了人们对一种能够桥接不同通信机制的通用中继工具的需求。该项目持续活跃维护，在网络管理中被广泛使用。

# INSTALL

```apt: sudo apt install socat```

```dnf: sudo dnf install socat```

```pacman: sudo pacman -S socat```

```apk: sudo apk add socat```

```zypper: sudo zypper install socat```

```brew: brew install socat```

```nix: nix profile install nixpkgs#socat```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nc](/man/nc)(1), [netcat](/man/netcat)(1), [stunnel](/man/stunnel)(1), [ssh](/man/ssh)(1)
