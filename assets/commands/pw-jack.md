# TAGLINE

在 PipeWire 上运行 JACK 应用

# TLDR

使用 **PipeWire** 运行命令及其参数

```pw-jack command arg1 arg2```

以**详细输出**模式运行命令

```pw-jack -v command```

连接到特定的**远程** PipeWire 实例

```pw-jack -r remote_instance command```

显示**帮助**

```pw-jack -h```

# SYNOPSIS

**pw-jack** [_options_] _command_ [_arguments_...]

# PARAMETERS

**-v**
> 启用详细模式

**-r** _name_
> 连接到特定的远程 PipeWire 实例

**-h**
> 显示帮助信息

# DESCRIPTION

**pw-jack** 以 PipeWire 作为音频后端来运行 JACK 应用。它提供一个兼容层，使基于 JACK 的音频应用能够无缝地与 PipeWire 协同工作。

该封装器会拦截 JACK 库调用，并将其重定向到 PipeWire 的 JACK 兼容实现。

# CAVEATS

某些高级 JACK 特性在 PipeWire 下行为可能不同。依赖特定 JACK 服务器行为的应用可能需要调整。

# HISTORY

**PipeWire**（Linux 上的现代多媒体框架）的一部分。无需单独的 JACK 服务器即可实现 JACK 应用兼容性。

# INSTALL

```apt: sudo apt install pipewire-jack```

```pacman: sudo pacman -S pipewire-jack```

```apk: sudo apk add pipewire-jack```

```zypper: sudo zypper install pipewire-jack```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pipewire](/man/pipewire)(1), [jackd](/man/jackd)(1), [pw-cli](/man/pw-cli)(1)
