# TAGLINE

面向独立博客的嵌入优先搜索引擎管理 CLI

# TLDR

**同步**依赖并启动 Postgres

```uv sync```

```docker compose up -d db```

复制 env 文件并设置 **EMBEDDING_API_KEY**，然后初始化数据库模式

```cp .env.example .env```

```uv run semsearch init-db```

**添加**博客（feed 必需；sitemap 可选）

```uv run semsearch site add https://[example.blog]/ --sitemap auto --feed auto```

**列出**已配置的站点

```uv run semsearch site list```

**移除**站点

```uv run semsearch site remove https://[example.blog]/```

运行**摄取守护进程**（轮询、抓取、生成嵌入）

```uv run semsearch daemon```

显示**索引状态**和失败的任务

```uv run semsearch status```

# SYNOPSIS

**semsearch** _command_ [_options_]

# PARAMETERS

**init-db**
> 为配置的嵌入模型和维度创建数据库模式。就绪后会打印模型名称、向量大小以及脱敏后的 DSN。

**site add** _url_ [**--sitemap** auto|none|_url_] [**--feed** auto|_url_]
> 注册或更新基于 feed 的站点。实际上 **--feed** 是必需的（自动发现或显式 URL）。**--sitemap** 默认为 **auto**。

**site list**
> 列出已配置的站点。

**site remove** _url_
> 从索引配置中移除站点。

**daemon**
> 长期运行的进程，轮询 feed、抓取页面、切分文本、生成嵌入并写入 **pgvector**。使用咨询锁保证同一时间只有一个守护进程在运行。

**status**
> 报告索引统计信息并列出失败的摄取任务。

# DESCRIPTION

**semsearch** 是基于 Typer 的管理 CLI，服务于 **Semsearch**——一个面向聚合与推广独立博客的以嵌入为核心的索引与搜索引擎。该技术栈由 **FastAPI** Web 前端搭配 **PostgreSQL + pgvector** 存储组成。CLI 负责数据库模式初始化、站点注册、后台摄取和运行状态查询；HTTP 应用提供搜索服务（参见 **uvicorn semsearch.web.app:app**）。

配置来自环境变量 / **.env**（参见 **.env.example**）：数据库 URL、嵌入 API 端点与密钥、模型名称和嵌入维度。切分与嵌入设置由 CLI 和 Web 共享。更改切分算法、嵌入维度或模型都需要完整重建索引。

典型的本地布局：通过 **docker compose** 运行 Postgres，Python 工具通过 **uv run semsearch …** 执行。生产环境中则在应用容器内运行同一个二进制文件（**docker compose exec app … semsearch …**）。

# CAVEATS

项目状态为**迈向生产环境的概念验证**。需要较新的 Python（上游锁定 **>=3.14**）、一个运行中且带 **pgvector** 的 Postgres，以及在开始索引前可用的嵌入 API 密钥。添加站点时 feed URL 实际上是必需的。它不是通用的桌面搜索工具——而是这个特定博客搜索服务的运维 CLI。

# HISTORY

**Semsearch** 是一个小型开源项目，探索面向独立博客的智能体式 RAG 嵌入流水线，管理工具位于 **semsearch** 控制台脚本之下。

# SEE ALSO

[curl](/man/curl)(1), [docker](/man/docker)(1), [uv](/man/uv)(1)

# RESOURCES

```[Source code](https://github.com/yikerman/semantic-search)```

```[Homepage](https://github.com/yikerman/semantic-search)```

<!-- verified: 2026-08-04 -->
