# TAGLINE

Cinnamon 桌面的窗口管理器和合成器

# TLDR

**启动 Muffin 窗口管理器**

```muffin```

**替换正在运行的窗口管理器**

```muffin --replace```

**连接到特定的 X display**

```muffin --display=[display]```

**显示版本**

```muffin --version```

# SYNOPSIS

**muffin** [_options_]

# PARAMETERS

**--replace**
> 用 Muffin 替换已在运行的窗口管理器。

**--display**=_DISPLAY_
> 连接到指定的 X display。

**--sm-client-id**=_ID_
> 指定会话管理客户端 ID。

**--sm-disable**
> 禁用会话管理。

**--sm-save-file**=_FILENAME_
> 从文件加载先前保存的会话。

**--version**
> 显示版本信息。

**-?**, **--help**
> 显示帮助信息。

# DESCRIPTION

**muffin** 是面向 Cinnamon 桌面环境的基于 Clutter 的合成窗口管理器。它是 GNOME Mutter 的分支，面向非技术用户，旨在与 Cinnamon 桌面紧密集成。

Muffin 负责窗口放置、合成和基本的窗口管理。它使用 GTK，并有意省略了传统 Unix 窗口管理器中的某些特性。

# CAVEATS

仅适用于 Cinnamon 桌面。需要 X11 合成支持。建议使用 GPU 加速。不支持 Wayland。

# HISTORY

muffin 从 **GNOME 的 Mutter** 分支而来，供 Linux Mint 的 Cinnamon 桌面环境使用。它作为 Cinnamon 项目的一部分进行维护。

# INSTALL

```apt: sudo apt install muffin```

```dnf: sudo dnf install muffin```

```pacman: sudo pacman -S muffin```

```zypper: sudo zypper install muffin```

```nix: nix profile install nixpkgs#muffin```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mutter](/man/mutter)(1), [cinnamon](/man/cinnamon)(1), [kwin](/man/kwin)(1), [openbox](/man/openbox)(1)
