# TAGLINE

在运行中的 LXC 容器内启动进程，相当于附加一个 shell

# TLDR

**附加**到容器

```sudo lxc-attach [container_name]```

显示**帮助**

```lxc-attach --help```

# SYNOPSIS

**lxc-attach** [_options_] **-n** _container_

# DESCRIPTION

**lxc-attach** 在运行中的 LXC 容器内启动一个进程，相当于在容器的命名空间内附加一个 shell 或运行命令。

# PARAMETERS

**-n, --name NAME**
> 容器名称

**-e, --elevated-privileges**
> 不丢弃 capabilities

**-a, --arch ARCH**
> 设置架构

**-s, --namespaces PID|MNT|...**
> 仅附加到指定的命名空间

**-- COMMAND**
> 在容器内运行的命令

**-?, --help**
> 显示帮助信息

# CAVEATS

需要 root 权限。容器必须处于运行状态。属于 LXC（而非 LXD）的一部分。

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

[lxc](/man/lxc)(1), [lxc-start](/man/lxc-start)(1), [lxc-stop](/man/lxc-stop)(1)
