# TAGLINE

控制控制台上的键盘 LED 指示灯

# TLDR

**点亮 NumLock LED**

```setleds +num```

**熄灭 CapsLock LED**

```setleds -caps```

**点亮 ScrollLock LED**

```setleds +scroll```

**将 NumLock 设为默认状态**（重置后仍保留）

```setleds -D +num```

**报告当前 LED 状态**

```setleds```

**仅更改 LED**而不影响按键状态

```setleds -L +num```

为**特定 TTY** 设置 LED

```setleds -D +num < /dev/tty1```

# SYNOPSIS

**setleds** [_-v_] [_-L_] [_-D_] [_-F_] [{_+|-_}**num**] [{_+|-_}**caps**] [{_+|-_}**scroll**]

# PARAMETERS

**+num** / **-num**
> 设置或清除 NumLock

**+caps** / **-caps**
> 设置或清除 CapsLock

**+scroll** / **-scroll**
> 设置或清除 ScrollLock

**-F**
> 仅更改 VT 标志（默认）；LED 可能会反映此更改

**-D**
> 更改标志和默认值；控制台重置后更改仍然保留

**-L**
> 仅更改 LED 而不影响 VT 标志

**-v**
> 详细模式；报告更改情况

# DESCRIPTION

**setleds** 控制 Linux 虚拟控制台上的键盘 LED 指示灯（NumLock、CapsLock、ScrollLock）。不带参数时，它报告当前的 LED 和标志设置。

该命令同时操作虚拟终端标志（影响键盘行为）和物理 LED 状态。使用 **-F** 仅更改 VT 行为，使用 **-L** 仅更改 LED，或使用 **-D** 设置持久的默认值。

它常用于 /etc/rc 脚本中，为控制台登录设置初始 NumLock 状态。

# CAVEATS

setleds 只影响虚拟控制台（TTY），不影响图形环境（X11/Wayland），后者由桌面环境管理键盘 LED。需要对目标终端设备的相应权限。属于 **kbd** 软件包的一部分。

# HISTORY

setleds 是 **kbd** 软件包的一部分，这是一组用于 Linux 控制台管理的键盘工具。它提供的对键盘指示灯的底层控制早于现代桌面环境。

# INSTALL

```apt: sudo apt install kbd```

```dnf: sudo dnf install kbd```

```pacman: sudo pacman -S kbd```

```apk: sudo apk add kbd```

```zypper: sudo zypper install kbd```

```nix: nix profile install nixpkgs#kbd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[showkey](/man/showkey)(1), [loadkeys](/man/loadkeys)(1), [dumpkeys](/man/dumpkeys)(1)
