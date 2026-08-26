# TAGLINE

AI 驱动的命令建议与解释工具

# TLDR

**向 Copilot 提问**

```gh copilot suggest "[how to find large files]"```

**解释一条命令**

```gh copilot explain "[git rebase -i HEAD~3]"```

**获取 shell 命令建议**

```gh copilot suggest -t shell "[task description]"```

**获取 gh CLI 建议**

```gh copilot suggest -t gh "[task description]"```

# SYNOPSIS

**gh** **copilot** _command_ [_options_]

# SUBCOMMANDS

**suggest**
> 获取命令建议。

**explain**
> 解释一条命令。

**config**
> 配置 Copilot。

# PARAMETERS

**-t**, **--target** _type_
> 目标类型（shell、gh、git）。

# DESCRIPTION

**gh copilot** 借助 GitHub Copilot 为命令行提供 AI 辅助。它通过自然语言交互帮助用户发现和理解命令。

suggest 子命令根据任务描述生成 shell、git 或 gh 命令，更容易找到正确的命令语法。explain 子命令把复杂命令拆解成易于理解的说明，帮助用户在执行前弄清命令的作用。

这一集成将 GitHub Copilot 的 AI 能力直接带入终端工作流，需要有效的 GitHub Copilot 订阅。

# CAVEATS

已弃用。**gh copilot** 扩展于 **2025 年 10 月**归档，被独立的智能体型 **GitHub Copilot CLI**（命令名为 **copilot**）取代。现有安装仍可使用，但新用户应改用替代品。

# INSTALL

```apt: sudo apt install gh```

```dnf: sudo dnf install gh```

```pacman: sudo pacman -S github-cli```

```apk: sudo apk add github-cli```

```zypper: sudo zypper install gh```

```brew: brew install gh```

```nix: nix profile install nixpkgs#gh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gh](/man/gh)(1), [gh-agent](/man/gh-agent)(1)

# RESOURCES

```[Source code](https://github.com/github/gh-copilot)```

```[Documentation](https://docs.github.com/copilot/github-copilot-in-the-cli)```

<!-- verified: 2026-07-15 -->
