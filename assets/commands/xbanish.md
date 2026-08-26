# TAGLINE

输入时隐藏 X11 鼠标指针

# TLDR

**打字时隐藏指针**，移动鼠标时重新显示

```xbanish```

**在程序运行期间始终隐藏指针**

```xbanish -a```

**忽略某个修饰键**，使其不隐藏指针

```xbanish -i [shift]```

**隐藏时把指针移到**屏幕角落

```xbanish -m [nw]```

**空闲若干秒后隐藏指针**

```xbanish -t [5]```

**开机自动运行**：将其加入 X 启动文件

```echo "xbanish &" >> ~/.xinitrc```

# SYNOPSIS

**xbanish** [_-a_] [_-d_] [_-i modifier_] [_-m position_] [_-t seconds_] [_-s_]

# DESCRIPTION

**xbanish** 在按下按键时隐藏 X11 鼠标指针，并在移动鼠标或点击按钮时重新显示。这样在进行键盘驱动的工作时指针不会碍事，而在真正需要鼠标时又能立刻看到。

它是作为 **unclutter -keystroke** 模式的替代品而编写的，后者必须抓取并重放按键，可能干扰其他客户端。xbanish 则使用 XInput 扩展被动地监听输入事件。在支持 XInput 2.2 的系统上它读取原始的运动和按钮事件；否则它会遍历窗口层级来注册事件。指针的实际显示与隐藏由 XFixes 扩展完成。

由于只监听事件，xbanish 作为一个轻量级后台守护进程运行，无论窗口管理器是什么都能作用于整个 X 会话。

# PARAMETERS

**-a**
> 运行期间始终保持指针隐藏。

**-d**
> 向标准输出打印调试消息。

**-i** _MODIFIER_
> 在按住给定修饰键时忽略按键，使指针保持可见。有效的修饰键为 shift、lock、control、mod1、mod2、mod3、mod4、mod5 或 all。可多次指定。

**-m** _POSITION_
> 隐藏指针时，将其移到屏幕角落（nw、ne、sw、se）或绝对位置（如 +50-100）。在角落前加 **w** 前缀可相对于当前窗口定位。

**-t** _SECONDS_
> 鼠标无移动达到指定秒数后隐藏指针。

**-s**
> 忽略滚动事件，这样滚动滚轮不会让指针重新出现。

# CAVEATS

仅适用于 X11，在原生 Wayland 会话下无效。需要 XInput 和 XFixes 扩展，而几乎所有现代 X 服务器都具备这些扩展。

# HISTORY

**xbanish** 由 Joshua Stein（jcs）编写，用基于 XInput 和 XFixes 扩展的更简洁的事件驱动实现，取代了 **unclutter** 的按键隐藏行为。

# INSTALL

```apt: sudo apt install xbanish```

```dnf: sudo dnf install xbanish```

```apk: sudo apk add xbanish```

```zypper: sudo zypper install xbanish```

```nix: nix profile install nixpkgs#xbanish```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[unclutter](/man/unclutter)(1), [xdotool](/man/xdotool)(1), [xinput](/man/xinput)(1), [xsetroot](/man/xsetroot)(1)

# RESOURCES

```[Source code](https://github.com/jcs/xbanish)```

<!-- verified: 2026-06-18 -->
