# TAGLINE

输入法框架

# TLDR

**启动 fcitx**

```fcitx```

**以守护进程模式启动**

```fcitx -d```

**重启 fcitx**

```fcitx -r```

**替换已有实例**

```fcitx --replace```

**显示版本**

```fcitx -v```

# SYNOPSIS

**fcitx** [_options_]

# PARAMETERS

**-d**, **--daemon**
> 以守护进程方式运行（后台）。

**-r**, **--replace**
> 替换已有实例。

**-D**, **--disable**
> 禁用加载指定附加组件。

**-s**, **--enable**
> 启用指定附加组件。

**-v**, **--version**
> 显示版本信息。

**--help**
> 显示帮助信息。

# DESCRIPTION

**fcitx**（Flexible Context-aware Input Tool with eXtension）是一个用于输入非拉丁字符的输入法框架。它通过各种输入法引擎支持中文、日文、韩文以及许多其他语言。

该框架采用模块化架构，提供针对拼音、五笔、韩文（Hangul）、Anthy 等不同输入法的附加组件。它通过 GTK 和 Qt 输入模块与桌面环境集成。

fcitx 处理输入法切换和候选词选择，并为文字输入提供可配置的用户界面。

# CONFIGURATION

**~/.config/fcitx/**
> 用户配置文件，涵盖输入法、快捷键和附加组件。

**/usr/share/fcitx/**
> 系统级的输入法数据和附加组件文件。

# CAVEATS

需要正确设置环境变量。可能与其他输入法框架冲突。桌面集成取决于工具包支持。

# HISTORY

fcitx 由 **Yuking** 于 2002 年创建，最初是 Linux 上的中文输入法。后来演变为通用输入法框架，**fcitx5** 是其现代重写版本，架构有所改进。

# INSTALL

```apt: sudo apt install fcitx-bin```

```dnf: sudo dnf install fcitx```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fcitx5](/man/fcitx5)(1), [ibus](/man/ibus)(1)
