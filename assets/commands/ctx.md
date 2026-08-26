# TAGLINE

跨编程代理会话历史的本地搜索工具

# TLDR

**为发现的全部本地代理会话建立索引**

```ctx setup```

**按关键词搜索历史会话**

```ctx search "failed migration"```

**搜索触及过某文件的会话**

```ctx search --file [path/to/file.rs]```

**显示匹配事件及其上下文**

```ctx show event [ctx-event-id] --window 3```

**显示紧凑的会话记录**

```ctx show session [ctx-session-id]```

# SYNOPSIS

**ctx** _command_ [_options_]

# PARAMETERS

**setup**
> 发现并导入本地代理历史到 SQLite 索引。

**search** _query_
> 跨已索引的会话和事件进行全文搜索。

**--file** _PATH_
> 将搜索范围限制为触及过指定文件的会话。

**--term** _TERM_
> 追加一个搜索词（可重复使用）。

**show event** _ID_
> 打印特定事件前后的记录上下文。

**show session** _ID_
> 打印紧凑的会话记录。

**sources**
> 列出本机上可导入的代理历史来源。

**sql** _QUERY_
> 对本地索引执行只读 SQL 查询。

**--json**
> 输出机器可读的 JSON。

# DESCRIPTION

**ctx** 是一个 Rust 编写的 CLI 工具，为本机上已有的编程代理会话日志建立索引，使其可以从 Shell 中检索。它从 Claude Code、Codex、Cursor、Pi、OpenCode、Antigravity、Factory AI Droid 和 Copilot CLI 导入历史，将会话与事件规范化后存入本地 SQLite 数据库。

编程代理往往每次都从零开始，无法恢复先前的决策、失败的命令或被否决的方案。**ctx** 让你（或当前运行的代理）在重复造轮子之前找回这些上下文。结果包含会话 ID、事件 ID、代码片段和引用的匹配项——比 grep 原始记录省得多得多的 token。

所有索引和搜索均在本地运行。任何提示词、记录或历史都不会发送到云端服务。

# CAVEATS

会话文本按本机存储的原样保留；分享到机器之外之前请先检查输出。源码构建和软件包管理器安装的版本不会自动升级——只有由安装器管理的二进制文件支持 **ctx upgrade**。

# INSTALL

```nix: nix profile install nixpkgs#ctx```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rg](/man/rg)(1), [jq](/man/jq)(1)

# RESOURCES

```[Source code](https://github.com/ctxrs/ctx)```

```[Homepage](https://ctx.rs)```

```[Documentation](https://ctx.rs/reference/cli)```

<!-- verified: 2026-07-03 -->
