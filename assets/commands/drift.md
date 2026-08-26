# TAGLINE

面向向量搜索的 Spark 原生嵌入生命周期管理

# TLDR

**将表嵌入向量接收端**

```drift embed --table [catalog.table] --text-col [body] --model [openai/text-embedding-3-small] --sink [qdrant://localhost:6333/demo]```

**通过 Delta CDC 增量刷新变更行**

```drift watch --table [catalog.table] --text-col [body] --sink [qdrant://localhost:6333/demo]```

**将嵌入迁移到新模型**

```drift migrate --from [openai/text-embedding-ada-002] --to [openai/text-embedding-3-small] --sink [qdrant://localhost:6333/demo] --strategy [drift-adapter]```

**显示接收端状态**

```drift status --sink [qdrant://localhost:6333/demo]```

# SYNOPSIS

**drift** _subcommand_ [_options_]

# DESCRIPTION

**drift** 是 **drift-spark** 的 CLI，后者是一套 Spark 原生工具包，管理嵌入的完整生命周期：初次生成、增量 CDC 刷新、模型迁移，以及成本或来源审计。它取代了过去每晚重新嵌入整张表的手写脚本。

**embed** 子命令批量调用嵌入提供方处理文本，按内容哈希跨运行去重，并将幂等的 point ID 写入配置的接收端（Qdrant 或 pgvector）。**watch** 从源表读取 Delta Change Data Feed，只重新嵌入插入、更新或删除的行。**migrate** 使用完整的 **dual-write** 重建索引，或采用避免重建索引的 **drift-adapter** 正交旋转，把向量升级到新模型。**status** 报告接收端的当前状态。

位于 **~/.drift/ledger.db** 的本地 SQLite 台账记录每次运行的成本、去重统计以及每个向量的来源。**--shadow-mode** 使用确定性 mock 向量且不需要 API 密钥，便于开发和 CI 使用。

通过 **pip install drift-spark** 安装。可选扩展：**[qdrant]**、**[pgvector]**、**[spark]**。需要 Python **3.11+**。

# PARAMETERS

**embed**

**--table** _name_
> 源 Delta 或 Spark 表。

**--text-col** _column_
> 包含待嵌入文本的列。

**--model** _provider/model_
> 嵌入模型，例如 **openai/text-embedding-3-small**。

**--sink** _uri_
> 目标接收端 URI，例如 **qdrant://host:port/collection**。

**--shadow-mode**
> 使用确定性 mock 向量；不发起 API 调用。

**watch**

**--table**, **--text-col**, **--sink**, **--model**, **--since-version**, **--shadow-mode**
> 增量 CDC 刷新；**since-version** 默认取台账中的水位线。

**migrate**

**--from**, **--to**, **--sink**, **--strategy**
> 模型迁移；策略为 **dual-write** 或 **drift-adapter**。

# CAVEATS

**embed()** 通过 **toPandas()** 把文本收集到 Spark driver，实际可用规模约为 200 万行。pgvector 接收端目前支持写入，但尚不支持 CDC 删除和 migrate。工具内的 API 定价是硬编码的；做预算前请核实提供方的最新费率。**watch** 需要启用了 CDF 的 Delta Lake。

# HISTORY

**drift-spark** 由 aayush4vedi 创建，其 **drift-adapter** 迁移策略基于 Drift-Adapter 论文（arXiv:2509.23471, EMNLP 2025）。0.5.0 版本发布了 **embed**、**watch**、**migrate** 以及 SQLite 血缘台账。

# INSTALL

```nix: nix profile install nixpkgs#drift```

<!-- packages: 2026-07-22 -->

# SEE ALSO


# RESOURCES

```[Source code](https://github.com/aayush4vedi/drift-spark)```

```[Documentation](https://github.com/aayush4vedi/drift-spark/blob/main/README.md)```

<!-- verified: 2026-06-11 -->
