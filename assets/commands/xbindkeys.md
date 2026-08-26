# TAGLINE

在 X11 中将按键绑定到命令

# TLDR

**启动 xbindkeys**

```xbindkeys```

**生成默认配置文件**

```xbindkeys --defaults > ~/.xbindkeysrc```

**交互式识别按键代码**

```xbindkeys -k```

**识别多键组合**

```xbindkeys -mk```

**显示当前绑定**

```xbindkeys -s```

**重新加载配置**

```killall -HUP xbindkeys```

**使用指定的配置文件**

```xbindkeys -f [~/.config/xbindkeysrc]```

# SYNOPSIS

**xbindkeys** [_options_]

# PARAMETERS

**-d**, **--defaults**
> 将默认配置打印到 stdout。

**-f**, **--file** _file_
> 使用指定的配置文件。

**-k**, **--key**
> 识别一个按键（在窗口中按下该键）。

**-mk**, **--multikey**
> 识别多键组合。

**-s**, **--show**
> 显示当前的按键绑定。

**-n**, **--nodaemon**
> 不以守护进程方式运行。

**-v**, **--verbose**
> 详细模式。

**-h**, **--help**
> 显示帮助。

**-X**, **--display** _display_
> 设置要使用的 X display。

**-g**, **--geometry** _geometry_
> 设置按键识别窗口的大小和位置（与 -k 或 -mk 配合使用）。

**-dg**, **--defaults-guile**
> 将默认的 Guile 配置文件打印到 stdout。

**-fg**, **--file-guile** _file_
> 使用替代的 Guile 配置文件。

**-V**, **--version**
> 显示版本。

# CONFIGURATION

配置文件语法（~/.xbindkeysrc）：
```
"command"
    modifier + key

# Example: Volume up
"pactl set-sink-volume @DEFAULT_SINK@ +5%"
    XF86AudioRaiseVolume

# Example: Screenshot
"scrot"
    Print
```

# MODIFIERS

**Control**、**Shift**、**Mod1**（Alt）、**Mod2**（NumLock）、**Mod3**（CapsLock）、**Mod4**（Super/Win）、**Mod5**（Scroll Lock）、**Release**（在按键释放时触发）

# DESCRIPTION

**xbindkeys** 在 X11 中将按键或按键组合绑定到 shell 命令。它独立于窗口管理器工作，因此非常适合配置包括多媒体键在内的全局快捷键。

使用 `xbindkeys -k` 可以交互式地识别按键名称。在弹出的窗口中按下目标按键，即可看到它的名称和键码。

默认从 ~/.xbindkeysrc 读取配置。守护进程会监视配置文件，在其被修改时自动重新加载。发送 SIGHUP 可强制重载。

对于复杂的设置，xbindkeys 通过 ~/.xbindkeysrc.scm 支持 Guile Scheme 配置。

# CAVEATS

仅支持 X11；在 Wayland 下无法使用。某些按键可能已被其他应用程序抓取。按键名称可在 /usr/include/X11/keysymdef.h 中查找。多媒体键需要正确的内核/X 配置。

# HISTORY

**xbindkeys** 的创建目的是提供一种不依赖窗口管理器的按键绑定命令的方式。它填补了那些缺少内置快捷键配置功能的桌面环境和窗口管理器的空白。

# INSTALL

```apt: sudo apt install xbindkeys```

```dnf: sudo dnf install xbindkeys```

```pacman: sudo pacman -S xbindkeys```

```apk: sudo apk add xbindkeys```

```zypper: sudo zypper install xbindkeys```

```nix: nix profile install nixpkgs#xbindkeys```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xev](/man/xev)(1), [xmodmap](/man/xmodmap)(1), [sxhkd](/man/sxhkd)(1), [xdotool](/man/xdotool)(1)
