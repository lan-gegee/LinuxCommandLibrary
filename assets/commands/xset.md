# TAGLINE

配置 X server 偏好设置

# TLDR

**禁用**屏保

```xset s off```

**关闭**铃声

```xset b off```

设置屏保**超时**

```xset s 3600 3600```

**禁用** DPMS

```xset -dpms```

**启用** DPMS

```xset +dpms```

**查询**当前设置

```xset q```

设置**键盘重复速率**

```xset r rate 200 30```

设置 **LED** 状态

```xset led 3```

# SYNOPSIS

**xset** [_-display display_] [_options_]

# DESCRIPTION

**xset** 是 X 的用户偏好设置工具。它可以为 X server 设置各种用户偏好选项，包括键盘、鼠标、屏保和 DPMS（Energy Star）设置。

# PARAMETERS

**s [timeout [cycle]]**
> 以秒为单位设置屏保超时和轮换时间

**s on|off|default**
> 启用、禁用或重置屏保

**s blank|noblank**
> 将屏保设为变黑模式或图案模式

**s expose|noexpose**
> 允许/禁止屏幕暴露事件

**-dpms**
> 禁用 DPMS（Display Power Management Signaling）

**+dpms**
> 启用 DPMS

**dpms standby suspend off**
> 以秒为单位设置 DPMS 超时

**dpms force on|standby|suspend|off**
> 立即强制进入指定 DPMS 状态

**b [volume [pitch [duration]]]**
> 设置铃声参数

**b on|off**
> 启用或禁用铃声

**r [keycode] on|off**
> 启用或禁用按键自动重复

**r rate [delay [rate]]**
> 设置键盘重复延迟（毫秒）和速率（每秒次数）

**led [on|off]**
> 打开或关闭所有 LED

**led N**
> 打开第 N 个 LED

**-led N**
> 关闭第 N 个 LED

**fp= path,...**
> 设置字体路径

**fp default**
> 将字体路径重置为默认值

**q**
> 查询当前设置

**-display display**
> 指定 X display

# CAVEATS

设置是临时的，X 重启后会重置。若要持久化设置，可将 xset 命令加入 ~/.xprofile 或会话启动脚本。DPMS 设置可能被桌面环境的电源管理覆盖。

# HISTORY

**xset** 是 X.Org 核心工具集的一部分，为历史上通过 X 资源或窗口管理器配置设置的 X server 偏好提供命令行访问方式。

# INSTALL

```apt: sudo apt install x11-xserver-utils```

```dnf: sudo dnf install xset```

```apk: sudo apk add xset```

```zypper: sudo zypper install xset```

```nix: nix profile install nixpkgs#xset```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xrandr](/man/xrandr)(1), [setxkbmap](/man/setxkbmap)(1), [xmodmap](/man/xmodmap)(1)
