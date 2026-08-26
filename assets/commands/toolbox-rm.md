# TAGLINE

删除 Toolbx 容器

# TLDR

**删除**一个容器

```toolbox rm [container_name]```

删除**所有**容器

```toolbox rm -a```

**强制**删除正在运行的容器

```toolbox rm -f [container_name]```

# SYNOPSIS

**toolbox rm** [_OPTIONS_] [_CONTAINER_...]

# PARAMETERS

**-a, --all**
> 删除所有 Toolbx 容器

**-f, --force**
> 强制删除正在运行的容器

# DESCRIPTION

**toolbox rm** 删除一个或多个 Toolbx 容器。除非使用强制选项，否则容器必须先停止才能删除。

可以通过在参数中指定名称来一次删除多个容器。--all 选项会一次性删除所有 Toolbx 容器。

# CAVEATS

正在运行的容器不使用 --force 无法删除。仅存储在容器内部的数据将会丢失。主目录（从宿主机挂载）会保留。

# INSTALL

```apt: sudo apt install podman-toolbox```

```dnf: sudo dnf install toolbox```

```pacman: sudo pacman -S toolbox```

```zypper: sudo zypper install toolbox```

```nix: nix profile install nixpkgs#toolbox```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[toolbox](/man/toolbox)(1), [toolbox-rmi](/man/toolbox-rmi)(1), [toolbox-list](/man/toolbox-list)(1)
