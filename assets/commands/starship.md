# TAGLINE

用 Rust 编写的跨 Shell 可定制提示符

# TLDR

**为 bash 初始化**

```eval "$(starship init bash)"```

**为 zsh 初始化**

```eval "$(starship init zsh)"```

**为 fish 初始化**

```starship init fish | source```

**为 PowerShell 初始化**

```Invoke-Expression (&starship init powershell)```

**打印当前配置**

```starship print-config```

**生成预设配置**

```starship preset [pastel-powerline] > ~/.config/starship.toml```

**列出可用的预设**

```starship preset --list```

**解释当前提示符的各段内容**

```starship explain```

**显示提示符渲染耗时**

```starship timings```

# SYNOPSIS

**starship** [_init shell_] [_prompt_] [_preset_] [_options_]

# PARAMETERS

**init** _SHELL_
> 生成 shell 初始化脚本。

**prompt**
> 打印提示符。

**preset** _NAME_
> 打印预设配置。

**print-config**
> 打印配置。

**explain**
> 解释提示符各段的内容。

**timings**
> 测量提示符渲染耗时。

**completions** _SHELL_
> 生成补全脚本。

**bug-report**
> 生成错误报告。

**--help**
> 显示帮助。

**--version**
> 显示版本。

# DESCRIPTION

**starship** 是一个极简、快速的跨 Shell 提示符。它以 Rust 编写，在 bash、zsh、fish、PowerShell 等多种 Shell 中提供一致的外观和功能。

~/.config/starship.toml 中的配置用于定制模块。每个模块显示特定信息：git 状态、语言版本、云环境上下文等。

模块按上下文出现。Python 版本只在 Python 项目中显示。Git 信息只在仓库中显示。这使提示符保持简洁。

预设提供了现成的配置。它们从极简到信息丰富不等，并带有各种配色方案。

速度是优先考量。即使启用了许多模块，提示符也能快速渲染。timings 命令有助于找出缓慢的模块。

该提示符是跨平台的，可在 Linux、macOS 和 Windows 上运行。配置可以在不同系统间移植。

# CONFIGURATION

**~/.config/starship.toml**
> 主配置文件，定义启用的模块、显示格式、颜色以及各模块的设置。

**STARSHIP_CONFIG**
> 用于指定其他配置文件路径的环境变量。

# CAVEATS

图标需要 Nerd Font。配置语法可能与特定 Shell 提示符不同。某些模块需要外部命令。

# HISTORY

**Starship** 由 **Matan Kushner** 于 **2019 年**前后创建。作为 Oh My Zsh 主题等框架专属提示符的快速、可配置替代品，它逐渐流行起来。

# INSTALL

```apt: sudo apt install starship```

```pacman: sudo pacman -S starship```

```apk: sudo apk add starship```

```zypper: sudo zypper install starship```

```brew: brew install starship```

```nix: nix profile install nixpkgs#starship```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bash](/man/bash)(1), [zsh](/man/zsh)(1), [fish](/man/fish)(1), [powerline](/man/powerline)(1)
