# TAGLINE

dunst 的运行时控制接口

# TLDR

**显示通知历史**

```dunstctl history-pop```

**关闭当前通知**

```dunstctl close```

**关闭所有通知**

```dunstctl close-all```

**切换勿扰模式**

```dunstctl set-paused toggle```

**检查是否已暂停**

```dunstctl is-paused```

**显示通知数量**

```dunstctl count```

**导出历史**为 JSON

```dunstctl history-export```

**清空通知历史**

```dunstctl history-clear```

**重载配置**

```dunstctl reload```

# SYNOPSIS

**dunstctl** _command_ [_args_]

# SUBCOMMANDS

**close**
> 关闭当前通知。

**close-all**
> 关闭所有通知。

**history-pop**
> 从历史中弹出一条通知显示。

**set-paused** _state_
> 设置暂停状态（true、false、toggle）。

**is-paused**
> 检查暂停状态。

**count** [_displayed_|_history_|_waiting_]
> 显示通知数量（不给参数时统计所有类别）。

**history-export**
> 将通知历史导出为 JSON。

**history-clear**
> 从历史中删除所有通知。

**reload**
> 重载配置。

**rule** _NAME_ _enable_|_disable_|_toggle_
> 启用、禁用或切换指定的具名规则。

**action** [_N_]
> 对位于第 N 位的通知执行默认动作（0 = 最上方）。

**get-pause-level**
> 获取当前暂停级别（0 = 未暂停，100 = 完全暂停）。

**set-pause-level** _LEVEL_
> 设置暂停级别（0-100），可与通知的 override_pause_level 组合使用。

**debug**
> 打印调试信息。

**context**
> 打开上下文菜单，列出当前打开通知的动作/URL。

# DESCRIPTION

**dunstctl** 是 dunst 通知守护进程的命令行控制接口。它提供运行时管理能力，无需修改配置文件或重启守护进程。

该工具允许以编程方式关闭通知、管理通知历史、切换暂停状态（勿扰模式）以及重载 dunst 的配置。它常被用在窗口管理器的按键绑定和脚本中进行通知管理。

主要特性包括历史导航（从历史中弹出最近的通知）、用于临时抑制通知的暂停状态管理，以及实时配置重载。close 命令可以针对特定通知，也可以一次性清除所有可见通知。暂停级别（0-100）可与每条通知的 override_pause_level 组合，在勿扰模式下实现有选择的显示。

# INSTALL

```apt: sudo apt install dunst```

```dnf: sudo dnf install dunst```

```pacman: sudo pacman -S dunst```

```apk: sudo apk add dunst```

```zypper: sudo zypper install dunst```

```nix: nix profile install nixpkgs#dunst```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dunst](/man/dunst)(1), [dunstify](/man/dunstify)(1), [notify-send](/man/notify-send)(1)
