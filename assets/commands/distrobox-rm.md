# TAGLINE

删除 Distrobox 容器

# TLDR

**删除**一个容器

```distrobox-rm [container_name]```

**强制**删除正在运行的容器

```distrobox-rm -f [container_name]```

删除**所有** Distrobox 容器

```distrobox-rm --all```

删除容器及其**独立的主目录**

```distrobox-rm --rm-home [container_name]```

删除一个**有根（rootful）**容器

```distrobox-rm --root [container_name]```

以**详细输出**删除

```distrobox-rm -v [container_name]```

# SYNOPSIS

**distrobox-rm** [_options_] _container_name_

# DESCRIPTION

**distrobox-rm** 删除一个 Distrobox 容器。建议先停止容器再删除。Distrobox 容器是与主机系统集成的 OCI 容器。

# PARAMETERS

**-f**, **--force**
> 即使容器正在运行也强制删除。

**-a**, **--all**
> 删除所有 Distrobox 容器。

**--rm-home**
> 当挂载的主目录与主机用户主目录不同时，一并删除该主目录。

**--root**, **-r**
> 以 root 权限启动 podman/docker/lilipod。优先于直接使用 sudo。

**-v**, **--verbose**
> 显示额外输出。

**-Y**, **--yes**
> 对所有提示自动回答 yes。

**-h**, **--help**
> 显示帮助信息。

# CAVEATS

删除容器会清除其中所有未映射到主机的数据。请先用 distrobox-stop 停止容器以实现干净的删除。使用 **--rm-home** 时要谨慎，它会永久删除容器的独立主目录。

# HISTORY

**distrobox-rm** 是 **Distrobox** 的一部分，后者用于创建和管理与主机系统紧密集成的容器。

# INSTALL

```dnf: sudo dnf install distrobox```

```pacman: sudo pacman -S distrobox```

```apk: sudo apk add distrobox```

```zypper: sudo zypper install distrobox```

```brew: brew install distrobox```

```nix: nix profile install nixpkgs#distrobox```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[distrobox](/man/distrobox)(1), [distrobox-create](/man/distrobox-create)(1), [distrobox-stop](/man/distrobox-stop)(1), [distrobox-list](/man/distrobox-list)(1), [distrobox-enter](/man/distrobox-enter)(1)
