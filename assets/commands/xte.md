# TAGLINE

生成伪造的 X11 输入事件

# TLDR

**模拟按键**

```xte 'key [Return]'```

**输入字符串**

```xte 'str [Hello World]'```

**点击鼠标左键**

```xte 'mouseclick 1'```

**移动鼠标到绝对位置**

```xte 'mousemove [100] [200]'```

**相对移动鼠标**

```xte 'mousermove [10] [-5]'```

**模拟 Ctrl+C**

```xte 'keydown Control_L' 'key c' 'keyup Control_L'```

**在动作之间休眠**

```xte 'mousemove 100 100' 'sleep 1' 'mouseclick 1'```

# SYNOPSIS

**xte** [_options_] _command_ [_command_...]

# COMMANDS

**key** _k_：按下并释放按键 k。

**keydown** _k_：按住按键 k。

**keyup** _k_：释放按键 k。

**str** _text_：输入文本字符串。

**mouseclick** _n_：点击鼠标按钮（1=左键，2=中键，3=右键）。

**mousedown** _n_：按下鼠标按钮。

**mouseup** _n_：释放鼠标按钮。

**mousemove** _x_ _y_：移动到绝对位置。

**mousermove** _x_ _y_：相对当前位置移动。

**sleep** _n_：休眠 n 秒。

**usleep** _n_：休眠 n 微秒。

# PARAMETERS

**-x** _display_
> 向指定 display 发送命令。

**-i** _id_
> 使用指定的 XInput 设备。

# DESCRIPTION

**xte** 使用 XTest X11 扩展生成伪造的键盘和鼠标输入。它属于 xautomation 软件包，可以在脚本中自动化 GUI 交互。

命令可以在单次调用中链式执行，也可以分多次调用。按键名遵循 X11 keysym 命名规范。鼠标按钮编号：1（左键）、2（中键）、3（右键）、4/5（滚轮）。

常见用途包括 GUI 测试、自动化重复任务和创建宏。经常与 xbindkeys 结合使用来实现键盘快捷键。

# CAVEATS

仅支持 X11；不支持 Wayland。str 命令对 Unicode 支持有限。某些应用程序可能检测到合成输入。属于 xautomation 软件包。

# HISTORY

**xte** 属于 xautomation，这是 Steve Slaven 创建的一套 X11 自动化工具。它为 XTest 扩展提供了简单的命令行接口，而 XTest 扩展正是为 X 应用程序的自动化测试而设计的。

# INSTALL

```apt: sudo apt install xautomation```

```dnf: sudo dnf install xautomation```

```pacman: sudo pacman -S xautomation```

```zypper: sudo zypper install xautomation```

```nix: nix profile install nixpkgs#xautomation```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xdotool](/man/xdotool)(1), [xbindkeys](/man/xbindkeys)(1), [xinput](/man/xinput)(1)
