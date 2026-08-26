# TAGLINE

面向 AI 智能体的本地优先 SQLite 记忆存储 CLI

# TLDR

通过 pip **安装**

```pip install remembrane```

将一条记忆**存入** SQLite 数据库

```remembrane --db [agent.db] store "[the user prefers dark mode]" --importance 0.8```

按查询**召回**匹配的记忆

```remembrane --db [agent.db] recall "[what theme?]"```

**列出**所有已存储的记忆

```remembrane --db [agent.db] list```

显示记忆数据库的**统计信息**

```remembrane --db [agent.db] stats```

将记忆**导出**为 JSON

```remembrane --db [agent.db] export > [backup.json]```

先对当前状态做**快照**，之后再对变更做 **diff**

```remembrane --db [agent.db] snapshot [v1]```

```remembrane --db [agent.db] diff [v1]```

# SYNOPSIS

**remembrane** [**--db** _path_] _subcommand_ [_options_] [_args_]

# DESCRIPTION

**remembrane** 是一个命令行界面，用于检查和管理以单个 SQLite 文件为后端的本地优先智能体记忆存储。同一软件包还提供 Python API、框架适配器（LangChain、CrewAI）以及可选的 MCP 服务器入口（**remembrane-mcp**）。

记忆可带可选的命名空间和重要性分数存储。**recall** 使用向量相似度与 BM25 关键词得分的混合方式对候选结果排序，并结合新近度衰减、重要性以及从任务结果反馈中学到的有用度。排序是精确的（对整个存储进行暴力遍历）而非近似最近邻；默认的嵌入器是基于纯标准库的哈希嵌入器，因此 **pip install remembrane** 无需额外依赖。

每次 store、forget 和 reinforce 操作都会记入日志，因此 **snapshot**、**diff** 和 **log** 可以对智能体已知的内容进行时间回溯。**conflicts** 会把相互矛盾的记忆呈现出来供裁定，而不是默默选择其一。**pack** 在 token 预算内选出最优（无 numpy 时为近似最优）的记忆集合。**merge** 可吸收另一个记忆数据库并对近重复项去重。

# PARAMETERS

**--db** _path_
> SQLite 记忆数据库的路径（默认：**remembrane.db**）。

**store** [_content_] [**--file** _path_|**-**] [**--namespace** _ns_] [**--importance** _f_]
> 存储一条记忆。内容可作为参数提供，或使用 **--file**（或用 **--file -** 表示 stdin）处理超出操作系统 argv 上限的大型负载。

**recall** _query_ [**--namespace** _ns_] [**-k** _n_] [**--mode** hybrid|vector|keyword] [**--explain**]
> 召回与 _query_ 最相关的记忆。**--explain** 会打印每个结果的排序明细。

**list** [**--namespace** _ns_]
> 列出已存储的记忆（可按命名空间过滤）。

**forget** _memory_id_
> 按 id 删除一条记忆。

**export** [**--namespace** _ns_]
> 将记忆导出为 JSON 并输出到 stdout。

**stats**
> 打印总体及各命名空间的记忆数量。

**snapshot** _label_
> 在日志中记录一个命名的时间点，供之后 **diff** 或重建使用。

**log** [**--namespace** _ns_] [**--limit** _n_]
> 按最新优先显示操作历史（默认限制 30 条）。

**diff** _a_ [_b_]
> 显示快照 _a_ 与快照 _b_ 之间的变化（省略 _b_ 时与当前状态比较）。

**conflicts** [_query_] [**--namespace** _ns_] [**--min-confidence** possible|likely]
> 呈现相互冲突的记忆（启发式冲突检测）。

**feedback** _memory_id_ **--useful**|**--useless**
> 记录任务结果反馈，用于调整有用度排序。

**pack** _query_ [**--budget** _tokens_] [**--namespace** _ns_]
> 在硬性 token 预算内选出适合上下文打包的记忆。

**merge** _source.db_ [**--dedupe-threshold** _f_]
> 将另一个记忆数据库合并进当前数据库。

# CAVEATS

CLI 会以调用用户权限写入 **--db** 指向的位置；它是本地工具，不是沙箱。默认嵌入器是词法层面的（n-gram 哈希），并非语义层面——要获得真正的语义召回需接入可选的嵌入器，且不要在同一数据库中混用不同嵌入器。冲突检测是启发式的：应把 **likely** / **possible** 的命中视为候选，由智能体或用户裁定。WAL 模式会在数据库文件旁边保留临时的 **-wal** / **-shm** 附属文件；请避免把记忆文件放在 NFS/SMB 上。若要通过 MCP 使用，请安装 **remembrane[mcp]** 并单独运行 **remembrane-mcp**。

# HISTORY

**remembrane** 是一个开源 Python 项目，用于不依赖向量数据库的本地智能体记忆。其在 PyPI 上的公开版本（0.4–0.5.x 系列）逐步完善了混合召回、冲突信号、有用度反馈和打包功能；软件包自带控制台脚本 **remembrane** 和 **remembrane-mcp**。

# SEE ALSO

[sqlite3](/man/sqlite3)(1), [pip](/man/pip)(1)

# RESOURCES

```[Source code](https://github.com/satyasairay/remembrane)```

```[Homepage](https://pypi.org/project/remembrane/)```

<!-- verified: 2026-08-07 -->
