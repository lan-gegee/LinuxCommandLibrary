# TAGLINE

现代输入法框架

# TLDR

**启动 fcitx5** 输入法守护进程

```fcitx5```

**以守护进程模式启动**（后台）

```fcitx5 -d```

**以详细输出启动**以便调试

```fcitx5 -v```

**替换已有的 fcitx5 实例**

```fcitx5 -r```

**显示版本**信息

```fcitx5 --version```

# SYNOPSIS

**fcitx5** [**-drvh**] [**--replace**] [**--verbose**]

# PARAMETERS

**-d**, **--daemon**
> 作为后台守护进程运行。

**-r**, **--replace**
> 替换已有的 fcitx5 实例。

**-v**, **--verbose**
> 启用详细输出以调试。

**-h**, **--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# DESCRIPTION

**Fcitx5** 是一个面向类 Unix 系统的灵活输入法框架，主要用于输入中文、日文、韩文（CJK）以及其他需要复杂输入法的语言。它是 Fcitx 的后继者，采用模块化的插件式架构。

该框架提供一个轻量的核心，通过附加组件扩展语言支持。各种语言的输入法引擎可以单独安装（例如中文的 fcitx5-chinese-addons、日文的 fcitx5-anthy、韩文的 fcitx5-hangul）。

为正常运行，应在桌面会话中设置以下环境变量：

```
XMODIFIERS=@im=fcitx
GTK_IM_MODULE=fcitx
QT_IM_MODULE=fcitx
```

Fcitx5 同时支持 X11 和 Wayland，并提供原生 Wayland text-input 协议支持以实现更好的集成。

# CONFIGURATION

**~/.config/fcitx5/**
> 用户配置目录，包含 profile 设置、输入法配置和附加组件设置。

**~/.local/share/fcitx5/**
> 用户数据目录，存放主题、词典和自定义数据。

**/etc/xdg/fcitx5/**
> 系统级配置目录。

# CAVEATS

不同的桌面环境可能需要不同的自启动和环境变量配置方法。在 Wayland 上，优先使用原生 text-input 协议而非旧式输入法模块。某些应用可能需要 GTK 或 Qt IM 模块才能获得正常的输入法支持。

# HISTORY

Fcitx（Flexible Context Input X）最初为 Linux 上的中文输入而开发。**Fcitx5** 是一次彻底重写，基于 LGPL-2.1+ 发布，提供了改进的架构、更好的 Wayland 支持和更强的可扩展性。模块化设计允许将输入法、主题和功能作为独立插件添加。

# INSTALL

```apt: sudo apt install fcitx5```

```dnf: sudo dnf install fcitx5```

```pacman: sudo pacman -S fcitx5```

```apk: sudo apk add fcitx5```

```zypper: sudo zypper install fcitx5```

```nix: nix profile install nixpkgs#fcitx5```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ibus](/man/ibus)(1)
