# TAGLINE

针对 RAG 向量索引的只读过期检查工具

# TLDR

对照文档清单审计 **pgvector** 表

```rag-staleness-check --engine pgvector --dsn [postgresql://user:pw@localhost:5432/db] --pg-table [chunks] --source [docs_manifest.json]```

审计 **Qdrant** 集合（需要 qdrant extra）

```rag-staleness-check --engine qdrant --dsn [http://localhost:6333] --collection [chunks] --source [docs_manifest.json]```

审计 **Chroma** 集合（需要 chroma extra）

```rag-staleness-check --engine chroma --dsn [localhost:8000] --collection [chunks] --source [docs_manifest.json]```

探测仍可被存储层或搜索检索到的**已删除 id**

```rag-staleness-check --engine pgvector --dsn [DSN] --pg-table [chunks] --deleted-ids [deleted_ids.json] --out [findings.json]```

在大型索引上限制**重复项**搜索范围

```rag-staleness-check --engine pgvector --dsn [DSN] --pg-table [chunks] --sample-size [1000] --min-similarity [0.98]```

# SYNOPSIS

**rag-staleness-check** **--engine** **pgvector**|**qdrant**|**chroma** **--dsn** _connection_ [_options_]

# PARAMETERS

**--engine** _pgvector_|_qdrant_|_chroma_
> 要审计的向量引擎（必填）

**--dsn** _string_
> 连接字符串，以只读方式打开。**pgvector**：Postgres DSN。**qdrant**：基础 URL。**chroma**：**host:port**

**--source** _file_
> 应当存在的文档的 JSON 清单（过期检查和孤儿检查必需）

**--out** _file_
> 将 JSON 评分卡写入此处（默认 **findings.json**）

**--deleted-ids** _file_
> 认为已被删除的块 id 的 JSON 数组；启用删除后仍可检索探测

**--min-similarity** _n_
> 近似重复检测的余弦相似度阈值（默认 **0.98**）

**--ann-k** _n_
> 重复检查中每个候选获取的最近邻数量（默认 **5**）

**--sample-size** _n_
> 限制余弦 ANN 重复扫描检查的候选数量

**--top-k** _a,b_
> 功能性泄漏探测使用的逗号分隔 top-k 截断值（默认 **5,10**）

**--months-threshold** _n_
> 同时报告早于该月数的可评估行数

**--share-anonymous-scorecard**
> 打印将被共享的匿名化评分卡。默认关闭；不会发起网络调用

**--pg-table** _name_
> 存放向量的表（使用 **--engine pgvector** 时必填）

**--pg-id-column** _name_
> 主键 / 点 id 列（默认 **id**）

**--pg-vector-column** _name_
> 向量列（默认 **embedding**）

**--pg-doc-id-column** _name_
> 存放源文档 id 的列

**--pg-last-modified-column** _name_
> 存放行最后修改时间戳的列

**--pg-content-hash-column** _name_
> 存放每行内容哈希的列

**--collection** _name_
> 集合名称（使用 **--engine qdrant** 或 **chroma** 时必填）

**--doc-id-field** _name_
> 存放源文档 id 的载荷/元数据字段（默认 **doc_id**）

**--last-modified-field** _name_
> 存放最后修改时间的载荷/元数据字段（默认 **last_modified**）

**--content-hash-field** _name_
> 存放每块内容哈希的载荷/元数据字段（默认 **content_sha256**）

**-h**, **--help**
> 显示帮助并退出

# DESCRIPTION

**rag-staleness-check** 是针对单个 **pgvector**、**Qdrant** 或 **Chroma** 向量索引的只读审计器。它将实际索引与文档清单（以及可选的已删除 id 列表）进行比对，并报告：

**staleness（过期）** — 索引中块的源文档 **last_modified** 比存储行更新的块

**orphans（孤儿）** — 其源文档已不在清单中的索引块

**duplicates（重复）** — 近乎相同的块（余弦相似度达到或超过 **--min-similarity**）；若配置了每块内容哈希列/字段，还会进行精确哈希扫描

**retrievable-after-delete（删除后仍可检索）** — 对于你认为已删除的 id，检查该向量是否仍能按 id 获取（存储层残留），以及是否仍出现在 top-k 搜索结果中（功能性泄漏）

每次运行都会将评分卡打印到标准输出，并将完整结果写入 **--out**。如果某项检查缺少必要输入（没有 **--source**、没有每行元数据映射、没有 **--deleted-ids**），该项检查会以 **skipped** 状态连同原因报告，而不是静默显示 0%。

该工具绝不会调用引擎的写入、删除或 upsert 方法。对于 pgvector，它还会以 **default_transaction_read_only = on** 打开会话，并在该设置未生效时拒绝继续。Qdrant 和 Chroma 没有等价的客户端只读断言；在这两个引擎上请使用仅具读取权限的 API 密钥。

默认安装方式为 **pip install rag-staleness-check**（仅支持 pgvector）。为支持其他引擎，请添加 extra：**[qdrant]**、**[chroma]** 或 **[all]**。要求 **Python 3.10+**。控制台脚本名为 **rag-staleness-check**。

# CAVEATS

这是单引擎、无台账的检查：它只报告发现的结果，不提供相对真值（ground truth）的精确率或召回率。

pgvector 必须提供 **--pg-table**；Qdrant 和 Chroma 必须提供 **--collection**。这些约束在运行时强制执行，而非通过 argparse 的 **required** 参数。

重复检测的精确哈希扫描需要存储每块的哈希值；否则只会退回到余弦 ANN。无法检索到向量的块不参与该扫描。

Qdrant 和 Chroma 客户端是可选 extra。缺少对应 extra 时连接这些引擎会因导入错误而失败。

默认不发送任何遥测数据。**--share-anonymous-scorecard** 只打印负载；不存在提交后端。连接 Chroma 会禁用 chromadb 自身的客户端遥测；某些 chromadb 版本可能仍会打印无害的 **capture()** 启动错误。

# HISTORY

**rag-staleness-check** 是 RAGproof "衰减 RAG 索引" 解析的开源自助部分。它用 Python 编写，采用 Apache-2.0 许可证，发布于 PyPI（软件包 **rag-staleness-check**，文档编写时版本为 0.1.1）。

# SEE ALSO

[psql](/man/psql)(1), [pip](/man/pip)(1), [pipx](/man/pipx)(1), [python](/man/python)(1)

# RESOURCES

```[Source code](https://github.com/rimironenko/rag-staleness-check)```

```[Documentation](https://github.com/rimironenko/rag-staleness-check#readme)```

<!-- verified: 2026-08-13 -->
