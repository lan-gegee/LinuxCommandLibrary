# TAGLINE

X11 键盘和鼠标自动化

# TLDR

**按名称搜索窗口**

```xdotool search --onlyvisible --name firefox```

执行**鼠标点击**

```xdotool click 1```

获取**活动窗口** ID

```xdotool getactivewindow```

**聚焦到指定窗口**

```xdotool windowfocus --sync 12345```

带延迟**输入文本**

```xdotool type --delay 500 "Hello world"```

按下一个**按键**

```xdotool key Return```

**移动鼠标**到指定位置

```xdotool mousemove 100 200```

获取**鼠标位置**

```xdotool getmouselocation```

# SYNOPSIS

**xdotool** _command_ [_options_] [_args_]

# DESCRIPTION

**xdotool** 在 X11 中模拟键盘和鼠标输入。它可以搜索窗口、发送按键、移动/点击鼠标以及操作窗口，非常适合自动化和脚本编写。

# COMMANDS

**search [options] pattern**
> 搜索匹配模式的窗口

**getactivewindow**
> 输出当前活动窗口的 ID

**getwindowfocus**
> 输出当前获得焦点的窗口 ID

**windowfocus [options] window_id**
> 聚焦一个窗口

**windowactivate [options] window_id**
> 激活（聚焦并提升）一个窗口

**windowmove [options] window_id x y**
> 移动一个窗口

**windowsize [options] window_id width height**
> 调整窗口大小

**windowminimize window_id**
> 最小化一个窗口

**key [options] keystroke**
> 发送一次按键

**keydown/keyup key**
> 按下/释放一个键

**type [options] text**
> 输入一串字符

**click [options] button**
> 点击鼠标按钮（1=左键，2=中键，3=右键）

**mousedown/mouseup button**
> 按下/释放鼠标按钮

**mousemove [options] x y**
> 移动鼠标光标

**getmouselocation**
> 获取当前鼠标位置

# PARAMETERS

**--delay milliseconds**
> 输入时按键之间的延迟

**--clearmodifiers**
> 命令前清除修饰键状态

**--sync**
> 等待窗口变为可见

**--onlyvisible**
> 仅搜索可见窗口

**--name**
> 按窗口名称搜索

**--class**
> 按窗口类搜索

**--window window_id**
> 定位到特定窗口

# CAVEATS

仅适用于 X11，不适用于 Wayland。某些应用程序可能不响应模拟输入。窗口 ID 是会话相关的，重启后会改变。

# HISTORY

**xdotool** 由 Jordan Sissel 编写，是一款 X11 自动化工具。它通过 XTEST 扩展提供可脚本化的输入事件模拟能力。

# INSTALL

```apt: sudo apt install xdotool```

```dnf: sudo dnf install xdotool```

```pacman: sudo pacman -S xdotool```

```apk: sudo apk add xdotool```

```zypper: sudo zypper install xdotool```

```brew: brew install xdotool```

```nix: nix profile install nixpkgs#xdotool```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xte](/man/xte)(1), [xprop](/man/xprop)(1), [wmctrl](/man/wmctrl)(1)
