# TAGLINE

控制 Wayland 的 mako 通知守护进程

# TLDR

**列出**当前通知

```makoctl list```

显示通知**历史**

```makoctl history```

**重新加载**配置

```makoctl reload```

**恢复**最近过期的通知

```makoctl restore```

关闭**所有**通知

```makoctl dismiss -a```

按 ID 关闭某条通知

```makoctl dismiss -n [id]```

**切换**勿扰模式

```makoctl mode -t do-not-disturb```

使用外部**菜单**程序选择通知动作

```makoctl menu [dmenu] -p 'Select action'```

# SYNOPSIS

**makoctl** _command_ [_options_]

# DESCRIPTION

**makoctl** 通过 D-Bus 向运行中的 mako(1) 通知守护进程发送 IPC 命令。它可以列出、关闭和管理通知，还可以重新加载配置和切换模式。

# PARAMETERS

**list**
> 获取当前通知的列表。

**history**
> 获取已关闭通知的列表。

**reload**
> 重新加载配置文件。

**restore**
> 从历史缓冲区恢复最近一条过期的通知。

**dismiss** [**-a**|**--all**] [**-g**|**--group**] [**-h**|**--no-history**] [**-n** _id_]
> 关闭通知。默认关闭第一条通知。使用 **-a** 关闭全部，**-g** 关闭第一组通知，**-n** 按 ID 关闭，**-h** 关闭时不加入历史记录。

**invoke** [**-n** _id_] [_action_]
> 对通知调用一个动作。未指定动作时调用默认动作。使用 **-n** 按 ID 指定通知。

**menu** [**-n** _id_] _program_ [_argument_...]
> 使用外部程序（如 dmenu、wofi）选择通知上的动作。各动作以换行符分隔传给该程序。

**mode** [**-s** _mode_...] [**-a** _mode_...] [**-r** _mode_...] [**-t** _mode_...]
> 管理通知模式。不带选项时列出当前模式。使用 **-s** 设置模式、**-a** 添加、**-r** 移除、**-t** 切换。

**-h**, **--help**
> 显示帮助信息并退出。

# INSTALL

```apt: sudo apt install mako-notifier```

```dnf: sudo dnf install mako```

```pacman: sudo pacman -S mako```

```apk: sudo apk add mako```

```zypper: sudo zypper install mako```

```brew: brew install mako```

```nix: nix profile install nixpkgs#mako```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mako](/man/mako)(1), [makoctl-dismiss](/man/makoctl-dismiss)(1), [notify-send](/man/notify-send)(1), [dunstctl](/man/dunstctl)(1)
