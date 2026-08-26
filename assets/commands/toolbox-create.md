# TAGLINE

创建 Toolbx 开发容器

# TLDR

为**特定发行版**创建 Toolbx 容器

```toolbox create -d [distribution]```

为当前发行版的特定**发布版本**创建容器

```toolbox create -r [release]```

使用**自定义镜像**创建容器

```toolbox create -i [name]```

从**自定义 Fedora 镜像**创建容器

```toolbox create -i quay.io/fedora/fedora:[tag]```

使用**特定 Fedora 版本**的默认镜像创建容器

```toolbox create -d fedora -r f[version]```

# SYNOPSIS

**toolbox create** [_options_] [_container_]

# PARAMETERS

**-d**, **--distro** _distro_
> 为指定发行版创建容器

**-r**, **--release** _release_
> 为指定发布版本创建容器

**-i**, **--image** _image_
> 使用指定的容器镜像

**-c**, **--container** _name_
> 为容器指定自定义名称

# DESCRIPTION

**toolbox create** 基于 OCI 镜像创建新的 Toolbx 容器。默认情况下，它会创建一个与宿主系统的发行版和版本相匹配的容器。可以指定自定义镜像，用于开发环境或跨发行版工作。

容器经过配置，可与宿主机无缝集成，包括主目录访问、用户权限以及图形应用支持。

# CAVEATS

需要已安装 podman。如果本地没有缓存，默认镜像将从发行版的 registry 拉取。容器名称在 toolbox 内必须唯一。

# INSTALL

```apt: sudo apt install podman-toolbox```

```dnf: sudo dnf install toolbox```

```pacman: sudo pacman -S toolbox```

```zypper: sudo zypper install toolbox```

```nix: nix profile install nixpkgs#toolbox```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[toolbox](/man/toolbox)(1), [toolbox-enter](/man/toolbox-enter)(1), [toolbox-list](/man/toolbox-list)(1)
