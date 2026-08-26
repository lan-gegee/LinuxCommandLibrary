# TAGLINE

终端登录会话管理器

# TLDR

在终端上**启动 getty**

```getty [tty1] [38400]```

**自动登录用户**

```getty -a [username] [tty1]```

指定终端类型

```getty -T [linux] [tty1] [38400]```

**等待载波信号**

```getty -w [ttyS0] [9600]```

# SYNOPSIS

**getty** [_options_] _port_ [_baud_]

# PARAMETERS

_PORT_
> 终端设备（tty1、ttyS0）。

_BAUD_
> 波特率。

**-a** _USER_, **--autologin** _USER_
> 自动登录指定用户。

**-n**, **--skip-login**
> 不提示登录。

**-T** _TERM_, **--term** _TERM_
> 终端类型。

**-w**, **--wait-cr**
> 等待载波信号/回车。

**--help**
> 显示帮助信息。

# DESCRIPTION

**getty**（get teletype）打开终端端口、设置工作模式并调用 login。它管理系统控制台和串口上的登录提示。

该程序由 init/systemd 为每个需要登录访问的终端启动。它负责串口终端的波特率检测和终端类型配置。

getty 是 Unix 系统的基础登录接口。

# CONFIGURATION

**/etc/inittab**
> System V init 配置文件，为每个终端定义 getty 实例（传统系统）。

**/etc/systemd/system/getty@.service**
> 现代 Linux 系统上 getty 实例使用的 systemd 服务模板。

# CAVEATS

通常由 init/systemd 启动。直接调用较少见。串口配置较为复杂。

# HISTORY

getty 可追溯至**早期 Unix**，当时用于管理电传打字机和终端。现代 Linux 使用 agetty（alternative getty），它提供了更多功能。

# INSTALL

```apt: sudo apt install util-linux```

```dnf: sudo dnf install util-linux```

```pacman: sudo pacman -S util-linux```

```zypper: sudo zypper install util-linux```

```brew: brew install util-linux```

```nix: nix profile install nixpkgs#util-linux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[agetty](/man/agetty)(1), [login](/man/login)(1), [init](/man/init)(1)

# RESOURCES

```[Source code](https://github.com/util-linux/util-linux)```

```[Documentation](https://manpages.debian.org/agetty)```

<!-- verified: 2026-07-15 -->
