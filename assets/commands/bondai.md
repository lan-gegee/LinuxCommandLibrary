# TAGLINE

带内置工具的 AI 智能体框架

# TLDR

使用 pip **安装**

```pip install bondai```

**启动交互式聊天会话**

```bondai```

**在 Docker 容器中运行 BondAI**（执行代码时推荐）

```docker run -it --rm -v ./agent-volume:/agent-volume -w /agent-volume -e OPENAI_API_KEY=[key] krohling/bondai:latest bondai```

运行前**设置所需的 API 密钥**

```export OPENAI_API_KEY=[sk-XXXXXXXXXX]```

# SYNOPSIS

**bondai** [_options_]

# DESCRIPTION

**BondAI** 是一个用于构建 AI 智能体系统的开源框架。其 CLI 提供交互式聊天界面，用户可以与 AI 智能体对话，该智能体可使用一整套强大的内置工具，涵盖搜索、文件操作、代码执行和外部集成。

智能体会处理复杂的实现细节，包括记忆与上下文管理、错误处理以及向量/语义搜索。它可以自主执行多步骤任务，根据需要调用工具来完成目标。

内置工具包括用于网络搜索的 **DuckDuckGoSearchTool** 和 **GoogleSearchTool**、用于查询网页内容的 **WebsiteQueryTool**、用于文件操作的 **FileWriteTool**、用于执行 Python 代码的 **PythonREPLTool**，以及用于访问 Shell 的 **ShellTool**。此外还支持 PostgreSQL 数据库、Gmail、用于交易的 Alpaca Markets 以及用于电话呼叫的 Bland AI 等集成。

# TOOLS

**DuckDuckGoSearchTool**
> 无需 API 密钥的网络搜索。

**GoogleSearchTool**
> 网络搜索（需要 Google API 密钥）。

**WebsiteQueryTool**
> 查询并提取网页内容。

**FileWriteTool**
> 创建和写入文件。

**PythonREPLTool**
> 执行 Python 代码（建议在 Docker 中使用）。

**ShellTool**
> 执行 Shell 命令（建议在 Docker 中使用）。

# CAVEATS

需要通过 OPENAI_API_KEY 环境变量设置 **OpenAI API 密钥**（或 Azure OpenAI 凭据）。执行任意代码的工具（**PythonREPLTool**）或访问你的 Shell 的工具（**ShellTool**）可能会损坏系统。强烈建议在使用这些工具时将 BondAI 运行在 **Docker 容器**中。可挂载卷以便在系统和智能体的工作目录之间共享文件。

# HISTORY

BondAI 由 **Kevin Rohling** 创建，并在 GitHub 上作为开源项目发布。它诞生于 **2023-2024 年**的 AI 智能体开发浪潮中，旨在通过处理记忆管理和工具集成等常见实现难题来简化自主 AI 系统的构建。该项目支持包括 OpenAI 和 Azure OpenAI 在内的多种 LLM 提供商。

# SEE ALSO

[python](/man/python)(1), [docker](/man/docker)(1), [claude](/man/claude)(1)

# RESOURCES

```[Source code](https://github.com/krohling/bondai)```

```[Homepage](https://bondai.dev)```

<!-- verified: 2026-06-19 -->
