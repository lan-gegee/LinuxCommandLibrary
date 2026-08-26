# TAGLINE

显示拉取请求详情和元数据

# TLDR

**查看当前 PR**

```gh pr view```

**查看特定 PR**

```gh pr view [pr-number]```

**在浏览器中打开 PR**

```gh pr view --web```

**以 JSON 查看**

```gh pr view --json [title,body,state]```

**查看 PR 评论**

```gh pr view --comments```

# SYNOPSIS

**gh pr view** [_pr-number_] [_options_]

# PARAMETERS

_PR-NUMBER_
> 拉取请求编号（默认为当前分支）。

**--web**
> 在浏览器而非终端中打开。

**--comments**
> 显示 PR 评论。

**--json** _FIELDS_
> 以 JSON 输出指定字段。

**-q** _QUERY_, **--jq** _QUERY_
> 使用 jq 语法过滤 JSON 输出。

**-t**, **--template** _TEMPLATE_
> 使用 Go template 格式化输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gh pr view** 显示拉取请求的详细信息，包括标题、正文、状态、审查者、标签和合并状态。它会在终端中渲染 Markdown 内容。

未指定编号时，命令默认显示当前分支对应的拉取请求。JSON 输出便于脚本访问 PR 数据，还可配合 jq 过滤。

# CAVEATS

终端中的 Markdown 渲染有所简化。过大的 PR 可能被截断。JSON 字段随 PR 状态而异。

# HISTORY

gh pr view 属于 **GitHub CLI** 的拉取请求命令集，提供基于终端的 PR 查看，可作为网页界面的替代方案。

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

[gh-pr](/man/gh-pr)(1), [gh-pr-checks](/man/gh-pr-checks)(1), [gh-issue](/man/gh-issue)(1)
