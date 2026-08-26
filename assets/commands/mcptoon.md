# TAGLINE

节省 token 的 Model Context Protocol (MCP) CLI 客户端

# TLDR

**在** **~/.mcptoon/config.json** 创建示例配置

```mcptoon init```

通过 stdio **添加** MCP 服务器

```mcptoon add [fetch] --stdio npx -y [@modelcontextprotocol/server-fetch]```

以紧凑的 TOON 形式**列出工具**

```mcptoon manifest --toon```

带 JSON 参数**调用工具**

```mcptoon call [fetch] [fetch] '{"url":"https://example.com"}' --toon```

通过 stdin **管道传入大型参数**

```echo '{"content":"..."}' | mcptoon call [server] [tool] --stdin --toon```

**诊断** Python、配置和服务器连通性

```mcptoon doctor```

**导出**工具清单用于 OpenAI function calling

```mcptoon manifest --format openai > [functions.json]```

# SYNOPSIS

**mcptoon** [_output-flags_] _command_ [_args_]

# DESCRIPTION

**mcptoon** 是一个零依赖的 Python CLI，它连接 MCP 服务器（stdio 或 HTTP），并以 **TOON** (Token-Optimized Object Notation) 或其他紧凑格式而非冗长的 JSON 返回工具列表和结果。通过 shell 调用 **mcptoon** 的智能体可以用远少于原始 MCP JSON 信封的上下文 token 来发现和调用工具。

用 **mcptoon add** 一次性配置服务器（保存在 **~/.mcptoon/config.json**，可选的项目级覆盖文件 **./.mcptoon.json**）。**manifest** 列出工具；**call** 调用工具；**discover** 和 **doctor** 检查健康状况。看起来危险的操作会被阻止，除非传入 **--destructive**。可选的工具投毒启发式检测会拒绝看似提示词注入的结果。

全局输出标志可选择 **--toon**、**--json**、**--compact**、**--raw**、截断（**--head**、**--max-chars**）以及导出格式（**--format** openai|openapi|mcp）。设置 **MCPTOON_AGENT_TYPE=claude** 后默认偏向 TOON。

# PARAMETERS

**init**

> 在 **~/.mcptoon/** 下写入示例配置。

**add** _name_ **--stdio** _cmd_ [_args_...] | **--http** _url_ [**--header** _H_]

> 注册 MCP 服务器。

**remove** _name_

> 移除已配置的服务器。

**list**

> 显示已配置的服务器及传输方式。

**manifest** [**--full**] [**--format** _fmt_]

> 列出工具（紧凑名称、完整 schema 或导出格式）。别名 **tools**。

**inspect** _server_ _tool_

> 显示某个工具的 schema。

**call** _server_ _tool_ [_json-args_] [**--stdin**] [**--destructive**]

> 调用工具。大型 JSON 负载请使用 **--stdin**。

**discover**

> 健康检查已配置的服务器。

**doctor**

> 自诊断运行时、配置和连通性。

**usage**

> **~/.cache/mcptoon/** 下的本地调用统计。

**completion** _bash|zsh|fish|ps_

> 打印 shell 补全脚本。

**--toon**, **--json**, **--compact**, **--raw**

> 输出渲染模式。

**--format** _openai|openapi|mcp|json|human_

> 清单导出风格。

**--head** _N_, **--max-chars** _N_, **--full**

> 截断或禁用默认大小上限。

# CONFIGURATION

**~/.mcptoon/config.json**

> 用户级服务器列表（stdio 命令或 HTTP 端点）。

**./.mcptoon.json**

> 可选的项目级覆盖配置。

**MCPTOON_AGENT_TYPE**

> 设为 **claude** 时，输出默认偏向 TOON。

# INSTALLATION

**pip**（Python 3.10+）：

```
pip install mcptoon
```

从仓库进行可编辑/开发安装：

```
pip install -e . --no-build-isolation
```

# CAVEATS

服务器必须已在运行或可以启动（例如通过 **npx**）。TOON 是面向智能体的紧凑交换格式；某些脚本场景仍需 **--json**。安全拦截和投毒检测可能误报；被拦截的写入/删除类工具需要 **--destructive** 才能执行。纯 Python 3.10+，无第三方依赖；通过 **pip install mcptoon** 安装。

# HISTORY

**mcptoon** 是 **activeing123** 于 2025–2026 年开发的 Apache-2.0 项目，旨在削减多智能体 shell 工作流中 MCP 工具发现和结果的开销。v0.2.x 新增了 **--stdin**、**doctor**、模糊"你是不是想找"、投毒防护以及跨智能体清单导出。

# SEE ALSO

[mcp-probe](/man/mcp-probe)(1), [claude](/man/claude)(1), [codex](/man/codex)(1)

# RESOURCES

```[Source code](https://github.com/activeing123/mcptoon)```

```[Homepage](https://pypi.org/project/mcptoon/)```

<!-- verified: 2026-08-11 -->
