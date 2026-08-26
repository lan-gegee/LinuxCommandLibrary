# TAGLINE

XFCE 截图工具

# TLDR

启动**图形界面**

```xfce4-screenshooter```

捕获**全屏**

```xfce4-screenshooter -f```

捕获并**保存**

```xfce4-screenshooter -f -s [path/to/directory]```

**延迟**后捕获

```xfce4-screenshooter -d [seconds]```

捕获**选区**

```xfce4-screenshooter -r```

捕获**窗口**到剪贴板

```xfce4-screenshooter -w -c```

捕获并使用程序**打开**

```xfce4-screenshooter -w -o [gimp]```

# SYNOPSIS

**xfce4-screenshooter** [_OPTIONS_]

# PARAMETERS

**-f, --fullscreen**
> 捕获整个屏幕

**-w, --window**
> 捕获活动窗口

**-r, --region**
> 用鼠标选择区域

**-d, --delay** _SECONDS_
> 捕获前的等待时间

**-m, --mouse**
> 在截图中包含鼠标光标

**--no-border**
> 从截图中去除窗口边框

**-s, --save** _PATH_
> 保存到文件路径或目录

**-c, --clipboard**
> 复制到剪贴板

**-o, --open** _APPLICATION_
> 使用应用程序打开

**-S, --show-in-folder**
> 在文件管理器中显示已保存的文件

**-V, --version**
> 显示版本信息

**--supported-formats**
> 列出支持的图像格式（取决于已安装的 pixbuf 加载器）

# DESCRIPTION

**xfce4-screenshooter** 是 XFCE 桌面环境的截图工具。它可以捕获整个屏幕、某个窗口或选定区域。

截图可以保存为文件、复制到剪贴板，或在图像编辑器中打开。保存选项支持 **png**、**jpg** 和 **bmp** 文件扩展名。

# CAVEATS

为 XFCE 设计，但也可在其他桌面上使用。区域选择需要鼠标交互。

# INSTALL

```apt: sudo apt install xfce4-screenshooter```

```dnf: sudo dnf install xfce4-screenshooter```

```pacman: sudo pacman -S xfce4-screenshooter```

```apk: sudo apk add xfce4-screenshooter```

```zypper: sudo zypper install xfce4-screenshooter```

```nix: nix profile install nixpkgs#xfce4-screenshooter```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[scrot](/man/scrot)(1), [gnome-screenshot](/man/gnome-screenshot)(1), [flameshot](/man/flameshot)(1), [maim](/man/maim)(1), [spectacle](/man/spectacle)(1), [import](/man/import)(1)
