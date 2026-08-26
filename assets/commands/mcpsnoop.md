# TAGLINE

MCP 的 Wireshark —— 面向 AI 客户端/服务器流量的透明代理与实时 TUI

# TLDR

**包装服务器**以查看实时 MCP (Model Context Protocol) JSON-RPC 流量

```mcpsnoop -- node build/index.js```

**运行演示**

```mcpsnoop demo```

**代理 HTTP MCP 服务器**

```mcpsnoop http --target http://localhost:3000/mcp --listen :7000```

**启动 TUI**（与被包装的服务器自动配对）

```mcpsnoop```

# SYNOPSIS

**mcpsnoop** [--] [_server_ _args_...]

**mcpsnoop** http [--target _url_] [--listen _addr_]

**mcpsnoop** demo

**mcpsnoop** export|open|remote|help ...

# DESCRIPTION

mcpsnoop 是一个透明代理和交互式终端 UI，用于调试 AI 客户端（Claude Desktop、Cursor、Claude Code 等）与 MCP 服务器之间的流量。与作为独立客户端连接的官方 MCP Inspector 不同，mcpsnoop 位于实际数据路径中，因此能看到你的客户端发出的真实调用。

它在单个二进制文件中包含两个协作角色：

- shim（`mcpsnoop -- <服务器命令>`），由你的客户端启动。它逐字节转发数据，同时捕获每一个 JSON-RPC 帧。
- hub/TUI（无参数的 `mcpsnoop`），接收帧并提供实时、可过滤、可重放的界面。

两部分通过一个众所周知的套接字和磁盘上的日志自动发现彼此；启动顺序无关紧要。

# FEATURES

- 实时彩色编码的 JSON-RPC 流（请求、响应、通知、服务器 stderr）
- 挂起调用检测，带实时计时器
- 能力检查器
- 帧检查器，支持搜索
- 对任意捕获的工具调用进行重放，作用于新启动的服务器副本
- 强大的过滤查询语言（`tool:`、`status:`、`dir:` 等）
- 会话导出（json / html / text / otlp）
- 单个静态二进制文件，零运行时依赖

# INSTALL

```bash
go install github.com/kerlenton/mcpsnoop/cmd/mcpsnoop@latest
```

或通过 Homebrew：

```bash
brew install kerlenton/mcpsnoop/mcpsnoop
```

预编译的二进制文件可从 Releases 页面获取。

# PARAMETERS

**--**
> 结束标志处理；其后所有内容均为被包装的服务器命令及其参数。

HTTP 反向代理模式的选项：

**--target** _url_
> 目标 HTTP MCP 端点。

**--listen** _addr_
> 监听地址（例如 `:7000`）。

可选的项目配置可放在 `.mcpsnoop.toml`（仅限当前工作目录）：`label`、`trace-file`、`redact-secrets`、`redact-key`、`no-trace`。CLI 标志优先于该文件。

# CAVEATS

只包装你信任的服务器。mcpsnoop 会执行你配置的命令。捕获的帧可能包含提示词、凭据和工具结果 —— 必要时请使用脱敏标志。该工具处于 pre-1.0 阶段；行为可能在次版本中变化。

# RESOURCES

```[Source code](https://github.com/kerlenton/mcpsnoop)```

<!-- verified: 2026-07-11 -->
