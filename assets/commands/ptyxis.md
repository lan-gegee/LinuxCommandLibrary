# TAGLINE

面向容器的 GNOME 终端模拟器

# TLDR

打开**新窗口**

```ptyxis --new-window```

**执行**命令

```ptyxis -x [command]```

打开**新标签页**

```ptyxis --tab```

设置标签页**标题**

```ptyxis --tab -T "[title]"```

设置**工作目录**

```ptyxis -d [path/to/directory] --tab```

# SYNOPSIS

**ptyxis** [**--new-window**] [**--tab**] [**-x** _command_] [**-d** _dir_] [**-T** _title_]

# PARAMETERS

**--new-window**
> 在新窗口中打开

**--tab**
> 在最后一个窗口中打开新标签页

**-x, --execute _command_**
> 在新终端中执行命令

**-d, --working-directory _dir_**
> 设置工作目录

**-T, --title _title_**
> 设置终端标题

# DESCRIPTION

**ptyxis** 是一款面向容器的 GNOME 终端模拟器。它专为与 Flatpak、Toolbox 和 Distrobox 容器无缝协作而设计，便于在不同容器环境中运行命令。

该终端提供 GPU 加速、标签页和容器集成等现代特性，同时保持简洁的 GNOME 设计风格。

# CAVEATS

需要 GNOME 环境。容器功能需要安装 Flatpak/Toolbox/Distrobox。仍在活跃开发中。

# HISTORY

**ptyxis** 由 **Christian Hergert**（GNOME Builder 开发者）创建，是一款拥抱容器化工作流的现代终端。名称源自希腊语，意为"折叠的书板"。

# INSTALL

```apt: sudo apt install ptyxis```

```dnf: sudo dnf install ptyxis```

```pacman: sudo pacman -S ptyxis```

```apk: sudo apk add ptyxis```

```zypper: sudo zypper install ptyxis```

```nix: nix profile install nixpkgs#ptyxis```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gnome-terminal](/man/gnome-terminal)(1), [toolbox](/man/toolbox)(1), [distrobox](/man/distrobox)(1)
