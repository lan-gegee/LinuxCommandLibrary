# TAGLINE

GDB 的远程调试桩

# TLDR

**启动调试服务器**

```gdbserver :[port] [program]```

**附加到进程**

```gdbserver --attach :[port] [pid]```

**多进程模式**

```gdbserver --multi :[port]```

**带参数调试**

```gdbserver :[port] [program] [arg1] [arg2]```

# SYNOPSIS

**gdbserver** _comm_ [_program_] [_args_...]

# PARAMETERS

_COMM_
> 连接方式：`:port` 或 `host:port`。

_PROGRAM_
> 要调试的程序。

**--attach** _PID_
> 附加到正在运行的进程。

**--multi**
> 多进程模式。

**--once**
> 客户端断开连接后退出。

**--debug**
> 启用调试输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gdbserver** 是一个轻量级远程调试桩，运行在目标系统上，让在另一台机器上运行的完整 GDB 调试器能够远程控制和调试程序。这种架构对于嵌入式开发、交叉编译工作流以及在资源受限设备上进行调试至关重要。

服务器组件运行在目标系统上（嵌入式设备、远程服务器或不同架构），而完整的 GDB 客户端则运行在开发者的工作站上。两者通过 TCP/IP 或串行连接通信，gdbserver 将 GDB 的调试协议转换为系统级调试操作。

这种分离架构最大限度地减少了目标系统上的占用，因为 gdbserver 比完整 GDB 小得多，依赖也更少。它对嵌入式 Linux 系统、IoT 设备以及目标缺乏足够资源运行完整调试环境的场景特别有价值。

典型工作流是在目标机上用待调试程序启动 gdbserver，然后在 GDB 客户端中使用 "target remote host:port" 之类的命令连接。GDB 的全部功能都可以远程使用，包括断点、单步执行、内存检查和核心文件生成。

# CAVEATS

需要能通过网络访问目标。注意调试连接的安全性。目标机需要安装 gdbserver。

# HISTORY

gdbserver 是 **GDB**（GNU Debugger）的一部分，自 GDB 4.x 起就支持远程调试场景。它是嵌入式开发和跨平台调试的重要工具。

# INSTALL

```apt: sudo apt install gdbserver```

```dnf: sudo dnf install gdb```

```pacman: sudo pacman -S gdb```

```apk: sudo apk add gdb```

```zypper: sudo zypper install gdbserver```

```brew: brew install gdb```

```nix: nix profile install nixpkgs#gdb```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gdb](/man/gdb)(1)
