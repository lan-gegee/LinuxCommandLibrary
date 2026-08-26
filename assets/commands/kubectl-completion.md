# TAGLINE

生成 Shell 自动补全脚本

# TLDR

**生成 bash 补全**

```kubectl completion bash```

**生成 zsh 补全**

```kubectl completion zsh```

**在当前会话中启用**

```source <(kubectl completion bash)```

**添加到 bashrc**

```echo "source <(kubectl completion bash)" >> ~/.bashrc```

**添加到 zshrc**

```echo "source <(kubectl completion zsh)" >> ~/.zshrc```

# SYNOPSIS

**kubectl completion** _shell_

# PARAMETERS

_SHELL_
> Shell 类型（bash、zsh、fish、powershell）。

**bash**
> 生成 bash 补全。

**zsh**
> 生成 zsh 补全。

**fish**
> 生成 fish 补全。

**--help**
> 显示帮助信息。

# DESCRIPTION

**kubectl completion** 生成 Shell 自动补全脚本。它为 kubectl 命令启用 Tab 键补全功能。

该命令输出特定 Shell 的补全代码。将其 source 到 Shell 配置中即可获得持久化的补全功能。

# CAVEATS

kubectl 的子命令。bash 补全需要 bash-completion 软件包。补全与具体 Shell 相关。

# HISTORY

kubectl completion 为 **kubectl** 提供 Shell 集成，提升命令行使用效率。

# INSTALL

```apt: sudo apt install kubectl```

```pacman: sudo pacman -S kubectl```

```apk: sudo apk add kubectl```

```brew: brew install kubectl```

```nix: nix profile install nixpkgs#kubectl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [bash](/man/bash)(1), [zsh](/man/zsh)(1)
