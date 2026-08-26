# TAGLINE

CUPS 打印服务器守护进程

# TLDR

**启动 CUPS 守护进程**

```cupsd```

**以前台方式启动**

```cupsd -f```

**测试配置**

```cupsd -t```

使用备用配置文件

```cupsd -c [/path/to/cupsd.conf]```

# SYNOPSIS

**cupsd** [_options_]

# PARAMETERS

**-f**
> 前台运行。

**-F**
> 前台运行且不 fork 子进程。

**-c** _config_
> 使用备用的配置文件。

**-t**
> 测试配置后退出。

**-h**
> 显示帮助。

# DESCRIPTION

**cupsd** 是 CUPS（Common Unix Printing System）的调度守护进程。它管理打印队列、处理打印请求并负责与打印机的通信。

通常由 systemd 或 init 脚本自动启动。

# CONFIGURATION

**/etc/cups/cupsd.conf**
> 主配置文件，控制守护进程行为、端口设置、访问控制和日志级别。

# CAVEATS

通常由系统服务管理器管理。一般只在调试时才需要直接调用。

# INSTALL

```apt: sudo apt install cups-daemon```

```dnf: sudo dnf install cups```

```pacman: sudo pacman -S cups```

```apk: sudo apk add cups```

```zypper: sudo zypper install cups```

```brew: brew install cups```

```nix: nix profile install nixpkgs#cups```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cupsctl](/man/cupsctl)(1), [lp](/man/lp)(1), [lpstat](/man/lpstat)(1)

# RESOURCES

```[Source code](https://github.com/OpenPrinting/cups)```

```[Homepage](https://www.cups.org)```

```[Documentation](https://openprinting.github.io/cups/)```

<!-- verified: 2026-06-26 -->
