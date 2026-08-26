# TAGLINE

清空终端屏幕

# TLDR

**清空终端屏幕**

```clear```

**清空并重置回滚缓冲区**

```clear -x```

为特定终端类型执行**清空**

```clear -T [xterm-256color]```

使用 ANSI 转义码的替代方案

```printf '\033[2J\033[H'```

# SYNOPSIS

**clear** [_-Ttype_] [_-V_] [_-x_]

# PARAMETERS

**-T** _type_
> 指定要使用的终端类型，而非 $TERM

**-V**
> 输出版本信息并退出

**-x**
> 不尝试清除终端的回滚缓冲区

# DESCRIPTION

**clear** 在可行的情况下清空终端屏幕，包括其回滚缓冲区（如果定义了扩展的 E3 能力）。它会从环境中查找由环境变量 TERM 给出的终端类型，然后查询 terminfo 数据库以确定如何清屏。

该命令输出转义序列，指示终端模拟器清空可见屏幕区域，默认情况下还包括回滚缓冲区。这相当于在许多 shell 中按 Ctrl+L，不过 Ctrl+L 通常只清空可见部分而不影响回滚缓冲区。

clear 命令可用于保护隐私（将敏感输出移出视野）、减少长终端会话中的视觉杂乱，以及将终端重置到已知状态。

# CAVEATS

并非所有终端都支持清空回滚缓冲区；此时只会清空可见屏幕。具体行为取决于终端模拟器对清屏序列的实现。在某些配置下，Ctrl+L 提供类似功能，但在处理回滚方面可能表现不同。被清除的内容并未从内存中安全擦除；对于敏感数据，建议彻底关闭终端。

# HISTORY

**clear** 命令自 Unix 早期就存在，源自用于实现终端无关屏幕处理的 **termcap** 库系统。现代实现属于 **ncurses** 软件包，它为类 Unix 系统提供终端处理能力。数十年来该命令的功能基本未变，只是底层的终端处理机制已从 termcap 演变为 terminfo。

# INSTALL

```apt: sudo apt install ncurses-bin```

```dnf: sudo dnf install ncurses```

```pacman: sudo pacman -S ncurses```

```apk: sudo apk add ncurses```

```brew: brew install ncurses```

```nix: nix profile install nixpkgs#ncurses```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[reset](/man/reset)(1), [tput](/man/tput)(1), [stty](/man/stty)(1), [tty](/man/tty)(1)

# RESOURCES

```[Homepage](https://invisible-island.net/ncurses/)```

```[Documentation](https://invisible-island.net/ncurses/man/clear.1.html)```

<!-- verified: 2026-06-22 -->
