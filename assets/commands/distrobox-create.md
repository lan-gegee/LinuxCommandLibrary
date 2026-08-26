# TAGLINE

从 Linux 发行版镜像创建 Distrobox 容器

# TLDR

使用 **Ubuntu 镜像**创建容器

```distrobox-create --name [container_name] --image [ubuntu:latest]```

**克隆**现有容器

```distrobox-create --clone [source_container] --name [new_container]```

以非交互方式创建，**拉取镜像**并安装额外的软件包

```distrobox-create -Y -n [dev] -i [fedora:latest] -ap "[git vim]"```

**显示兼容的镜像**

```distrobox-create --compatibility```

# SYNOPSIS

**distrobox-create** [_options_] [_name_]

# DESCRIPTION

**distrobox-create** 从任意 Linux 发行版镜像创建 Distrobox 容器。容器与主机紧密集成，共享用户的主目录、外部存储、USB 设备、图形（X11/Wayland）和音频。

# PARAMETERS

**-i, --image** _image_
> 要使用的容器镜像

**-n, --name** _name_
> 容器名称

**-c, --clone** _container_
> 克隆现有容器

**-H, --home** _path_
> 自定义主目录

**-p, --pull**
> 即使镜像已存在本地也拉取（隐含 --yes）

**-Y, --yes**
> 非交互；直接拉取镜像而不询问

**-ap, --additional-packages** _packages_
> 初始设置期间要安装的额外软件包

**--volume** _spec_
> 要挂载进容器的额外卷

**-I, --init**
> 在容器内使用 init 系统（如 systemd）

**--nvidia**
> 将主机的 NVIDIA 驱动集成到容器中

**-r, --root**
> 创建有根（rootful）容器（以 root 启动容器管理器）

**-C, --compatibility**
> 显示兼容镜像列表

# CAVEATS

需要 Podman 或 Docker。镜像必须是兼容的 Linux 发行版。主目录共享是双向的。首次进入可能因初始化而耗时较长。

# INSTALL

```dnf: sudo dnf install distrobox```

```pacman: sudo pacman -S distrobox```

```apk: sudo apk add distrobox```

```zypper: sudo zypper install distrobox```

```brew: brew install distrobox```

```nix: nix profile install nixpkgs#distrobox```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[distrobox](/man/distrobox)(1), [distrobox-enter](/man/distrobox-enter)(1), [podman](/man/podman)(1)

# RESOURCES

```[Source code](https://github.com/89luca89/distrobox)```

```[Homepage](https://distrobox.it)```

<!-- verified: 2026-07-11 -->
