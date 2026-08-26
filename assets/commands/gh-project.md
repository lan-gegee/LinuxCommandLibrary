# TAGLINE

管理 GitHub 项目看板和工作项

# TLDR

**列出项目**

```gh project list```

**查看项目**

```gh project view [number]```

**创建项目**

```gh project create --title "[title]"```

**向项目添加条目**

```gh project item-add [number] --url [issue_url]```

**删除项目**

```gh project delete [number]```

# SYNOPSIS

**gh** **project** _command_ [_options_]

# SUBCOMMANDS

**list**
> 列出项目。

**view**
> 查看项目。

**create**
> 创建项目。

**copy**
> 复制项目。

**edit**
> 编辑项目设置。

**close**
> 关闭项目。

**delete**
> 删除项目。

**link** / **unlink**
> 将仓库或团队与项目关联或解除关联。

**mark-template**
> 将项目标记为模板。

**item-add**
> 将现有的 issue 或 PR 添加到项目。

**item-create**
> 在项目中创建草稿条目。

**item-edit**
> 编辑条目的字段值。

**item-archive**
> 归档条目。

**item-delete**
> 移除条目。

**item-list**
> 列出项目条目。

**field-create** / **field-list** / **field-delete**
> 管理项目上的自定义字段。

# PARAMETERS

**--owner** _owner_
> 项目所有者（用户或组织）。

**--title** _title_
> 项目标题。

**--url** _url_
> 要添加的 issue 或 PR URL。

**--format** _format_
> 输出格式（例如 json）。

**-q**, **--jq** _expression_
> 使用 jq 表达式过滤 JSON 输出。

# DESCRIPTION

**gh project** 用于在命令行中管理 GitHub Projects（项目看板）。它借助可自定义的视图、字段和自动化能力来组织和跟踪工作。

项目可以包含 issue、拉取请求和草稿条目，并通过自定义列和过滤器组织成看板。该命令提供从创建到关闭的完整生命周期管理。

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

[gh](/man/gh)(1), [gh-issue](/man/gh-issue)(1), [gh-pr](/man/gh-pr)(1), [gh-repo](/man/gh-repo)(1)
