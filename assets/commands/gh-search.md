# TAGLINE

在 GitHub 上搜索仓库、代码、issue 等

# TLDR

**搜索仓库**

```gh search repos [query]```

**搜索 issues**

```gh search issues [query]```

**搜索拉取请求**

```gh search prs [query]```

**搜索代码**

```gh search code [query]```

**搜索提交**

```gh search commits [query]```

**使用过滤器搜索**

```gh search repos [query] --language [python] --stars "[>100]"```

# SYNOPSIS

**gh** **search** _type_ _query_ [_options_]

# SUBCOMMANDS

**repos**
> 搜索仓库。

**issues**
> 搜索 issues。

**prs**
> 搜索拉取请求。

**code**
> 搜索代码。

**commits**
> 搜索提交。

# PARAMETERS

**--language** _lang_
> 按编程语言过滤（repos、code、issues、prs）。

**--stars** _range_
> 按 star 数量过滤（仅 repos；例如 `>100`）。

**--owner** _user_
> 按仓库所有者过滤。

**--repo** _owner/repo_
> 按仓库过滤（code、issues、prs、commits）。

**--topic** _topic_
> 按主题过滤（repos）。

**--license** _key_
> 按许可证类型过滤（repos）。

**--sort** _field_
> 对返回的结果排序（例如 stars、forks、updated）。

**--order** _asc|desc_
> 结果排序方向（配合 --sort 使用）。

**-L**, **--limit** _num_
> 结果数量上限（默认 30）。

**--json** _fields_
> 输出包含指定字段的 JSON。

**-w**, **--web**
> 在浏览器中打开搜索结果。

# DESCRIPTION

**gh search** 在命令行中提供 GitHub 强大的搜索能力，可覆盖仓库、代码、issue、拉取请求和提交。它支持 GitHub 完整的搜索语法，包括限定符、过滤器和布尔运算符。

仓库搜索可按语言、star 数、主题和其他元数据查找项目。代码搜索会为公开仓库的文件内容建立索引，便于查找示例实现。Issue 与 PR 搜索支持按状态、作者、标签和提及进行过滤。

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
