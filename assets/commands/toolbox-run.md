# TAGLINE

在 Toolbx 容器中运行命令

# TLDR

在容器中**运行**命令

```toolbox run -c [container_name] [command]```

在**发行版**容器中运行

```toolbox run -d [distribution] -r [release] [command]```

在 Fedora 容器中运行 **emacs**

```toolbox run -d fedora -r f[version] emacs```

# SYNOPSIS

**toolbox run** [_OPTIONS_] _COMMAND_ [_ARGS_...]

# PARAMETERS

**-c, --container** _NAME_
> 指定容器名称

**-d, --distro** _DISTRO_
> 指定发行版

**-r, --release** _RELEASE_
> 指定发行版的发布版本

# DESCRIPTION

**toolbox run** 在现有的 Toolbx 容器内执行命令，无需进入交互式会话。命令在容器环境中运行，完成后返回宿主机。

这适用于在不离开宿主机系统的情况下，于容器环境中运行单条命令或脚本。

# CAVEATS

容器必须已存在且正在运行。命令必须能在容器内部使用。某些情况下环境与交互式会话有所不同。

# INSTALL

```apt: sudo apt install podman-toolbox```

```dnf: sudo dnf install toolbox```

```pacman: sudo pacman -S toolbox```

```zypper: sudo zypper install toolbox```

```nix: nix profile install nixpkgs#toolbox```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[toolbox](/man/toolbox)(1), [toolbox-enter](/man/toolbox-enter)(1), [toolbox-create](/man/toolbox-create)(1)
