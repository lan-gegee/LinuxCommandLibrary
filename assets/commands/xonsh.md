# TAGLINE

由 Python 驱动的跨平台 shell

# TLDR

**启动 xonsh**

```xonsh```

**运行命令**

```xonsh -c "[print('hello')]"```

**运行脚本**

```xonsh [script.xsh]```

**交互式 Python 模式**

```xonsh -i```

# SYNOPSIS

**xonsh** [_-c command_] [_-i_] [_options_] [_file_]

# PARAMETERS

**-c** _CMD_
> 执行命令。

**-i**
> 交互模式。

**--login**
> 登录 shell。

**--help**
> 显示帮助。

# DESCRIPTION

**xonsh** 是一个跨平台 shell，它将 Python 的能力与传统 Unix shell 的熟悉感结合在一起。它允许用户在同一个会话中无缝混用 Python 表达式和标准 shell 命令，以 Python 语法作为主要语言，同时支持传统的 shell 操作。

该 shell 提供上下文感知的制表符补全、语法高亮和可自定义的提示符。shell 命令原生运行，而 Python 代码可以在任何地方使用，用于变量操作、控制流和数据处理。脚本使用 **.xsh** 扩展名，可以同时包含 Python 和 shell 语法。

xonsh 可在任何有 Python 的平台上运行，对于希望将 Python 的表达力直接融入 shell 工作流的用户来说是一个可移植的选择。

# CAVEATS

需要 Python。与 bash 不同。有学习曲线。

# HISTORY

**xonsh** 的创建目的是将 Python 的强大功能与 shell 脚本的熟悉感结合起来。

# INSTALL

```dnf: sudo dnf install xonsh```

```pacman: sudo pacman -S xonsh```

```zypper: sudo zypper install xonsh```

```brew: brew install xonsh```

```nix: nix profile install nixpkgs#xonsh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bash](/man/bash)(1), [zsh](/man/zsh)(1), [python](/man/python)(1), [fish](/man/fish)(1)
