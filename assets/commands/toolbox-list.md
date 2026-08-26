# TAGLINE

列出 Toolbx 容器和镜像

# TLDR

列出**所有** Toolbx 容器和镜像

```toolbox list```

只列出**容器**

```toolbox list -c```

只列出**镜像**

```toolbox list -i```

# SYNOPSIS

**toolbox list** [_options_]

# PARAMETERS

**-c**, **--containers**
> 只列出容器

**-i**, **--images**
> 只列出镜像

# DESCRIPTION

**toolbox list** 显示现有的 Toolbx 容器和镜像。它会显示容器名称、所用镜像、创建时间和运行状态。这有助于管理多个开发环境，并了解哪些容器可用。

输出会区分容器（可运行的环境）和镜像（创建容器所用的基础模板）。

# INSTALL

```apt: sudo apt install podman-toolbox```

```dnf: sudo dnf install toolbox```

```pacman: sudo pacman -S toolbox```

```zypper: sudo zypper install toolbox```

```nix: nix profile install nixpkgs#toolbox```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[toolbox](/man/toolbox)(1), [toolbox-create](/man/toolbox-create)(1), [toolbox-rm](/man/toolbox-rm)(1)
