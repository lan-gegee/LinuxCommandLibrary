# TAGLINE

高度可配置的 X11 窗口管理器

# TLDR

**启动 FVWM**

```fvwm```

**以指定配置启动**

```fvwm -f [~/.fvwm/config]```

**替换正在运行的窗口管理器**

```fvwm --replace```

**显示版本**

```fvwm --version```

# SYNOPSIS

**fvwm** [_options_]

# PARAMETERS

**-f** _file_
> 配置文件。

**-c** _command_
> 启动时执行命令。

**-d** _display_
> 要使用的 X display。

**--replace**
> 替换正在运行的窗口管理器。

**-s**
> 单屏幕模式。

**-v**, **--version**
> 显示版本。

# DESCRIPTION

**FVWM**（F Virtual Window Manager）是 X11 上高度可配置的窗口管理器。它提供虚拟桌面、丰富的主题定制和强大的配置语言。

FVWM 以灵活性和低资源占用著称。配置通过文本文件完成，其中包含窗口装饰、菜单、按键绑定和模块加载等命令。

# CONFIGURATION

**~/.fvwm/config**
> 主配置文件，定义窗口样式、按键绑定、菜单和模块。

# CONFIGURATION EXAMPLE

```
# ~/.fvwm/config
Style * BorderWidth 5
Style * HandleWidth 5
Style * MWMButtons

Key Tab A M WindowList Root c c

Mouse 1 R A Menu MainMenu
Mouse 3 R A WindowList

AddToMenu MainMenu "Main" Title
+ "Terminal" Exec exec xterm
+ "Exit" Quit
```

# CAVEATS

配置有一定学习曲线。文档可能比较零散。FVWM3 是当前的主要版本。部分功能依赖外部模块。

# HISTORY

FVWM 由 **Robert Nation** 于 **1993 年**从 TWM 衍生而来。名字最初意为 "Feeble Virtual Window Manager"，但含义后来多次变更。FVWM2 是 1996 年的一次重大重写，FVWM3 则于 2020 年发布。

# INSTALL

```dnf: sudo dnf install fvwm```

```apk: sudo apk add fvwm```

```nix: nix profile install nixpkgs#fvwm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[openbox](/man/openbox)(1), [i3](/man/i3)(1), [twm](/man/twm)(1)
