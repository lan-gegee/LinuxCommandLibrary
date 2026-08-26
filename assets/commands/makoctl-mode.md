# TAGLINE

管理 mako 通知守护进程中的通知模式

# TLDR

打印 **当前激活的** mako 模式

```makoctl mode```

**启用**一个模式（如 do-not-disturb）

```makoctl mode -a [do-not-disturb]```

**禁用**一个模式

```makoctl mode -r [do-not-disturb]```

**切换**一个模式的开关状态

```makoctl mode -t [do-not-disturb]```

用一个明确的**列表**替换整个模式集合

```makoctl mode -s [mode1] [mode2]```

# SYNOPSIS

**makoctl mode** [_options_] [_mode_...]

# PARAMETERS

**-a _mode_**
> 向激活集合中添加一个模式

**-r _mode_**
> 从激活集合中移除一个模式

**-t _mode_**
> 切换一个模式（未激活则添加，已激活则移除）

**-s _modes_**
> 设置确切的激活模式列表，替换所有当前模式

# DESCRIPTION

**makoctl mode** 管理 mako 通知守护进程中的通知模式。模式允许根据上下文改变通知行为——例如启用 "do-not-disturb"（勿扰）模式，在演示或专注工作时静默通知。

模式在 mako 的配置文件中定义，带有特定的匹配条件和动作。当某个模式处于激活状态时，匹配该模式条件的通知会得到不同的处理（隐藏、分组、采用不同样式等）。

多个模式可以同时激活，它们的效果按照 mako 的配置规则组合生效。

# CAVEATS

模式名必须先在 mako 的配置文件中定义才能使用。没有配置时模式不会产生任何效果。更改立即生效并持续存在，直到被显式移除或 mako 重启。

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

[makoctl](/man/makoctl)(1), [makoctl-invoke](/man/makoctl-invoke)(1), [mako](/man/mako)(5)
