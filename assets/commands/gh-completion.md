# TAGLINE

生成 shell 补全脚本

# TLDR

**生成 bash 补全**

```gh completion -s bash > ~/.local/share/bash-completion/completions/gh```

**生成 zsh 补全**

```gh completion -s zsh > "${fpath[1]}/_gh"```

**生成 fish 补全**

```gh completion -s fish > ~/.config/fish/completions/gh.fish```

**生成 PowerShell 补全**

```gh completion -s powershell | Out-String | Invoke-Expression```

# SYNOPSIS

**gh completion** **-s** _shell_

# PARAMETERS

**-s** _SHELL_, **--shell** _SHELL_
> Shell 类型：bash、zsh、fish、powershell。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gh completion** 为 GitHub CLI 生成 shell 补全脚本。这些脚本支持 gh 命令、子命令、标志以及仓库名称和分支等动态值的 Tab 补全。

补全脚本与各 shell 的原生补全系统集成，提供上下文感知的建议。动态补全会向 GitHub 查询仓库、issue 和 pull request。

gh 更新后应重新生成补全脚本，以纳入新命令。

# CAVEATS

输出必须保存到相应的 shell 补全目录。可能需要重启 shell 或重新 source 才能加载补全。动态补全需要认证。

# HISTORY

gh completion 内置于 **GitHub CLI**，遵循 Unix 通过补全脚本提供 shell 集成的惯例。

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

[gh](/man/gh)(1), [bash](/man/bash)(1), [zsh](/man/zsh)(1), [fish](/man/fish)(1)
