# TAGLINE

显示 MATE 桌面环境的相关信息

# TLDR

**打开 MATE 关于对话框**

```mate-about```

**显示 MATE 版本字符串**

```mate-about --version```

# SYNOPSIS

**mate-about** [_options_]

# PARAMETERS

**--version**
> 将 MATE 桌面环境版本打印到终端并退出。

**--gtk-module** _module_
> 加载额外的 GTK 模块。

**--display** _display_
> 要使用的 X display。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mate-about** 显示 MATE 桌面环境的相关信息，包括版本号、贡献者名单和许可信息。MATE 是 GNOME 2 的一个分支，为 Linux 及其他类 Unix 系统提供传统桌面体验。

不带选项运行时，它会打开一个图形对话框，展示 MATE 版本详情、贡献者和许可证。**--version** 选项则只向终端输出版本字符串，不打开图形界面。

# HISTORY

MATE 始于 **2011 年**，是 GNOME 3 转向全新界面范式后对 GNOME 2 桌面的延续。其名称来自马黛茶（yerba mate），一种南美植物。

# INSTALL

```apt: sudo apt install mate-desktop```

```dnf: sudo dnf install mate-desktop```

```pacman: sudo pacman -S mate-desktop```

```apk: sudo apk add mate-desktop```

```zypper: sudo zypper install mate-desktop```

```nix: nix profile install nixpkgs#mate-desktop```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mate-about](/man/mate-about)(1)
