# TLDR

# TAGLINE

面向 X11 的轻量级 Unicode 终端模拟器

# TLDR

打开新**窗口**

```urxvt```

在特定**目录**中打开

```urxvt -cd [path/to/directory]```

运行**命令**

```urxvt -e [command]```

运行命令并**保持**窗口打开

```urxvt --hold -e [command]```

经由 **shell** 运行

```urxvt -e sh -c [command]```

# SYNOPSIS

**urxvt** [_OPTIONS_]

# PARAMETERS

**-cd** _DIR_
> 在指定目录中启动

**-e** _COMMAND_
> 执行指定命令而非 shell

**--hold**
> 命令退出后仍保持窗口开启

**-fn** _FONT_
> 指定字体

**-fg** _COLOR_
> 前景颜色

**-bg** _COLOR_
> 背景颜色

# DESCRIPTION

**urxvt**（rxvt-unicode）是一款高度可定制的终端模拟器，支持 Unicode、透明效果和 Perl 扩展。它以轻量快速著称，同时可以通过 X 资源实现深度定制。

配置一般通过 ~/.Xresources 或命令行选项完成。

# CAVEATS

需要 X11 显示环境。通过 X 资源进行配置的方式起初可能让人感到复杂。部分功能需要启用 Perl 扩展才能使用。

# INSTALL

```apt: sudo apt install rxvt-unicode```

```dnf: sudo dnf install rxvt-unicode```

```pacman: sudo pacman -S rxvt-unicode```

```apk: sudo apk add rxvt-unicode```

```zypper: sudo zypper install rxvt-unicode```

```brew: brew install rxvt-unicode```

```nix: nix profile install nixpkgs#rxvt-unicode```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xterm](/man/xterm)(1), [st](/man/st)(1)
