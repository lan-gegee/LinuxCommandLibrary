# TAGLINE

从配置文件同步 GitHub 仓库标签

# TLDR

**将标签同步到仓库**

```github-label-sync --labels [labels.json] [owner/repo]```

**预览变更而不实际应用**

```github-label-sync --dry-run --labels [labels.json] [owner/repo]```

保留配置中未列出的标签而不删除它们

```github-label-sync --allow-added-labels --labels [labels.json] [owner/repo]```

**使用指定的访问令牌**

```github-label-sync --access-token [token] --labels [labels.json] [owner/repo]```

**使用托管在 URL 上的标签文件**

```github-label-sync --labels [https://example.com/labels.json] [owner/repo]```

# SYNOPSIS

**github-label-sync** [_options_] _owner/repo_

# PARAMETERS

**-l**, **--labels** _path-or-url_
> JSON 标签配置文件的路径或 URL。

**-d**, **--dry-run**
> 计算所需的变更但不实际应用。

**-a**, **--allow-added-labels**
> 不删除仓库上存在但配置中未列出的标签。

**-A**, **--access-token** _token_
> GitHub 个人访问令牌。若省略则回退到 `GITHUB_ACCESS_TOKEN` 环境变量。

# DESCRIPTION

**github-label-sync** 将 GitHub 标签与 JSON 配置文件同步。它通过声明式定义标签来保证各仓库间标签的一致性：添加缺失的标签、更新已更改的标签，并且（默认情况下）删除配置文件中不存在的标签。

标签文件是一个 JSON 数组，每个元素为一个标签对象，包含 `name`、`color`，以及可选的 `description` 和 `aliases`（用于重命名的旧名称，可保留现有的 issue/PR 关联）。

# SEE ALSO

[gh-label](/man/gh-label)(1)

# RESOURCES

```[Source code](https://github.com/Financial-Times/github-label-sync)```

<!-- verified: 2026-07-17 -->
