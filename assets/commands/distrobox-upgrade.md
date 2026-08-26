# TAGLINE

使用各容器原生软件包管理器升级 Distrobox 容器

# TLDR

**升级**一个容器

```distrobox-upgrade [container_name]```

升级**所有**容器

```distrobox-upgrade -a```

升级**指定的**容器

```distrobox-upgrade [container1] [container2]```

以 **root** 权限在后台运行升级

```distrobox-upgrade --root [container_name]```

# SYNOPSIS

**distrobox-upgrade** [_options_] [_containers_...]

# DESCRIPTION

**distrobox-upgrade** 使用每个容器的原生软件包管理器升级一个或多个 Distrobox 容器。它会根据容器所用的发行版运行相应的更新命令（apt、dnf、pacman 等）。

# PARAMETERS

**-a**, **--all**
> 升级所有容器。

**--root**
> 以 root 权限启动 podman/docker/lilipod。适用于用 --root 创建的容器。

**-v**, **--verbose**
> 显示更详细的输出。

_containers_
> 要升级的容器名称列表，以空格分隔。

# CAVEATS

每个容器都用自己的软件包管理器进行升级。大型升级可能耗费大量时间和磁盘空间。

# INSTALL

```dnf: sudo dnf install distrobox```

```pacman: sudo pacman -S distrobox```

```apk: sudo apk add distrobox```

```zypper: sudo zypper install distrobox```

```brew: brew install distrobox```

```nix: nix profile install nixpkgs#distrobox```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[distrobox](/man/distrobox)(1), [distrobox-enter](/man/distrobox-enter)(1), [distrobox-create](/man/distrobox-create)(1), [distrobox-list](/man/distrobox-list)(1)
