# TAGLINE

轻量级 Wayland 通知守护进程

# TLDR

启动**通知守护进程**

```mako```

以**自定义配置文件**启动

```mako --config [path/to/config]```

设置通知的**最大可见数量**

```mako --max-visible=5```

设置以毫秒为单位的**默认超时时间**（0 表示禁用）

```mako --default-timeout=2000```

按应用名称对通知进行**分组**

```mako --group-by=app-name```

将通知锚定到某个**屏幕位置**

```mako --anchor=top-right```

# SYNOPSIS

**mako** [_options_]

# DESCRIPTION

**mako** 是一个面向 Wayland 合成器的轻量级通知守护进程，实现了 **org.freedesktop.Notifications** D-Bus 规范。它专为 **sway** 及其他基于 wlroots 的合成器设计。

配置文件中接受的任何选项也可以通过 **--key=value** 的形式在命令行上提供。运行中的守护进程可通过 **makoctl** 在运行时控制。

# PARAMETERS

**-c** _FILE_, **--config** _FILE_
> 使用指定的配置文件代替默认文件

**-h**, **--help**
> 显示帮助并退出

**--key=value**
> 任何配置文件风格的选项（例如 **--max-visible=5**、**--default-timeout=2000**、**--group-by=app-name**、**--sort=-time**、**--anchor=top-right**）。完整列表见 **mako(5)**。

# CAVEATS

仅支持 Wayland；需要支持 **wlr-layer-shell** 协议的合成器。配置文件位置为 **$XDG_CONFIG_HOME/mako/config**（通常是 **~/.config/mako/config**）。使用 **makoctl** 控制运行中的实例。配置键和匹配条件的完整列表见 **mako(5)**。

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

[makoctl](/man/makoctl)(1), [dunst](/man/dunst)(1)
