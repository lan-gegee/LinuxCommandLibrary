# TAGLINE

轻量级系统监视器

# TLDR

**以默认配置启动**

```conky```

**将默认配置打印到 stdout**

```conky -C```

**使用指定的配置文件**

```conky -c [path/to/config]```

**以后台守护进程运行**

```conky -d```

**设置刷新间隔**（秒）

```conky -u [2]```

**设置桌面上的对齐位置**

```conky -a [top_right]```

# SYNOPSIS

**conky** [_options_]

# DESCRIPTION

**conky** 是一款面向 X11 的轻量级系统监视器，可将系统信息显示在桌面根窗口或独立窗口中。它提供超过 250 个内置监控对象，并支持广泛的定制，包括字体、颜色和 Lua 脚本。

# PARAMETERS

**-c, --config FILE**
> 加载指定的配置文件

**-C, --print-config**
> 将默认配置打印到 stdout

**-d, --daemonize**
> 以后台守护进程运行

**-o, --own-window**
> 创建独立窗口

**-p, --pause SECONDS**
> 启动前暂停

**-t, --text TEXT**
> 指定要渲染的文本

**-u, --interval SECONDS**
> 设置刷新间隔

**-a, --alignment ALIGNMENT**
> 设置窗口对齐方式（top_left、top_right、bottom_left、bottom_right 等）

**-x X**
> 设置 X 位置

**-y Y**
> 设置 Y 位置

**-v, --version**
> 显示版本信息

# CONFIGURATION

**~/.config/conky/conky.conf**
> 用户级配置文件，包含 conky.config 和 conky.text 两节。

**/etc/conky/conky.conf**
> 系统级默认配置。

# CAVEATS

配置采用 Lua 语法，分为两节：**conky.config** 存放设置，**conky.text** 定义显示内容。发送 **SIGUSR1** 可在不重启的情况下重新加载配置。需要支持 X11 的 X11 或 Wayland 合成器；不支持原生 Wayland。

# HISTORY

**conky** 是 Torsmo 的分支版本，如今已成为 Linux 桌面环境中最流行的系统监视器之一。它支持监控 CPU、内存、磁盘、网络以及许多其他系统指标。

# INSTALL

```apt: sudo apt install conky-all```

```dnf: sudo dnf install conky```

```pacman: sudo pacman -S conky```

```apk: sudo apk add conky```

```zypper: sudo zypper install conky```

```nix: nix profile install nixpkgs#conky```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[top](/man/top)(1), [htop](/man/htop)(1), [nmon](/man/nmon)(1)
