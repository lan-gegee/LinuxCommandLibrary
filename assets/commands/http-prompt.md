# TAGLINE

具有自动补全和语法高亮的交互式命令行 HTTP 客户端

# TLDR

启动一个针对 **localhost** 的会话

```http-prompt```

以**指定 URL** 启动会话

```http-prompt [http://example.com]```

以带**认证**的方式启动会话

```http-prompt [localhost:8000/api] --auth [username:password]```

# SYNOPSIS

**http-prompt** [_URL_] [_options_]

# PARAMETERS

**--auth** _USER:PASS_
> 设置 HTTP 基本认证凭据

**--version**
> 显示版本信息

# DESCRIPTION

**http-prompt** 是一个交互式命令行 HTTP 客户端，具备自动补全和语法高亮功能。它提供一个 REPL（读取-求值-打印循环）环境，用于探索和测试 HTTP API。

它构建在 HTTPie 之上，以交互方式构造 HTTP 请求，支持对 HTTP 方法、请求头以及先前使用过的值进行 Tab 补全。会话会持久保存设置，并可在之后恢复。

在提示符中，你可以逐步设置请求头、查询参数和请求体数据，然后使用标准 HTTP 方法（GET、POST、PUT、DELETE 等）执行请求。

# CAVEATS

需要 Python 和 HTTPie。会话保存在本地，并在多次调用之间保持。不适合用于自动化脚本；此类需求请使用 HTTPie 或 curl。

# HISTORY

http-prompt 由 Chang-Hung Liang 创建并于 **2016 年**发布。它的灵感来自数据库客户端的交互性，旨在为 HTTP API 探索提供类似的便利体验。

# INSTALL

```brew: brew install http-prompt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[http](/man/http)(1), [curl](/man/curl)(1), [httpie](/man/httpie)(1)
