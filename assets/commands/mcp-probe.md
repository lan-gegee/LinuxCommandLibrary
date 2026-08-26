# TAGLINE

交互式 MCP 协议调试器与测试 TUI

# TLDR

通过 stdio **调试 MCP 服务器**

```mcp-probe debug --stdio [command]```

通过 HTTP+SSE **调试**

```mcp-probe debug --http-sse [url]```

通过 Streamable HTTP **调试**

```mcp-probe debug --streamable-http [url]```

**运行合规性验证**

```mcp-probe validate --http-sse [url] --suite all```

# SYNOPSIS

**mcp-probe** _command_ [_options_]

# PARAMETERS

**debug**
> 为 MCP 服务器启动交互式 TUI 调试器。

**validate**
> 对 MCP 服务器运行自动化合规性测试。

**--stdio** _COMMAND_
> 通过 stdio 传输连接到 MCP 服务器。

**--http-sse** _URL_
> 通过 HTTP+SSE 传输连接到 MCP 服务器。

**--streamable-http** _URL_
> 通过 Streamable HTTP 传输连接到 MCP 服务器。

**--suite** _SUITE_
> 要运行的合规性测试套件（all、initialization、capabilities、security、performance）。

**--format** _FORMAT_
> 验证报告的输出格式（html、markdown、json、yaml）。

# DESCRIPTION

**mcp-probe** 是面向 Model Context Protocol (MCP) 服务器的交互式调试器和测试工具集。其 TUI 提供工具、资源和提示词的自动发现、高级模糊搜索以及多种视图模式来检查服务器响应。

它支持合规性测试，并可生成 HTML、Markdown、JSON 和 YAML 格式的报告，适合集成到 CI/CD 流水线中。

# CAVEATS

需要有正在运行的 MCP 服务器才能连接。传输方式支持情况取决于服务器的实现。

# HISTORY

**mcp-probe** 由 **conikeec** 创建，用 **Rust** 编写，基于 Ratatui 库。

# INSTALL

```aur: yay -S mcp-probe```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[claude](/man/claude)(1)
