# TAGLINE

面向 X11 的命令行截图工具

# TLDR

截取**屏幕截图**并以当前日期作为文件名保存

```scrot```

截取屏幕截图并保存为 **capture.png**

```scrot capture.png```

**交互式**截取屏幕截图（选择区域/窗口）

```scrot -s```

交互式截取屏幕截图，键盘输入时**不退出**

```scrot -is```

截取带**彩色选择线**的屏幕截图

```scrot -s -l color=[x11_color]```

截取**当前获得焦点的窗口**

```scrot -u```

截图前显示 **10 秒倒计时**

```scrot -c -d 10```

# SYNOPSIS

**scrot** [_options_] [_file_]

# PARAMETERS

**-s**, **--select**
> 用鼠标交互式选择窗口或矩形区域

**-u**, **--focused**
> 截取当前获得焦点的窗口

**-b**, **--border**
> 配合 -u 包含窗口边框

**-d**, **--delay** _sec_
> 截图前等待 _sec_ 秒

**-c**, **--count**
> 使用延迟时显示倒计时

**-q**, **--quality** _num_
> JPEG 图像质量（1-100）

**-t**, **--thumb** _num_
> 按指定百分比生成缩略图

**-e**, **--exec** _cmd_
> 对已保存的图像执行命令

**-l**, **--line** _style_
> 设置选择框线条样式（颜色、宽度等）

**-i**, **--ignorekeyboard**
> 键盘输入时不退出选择模式

**-p**, **--pointer**
> 在截图中包含鼠标指针

**-o**, **--overwrite**
> 若文件存在则覆盖

# DESCRIPTION

**scrot**（SCReenshot）是一款简单的 X11 命令行屏幕捕获工具。它可以截取整个屏幕、特定窗口或用户选择的区域。截图可保存为 PNG、JPEG 或 GIF 文件。

该工具支持延迟截图、生成缩略图以及对生成的图像执行命令（便于自动上传或编辑）。特殊的格式字符串可以基于日期、时间和尺寸动态生成文件名。

# CAVEATS

仅支持 X11；Wayland 环境请使用 **grim** 配合 **slurp**。选择模式可能无法在所有窗口管理器下工作。某些合成器可能导致窗口截取出现问题。

# HISTORY

最初由 Tom Gilbert 编写，他也是 **feh** 的作者。这是一款简单而专注的截图工具，在 Linux 桌面环境中广泛使用，通常与键盘快捷键集成以实现快速截图。

# INSTALL

```apt: sudo apt install scrot```

```dnf: sudo dnf install scrot```

```pacman: sudo pacman -S scrot```

```apk: sudo apk add scrot```

```zypper: sudo zypper install scrot```

```nix: nix profile install nixpkgs#scrot```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[maim](/man/maim)(1), [grim](/man/grim)(1), [import](/man/import)(1), [flameshot](/man/flameshot)(1)
