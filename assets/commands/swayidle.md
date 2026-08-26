# TAGLINE

Sway 的空闲管理守护进程

# TLDR

**空闲时锁定屏幕**

```swayidle timeout [300] 'swaylock -f'```

**关闭显示器**

```swayidle timeout [600] 'swaymsg "output * dpms off"' resume 'swaymsg "output * dpms on"'```

**睡眠前锁定**

```swayidle before-sleep 'swaylock -f'```

**多个超时事件**

```swayidle timeout [300] 'swaylock -f' timeout [600] 'systemctl suspend'```

**配合锁定事件**

```swayidle lock 'swaylock -f'```

# SYNOPSIS

**swayidle** [_options_] [_events_]

# PARAMETERS

**timeout** _SECONDS_ _COMMAND_
> 在空闲指定时间后运行。

**resume** _COMMAND_
> 在检测到活动时运行。

**before-sleep** _COMMAND_
> 在挂起前运行。

**after-resume** _COMMAND_
> 在唤醒后运行。

**lock** _COMMAND_
> 在锁定事件时运行。

**unlock** _COMMAND_
> 在解锁时运行。

**-w**
> 等待命令执行完毕后再继续

**-d**
> 启用调试输出

**-C** _path_
> 配置文件路径（默认：$XDG_CONFIG_HOME/swayidle/config）

**-S** _seat_
> 指定要使用的 seat 名称

# DESCRIPTION

**swayidle** 是一个空闲管理守护进程，兼容任何实现了 ext-idle-notify 协议的 Wayland 合成器。它根据用户的不活动状态触发命令，支持多个超时事件——在指定的空闲时间后执行相应命令——从而实现分阶段的电源管理，例如先调暗屏幕、再锁屏、最后挂起。

恢复动作在超时后检测到用户活动时执行，可以撤销超时的效果，比如重新点亮显示器。before-sleep 和 after-resume 事件与 systemd 的睡眠/唤醒周期集成，常用于确保系统挂起前屏幕已锁定。

锁定和解锁事件响应来自 logind 的会话锁定信号，可与来自系统设置或其他应用的外部锁定请求协同工作。

# CAVEATS

需要支持 ext-idle-notify 的 Wayland 合成器。命令通过 Shell 执行。在某些合成器上，音频播放可能会阻止空闲检测。

# HISTORY

**swayidle** 是 **Sway** 合成器的空闲管理器，负责处理电源管理和屏幕锁定触发。

# INSTALL

```apt: sudo apt install swayidle```

```dnf: sudo dnf install swayidle```

```pacman: sudo pacman -S swayidle```

```apk: sudo apk add swayidle```

```zypper: sudo zypper install swayidle```

```nix: nix profile install nixpkgs#swayidle```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sway](/man/sway)(1), [swaylock](/man/swaylock)(1), [swaymsg](/man/swaymsg)(1)
