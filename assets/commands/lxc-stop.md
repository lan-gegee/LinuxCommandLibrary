# TAGLINE

停止运行中的 Linux 容器

# TLDR

**停止**容器

```sudo lxc-stop [container_name]```

显示**帮助**

```lxc-stop --help```

# SYNOPSIS

**lxc-stop** **-n** _name_ [_options_]

# DESCRIPTION

**lxc-stop** 停止运行中的 Linux 容器。它会发送 SIGPWR 和 SIGKILL 信号来妥善关闭容器的 init 进程。

# PARAMETERS

**-n, --name NAME**
> 容器名称

**-k, --kill**
> 立即杀掉容器（SIGKILL）

**-W, --nowait**
> 不等待关机完成

**-t, --timeout SECONDS**
> 强制终止前的超时时间

**-r, --reboot**
> 重启而不是停止

**-?, --help**
> 显示帮助信息

# CAVEATS

需要 root 权限。优雅关机可能需要一些时间。如需立即终止请使用 --kill。

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

[lxc-start](/man/lxc-start)(1), [lxc-destroy](/man/lxc-destroy)(1), [lxc-info](/man/lxc-info)(1)
