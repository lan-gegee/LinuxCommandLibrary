# TAGLINE

功能集成的 KDE 文件管理器

# TLDR

**启动**文件管理器

```dolphin```

打开**指定目录**

```dolphin [path/to/directory1] [path/to/directory2]```

打开并**选中**指定文件/目录

```dolphin --select [path/to/file1] [path/to/file2]```

打开**新窗口**

```dolphin --new-window```

以**分屏视图**打开

```dolphin --split [path/to/directory1] [path/to/directory2]```

启动**守护进程**以加快启动速度

```dolphin --daemon```

# SYNOPSIS

**dolphin** [_options_] [_urls_]

# DESCRIPTION

**dolphin** 是 KDE 的文件管理器。它提供图形界面来管理文件和目录，具备标签页、分屏视图、集成终端和文件预览等功能。

它是 KDE Plasma 桌面环境的组成部分，但在安装了 KDE/Qt 库的其他桌面环境中同样可以使用。

# PARAMETERS

**--select** _files_
> 打开时在其所在文件夹中选中指定的文件或目录。

**--new-window**
> 强制打开新窗口，而不是复用已有窗口。

**--split** _dir1_ _dir2_
> 以分屏视图并排打开两个目录。

**--daemon**
> 让 Dolphin 作为 D-Bus 服务在后台运行，从而加快后续启动速度。

**-h**, **--help**
> 显示帮助信息。

**--author**
> 显示作者信息。

**--version**
> 显示版本信息。

# CAVEATS

KDE 应用，依赖 Qt/KDE 库。完整功能需要 KDE 桌面环境。GNOME 用户可参考 Nautilus，XFCE 用户可参考 Thunar。--daemon 选项会让 Dolphin 在后台持续运行，即使没有打开任何窗口也会占用内存。

# INSTALL

```apt: sudo apt install dolphin```

```dnf: sudo dnf install dolphin```

```pacman: sudo pacman -S dolphin```

```apk: sudo apk add dolphin```

```zypper: sudo zypper install dolphin```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nautilus](/man/nautilus)(1), [thunar](/man/thunar)(1), [ranger](/man/ranger)(1), [nemo](/man/nemo)(1), [mc](/man/mc)(1)
