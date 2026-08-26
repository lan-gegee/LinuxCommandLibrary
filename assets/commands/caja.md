# TAGLINE

MATE 桌面的文件管理器

# TLDR

打开**主目录**

```caja```

在单独的窗口中打开**指定目录**

```caja [path/to/directory1] [path/to/directory2] ...```

以**标签页**方式打开目录

```caja -t [path/to/directory1] [path/to/directory2] ...```

以**指定的窗口大小**打开

```caja -g [600]x[400] [path/to/directory]```

**关闭**所有窗口

```caja -q```

# SYNOPSIS

**caja** [_options_] [_directories_...]

# DESCRIPTION

**caja** 是 MATE 桌面环境的默认文件管理器。它提供图形界面，用于浏览文件和目录、管理文件操作以及访问网络位置。

Caja 是 GNOME 的 Nautilus 文件管理器的一个分支，保留了传统的桌面文件管理体验。

# PARAMETERS

**-t, --tabs**
> 以标签页而非窗口的方式打开目录

**-g, --geometry** _WxH_
> 以像素为单位设置窗口大小

**-q, --quit**
> 关闭所有 Caja 窗口

**-n, --no-default-window**
> 仅为显式指定的路径创建窗口

**--browser**
> 打开浏览器窗口

# INSTALL

```apt: sudo apt install caja```

```dnf: sudo dnf install caja```

```pacman: sudo pacman -S caja```

```apk: sudo apk add caja```

```zypper: sudo zypper install caja```

```nix: nix profile install nixpkgs#caja```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nautilus](/man/nautilus)(1), [dolphin](/man/dolphin)(1), [thunar](/man/thunar)(1), [ranger](/man/ranger)(1)

# RESOURCES

```[Source code](https://github.com/mate-desktop/caja)```

```[Homepage](https://mate-desktop.org/)```

<!-- verified: 2026-06-22 -->
