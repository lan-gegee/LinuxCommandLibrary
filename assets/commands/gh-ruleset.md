# TAGLINE

管理 GitHub 仓库和组织规则集

# TLDR

**列出当前仓库中的规则集**

```gh ruleset list```

**列出规则集，包括从上级继承的部分**

```gh ruleset list --parents```

**按 ID 查看特定规则集**

```gh ruleset view [ruleset_id]```

**在网页浏览器中查看规则集**

```gh ruleset view [ruleset_id] --web```

**查看哪些规则适用于指定分支**

```gh ruleset check [branch]```

**列出组织级规则集**

```gh ruleset list --org [organization]```

# SYNOPSIS

**gh** **ruleset** _command_ [_flags_]

# SUBCOMMANDS

**check** [_branch_]
> 显示当前仓库中适用于指定分支的规则。

**list**
> 列出仓库或组织的规则集。

**view** [_ruleset-id_]
> 查看规则集的信息。不提供 ID 时以交互方式运行。

# PARAMETERS

**-R**, **--repo** _\[HOST/\]OWNER/REPO_
> 以 \[HOST/\]OWNER/REPO 格式选择其他仓库。

**-o**, **--org** _organization_
> 操作组织的规则集而非仓库的规则集。

**-p**, **--parents**
> 包含从上级组织继承的规则集（用于 list/view）。

**-L**, **--limit** _int_
> 最多列出的规则集数量（默认 30）。

**-w**, **--web**
> 在浏览器中打开规则集（用于 view）。

**-t**, **--default-branch**
> 检查仓库默认分支的规则（用于 check）。

# DESCRIPTION

**gh ruleset** 管理 GitHub 仓库和组织的规则集（ruleset）。规则集中定义了分支与标签保护规则、必需状态检查、必需审查、部署保护和合并要求。相比经典的分支保护规则，规则集的表达能力更强。

一个规则集可以使用 fnmatch 模式同时面向多个分支或标签，可以作用于组织内的所有仓库，还可以定义可绕过规则的角色。**check** 命令会评估当前有哪些规则适用于特定分支，有助于弄清推送或合并为何被拒绝。

CLI 不直接支持创建和编辑规则集；请使用 GitHub 网页 UI，或通过 **gh api** 调用 REST API。

# CAVEATS

需要通过 **gh auth login** 进行身份验证。查看组织规则集需要组织权限。除非使用 **--parents**，否则企业级或组织级定义的规则可能不会显示。

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

[gh](/man/gh)(1), [gh-api](/man/gh-api)(1), [gh-repo](/man/gh-repo)(1), [gh-auth](/man/gh-auth)(1)
