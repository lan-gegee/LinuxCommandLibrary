# TAGLINE

删除 Toolbx 容器镜像

# TLDR

**删除**镜像

```toolbox rmi [image_name1] [image_name2]```

删除**所有**镜像

```toolbox rmi -a```

**强制**删除正在使用的镜像

```toolbox rmi -f [image_name]```

# SYNOPSIS

**toolbox rmi** [_OPTIONS_] [_IMAGE_...]

# PARAMETERS

**-a, --all**
> 删除所有 Toolbx 镜像

**-f, --force**
> 强制删除正被容器使用的镜像

# DESCRIPTION

**toolbox rmi** 删除一个或多个 Toolbx 容器镜像。当前正被容器使用的镜像，除非使用强制选项，否则无法删除。

对已有容器的镜像使用 --force 时，这些容器将随镜像一并被删除。

# CAVEATS

正被容器使用的镜像不使用 --force 无法删除。强制删除会连带删掉相关联的容器。删除基础镜像后，之后需要重新下载。

# INSTALL

```apt: sudo apt install podman-toolbox```

```dnf: sudo dnf install toolbox```

```pacman: sudo pacman -S toolbox```

```zypper: sudo zypper install toolbox```

```nix: nix profile install nixpkgs#toolbox```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[toolbox](/man/toolbox)(1), [toolbox-rm](/man/toolbox-rm)(1), [toolbox-list](/man/toolbox-list)(1)
