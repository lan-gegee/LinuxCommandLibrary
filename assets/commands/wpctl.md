# TAGLINE

WirePlumber 音频控制工具

# TLDR

列出**对象**

```wpctl status```

**检查**对象

```wpctl inspect [id]```

设置**默认设备**

```wpctl set-default [id]```

**获取**音量

```wpctl get-volume [id]```

**设置**音量

```wpctl set-volume [id] [n]%```

**调整**音量

```wpctl set-volume [id] [n]%[+|-]```

带**上限**设置音量

```wpctl set-volume -l 1 [id] [n]%+```

切换**静音**

```wpctl set-mute [id] [1|0|toggle]```

# SYNOPSIS

**wpctl** _COMMAND_ [_OPTIONS_]

# COMMANDS

**status**
> 列出所有受管对象

**inspect** _ID_
> 打印对象属性

**set-default** _ID_
> 为某组设置默认项

**get-volume** _ID_
> 获取 sink 音量

**set-volume** _ID_ _LEVEL_
> 设置 sink 音量

**set-mute** _ID_ _STATE_
> 设置静音状态

# PARAMETERS

**-l, --limit** _MAX_
> 将音量限制在最大值以内

**@DEFAULT_SINK@**
> 表示默认 sink 的特殊名称

# DESCRIPTION

**wpctl** 管理 WirePlumber，即 PipeWire 的会话与策略管理器。它控制音频路由、音量和设备选择。

可以使用特殊名称 @DEFAULT_SINK@ 代替数字 ID 来操作当前默认的 sink。

# CAVEATS

需要 WirePlumber 正在运行。对象 ID 在不同会话之间可能变化。若不加限制，音量百分比可能超过 100%。

# INSTALL

```apt: sudo apt install wireplumber```

```dnf: sudo dnf install wireplumber```

```pacman: sudo pacman -S wireplumber```

```apk: sudo apk add wireplumber```

```zypper: sudo zypper install wireplumber```

```brew: brew install wireplumber```

```nix: nix profile install nixpkgs#wireplumber```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wireplumber](/man/wireplumber)(1), [pw-cli](/man/pw-cli)(1), [pactl](/man/pactl)(1)
