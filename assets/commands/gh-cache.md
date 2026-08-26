# TAGLINE

管理 GitHub Actions 工作流缓存

# TLDR

**列出缓存**：当前仓库的所有缓存

```gh cache list```

**列出缓存**：按大小排序

```gh cache list --sort size_in_bytes --order desc```

**按键前缀筛选缓存**

```gh cache list --key [key_prefix]```

**删除单个缓存**（按 ID 或键）

```gh cache delete [cache_id_or_key]```

**删除特定 ref 的所有缓存**

```gh cache delete --all --ref refs/heads/[branch]```

**删除仓库中的所有缓存**

```gh cache delete --all```

# SYNOPSIS

**gh** **cache** _subcommand_ [_options_]

# SUBCOMMANDS

**list**
> 列出当前仓库的缓存。

**delete**
> 按 ID、键删除一个或多个缓存，或一次性全部删除。

# PARAMETERS

**-k**, **--key** _prefix_
> 按缓存键前缀筛选（list），或按键匹配（delete）。

**-L**, **--limit** _N_
> 获取缓存的最大数量（默认：30）。（仅限 list）

**-S**, **--sort** _field_
> 排序字段：created_at、last_accessed_at、size_in_bytes（默认：last_accessed_at）。（仅限 list）

**-O**, **--order** _direction_
> 结果排序方式：asc 或 desc（默认：desc）。（仅限 list）

**-r**, **--ref** _ref_
> 按 ref 筛选或删除，例如 refs/heads/main 或 refs/pull/123/merge。

**-a**, **--all**
> 删除所有缓存。可与 --ref 组合以限定范围。

**--succeed-on-no-caches**
> 未找到缓存时也返回退出码 0（与 --all 配合使用）。

**--json** _fields_
> 以 JSON 输出指定字段。（仅限 list）

**-q**, **--jq** _expression_
> 用 jq 表达式过滤 JSON 输出。（仅限 list）

**-t**, **--template** _format_
> 用 Go 模板格式化 JSON 输出。（仅限 list）

**-R**, **--repo** _owner/repo_
> 针对特定仓库操作。

# DESCRIPTION

**gh cache** 管理仓库的 GitHub Actions 缓存。缓存存放依赖项和构建产物，通过在多次运行之间复用数据来加快工作流执行速度。

缓存系统采用基于键的存储，工作流使用唯一键保存和恢复缓存数据。缓存条目有大小限制，并根据使用策略自动清理。手动管理缓存有助于排查工作流问题和回收存储空间。

`gh cache list` 也可以写作 `gh cache ls` 来调用。

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

[gh](/man/gh)(1), [gh-run](/man/gh-run)(1), [gh-secret](/man/gh-secret)(1)
