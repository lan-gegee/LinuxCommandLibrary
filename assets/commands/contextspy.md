# TAGLINE

面向 LLM 代理的上下文窗口分析器

# TLDR

**启动**代理和仪表盘

```contextspy start```

通过代理**运行**某个代理程序

```contextspy run [claude] [path]```

**安装**代理的 HTTPS 证书

```contextspy install-cert```

**重置**本地请求数据库

```contextspy reset-db```

# SYNOPSIS

**contextspy** _command_ [_options_]

# DESCRIPTION

**contextspy** 是一款面向大语言模型（LLM）代理的上下文分析器。它作为 HTTPS 正向代理（对本地托管的模型则是反向代理）位于代理程序与模型提供商之间，拦截每个请求并将提示词分解为多个类别，让你看清是什么在消耗上下文窗口。

令牌被归入八个桶：系统提示词、工具定义、工具结果、文件内容、对话历史、用户消息、助手预填充以及未分类的剩余部分。实时仪表盘会按请求绘制这一构成，并允许将请求分组为会话，以便跨时间对比任务。它能识别 Copilot、Claude Desktop、Claude Code、opencode 和 Cursor 等常见代理。

所有数据都存储在本地的 SQLite 中，不会向云端发送任何内容。这使 contextspy 在代理开发过程中有助于理解并降低令牌用量和成本。

# PARAMETERS

**start**

> 启动代理和 Web 仪表盘（默认服务地址为 http://127.0.0.1:5173）。

**run** _agent_ [_path_]

> 启动一个已被识别的代理程序，使其流量经由本代理转发。

**install-cert**

> 安装代理的根证书，以便检查 HTTPS 流量。

**reset-db**

> 清空存储已捕获请求的本地 SQLite 数据库。

# CAVEATS

检查 HTTPS 流量需要安装该代理的证书，这意味着你要信任被拦截连接上的中间人；只在你自己掌控的机器上使用。contextspy 是一款年轻的第三方工具，与任何模型提供商均无关联。

# SEE ALSO

[mitmproxy](/man/mitmproxy)(1), [claude](/man/claude)(1), [ollama](/man/ollama)(1)

# RESOURCES

```[Source code](https://github.com/RimantasZ/contextspy)```

<!-- verified: 2026-06-16 -->
