# TAGLINE

Interception Tools 套件的组成部分，用于拦截和多路复用事件流

# TLDR

**创建**指定名称的新 muxer

```mux -c [muxer_name1] [muxer_name2]```

设置 muxer 的**内部队列大小**

```mux -s [100]```

从命名的 muxer **读取输入**

```mux -i [input_muxer_name]```

向命名的 muxer **写入输出**

```mux -o [output_muxer_name]```

# SYNOPSIS

**mux** [**-h** | [**-s** _size_] **-c** _name_ | [**-i** _name_] [**-o** _name_]]

# PARAMETERS

**-h**
> 显示帮助消息并退出

**-c _name_**
> 创建指定名称的 muxer（可重复）

**-s _size_**
> 设置 muxer 队列大小；默认为 100

**-i _name_**
> 从命名的 muxer 读取输入；在切换模式下可以重复

**-o _name_**
> 向命名的 muxer 写入输出；可以重复

# DESCRIPTION

**mux** 是 Interception Tools 套件的一部分，用于对输入事件流进行多路复用。必须先用 **-c** 创建 muxer，然后才能将其用作给定管道的输入或输出。

除了将多条管道合并为一条之外，mux 还能复制它们（使用多个 **-o** 选项），并能根据其他管道中的活动充当切换开关（使用多个 **-i** 选项）。

该工具通常与 udevmon 及其他 Interception Tools 组件配合使用，在底层实现键盘重映射、事件过滤和输入设备操控。

# CAVEATS

需要安装并配置 Interception Tools 框架。命名的 muxer 以 FIFO 文件形式创建。队列大小会影响延迟和内存占用。通常需要 root 权限或属于 uinput 组。

# HISTORY

**mux** 是 **Interception Tools** 的一部分，由 Francisco Lopes（oblitum）开发。该框架提供 Linux 上的底层输入事件拦截能力，催生了 caps2esc、space2meta 等键盘定制工具。

# INSTALL

```apt: sudo apt install interception-tools```

```pacman: sudo pacman -S interception-tools```

```nix: nix profile install nixpkgs#interception-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[intercept](/man/intercept)(1), [udevmon](/man/udevmon)(1), [uinput](/man/uinput)(1)
