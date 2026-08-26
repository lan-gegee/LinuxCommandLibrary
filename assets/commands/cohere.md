# TAGLINE

Cohere AI 模型的终端聊天界面

# TLDR

**启动交互式聊天**会话

```cohere```

**切换到 Command A** 模型

```cohere``` 然后 ```:m a```

**执行网络搜索**查询

```:w [search query]```

**上传文件**进行分析

```:u [path/to/file.pdf]```

**显示当前模型**信息

```:i```

**切换调试模式**以查看 API 调用

```:d```

# SYNOPSIS

**cohere**

# INTERACTIVE COMMANDS

**:w** _query_
> 执行单轮带引用来源的网络搜索。

**:u** _file_
> 上传 PDF 或 TXT 文件进行分析（最大 20MB）。

**:m** _model_
> 在不同 AI 模型之间切换。别名：r+（Command R+）、a（Command A）。

**:i**
> 显示当前模型信息。

**:h**
> 显示所有可用命令。

**:c**
> 清屏但不丢失会话历史。

**:d**
> 切换调试模式，查看 API 请求和响应。

**:q**
> 退出程序。

# DESCRIPTION

**cohere** 是一个命令行界面，用于在终端中直接与 Cohere 的 AI 模型聊天。它提供交互式聊天体验，支持多轮对话并跨消息维护上下文。

该 CLI 支持 Cohere 的 Command 系列模型，包括 **Command R+** 和 **Command A**（其性能最强的模型，拥有 111B 参数和 256K 上下文长度）。用户可以在对话中途使用 **:m** 命令切换模型，可用 **r+**、**a** 等别名或完整模型名。

主要特性包括通过 Cohere connector 集成网络搜索，返回的结果附带规范的引用来源。文件上传功能支持分析最大 20MB 的 PDF 和 TXT 文档，PDF 使用 pdftotext 在本地预处理。

# CONFIGURATION

**~/.config/cohere-cli/config.env**
> API 密钥和 CLI 设置。

**~/.config/cohere-cli/chat-memory.json**
> 会话历史持久化存储。

# CAVEATS

需要安装 **curl**、**jq** 和 **gum**。处理 PDF 需要 poppler-utils 软件包中的 **pdftotext**。首次运行时需要配置有效的 Cohere API 密钥。该 CLI 是社区构建的工具，并非 Cohere 官方维护。

# HISTORY

cohere-cli 是一个社区项目，旨在为 Cohere 的 AI 模型提供终端访问能力。Cohere 由前 Google 研究员创立于 **2019 年**，专注于企业级 AI 和自然语言处理。其 Command 模型系列从 Command R 和 R+ 一路演进到 Command A——后者于 **2025 年 3 月**发布，具备更强的推理能力。

# SEE ALSO

[anthropic](/man/anthropic)(1), [ollama](/man/ollama)(1), [llm](/man/llm)(1)

# RESOURCES

```[Source code](https://github.com/plyght/cohere-cli)```

<!-- verified: 2026-06-22 -->
