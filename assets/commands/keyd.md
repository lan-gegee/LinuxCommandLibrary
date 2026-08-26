# TAGLINE

使用内核级输入的 Linux 按键重映射守护进程

# TLDR

**启动并启用** keyd 服务

```systemctl enable keyd --now```

显示**按键**信息（监控模式）

```sudo keyd monitor```

带**时间戳**显示按键事件

```sudo keyd monitor -t```

**重新加载**配置文件

```sudo keyd reload```

**列出**所有有效的键名

```keyd list-keys```

创建**临时绑定**

```sudo keyd bind "[pressed_key] = [output_key]"```

**重置**所有临时绑定

```sudo keyd bind reset```

像键盘输入一样**输入**文本

```sudo keyd input "[text]"```

# SYNOPSIS

**keyd** [_options_] [_command_]

# PARAMETERS

**monitor** [**-t**]
> 实时显示按键信息。若提供 -t，还会以毫秒为单位打印距上一个事件的时间。

**listen**
> 将正在运行的 keyd 守护进程的层状态变化打印到 stdout。便于编写脚本。

**reload**
> 重置绑定并从 /etc/keyd 重新加载配置。

**list-keys**
> 显示所有有效的键名。

**bind** reset|_BINDING_ [_BINDING_...]
> 应用提供的按键绑定，或重置所有绑定。

**input** [**-t** _timeout_] _text_ [_text_...]
> 将提供的文本作为键盘事件输入。若无参数则从 stdin 读取。超时时间（微秒）设定事件发送之间的延迟。

**-v**, **--version**
> 打印当前版本并退出。

**-h**, **--help**
> 打印帮助并退出。

# DESCRIPTION

**keyd** 是一个工作在内核层级的按键重映射守护进程，基于 evdev 实现。它可以在整个系统范围内重映射按键，不依赖显示服务器（适用于 X11、Wayland 和虚拟控制台）。

/etc/keyd/ 中的配置文件定义键映射、层和宏。守护进程拦截输入事件，按配置对其进行转换后再传递给应用程序。功能包括分层、一次性修饰键和宏。

# CAVEATS

大多数操作需要 root 权限。配置更改需要通过 `keyd reload` 重载才能生效。它工作在比 X11 键盘映射更低的层级，因此重映射在各处都生效，包括虚拟控制台。

# HISTORY

keyd 的开发目标是提供一个现代、简洁且能在各种显示服务器上通用工作的按键重映射方案。它提供类似 xmodmap 等工具的功能，但工作在内核输入层级。

# INSTALL

```apt: sudo apt install onak```

```pacman: sudo pacman -S keyd```

```apk: sudo apk add keyd```

```zypper: sudo zypper install keyd```

```brew: brew install keyd```

```nix: nix profile install nixpkgs#keyd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xmodmap](/man/xmodmap)(1), [setxkbmap](/man/setxkbmap)(1), [evtest](/man/evtest)(1), [systemctl](/man/systemctl)(1)
