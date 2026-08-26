# TAGLINE

面向 lazy Git 挂载的远程代码搜索 grep

# TLDR

在当前仓库中**搜索已提交内容**

```sgrep [pattern]```

在远程索引上**搜索特定仓库**

```sgrep --repo [owner/repo] [pattern]```

使用文件类型过滤器**列出匹配文件**

```sgrep -l --file '\.ts$' '[pattern]'```

只搜索本地已更改的文件

```sgrep --changed [file] '[pattern]'```

# SYNOPSIS

**sgrep** [_options_] _pattern_

# DESCRIPTION

**sgrep** 是一个远程代码搜索客户端，适用于 **git-lazy-mount** 工作树以及其他由云端搜索索引支撑的仓库。在 lazy 挂载上，普通的 **grep** 或 **rg** 会读取每个文件并将整个仓库实体化，使按需获取失去意义。**sgrep** 改为向搜索服务方发起查询，因此无需加载本地 blob 即可找到已提交的内容。

结果会自动与未提交的编辑叠加：已更改的文件在磁盘上搜索，过期的远程命中被丢弃，新增或修改的行会正确显示。默认情况下，该工具使用 **Sourcegraph** 作为服务方；当省略 **--repo** 时，会从 **origin** 远程推断仓库。

该二进制文件是自带 rustls TLS 的独立 Rust 程序，除网络连接外不依赖任何系统库。

# PARAMETERS

**--repo** _OWNER/REPO_
> 搜索指定仓库，而不是从 **origin** 推断。

**-l**
> 只打印包含匹配项的文件路径（files-with-matches 模式）。

**--file** _GLOB_
> 将结果限制在匹配文件 glob 的路径。

**-i**
> 不区分大小写搜索。

**--literal**
> 将模式视为字面字符串而非正则表达式。

**--count** _N_
> 最多请求 _N_ 条远程结果（默认 100）。

**--timeout-secs** _SECONDS_
> 查询超过时限时快速失败。

**--changed** _FILE_
> 只搜索指定的本地已更改文件。

**--no-cache**
> 绕过本地结果缓存，重新查询服务方。

# CONFIGURATION

**SRC_ENDPOINT**
> 服务方 API 端点（默认 `https://sourcegraph.com`）。

**SRC_ACCESS_TOKEN**
> 私有仓库的访问令牌；公共仓库可选。

**SGREP_PROVIDER**
> 当前使用的搜索后端（默认 `sourcegraph`，或用 `exec` 指定自定义命令）。

**SGREP_BROAD_TIMEOUT_SECS**
> 仅应用于不带 **--file** 的宽泛搜索的超时时间，对智能体工作流很有用。

**SGREP_CACHE_TTL_SECS**
> 远程结果的缓存有效期（默认 600 秒）。

# CAVEATS

**sgrep** 依赖网络访问所配置的搜索服务方，在 **git-lazy-mount** 树或本地 ripgrep 开销过大的超大仓库上最有价值。它通过索引加本地编辑来搜索已提交内容；并不能取代所有 **git grep** 使用场景。对于编码智能体，项目文档通常建议禁用内置 grep 工具，并在可能时通过 **sgrep** 配合 **--file** 过滤器进行搜索。

# HISTORY

**sgrep** 由 **Mohsen Azimi** 添加到 **git-lazy-mount** 项目中，作为 microVM 和智能体环境的配套工具——在这些环境中仓库以惰性方式挂载，全树搜索会慢得难以接受。

# INSTALL

```apt: sudo apt install sgrep```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-lazy-mount](/man/git-lazy-mount)(1), [git](/man/git)(1), [rg](/man/rg)(1), [grep](/man/grep)(1)

# RESOURCES

```[Source code](https://github.com/mohsen1/git-lazy-mount/tree/main/crates/sgrep)```

<!-- verified: 2026-06-30 -->
