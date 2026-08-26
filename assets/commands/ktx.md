# TAGLINE

面向数据与分析智能体的上下文层 CLI

# TLDR

**初始化或恢复本地 ktx 项目**

```ktx setup```

**检查项目就绪状态**

```ktx status```

**从已配置的数据源构建上下文**

```ktx ingest```

**搜索语义层指标**

```ktx sl "revenue"```

**搜索本地 wiki 页面**

```ktx wiki "refund policy"```

**为智能体客户端启动 MCP 服务器**

```ktx mcp start```

# SYNOPSIS

**ktx** _subcommand_ [_options_]

# DESCRIPTION

**ktx** 是 ktx 上下文层的命令行接口，这是一款教会 AI 智能体如何准确查询数据仓库的本地工具。它摄取仓库元数据、dbt 或 MetricFlow 定义、BI 工具导出内容和 wiki 页面，然后通过 CLI 和 MCP 工具暴露经过批准的指标、连接路径（join path）和业务知识。

**ktx setup** 创建或恢复项目目录，其中包含 **ktx.yaml**、**semantic-layer/** 目录树、**wiki/** 页面以及被 git 忽略的 **.ktx/** 状态目录。**ktx ingest** 从每个已配置的连接重建上下文。**ktx sl** 和 **ktx wiki** 分别搜索语义层和 wiki。**ktx mcp start** 启动 MCP 守护进程，供智能体客户端（Claude Code、Codex、Cursor、OpenCode）在查询时调用。

连接是只读的；ktx 从不写入数据仓库。支持的数据库包括 PostgreSQL、Snowflake、BigQuery、ClickHouse、MySQL、SQL Server 和 SQLite。LLM 后端包括 Anthropic API、Google Vertex AI、AI Gateway、Claude Code 会话以及本地 Codex 认证。

全局安装方式：**npm install -g @kaelio/ktx**。项目解析顺序依次为 **KTX_PROJECT_DIR**、最近的 **ktx.yaml**、当前目录。

# PARAMETERS

**--project-dir** _path_
> 为脚本化使用覆盖项目目录。

**ktx sl** _query_
> 对语义层实体进行全文和语义搜索。

**ktx wiki** _query_
> 搜索本地 wiki 页面。

**ktx mcp start**
> 启动本地 MCP 服务器；如有需要，请使用 **ktx status** 输出的路径。

# CONFIGURATION

Setup 完成后的项目布局：

```
my-project/
├── ktx.yaml
├── semantic-layer/<connection-id>/
├── wiki/global/
├── wiki/user/<user-id>/
├── raw-sources/<connection-id>/
└── .ktx/          # local state and secrets (git-ignored)
```

提交 **ktx.yaml**、**semantic-layer/** 和 **wiki/**；将 **.ktx/** 保留在本地。LLM 提供商和连接器的配置参见官方文档。

# CAVEATS

需要 SQL 数据仓库；ktx 构建在其之上而非取而代之。远程 LLM 调用发送的是本地构建的提示词，而不是原始仓库行数据。当 **ktx status** 提示需要 MCP 守护进程时，必须先启动它再打开智能体客户端。

# HISTORY

**ktx** 由 Kaelio (Y Combinator P25) 构建和维护。它将自动仓库内省、语义层摄取和 wiki 整合统一为一个面向智能体的上下文层。

# SEE ALSO

[dbt](/man/dbt)(1), [codex](/man/codex)(1)

# RESOURCES

```[Source code](https://github.com/Kaelio/ktx)```

```[Homepage](https://docs.kaelio.com/ktx)```

```[Documentation](https://docs.kaelio.com/ktx/docs/)```

<!-- verified: 2026-06-11 -->
