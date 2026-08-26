# TAGLINE

配置 xscreensaver 偏好设置

# TLDR

**打开屏保设置**

```xscreensaver-settings```

**带调试输出打开设置**

```xscreensaver-settings --debug```

# SYNOPSIS

**xscreensaver-settings** [**--display** _host:display.screen_] [**--debug**]

# PARAMETERS

**--display** _host:display.screen_
> 设置窗口和受控 xscreensaver 守护进程共同使用的 X display

**--debug**
> 将诊断信息打印到 stderr

# DESCRIPTION

**xscreensaver-settings** 是 xscreensaver 的图形化配置工具。它允许启用/禁用单个屏保、设置空闲超时、锁屏选项和显示偏好。

界面有两个主要标签页：Display Modes 用于选择和预览屏保，Advanced 用于计时、锁定和电源管理设置。更改会保存到 ~/.xscreensaver。

关键设置包括屏幕变黑前的空闲超时、锁屏延迟、屏保之间的轮换时间，以及是让所有显示器一起变黑还是在每个显示器上运行不同屏保。

# SETTINGS

**Blank After**：屏幕变黑前的空闲时间。

**Cycle After**：切换屏保前的时间。

**Lock Screen After**：要求输入密码前的宽限时间。

**Power Management**：显示器节能选项。

**Mode**：Disable、Blank Only、One Random 或 Random。

# CAVEATS

更改保存在 ~/.xscreensaver 文件中。Wayland 下无法使用 GUI（请手动编辑文件）。需要 xscreensaver 守护进程处于运行状态。之前名为 xscreensaver-demo。

# HISTORY

**xscreensaver-settings**（原名 xscreensaver-demo）是 xscreensaver 的图形配置界面，由 Jamie Zawinski 于 1992 年创建。Xscreensaver 成为最流行的 X11 屏保，多年来开发了数百个显示模块。

# INSTALL

```apt: sudo apt install xscreensaver```

```dnf: sudo dnf install xscreensaver```

```pacman: sudo pacman -S xscreensaver```

```apk: sudo apk add xscreensaver```

```zypper: sudo zypper install xscreensaver```

```nix: nix profile install nixpkgs#xscreensaver```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xscreensaver](/man/xscreensaver)(1), [xscreensaver-command](/man/xscreensaver-command)(1)
