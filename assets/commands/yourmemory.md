# TAGLINE

带遗忘曲线衰减机制的智能体 AI 记忆 MCP 服务器

# TLDR

**运行** stdio MCP 服务器（通常由 AI 客户端启动，而非人工）

```yourmemory```

**打印可执行文件路径**及可直接粘贴的 MCP 配置块

```yourmemory-path```

从 PyPI **安装** CLI

```pip install yourmemory```

通过环境变量标识拥有记忆命名空间的**智能体**

```YOURMEMORY_USER=[agent_name] yourmemory```

# SYNOPSIS

**yourmemory**

**yourmemory-path**

# PARAMETERS

**yourmemory**
> 启动 stdio Model Context Protocol 服务器。在 stdin 上读取 JSON-RPC 请求并在 stdout 上写出响应；设计为由兼容 MCP 的客户端启动。

**yourmemory-path**
> 打印 **yourmemory** 可执行文件的绝对路径，以及一段可直接粘贴到 MCP 客户端配置中的 JSON 配置片段。

**YOURMEMORY_USER** (环境变量)
> 标识拥有记忆命名空间的智能体。同一实例上的多个智能体可获得相互隔离的私有记忆以及共享上下文。

# DESCRIPTION

**yourmemory** 是一个 Model Context Protocol (MCP) 服务器，为 AI 编程智能体提供长期记忆，其衰减机制仿照 **艾宾浩斯遗忘曲线**。经常被回忆的记忆会得到增强，不被访问的记忆则随时间衰减，模拟人类的记忆保持规律。

该服务器向 MCP 客户端暴露三个工具：

**recall_memory(query)**
> 混合检索，结合向量相似度、BM25 关键词评分和图扩展，按相似度和强度排序。

**store_memory(content, importance, category?, visibility?)**
> 持久化一条新记忆并赋予重要性分数（0-1）。类别包括 **strategy**、**fact**、**assumption** 和 **failure**。可见性可为 **private** 或 **shared**。

**update_memory(id, new_content, importance)**
> 重新嵌入并替换现有的记忆条目。

它可以接入任何支持 MCP 的客户端（Claude Code、Cursor、Cline、Windsurf、Continue、Zed），并支持多个智能体共享一个实例且命名空间相互隔离。

# CONFIGURATION

大多数客户端使用一段 JSON 配置片段，将 **command** 指向 **yourmemory** 可执行文件：

```
{
  "mcpServers": {
    "yourmemory": {
      "command": "yourmemory",
      "env": { "YOURMEMORY_USER": "agent-1" }
    }
  }
}
```

运行 **yourmemory-path** 可获取客户端所需的绝对可执行路径（适用于启动时不解析 **PATH** 的客户端）。无需外部数据库或服务；存储在本地完成。

# CAVEATS

不是通用 Linux 命令——只有由 MCP 客户端启动时 **yourmemory** 才有意义。直接运行它会一直等待 stdin 上的 JSON-RPC 流量。由于存在衰减模型，未被强化的记忆最终会较少被呈现；应谨慎选择重要性和类别，以免丢失关键事实。安装需要 Python 3 和 **pip**。

# HISTORY

**YourMemory** 由 **sachitrafa** 于 **2025 年**发布，是一个开源 MCP 记忆服务器。它引用了在 **LoCoMo** 长上下文对话基准上的测试结果，声称召回率比 Mem0 高约 16 个百分点。该项目以 Python 编写并通过 PyPI 分发。

# SEE ALSO

[claude](/man/claude)(1), [pip](/man/pip)(1)
