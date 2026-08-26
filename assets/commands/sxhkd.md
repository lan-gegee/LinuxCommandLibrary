# TAGLINE

简单的 X11 热键守护进程

# TLDR

以默认配置**启动 sxhkd**

```sxhkd &```

**使用自定义配置**文件启动

```sxhkd -c [~/.config/sxhkd/custom_sxhkdrc] &```

**启动并将状态输出**到 FIFO

```sxhkd -s [/tmp/sxhkd.fifo] &```

将命令输出**重定向**到文件

```sxhkd -r [/tmp/sxhkd.log] &```

不重启而**重新加载配置**

```pkill -USR1 sxhkd```

**切换热键抓取状态**

```pkill -USR2 sxhkd```

将**组合键链超时**设为 3 秒

```sxhkd -t 3 &```

# SYNOPSIS

**sxhkd** [**-hv**] [**-m** _count_] [**-t** _timeout_] [**-c** _config_file_] [**-r** _redir_file_] [**-s** _status_fifo_] [_config_file_...]

# PARAMETERS

**-h**
> 显示帮助并退出

**-v**
> 显示版本并退出

**-c** _config_file_
> 从指定文件而非默认位置读取配置

**-r** _redir_file_
> 将命令输出重定向到指定文件

**-s** _status_fifo_
> 将状态信息写入指定 FIFO

**-t** _timeout_
> 组合键链超时时间（秒）

**-m** _count_
> 处理前 count 个映射通知事件（用于键盘布局切换）

# DESCRIPTION

**sxhkd**（Simple X Hotkey Daemon）监听 X11 上的键盘和鼠标事件，并执行其配置文件中定义的命令。它与窗口管理器无关，常与 **bspwm** 等平铺式窗口管理器搭配使用。

配置默认从 **~/.config/sxhkd/sxhkdrc** 读取。每条绑定由一行热键和随后的命令行（用空白缩进）组成。修饰键包括 **super**、**alt**、**ctrl**、**shift** 和 **mod1-mod5**。

主要特性包括组合键绑定（如 **super + a ; b** 的序列）、按键释放事件（在 keysym 前加 **@**）以及鼠标按钮（**button1-button24**）。含 **{a,b,c}** 的序列会展开为多条绑定。

命令通过 **$SXHKD_SHELL** 或 **$SHELL** 执行。发送 **SIGUSR1** 可重新加载配置，发送 **SIGUSR2** 可切换热键抓取。

# CONFIGURATION

**~/.config/sxhkd/sxhkdrc**
> 默认配置文件，定义热键绑定及其关联的命令。

# CAVEATS

sxhkd 只能在 X11 上工作，不支持 Wayland。keysym 名称可通过 **xev** 查询。某些按键组合可能与窗口管理器或其他抓取相同按键的应用冲突。

# HISTORY

**sxhkd** 由 **Bastien Dejean**（baskerville）创建，他也是 **bspwm** 的开发者。它于 **2013 年**前后首次发布，是一个可与任意窗口管理器配合的独立热键守护进程，满足了人们对独立于窗口管理器的简单、可脚本化按键绑定系统的需求。

# INSTALL

```apt: sudo apt install sxhkd```

```dnf: sudo dnf install sxhkd```

```pacman: sudo pacman -S sxhkd```

```apk: sudo apk add sxhkd```

```zypper: sudo zypper install sxhkd```

```nix: nix profile install nixpkgs#sxhkd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xev](/man/xev)(1), [xdotool](/man/xdotool)(1), [bspwm](/man/bspwm)(1), [xbindkeys](/man/xbindkeys)(1)
