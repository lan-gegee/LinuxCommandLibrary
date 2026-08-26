# TAGLINE

在容器中运行 Linux 发行版并与宿主机深度集成

# TLDR

**创建新容器**

```distrobox create --name [mycontainer] --image [ubuntu:latest]```

**列出所有容器**

```distrobox list```

**进入容器**

```distrobox enter [mycontainer]```

**在容器内运行命令**

```distrobox enter [mycontainer] -- [command]```

**将应用从容器导出到宿主机**

```distrobox-export --app [application]```

**升级所有容器**

```distrobox upgrade --all```

**停止容器**

```distrobox stop [mycontainer]```

**删除容器**

```distrobox rm [mycontainer]```

# SYNOPSIS

**distrobox** [_global_options_] _subcommand_ [_options_] [_arguments_]

# PARAMETERS

**create**
> 创建新容器。

**enter**
> 进入已有容器。

**list**
> 列出用 distrobox 创建的容器。

**rm**
> 删除容器。

**stop**
> 停止正在运行的容器。

**upgrade**
> 升级一个或多个容器。

**--help**, **-h**
> 显示帮助信息。

**--root**
> 以 root 身份运行 distrobox（使用 sudo/doas）。

# DESCRIPTION

**distrobox** 可以在终端容器中运行任意 Linux 发行版，同时与宿主机操作系统紧密集成。容器共享主目录、存储和硬件访问（包括图形和音频）。

它构建于 Podman 或 Docker 之上，可无缝使用不同发行版的软件包管理器和软件。安装在容器内的应用可以导出到宿主机的应用菜单中显示。

# INSTALL

```dnf: sudo dnf install distrobox```

```pacman: sudo pacman -S distrobox```

```apk: sudo apk add distrobox```

```zypper: sudo zypper install distrobox```

```brew: brew install distrobox```

```nix: nix profile install nixpkgs#distrobox```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[distrobox-create](/man/distrobox-create)(1), [distrobox-enter](/man/distrobox-enter)(1), [distrobox-list](/man/distrobox-list)(1), [distrobox-rm](/man/distrobox-rm)(1), [distrobox-stop](/man/distrobox-stop)(1), [distrobox-upgrade](/man/distrobox-upgrade)(1), [distrobox-export](/man/distrobox-export)(1), [distrobox-host-exec](/man/distrobox-host-exec)(1), [podman](/man/podman)(1), [docker](/man/docker)(1)
