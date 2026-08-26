# TAGLINE

启动已停止的 Linux 容器

# TLDR

启动 **lxc 服务**

```systemctl start lxc-net```

**启动**容器

```sudo lxc-start [container_name]```

在**前台**启动

```sudo lxc-start [container_name] --foreground```

以**调试日志**启动

```sudo lxc-start [container_name] -l DEBUG -o [path/to/logfile]```

显示**帮助**

```lxc-start --help```

# SYNOPSIS

**lxc-start** **-n** _name_ [_options_]

# DESCRIPTION

**lxc-start** 启动已停止的 Linux 容器。默认在后台运行，调试时可使用前台模式。

# PARAMETERS

**-n, --name NAME**
> 容器名称

**-F, --foreground**
> 在前台运行

**-d, --daemon**
> 以守护进程方式运行（默认）

**-l, --logpriority LEVEL**
> 日志优先级（DEBUG、INFO 等）

**-o, --logfile FILE**
> 日志输出文件

**-p, --pidfile FILE**
> 守护进程模式的 PID 文件

**-?, --help**
> 显示帮助信息

# CAVEATS

需要 root 权限。容器必须存在且处于停止状态。前台启动的容器请用 lxc-stop 停止。

# INSTALL

```apt: sudo apt install lxc```

```dnf: sudo dnf install lxc```

```pacman: sudo pacman -S lxc```

```apk: sudo apk add lxc```

```zypper: sudo zypper install lxc```

```brew: brew install lxc```

```nix: nix profile install nixpkgs#lxc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lxc-stop](/man/lxc-stop)(1), [lxc-create](/man/lxc-create)(1), [lxc-attach](/man/lxc-attach)(1)
