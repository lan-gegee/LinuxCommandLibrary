# TAGLINE

查看 GitHub 仓库规则集（gh ruleset 的别名）

# TLDR

**列出当前仓库的规则集**

```gh rs list```

**列出其他仓库的规则集**，包括继承的规则集

```gh rs list --repo [owner/repo] --parents```

**列出组织范围**的规则集

```gh rs list --org [org-name]```

**按 ID 查看特定规则集**

```gh rs view [43]```

**在网页浏览器中打开规则集**

```gh rs view [43] --web```

**查看适用于当前分支的规则**

```gh rs check```

**查看适用于另一仓库默认分支的规则**

```gh rs check --default --repo [owner/repo]```

# SYNOPSIS

**gh rs** _command_ [_flags_]

# PARAMETERS

**list**
> 列出仓库或组织的规则集。

**view** [_ruleset-id_]
> 查看规则集的信息。未提供 ID 时以交互方式提示选择。

**check** [_branch_]
> 查看将应用于指定分支的规则。未指定分支时使用当前分支。

**-R**, **--repo** _[HOST/]OWNER/REPO_
> 选择其他仓库而非当前仓库。

# LIST FLAGS

**-L**, **--limit** _int_
> 最多列出的规则集数量（默认 30）。

**-o**, **--org** _string_
> 列出组织范围的规则集。需要 **admin:org** 令牌权限范围。

**-p**, **--parents**
> 包含在更高层级配置、且同样生效的规则集（默认 true）。

**-w**, **--web**
> 在网页浏览器中打开规则集列表。

# VIEW/CHECK FLAGS

**-o**, **--org** _string_
> 组织名称，当传给 **view** 的 ID 是组织级规则集时使用。

**--default**
> 配合 **check** 使用，查看仓库默认分支上的规则。

**-w**, **--web**
> 在网页浏览器中打开规则集或分支规则页面。

# DESCRIPTION

**gh rs** 是官方 **GitHub CLI** 中 **gh ruleset** 的内置别名。规则集让仓库和组织管理员能够在分支和标签上强制执行规则（必需审查、状态检查、分支命名、禁止强推等）。这组命令是只读的：它会列出并检查规则集，并显示哪些规则适用于给定分支，但不会创建或编辑规则集。

# CAVEATS

只读：规则集本身需要在 GitHub.com 网页上或通过 API 创建和编辑，不能通过 **gh ruleset** 完成。使用 **--org** 列出组织范围的规则集需要具有 **admin:org** 权限范围的令牌，可通过 **gh auth refresh -s admin:org** 获取。

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

[gh](/man/gh)(1), [gh-repo](/man/gh-repo)(1)

# RESOURCES

```[Manual](https://cli.github.com/manual/gh_ruleset)```

```[Source code](https://github.com/cli/cli)```

<!-- verified: 2026-07-17 -->
