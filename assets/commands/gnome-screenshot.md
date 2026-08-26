# TAGLINE

GNOME 屏幕截图工具

# TLDR

拍摄**屏幕截图**并保存到默认位置

```gnome-screenshot```

保存到**指定文件**

```gnome-screenshot -f path/to/file.png```

保存到**剪贴板**

```gnome-screenshot -c```

**延迟**后截图

```gnome-screenshot -d 5```

仅截取**当前窗口**

```gnome-screenshot -w```

截取**选定区域**

```gnome-screenshot -a```

打开**交互式**对话框

```gnome-screenshot -i```

在截图中包含**鼠标指针**

```gnome-screenshot -p```

# SYNOPSIS

**gnome-screenshot** [**-c**] [**-w**] [**-a**] [**-p**] [**-d** _SECONDS_] [**-i**] [**-f** _FILENAME_]

# PARAMETERS

**-c, --clipboard**
> 将截图发送到剪贴板而非保存为文件

**-w, --window**
> 仅截取当前活动窗口

**-a, --area**
> 截取用户选定的屏幕区域

**-p, --include-pointer**
> 在截图中包含鼠标指针

**-d, --delay=SECONDS**
> 截图前等待指定的秒数

**-e, --border-effect=EFFECT**
> 应用视觉效果（shadow、border、vintage 或 none）

**-i, --interactive**
> 启动交互式对话框来设置截图选项

**-f, --file=FILENAME**
> 指定输出文件名

**--display=DISPLAY**
> 指定要截取的 X display

# DESCRIPTION

**gnome-screenshot** 是一款 GNOME 工具，可截取整个屏幕、某个窗口或用户自定义区域，并将图像保存到文件或剪贴板。它提供命令行和交互两种模式，支持灵活的屏幕捕获。

截图默认保存到 ~/Pictures。该工具与 GNOME 桌面集成，便于快速截屏。

# CAVEATS

边框效果功能已弃用，默认为 "none"。**gnome-screenshot 自 GNOME 42 起（2022 年 3 月）已弃用**，替代方案是 GNOME Shell 内置的截图工具（PrtSc）。在 GNOME 49+ 的 Wayland 下无法使用。

# HISTORY

**gnome-screenshot** 是 GNOME 桌面环境的一部分，提供了一个简单的屏幕内容捕获工具。

# INSTALL

```apt: sudo apt install gnome-screenshot```

```dnf: sudo dnf install gnome-screenshot```

```pacman: sudo pacman -S gnome-screenshot```

```apk: sudo apk add gnome-screenshot```

```zypper: sudo zypper install gnome-screenshot```

```nix: nix profile install nixpkgs#gnome-screenshot```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[scrot](/man/scrot)(1), [import](/man/import)(1)
