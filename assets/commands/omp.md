# TAGLINE

面向终端的 AI 编程智能体（Oh My Pi）

# TLDR

**启动**智能体

```omp```

**安装**（Linux/macOS 脚本）

```curl -fsSL https://omp.sh/install | sh```

**生成 Shell 补全**（zsh）

```eval "$(omp completions zsh)"```

**生成 Shell 补全**（bash）

```eval "$(omp completions bash)"```

# SYNOPSIS

**omp** [*options*] [*prompt*|*subcommand*]

# DESCRIPTION

**omp** 是 **oh-my-pi** 的 CLI。oh-my-pi 是一个开放的 AI 编程智能体，专注于终端工作流：哈希锚定编辑、工具框架、LSP、浏览器工具、子智能体以及多提供商模型支持。可通过 **omp.sh**、Homebrew（**can1357/tap/omp**）或 **bun install -g @oh-my-pi/pi-coding-agent** 安装。

**omp completions** 基于实时的命令元数据输出适用于 bash、zsh 和 fish 的补全脚本，使补全内容始终与标志和模型保持一致。

# PARAMETERS

**omp**

> 启动交互式智能体会话（默认）。

**completions** *shell*

> 输出 **bash**、**zsh** 或 **fish** 的补全脚本。

其他子命令和标志（**--model**、会话恢复、规划模式等）迭代很快——请使用 **omp --help** 查看已安装版本的说明。

# CAVEATS

根据配置不同，需要 API 密钥或本地模型端点。智能体工具可以修改文件并运行 Shell 命令——请在受信任的目录中使用。其他无关工具也使用 "omp" 字母组合（例如某些提示符主题）；请确保 PATH 中的 omp 二进制是 oh-my-pi 的 **omp**。

# INSTALL

```aur: yay -S omp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gemini](/man/gemini)(1), [claude](/man/claude)(1), [aider](/man/aider)(1)

# RESOURCES

```[Source code](https://github.com/can1357/oh-my-pi)```

```[Homepage](https://omp.sh)```

<!-- verified: 2026-07-19 -->
