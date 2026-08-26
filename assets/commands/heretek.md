# TAGLINE

用于远程和嵌入式调试的 GDB TUI 仪表盘

# TLDR

以默认 GDB **启动 heretek**

```heretek```

通过 netcat **连接远程目标**

```heretek -r [host:port]```

**使用自定义 GDB 二进制文件**

```heretek --gdb-path [path/to/gdb]```

**以 32 位模式运行**

```heretek --ptr-size 32```

**从文件执行 GDB 命令**

```heretek -c [path/to/commands.gdb]```

# SYNOPSIS

**heretek** [**--gdb-path** _path_] [**-r** _host:port_] [**--ptr-size** _size_] [**-c** _file_] [_options_]

# PARAMETERS

**--gdb-path** _PATH_
> 覆盖 gdb 可执行文件路径

**-r**, **--remote** _HOST:PORT_
> 连接到 netcat 会话进行远程调试

**--ptr-size** _SIZE_
> 设置指针大小模式（可选值：32、64、auto；默认：auto）

**-c**, **--cmds** _FILE_
> 从文件逐行执行 GDB 命令（以 # 开头的行会被忽略）

**--log-path** _PATH_
> 日志文件的写入路径（设置 RUST_LOG 环境变量可更改日志级别）

**-h**, **--help**
> 打印帮助信息

**-V**, **--version**
> 打印版本信息

# DESCRIPTION

**heretek** 是一个 GDB TUI 仪表盘，设计目标是在即使没有可用的 gdbserver 的情况下也能无缝连接远程目标。它以单个静态链接的 **musl** 二进制文件发布，没有 Python 依赖，非常适合嵌入式和精简环境——这类环境中厂商提供的 GDB 可能不带 Python 支持。

heretek 只需要系统上存在 **gdb**、**nc**（netcat）和 **mkfifo** 即可工作，从而绕开了 gdbserver 二进制损坏等常见问题。该仪表盘以井然有序的 TUI 布局显示寄存器、反汇编、栈和内存。

# CAVEATS

目标系统上至少需要有 **gdb**、**nc** 和 **mkfifo**。某些依赖 Python 扩展的高级 GDB 功能不可用。TUI 布局可能需要足够宽的终端。

# HISTORY

**heretek** 由 **wcampbell0x2a** 创建，使用 **Rust** 编写。它的开发初衷是解决嵌入式系统上的调试痛点——在这类系统中，传统 GDB 前端常因缺少 Python 或 gdbserver 安装损坏而无法使用。

# INSTALL

```pacman: sudo pacman -S heretek```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gdb](/man/gdb)(1), [nc](/man/nc)(1)
