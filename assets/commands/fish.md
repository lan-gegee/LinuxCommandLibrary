# TAGLINE

友好的交互式 Shell

# TLDR

**启动 fish shell**

```fish```

**执行命令**

```fish -c "[echo hello]"```

**运行脚本**

```fish [script.fish]```

**跳过配置启动**

```fish --no-config```

**检查语法**

```fish -n [script.fish]```

# SYNOPSIS

**fish** [_options_] [_file_] [_arguments_...]

# PARAMETERS

_FILE_
> 要执行的脚本文件。

**-c** _COMMAND_
> 执行命令后退出。

**-n**, **--no-execute**
> 只做语法检查。

**--no-config**
> 跳过配置文件的加载。

**-i**, **--interactive**
> 强制进入交互模式。

**-l**, **--login**
> 充当登录 Shell。

**-p**, **--profile** _FILE_
> 输出性能分析数据。

**--help**
> 显示帮助信息。

# CONFIGURATION

**~/.config/fish/config.fish**
> Shell 启动时加载的用户配置文件。

**~/.config/fish/fish_variables**
> 跨会话持久保存的通用变量（universal variables）。

**~/.config/fish/functions/*.fish**
> 用户自定义函数，每个文件存放一个函数。

# DESCRIPTION

**fish**（Friendly Interactive Shell）是一款智能、好用的 Shell，语法高亮、自动建议和 Tab 补全都开箱即用。

与 bash 或 zsh 不同，fish 不需要繁琐的配置就能发挥威力。它提供基于网页的配置界面、信息丰富的错误提示，以及容易被发现的功能设计。

fish 使用了一套更干净的脚本语法，与 POSIX Shell 并不相同——它把易用性置于兼容性之上。

# CAVEATS

不兼容 POSIX。脚本必须使用 fish 特有语法。部分命令与 bash/zsh 存在差异。

# HISTORY

fish 由 **Axel Liljencrantz** 于 2005 年创建，目的是解决 Shell 的易用性问题。它优先考虑交互体验和功能的可发现性，为了改善用户体验而接受与 POSIX 不兼容的代价。

# INSTALL

```apt: sudo apt install fish```

```dnf: sudo dnf install fish```

```pacman: sudo pacman -S fish```

```apk: sudo apk add fish```

```zypper: sudo zypper install fish```

```brew: brew install fish```

```nix: nix profile install nixpkgs#fish```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bash](/man/bash)(1), [zsh](/man/zsh)(1), [fisher](/man/fisher)(1)

# RESOURCES

```[Homepage](https://fishshell.com/)```

```[Source code](https://github.com/fish-shell/fish-shell)```

<!-- verified: 2026-07-15 -->
