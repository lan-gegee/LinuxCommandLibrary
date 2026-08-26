# TAGLINE

进入 Distrobox 容器并在其中运行命令

# TLDR

**进入**容器

```distrobox-enter [container_name]```

进入并**运行命令**

```distrobox-enter [container_name] -- [sh -l]```

**不使用 TTY** 进入（用于脚本）

```distrobox-enter -T [container_name] -- [uptime --pretty]```

# SYNOPSIS

**distrobox-enter** [_options_] [_name_] [_-- command_]

# DESCRIPTION

**distrobox-enter** 用于进入一个 Distrobox 容器。默认运行你的 $SHELL，但也可以指定其他 Shell 或完整命令。

对于脚本、应用或服务，请使用 --no-tty 禁用 TTY 和交互性。

# PARAMETERS

**-n, --name** _name_
> 容器名称（默认为 my-distrobox）

**-T, --no-tty**
> 不实例化 tty（用于脚本）

**-nw, --no-workdir**
> 从容器的主目录而非当前目录启动

**-a, --additional-flags** _flags_
> 传递给容器管理器命令的额外标志

**-r, --root**
> 以 root 权限启动 podman/docker

**-d, --dry-run**
> 仅打印生成的容器管理器命令

**-v, --verbose**
> 显示更详细的输出

**-- command**
> 终止选项解析；其余参数在容器内执行

# CAVEATS

容器必须已存在（用 distrobox-create 创建）。首次进入会初始化容器，耗时较长。`--` 之后的命令会被传给容器。

# INSTALL

```dnf: sudo dnf install distrobox```

```pacman: sudo pacman -S distrobox```

```apk: sudo apk add distrobox```

```zypper: sudo zypper install distrobox```

```brew: brew install distrobox```

```nix: nix profile install nixpkgs#distrobox```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[distrobox](/man/distrobox)(1), [distrobox-create](/man/distrobox-create)(1), [distrobox-export](/man/distrobox-export)(1)
