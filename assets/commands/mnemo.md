# TAGLINE

本地优先的 AI 记忆层，附带知识图谱和 CLI

# TLDR

**存入**一段记忆以便日后检索

```mnemo ingest "I prefer Neovim with dark mode"```

**搜索**相关上下文并注入提示词

```mnemo search "what editor do I use?"```

**列出**提取出的实体

```mnemo entities```

**查看**单个实体及其图上的邻居

```mnemo entity <uuid> --neighbors```

**检查**服务器和数据库健康状况

```mnemo health```

**清空**所有已存储的记忆（需要确认）

```mnemo wipe --yes```

# SYNOPSIS

**mnemo** _subcommand_ [_arguments_] [_options_]

# DESCRIPTION

**mnemo** 是一个本地 AI 记忆服务的命令行客户端。它与 **mnemo-api** 通信（默认 `http://localhost:8080`），后者负责摄取文本、使用 OpenAI 兼容的 LLM 提取实体和关系、将其存入 SQLite，并维护一个基于内存的 **petgraph** 知识图谱以支持多跳检索。

典型工作流：先运行 **mnemo-api**（或在项目目录中 `docker compose up`），然后用 **mnemo ingest** 摄取对话或笔记，再调用 **mnemo search** 获取一个经过排序的 **context_prompt** 字符串，可注入到任何 LLM 应用中。后端支持 **Ollama**（完全本地）、OpenAI、Anthropic 或任何 OpenAI 兼容的 API。

服务端暴露 REST 端点（`/ingest`、`/retrieve`、`/entities`、`/chunks`、`/search`、`/stats`、`/wipe`）。CLI 是这些端点之上的一个薄封装，使用阻塞式 HTTP。

# PARAMETERS

**ingest** _text_
> 将文本 POST 到 `/ingest` 进行实体提取并存入图数据库。

**search** _query_
> 为自然语言查询检索排序后的记忆上下文。

**entities**
> 列出已存储的实体（由服务器分页）。

**entity** _uuid_ [**--neighbors**]
> 显示一个实体；可选遍历图上的邻居。

**chunks**
> 列出原始记忆块。

**health**
> 报告 API、数据库和 LLM 的连通性。

**stats**
> 打印实体、记忆块和图的数量以及运行时间。

**wipe** [**--yes**]
> 删除全部记忆；设置 **--yes** 时跳过确认提示。

**--server** _url_
> 使用非默认的 API 基础 URL（默认 `http://localhost:8080`）。

# CONFIGURATION

API 会读取环境变量（或通过 **--config** 读取 `mnemo.example.toml`）：

| Variable | Default | Purpose |
|----------|---------|---------|
| **MNEMO_DB_PATH** | `mnemo.db` | SQLite 数据库文件 |
| **MNEMO_PORT** | `8080` | API 监听端口 |
| **MNEMO_LLM_BASE_URL** | `http://localhost:11434/v1` | OpenAI 兼容的 LLM 端点 |
| **MNEMO_LLM_MODEL** | `llama3` | 用于提取的模型 |
| **MNEMO_LLM_API_KEY** | `ollama` | API 密钥（对 Ollama 而言任意值均可） |
| **MNEMO_LLM_PROVIDER** | `ollama` | `ollama`、`openai`、`anthropic` 或 `custom` |

环境变量优先于 TOML 配置值。

# CAVEATS

**mnemo** 要求 **mnemo-api** 正在运行。实体提取的质量取决于所配置的 LLM。**mnemo wipe** 不可逆。可在上游仓库中用 `cargo install --path crates/mnemo-cli` 安装此 CLI。

# INSTALL

```aur: yay -S mnemo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ollama](/man/ollama)(1), [curl](/man/curl)(1), [docker](/man/docker)(1)
