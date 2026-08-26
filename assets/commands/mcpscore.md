# TAGLINE

审计 Model Context Protocol (MCP) 服务器并评分

# TLDR

**审计远程** MCP 服务器 URL

```mcpscore https://[example.com]/mcp```

**审计本地** Python 或 Node MCP 服务器（stdio）

```mcpscore [path/to/server.py]```

```mcpscore [path/to/server.js]```

通过任意 stdio 命令**审计任意语言**的服务器

```mcpscore --stdio ./[my-server]```

```mcpscore --stdio java -jar [server.jar]```

向 stdio 服务器传递**环境变量**（不带值的形式会从环境中复制密钥）

```API_KEY=... mcpscore --env API_KEY --stdio ./[my-server]```

输出供 CI 使用的 **JSON 报告**

```mcpscore https://[example.com]/mcp --json > report.json```

使用 bearer token 审计有**身份验证**保护的服务器

```mcpscore https://[example.com]/mcp --token [$MY_TOKEN]```

# SYNOPSIS

**mcpscore** [_target_] [**--stdio** _command_ ...] [**--env** _NAME_[=_VALUE_]] [**--json**] [**--token** _TOKEN_] [**--header** '_Name: Value_'] [**--oauth**] [**--client-id** _ID_] [**--callback-port** _PORT_] [**--version**]

# PARAMETERS

**_target_**
> 本地 MCP 服务器脚本（**.py**、**.js**）的路径或远程服务器的 **http(s)** URL。使用 **--stdio** 时省略。

**--stdio** _COMMAND_ ...
> 以任意 stdio 进程启动本地 MCP 服务器（任何语言）。它会消耗命令行的剩余部分，因此请把所有 mcpscore 选项放在它之前。取代位置参数 target。

**--env** _NAME_[=_VALUE_]
> 传给 **--stdio** 子进程的额外环境变量。可重复。**NAME=VALUE** 为内联设置；仅写 **NAME** 则从 mcpscore 自身的环境复制（涉及机密时建议用这种形式）。仅在配合 **--stdio** 时有效。

**--json**
> 将机器可读的报告写到 stdout（人类可读日志输出到 stderr）。

**--token** _TOKEN_
> 发送 **Authorization: Bearer** _TOKEN_。未设置时回退到 **MCPSCORE_TOKEN** 环境变量。

**--header** '_Name: Value_'
> 远程目标的额外 HTTP 头。可重复。值绝不会被记录或写入报告。

**--oauth**
> 交互式获取令牌（浏览器中的授权码 + PKCE）。需要 HTTP(S) 目标。与已有的 Authorization 凭据冲突。

**--client-id** _ID_
> 当授权服务器不支持动态客户端注册时，为 **--oauth** 提供预先注册的 OAuth 客户端 ID。

**--callback-port** _PORT_
> **--oauth** 重定向 URI 使用的固定回环端口（1–65535）。

**--version**
> 打印已安装的 mcpscore 版本并退出。

# DESCRIPTION

**mcpscore** 审计任意 Model Context Protocol (MCP) 服务器并产出按严重度加权的质量分数。它以真实的 **initialize** 握手建立连接，然后评估协议符合性、工具/提示词/资源目录质量、安全与认证态势以及对下一版 MCP 规范的就绪程度。评分过程是确定性的，无需 API 密钥。

传输方式：本地服务器走 **stdio**（直接 **.py**/**.js** 路径，其他语言用 **--stdio**），远程服务器走 Streamable HTTP 或 SSE（自动检测）。有认证保护的 HTTP 服务器可以在没有凭据的情况下部分评分（TLS、质询、受保护资源元数据），也可以通过 **--token**、**--header**、**MCPSCORE_TOKEN** 或 **--oauth** 完整评分。

退出码（CLI 契约）：**0** 成功，**1** 用法错误，**2** 连接失败（目标不是可用的 MCP 端点）。

# CAVEATS

需要 **Python 3.11+**。本地审计要求服务器运行时位于 **PATH** 中（**.py** 需要 Python，**.js** 需要 Node，或由 **--stdio** 调用的任何内容）。使用 **--stdio** 时切勿在命令行上传递机密 —— 它们会出现在进程列表中并成为报告的目标；应先导出变量再使用 **--env NAME**。仅认证部分的得分与完整审计不可比。

# HISTORY

**mcpscore** 由 **mcp-box**（作者 Alex Akimov）以 MIT 许可证开发。它以 **mcpscore** 名称发布在 PyPI 上，文档位于 **docs.mcpscore.dev**，并在 **mcpscore.dev** 提供托管审计入口。

# SEE ALSO

[mcp-probe](/man/mcp-probe)(1), [mcpsnoop](/man/mcpsnoop)(1), [pip](/man/pip)(1), [uv](/man/uv)(1)

# RESOURCES

```[Source code](https://github.com/mcp-box/mcpscore)```

```[Homepage](https://mcpscore.dev)```

```[Documentation](https://docs.mcpscore.dev)```

<!-- verified: 2026-08-05 -->
