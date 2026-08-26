# TAGLINE

以 Markdown 文件为存储、用 SQLite 索引的智能体持久记忆

# TLDR

对当前工作区建立**索引**，为所有已更改的 Markdown 文件生成嵌入

```memweave index --workspace [.]```

**强制**对所有文件重新生成嵌入

```memweave index --workspace [.] --force```

**索引**单个新记忆文件

```memweave add [memory/2026-04-26.md] --workspace [.]```

使用关键词 + 向量混合查询**搜索**索引

```memweave search "[PostgreSQL JSONB]" --workspace [.]```

**限制**结果数量并要求最低分数

```memweave search "[caching layer]" --max-results [3] --min-score [0.3]```

**仅按关键词**搜索（不产生嵌入成本）

```memweave search "[Redis]" --strategy [keyword]```

**显示**机器可读的 JSON 输出

```memweave search "[topic]" --json```

**展示**索引统计信息

```memweave stats --workspace [.]```

**列出**所有被跟踪的文件

```memweave files --workspace [.]```

# SYNOPSIS

**memweave** _command_ [_options_] [_args_]

# PARAMETERS

**index**
> 遍历工作区，为所有 SHA-256 自上次运行以来发生变化的 Markdown 文件生成嵌入。

**add** _file_
> 立即索引单个 Markdown 文件。

**search** _query_
> 对索引执行混合（BM25 关键词 + 向量）搜索。

**files**
> 列出每个被跟踪文件及其来源标签和分块数。

**stats**
> 打印索引状态、搜索模式、缓存使用情况和过期警告的摘要。

**-w**, **--workspace** _PATH_
> 要操作的工作区目录（默认 **$PWD**）。

**--embedding-model** _NAME_
> 覆盖嵌入模型（例如 **text-embedding-3-small**）。

**--force**
> 跳过变更检测并重新处理所有文件。

**--max-results** _N_
> 返回的最大搜索命中数。

**--min-score** _F_
> 丢弃低于相关性分数下限的结果。

**--source-filter** _NAME_
> 将结果限制到带标签的来源（例如 **sessions**）。

**--strategy** _NAME_
> 搜索策略：**hybrid**（默认）、**keyword** 或 **semantic**。

**--mmr-lambda** _F_
> 最大边际相关性（MMR）在相关性与多样性之间的权衡系数。

**--decay-half-life-days** _N_
> 应用时间衰减，使较旧的笔记随时间推移排名降低。

**--json**
> 输出适合管道传给其他工具的 JSON。

# DESCRIPTION

**memweave** 是一个 Python 库和 CLI 工具，为 AI 智能体提供可持久化、可检索的记忆，其主存储格式是纯 Markdown。每个记忆文件都会被哈希、分块并嵌入到一个本地 **SQLite** 数据库中，该数据库将 **FTS5** 关键词排序与 **sqlite-vec** 向量搜索相结合，因此检索可以完全离线进行，并在同一份排序列表中融合关键词与语义两种信号。

每个子命令都直接对应底层 **MemWeave** Python 类的一个方法，这使得 memweave 很容易与 shell 管道、编辑器钩子和 CI 任务组合使用，而无需编写 Python。嵌入结果按内容哈希缓存，因此在大多数文件未变时重新运行 **memweave index** 的开销很小；**memweave search** 从不调用 LLM——只调用嵌入端点。

# CONFIGURATION

memweave 默认将数据库存放在工作区旁边。当前使用的嵌入模型可通过 **--embedding-model** 选择，或从所选提供商暴露的环境变量读取（OpenAI 嵌入对应 **OPENAI_API_KEY**）。若需要可选的文件监视集成，请附带 **watch** extra 安装：

```
pip install memweave[watch]
```

# CAVEATS

memweave 有意保持零基础设施——没有服务器组件、共享模型或访问控制层。混合索引假定输入为 Markdown；二进制文件会被忽略。由于嵌入按内容哈希缓存，切换嵌入模型需要 **--force** 来使之前的向量失效。存在多个名字相似但无关的项目；本页记录的是 **sachinsharma9780/memweave**。

# HISTORY

**memweave** 由 **Sachin Sharma**（**sachinsharma9780**）创建，以 **memweave** 之名发布在 **PyPI** 上，GitHub 地址为 **github.com/sachinsharma9780/memweave**。它被定位为向量数据库技术栈的轻量替代方案，适合已经以 Markdown 作为写作格式的智能体工作流。

# SEE ALSO

[sqlite3](/man/sqlite3)(1), [pip](/man/pip)(1), [grep](/man/grep)(1), [ripgrep](/man/ripgrep)(1)
