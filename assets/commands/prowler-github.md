# TAGLINE

GitHub 组织安全评估

# TLDR

**运行 GitHub 安全评估**

```prowler github```

**检查特定组织**

```prowler github --organization [org-name]```

**运行特定检查项**

```prowler github --checks [repository_secret_scanning]```

# SYNOPSIS

**prowler github** [_options_]

# PARAMETERS

**--organization** _name_
> GitHub 组织。

**--repository** _name_
> 特定仓库。

**--checks** _checks_
> 要运行的特定检查项。

**-M**, **--output-modes** _format_
> 输出格式。

**-o**, **--output-directory** _dir_
> 输出目录。

# DESCRIPTION

**prowler github** 对 GitHub 组织和仓库执行安全评估。它检查安全配置错误、缺失的保护措施以及最佳实践的符合情况。

# INSTALL

```brew: brew install prowler```

```nix: nix profile install nixpkgs#prowler```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[prowler](/man/prowler)(1), [gh](/man/gh)(1)
