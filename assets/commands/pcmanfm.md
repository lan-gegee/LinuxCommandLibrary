# TAGLINE

轻量级文件管理器

# TLDR

**打开文件管理器**

```pcmanfm```

**打开指定目录**

```pcmanfm [/path/to/directory]```

**以桌面管理模式打开**

```pcmanfm --desktop```

**新建窗口**

```pcmanfm -n [path]```

**设置壁纸**

```pcmanfm --set-wallpaper=[image.jpg]```

# SYNOPSIS

**pcmanfm** [_options_] [_path_]

# PARAMETERS

_PATH_
> 要打开的目录。

**--desktop**
> 桌面管理模式。

**-n**
> 新建窗口。

**--set-wallpaper** _FILE_
> 设置桌面壁纸。

**--wallpaper-mode** _MODE_
> 壁纸显示模式。

# DESCRIPTION

**pcmanfm** 是一款轻量级文件管理器。属于 LXDE 桌面环境。

该应用提供文件浏览功能。还负责桌面图标管理。

# CAVEATS

基于 GTK。轻量的替代方案。LXDE 的组件。

# HISTORY

PCManFM 是作为 LXDE 桌面的**轻量级文件管理器**而创建的。

# INSTALL

```apt: sudo apt install pcmanfm```

```dnf: sudo dnf install pcmanfm```

```pacman: sudo pacman -S pcmanfm```

```apk: sudo apk add pcmanfm```

```zypper: sudo zypper install pcmanfm```

```nix: nix profile install nixpkgs#pcmanfm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[thunar](/man/thunar)(1), [nautilus](/man/nautilus)(1), [dolphin](/man/dolphin)(1)
