# TAGLINE

面向不可变 Linux 的容器化环境

# TLDR

交互式**进入** Toolbx 容器

```toolbox enter [container]```

**删除**一个或多个容器

```toolbox rm [container1] [container2]```

**删除**一个或多个镜像

```toolbox rmi [image1] [image2]```

**显示**特定子命令的帮助

```toolbox help [subcommand]```

# SYNOPSIS

**toolbox** [_command_] [_options_]

# PARAMETERS

**create**
> 创建新的 Toolbx 容器

**enter**
> 进入容器进行交互式使用

**list**
> 列出现有的容器和镜像

**rm**
> 删除一个或多个容器

**rmi**
> 删除一个或多个镜像

**run**
> 在容器中运行命令

**-h, --help**
> 显示帮助信息

**--version**
> 显示版本信息

# DESCRIPTION

**toolbox**（或称 Toolbx）在 Linux 上提供容器化的命令行环境，主要面向 Fedora Silverblue、CoreOS 以及其他基于 immutable/ostree 的发行版。它创建的易变容器可与宿主系统无缝集成。

容器可以访问用户的主目录、网络和图形环境，同时与不可变的宿主操作系统保持隔离。这样无需修改基础系统即可安装和使用开发工具。

# CAVEATS

需要 Podman 作为容器运行时。最适合不可变 Linux 发行版。容器镜像因发行版而异。与宿主机的集成程度可能有所不同。

# INSTALL

```apt: sudo apt install podman-toolbox```

```dnf: sudo dnf install toolbox```

```pacman: sudo pacman -S toolbox```

```zypper: sudo zypper install toolbox```

```nix: nix profile install nixpkgs#toolbox```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[podman](/man/podman)(1), [distrobox](/man/distrobox)(1)
