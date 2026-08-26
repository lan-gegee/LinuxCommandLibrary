# TAGLINE

用于家庭管理与维护跟踪的终端 UI

# TLDR

使用你的房屋数据库**启动 micasa**

```micasa```

在演示模式中用示例数据**探索**

```micasa --demo```

**使用指定的数据库文件**

```micasa [path/to/house.db]```

将演示数据**持久化到文件**而非内存

```micasa --demo [path/to/demo.db]```

为脚本化操作**打印解析后的数据库路径**

```micasa --print-path```

# SYNOPSIS

**micasa** [**--demo**] [**--print-path**] [**--version**] [_db-path_]

# PARAMETERS

**--demo**
> 使用虚构的示例数据启动：房屋档案、项目、维护事项、家电、服务日志条目和报价。与 _db-path_ 同时使用时，演示数据会持久化到磁盘，而不是保存在内存中。

**--print-path**
> 将解析后的数据库路径输出到标准输出并退出。便于脚本化和备份。

**--version**
> 显示版本并退出。

**-h**, **--help**
> 显示帮助信息。

**_db-path_**
> 可选的位置参数，指定 SQLite 数据库文件的位置。

# DESCRIPTION

**micasa** 是一个以键盘驱动的终端 UI 应用，用于管理家中的一切事务。它跟踪维护计划、项目、事件记录、供应商报价、家电、保修、服务历史和文件附件。所有数据存储在一个本地 SQLite 文件中——无云端、无账户、无订阅。

该应用集成了 LLM 助手，连接本地 Ollama 实例或任何 OpenAI 兼容 API 时，可帮助生成维护建议和项目计划。

# CONFIGURATION

配置存储在特定平台的目录中：

```
Linux:   ~/.config/micasa/config.toml
macOS:   ~/Library/Application Support/micasa/config.toml
Windows: %APPDATA%\micasa\config.toml
```

**[llm]** 段控制可选的 LLM 集成：

**base_url**
> OpenAI 兼容的 API 端点（默认：**http://localhost:11434/v1**）

**model**
> 模型标识符（默认：**qwen3**）

**extra_context**
> 追加到所有系统提示词的自定义文本

**timeout**
> LLM 操作的最大等待时间（默认：**"5s"**）

环境变量可以覆盖配置值：

**MICASA_DB_PATH** — 未提供参数时设置默认数据库路径
**OLLAMA_HOST** — 覆盖 LLM API 基础 URL
**MICASA_LLM_MODEL** — 覆盖 LLM 模型名称
**MICASA_LLM_TIMEOUT** — 使用 Go 时长语法覆盖 LLM 超时

# CAVEATS

micasa 需要支持鼠标和键盘的终端。可选的 LLM 功能依赖于正在运行的 Ollama 实例或兼容的 API 端点。数据库是单个 SQLite 文件，不支持多个实例并发访问。

# HISTORY

**micasa**（西班牙语"我的家"）由 **Phillip Cloud**（cpcloud）创建，是托管在 GitHub 上的开源 Go 项目。它被设计为基于云的家庭管理应用的隐私优先替代方案，所有数据都保存在单个 SQLite 数据库中。其 TUI 设计受 VisiData 启发。

# INSTALL

```brew: brew install micasa```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sqlite3](/man/sqlite3)(1), [ollama](/man/ollama)(1)
