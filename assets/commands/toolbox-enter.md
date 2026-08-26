# TAGLINE

交互式进入 Toolbx 容器

# TLDR

使用**特定发行版**的默认镜像进入 Toolbx 容器

```toolbox enter -d [distribution]```

使用**特定发布版本**的默认镜像进入容器

```toolbox enter -r [release]```

进入**特定 Fedora 版本**的容器

```toolbox enter -d fedora -r f[version]```

# SYNOPSIS

**toolbox enter** [_options_] [_container_]

# PARAMETERS

**-d**, **--distro** _distro_
> 进入指定发行版的容器

**-r**, **--release** _release_
> 进入指定发布版本的容器

**container**
> 要进入的容器名称（默认：当前容器）

# DESCRIPTION

**toolbox enter** 在 Toolbx 容器内提供一个交互式 Shell。容器环境与宿主机无缝集成，共享主目录、用户身份以及图形和网络等系统资源。

这样可以在隔离环境中运行特定发行版的工具、测试软件或进行开发工作，同时保持对宿主机文件和服务的访问。

# CAVEATS

容器必须已存在；请先使用 **toolbox create**。对主目录的更改会在会话之间保留。系统目录是容器专属的，重新创建容器时会被重置。

# INSTALL

```apt: sudo apt install podman-toolbox```

```dnf: sudo dnf install toolbox```

```pacman: sudo pacman -S toolbox```

```zypper: sudo zypper install toolbox```

```nix: nix profile install nixpkgs#toolbox```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[toolbox](/man/toolbox)(1), [toolbox-create](/man/toolbox-create)(1), [toolbox-run](/man/toolbox-run)(1)
