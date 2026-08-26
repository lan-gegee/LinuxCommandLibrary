# TAGLINE

Xfce 图形文件管理器

# TLDR

打开**当前**目录

```thunar```

打开**指定**目录

```thunar [/path/to/directory]```

打开**批量重命名**工具

```thunar --bulk-rename```

批量重命名指定的**文件**

```thunar --bulk-rename [file1] [file2] [file3]```

**关闭**所有 Thunar 窗口

```thunar --quit```

# SYNOPSIS

**thunar** [_OPTIONS_] [_URI_...]

# PARAMETERS

**-B, --bulk-rename**
> 打开批量重命名工具。如果指定了 URI，则将其传递给重命名器。

**-q, --quit**
> 关闭所有 Thunar 窗口，若守护进程正在运行则将其终止。

**--daemon**
> 在后台作为守护进程运行，加快后续窗口的启动速度。

**--display** _DISPLAY_
> 要使用的 X display。

**-V, --version**
> 显示版本信息后退出。

**-h, --help**
> 显示帮助信息后退出。

# DESCRIPTION

**thunar** 是 Xfce 桌面环境的图形文件管理器。它提供简洁轻量的界面来浏览文件和目录，并支持自定义动作、标志（emblem）和插件。

URI 可以是 file: 或 trash: URI、绝对路径或相对于当前目录的路径。如果不指定 URI，则打开当前文件夹。

批量重命名工具可以使用模式和模板一次重命名多个文件。

# CAVEATS

主要为 Xfce 设计，但也能在其他桌面上运行。自定义动作等部分功能需要进行配置。插件可扩展归档、媒体等方面的功能。

# HISTORY

**Thunar** 由 **Benedikt Meurer** 为 Xfce 开发，取代了较旧的 xffm 文件管理器。它在强调速度和简洁的同时提供了必要的文件管理功能。

# INSTALL

```apt: sudo apt install thunar```

```pacman: sudo pacman -S thunar```

```apk: sudo apk add thunar```

```zypper: sudo zypper install thunar```

```nix: nix profile install nixpkgs#thunar```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nautilus](/man/nautilus)(1), [dolphin](/man/dolphin)(1), [pcmanfm](/man/pcmanfm)(1), [nemo](/man/nemo)(1)
