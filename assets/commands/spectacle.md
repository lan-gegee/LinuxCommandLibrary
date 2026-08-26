# TAGLINE

KDE Plasma 截图工具

# TLDR

**截图**

```spectacle```

**捕获全屏**

```spectacle -f```

**捕获活动窗口**

```spectacle -a```

**捕获矩形区域**

```spectacle -r```

**捕获光标下的窗口**

```spectacle -u```

**延迟捕获**（单位为秒）

```spectacle -d [5]```

后台模式**保存到文件**

```spectacle -b -o [screenshot.png]```

后台模式**复制到剪贴板**

```spectacle -b -c```

# SYNOPSIS

**spectacle** [_-f_] [_-a_] [_-r_] [_-d delay_] [_-o file_] [_options_]

# PARAMETERS

**-f**, **--fullscreen**
> 全屏捕获。

**-a**, **--activewindow**
> 活动窗口。

**-r**, **--region**
> 矩形区域。

**-d**, **--delay** _SECS_
> 延迟秒数。

**-o**, **--output** _FILE_
> 保存到文件。

**-c**, **--clipboard**
> 复制到剪贴板。

**-b**, **--background**
> 不显示 GUI。

**-u**, **--windowundercursor**
> 捕获光标下的窗口（包括弹窗父级）

**-t**, **--transientonly**
> 捕获光标下的窗口（不包括弹窗父级）

**-m**, **--currentmonitor**
> 捕获当前显示器

**-p**, **--pointer**
> 在截图中包含鼠标指针（后台模式）

**-w**, **--nowindow**
> 启动但不截图

**-n**, **--nonotify**
> 抑制通知

# DESCRIPTION

**spectacle** 是 KDE 的截图工具。它提供多种选项来捕获屏幕内容。

通过选择模式来确定捕获区域：全屏、当前显示器、活动窗口、光标下的窗口或矩形区域。

延迟选项让你有时间在捕获前摆放窗口或打开菜单。后台模式支持脚本化捕获而不显示 GUI。

# CAVEATS

KDE/Plasma 应用程序。在其他桌面上可能无法工作。Wayland 存在限制。

# HISTORY

**Spectacle** 是 **KDE Plasma** 的默认截图应用。它以现代化的界面取代了 KSnapshot。

# INSTALL

```apt: sudo apt install kde-spectacle```

```dnf: sudo dnf install spectacle```

```pacman: sudo pacman -S spectacle```

```apk: sudo apk add spectacle```

```zypper: sudo zypper install spectacle```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[scrot](/man/scrot)(1), [gnome-screenshot](/man/gnome-screenshot)(1), [flameshot](/man/flameshot)(1)
