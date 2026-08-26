# TAGLINE

在隔离的 PipeWire 安全上下文中运行应用

# TLDR

创建**新的安全上下文**并打印其套接字地址

```pw-container```

在**新的安全上下文**中运行程序

```pw-container [command] [arg1] [arg2]```

运行时连接到**特定的远程** PipeWire 实例

```pw-container -r [remote_name] [command]```

使用 JSON 指定**安全属性**运行

```pw-container -P '{"pipewire.sec.app-id": "[my-app]"}' [command]```

显示**帮助**

```pw-container -h```

# SYNOPSIS

**pw-container** [_options_] [_command_] [_arguments_...]

# PARAMETERS

**-r**, **--remote** _name_
> 连接到特定的远程 PipeWire 实例

**-P**, **--properties** _json_
> 使用 JSON 对象设置上下文属性

**-h**, **--help**
> 显示帮助信息

# DESCRIPTION

**pw-container** 使用 PipeWire SecurityContext 扩展 API 创建新的安全上下文。它会以给定属性建立一个作为服务器的临时 Unix 套接字，从该套接字创建的客户端都会附带这些安全属性。

如果指定了命令，它会在新的安全上下文中执行。如果没有给出命令，则将套接字地址打印到标准输出。该进程会一直运行直到被信号终止（收到 SIGINT/SIGTERM 时以 0 退出）。

这对沙箱化应用或以受限的 PipeWire 访问权限运行程序很有用。

# CAVEATS

PipeWire 配置必须支持安全上下文。属性必须是有效的 JSON 格式。进程会一直运行，直到收到信号。

# HISTORY

**PipeWire**（Linux 上的现代多媒体框架）的一部分。为音频和视频访问控制提供应用隔离能力。

# INSTALL

```apt: sudo apt install pipewire-bin```

```apk: sudo apk add pipewire-tools```

```zypper: sudo zypper install pipewire-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pipewire](/man/pipewire)(1), [pw-cli](/man/pw-cli)(1), [pw-cat](/man/pw-cat)(1), [wpctl](/man/wpctl)(1)
