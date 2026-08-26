# TAGLINE

防止把机密和凭据提交到 Git

# TLDR

**在仓库中安装钩子**

```git secrets --install```

**添加 AWS 模式**

```git secrets --register-aws```

**添加自定义模式**

```git secrets --add '[pattern]'```

**扫描仓库**

```git secrets --scan```

**扫描指定文件**

```git secrets --scan [file.txt]```

**列出模式**

```git secrets --list```

# SYNOPSIS

**git secrets** _command_ [_options_]

# PARAMETERS

**--install**
> 在当前仓库中安装钩子。

**--register-aws**
> 添加 AWS 机密模式。

**--add** _pattern_
> 添加禁止出现的模式。

**--add-allowed** _pattern_
> 添加允许的模式（例外情况）。

**--scan**
> 扫描仓库中的机密。

**--scan-history**
> 扫描整个提交历史。

**--list**
> 列出已注册的模式。

**--add-provider** _cmd_
> 添加机密提供方命令。

# DESCRIPTION

**git-secrets** 防止把机密和凭据提交到 Git 仓库。它会安装 pre-commit 钩子，按可配置的模式扫描暂存的改动，并阻止匹配已知机密格式的提交。

它由 AWS Labs 开发，内置了 AWS 凭据相关的模式，也支持为其他类型的机密添加自定义模式。

# CONFIGURATION

**~/.git-templates/git-secrets/**
> 全局 git 模板目录，用于在新仓库中自动安装钩子。

# CAVEATS

必须针对每个仓库安装，或通过模板安装。只能匹配特定模式，无法覆盖所有机密。历史扫描在大仓库上很慢。如需全面扫描可考虑 gitleaks 等工具。

# HISTORY

git-secrets 由 **AWS Labs** 创建，用于防止 AWS 凭据泄露。机密被意外提交到版本控制是一个普遍问题，它是解决这一问题的众多工具之一。

# INSTALL

```dnf: sudo dnf install git-secrets```

```brew: brew install git-secrets```

```nix: nix profile install nixpkgs#git-secrets```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [gitleaks](/man/gitleaks)(1), [trufflehog](/man/trufflehog)(1), [detect-secrets](/man/detect-secrets)(1)

# RESOURCES

```[Source code](https://github.com/awslabs/git-secrets)```

<!-- verified: 2026-07-17 -->
