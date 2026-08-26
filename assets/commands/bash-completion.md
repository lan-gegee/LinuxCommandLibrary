# TAGLINE

Bash 命令的可编程 Tab 补全。

# TLDR

在当前会话中**加载 bash 补全**

```source /usr/share/bash-completion/bash_completion```

为命令**安装补全**（复制到系统目录）

```sudo cp [command_completion.bash] /usr/share/bash-completion/completions/[command]```

仅为当前用户**安装补全**

```cp [command_completion.bash] ~/.local/share/bash-completion/completions/[command]```

**列出已加载的补全**

```complete -p```

**移除一个补全**

```complete -r [command]```

为命令**创建简单补全**

```complete -W "[option1 option2 option3]" [command]```

# SYNOPSIS

**complete** [_options_] _command_

# PARAMETERS

**complete -p** [_command_]
> 打印命令当前的补全规格。

**complete -r** _command_
> 移除命令的补全规格。

**complete -W** _wordlist_ _command_
> 使用单词列表定义补全。

**complete -F** _function_ _command_
> 使用 Shell 函数进行补全。

**complete -C** _command_ _command_
> 使用某个命令的输出进行补全。

**complete -o** _option_ _command_
> 启用补全选项（filenames、dirnames、default 等）。

**compgen**
> 在补全函数中以编程方式生成候选。

# DESCRIPTION

**bash-completion** 是一组 Shell 函数集合，为 Bash 提供可编程的命令行补全。按下 Tab 时，它不仅补全文件名，还能补全命令选项、子命令、主机名以及其他与上下文相关的值。

其工作原理是定义补全规格，告诉 Bash 如何为特定命令生成候选项。规格可以使用单词列表、函数或外部命令来动态生成补全。

补全脚本存储在 **/usr/share/bash-completion/completions/**（旧系统上是 **/etc/bash_completion.d/**）。它们会在首次对某命令按 Tab 时按需加载，从而缩短 Shell 启动时间。

# CONFIGURATION

**/etc/bash_completion**
> 系统级 bash-completion 配置，在 Shell 启动时 source。

**/usr/share/bash-completion/completions/**
> 系统级逐命令补全脚本，按需加载。

**/etc/bash_completion.d/**
> 旧式系统级补全脚本目录，启动时立即全部加载。

**~/.local/share/bash-completion/completions/**
> 用户级逐命令补全脚本。

# CAVEATS

补全是 Bash 专用的，在其他 Shell 中无法使用（Zsh 有自己的体系）。必须安装 bash-completion 软件包并在 profile 中 source。对于补全逻辑复杂的命令，补全函数可能拖慢 Tab 补全速度。并非所有命令都有可用的补全脚本。

# HISTORY

Bash 可编程补全在版本 **2.04**（2000）中加入 Bash。为常用命令提供补全集合的 bash-completion 项目由 **Ian Macdonald** 于 **2000** 年前后发起，此后由多位贡献者维护。如今大多数 Linux 发行版和 macOS Homebrew 都默认包含它。

# INSTALL

```dnf: sudo dnf install bash-completion```

```pacman: sudo pacman -S bash-completion```

```zypper: sudo zypper install bash-completion```

```brew: brew install bash-completion```

```nix: nix profile install nixpkgs#bash-completion```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[bash](/man/bash)(1)
