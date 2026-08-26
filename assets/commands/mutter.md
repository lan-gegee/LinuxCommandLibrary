# TAGLINE

GNOME 窗口管理器

# TLDR

**启动 Mutter**

```mutter```

**替换正在运行的窗口管理器**

```mutter --replace```

**以 Wayland 模式运行**

```mutter --wayland```

**以嵌套模式运行**

```mutter --nested```

**显示版本**

```mutter --version```

# SYNOPSIS

**mutter** [_options_]

# PARAMETERS

**--replace**
> 替换正在运行的窗口管理器。

**--wayland**
> 作为 Wayland 合成器运行。

**--nested**
> 嵌套在另一个会话中运行。

**--version**
> 显示版本信息。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mutter** 是 GNOME 的窗口管理器。它负责窗口管理和合成。

该工具同时支持 X11 和 Wayland。它是 GNOME Shell 的核心组件。

# CAVEATS

仅适用于 GNOME。需要 GPU 合成支持。通常通过 GNOME Shell 运行。

# HISTORY

Mutter 由 **Metacity** 演化而来，自 GNOME 3 起成为标准的 GNOME 窗口管理器。

# INSTALL

```apt: sudo apt install mutter```

```dnf: sudo dnf install mutter```

```pacman: sudo pacman -S mutter```

```apk: sudo apk add mutter```

```zypper: sudo zypper install mutter```

```nix: nix profile install nixpkgs#mutter```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[muffin](/man/muffin)(1)
