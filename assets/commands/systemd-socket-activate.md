# TAGLINE

测试守护进程的套接字激活

# TLDR

**监听端口**并在连接到来时启动命令

```systemd-socket-activate -l [8080] [command]```

为一个命令**监听多个**端口

```systemd-socket-activate -l [8080] -l [8081] [command]```

**接受连接**并为每个连接派生新实例

```systemd-socket-activate -l [8080] -a [command]```

使用数据报（UDP）套接字而非流式（TCP）套接字

```systemd-socket-activate -l [8080] -d [command]```

为被启动的进程**设置环境变量**

```systemd-socket-activate -l [8080] -E [VAR=value] [command]```

以 inetd 兼容模式运行

```systemd-socket-activate -l [8080] --inetd [command]```

# SYNOPSIS

**systemd-socket-activate** [_options_] _command_ [_arguments_]

# PARAMETERS

**-l** _ADDRESS_, **--listen=**_ADDRESS_
> 在指定地址上监听（端口号或 host:port）。

**-a**, **--accept**
> 为每个连接启动一个新的命令实例。不能与 --now 组合。

**-d**, **--datagram**
> 监听数据报套接字（SOCK_DGRAM）而非流式套接字。不能与 --seqpacket 组合。

**--seqpacket**
> 监听顺序包套接字（SOCK_SEQPACKET）而非流式套接字。不能与 --datagram 组合。

**-E** _VAR[=VALUE]_, **--setenv=**_VAR[=VALUE]_
> 为被启动的进程设置环境变量。若未给出值，则继承当前环境。

**--fdname=**_NAME[:NAME...]_
> 为传递的文件描述符指定名称。以便使用 sd_listen_fds_with_names(3)。

**--inetd**
> 使用 inetd 协议（经由 stdin/stdout）传递文件描述符，而不是 $LISTEN_FDS 协议。

**--now**
> 立即启动命令，而不是等待连接到来。不能与 --accept 组合。

**-h**, **--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# DESCRIPTION

**systemd-socket-activate** 是一个用于套接字激活的测试与开发工具。它监听套接字，并在连接到达时启动指定的命令，从而模拟 systemd 的套接字激活功能，无需配置完整的套接字和服务单元文件。

默认监听流式（TCP）套接字。UDP 请用 **--datagram**，顺序包套接字请用 **--seqpacket**。被激活的程序通过 **$LISTEN_FDS** 协议接收套接字文件描述符（在 **--inetd** 模式下则通过 stdin/stdout）。

# CAVEATS

主要用于测试，不适合生产环境。生产环境请配置正式的 systemd 套接字和服务单元。服务必须支持套接字激活协议。本命令是 systemd 套件的一部分。

# INSTALL

```apt: sudo apt install systemd```

```dnf: sudo dnf install systemd```

```pacman: sudo pacman -S systemd```

```zypper: sudo zypper install systemd```

```brew: brew install systemd```

```nix: nix profile install nixpkgs#systemd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemctl](/man/systemctl)(1), [systemd-run](/man/systemd-run)(1), [systemd-analyze](/man/systemd-analyze)(1)
