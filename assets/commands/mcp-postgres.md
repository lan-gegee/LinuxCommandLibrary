# TAGLINE

向 AI 助手暴露 PostgreSQL 工具的 MCP 服务器

# TLDR

**以 stdio 模式启动**，用于 Claude Desktop 集成

```mcp-postgres --database-url "[postgres://user:pass@localhost:5432/dbname]" --stdio```

在默认端口上**启动 TCP 服务器**

```mcp-postgres --database-url "[postgres://user:pass@localhost:5432/dbname]"```

**启动 HTTP/2 服务器**

```mcp-postgres --database-url "[postgres://user:pass@localhost:5432/dbname]" --http-port [3001]```

对生产数据库**使用受限访问模式**

```mcp-postgres --database-url "[postgres://user:pass@localhost:5432/dbname]" --access-mode restricted```

**启用 Prometheus 指标**

```mcp-postgres --database-url "[postgres://user:pass@localhost:5432/dbname]" --enable-metrics --metrics-port [9090]```

# SYNOPSIS

**mcp-postgres** **--database-url** _URL_ [_options_]

# PARAMETERS

**-d**, **--database-url** _URL_
> PostgreSQL 连接字符串（必需）

**--stdio**
> 以 stdio 模式运行，供 Claude Desktop 及兼容的 MCP 客户端使用

**-H**, **--host** _host_
> TCP 服务器绑定地址（默认：127.0.0.1）

**-p**, **--port** _port_
> TCP 服务器端口（默认：3000）

**--http-port** _port_
> HTTP/2 服务器端口（默认：3001）

**--min-connections** _n_
> 连接池最小大小（默认：5）

**--max-connections** _n_
> 连接池最大大小（默认：20）

**--log-level** _level_
> 日志详细程度：trace、debug、info、warn、error（默认：info）

**--access-mode** _mode_
> 安全级别：`unrestricted`（允许所有 SQL）或 `restricted`（仅安全查询）

**--enable-metrics**
> 启用 Prometheus 指标端点

**--metrics-port** _port_
> Prometheus 指标服务器端口（默认：9090）

**--tls-cert** _path_
> 用于 HTTPS 的 PEM 证书文件

**--tls-key** _path_
> 用于 HTTPS 的 PEM 私钥文件

**-V**, **--version**
> 显示版本号

# DESCRIPTION

**mcp-postgres** 是一个 Model Context Protocol (MCP) 服务器，将 Claude 等 AI 助手连接到 PostgreSQL 数据库。它提供超过 135 个工具，涵盖查询执行、schema 检查、DDL 操作、数据管理、监控和安全审计。

服务器支持三种传输模式：**stdio** 用于与 Claude Desktop 及兼容 MCP 客户端直接集成，**TCP** 用于端口 3000 上可网络访问的部署，**HTTP/2** 用于端口 3001 上的 Web 客户端。连接池自动管理，可配置最小和最大池大小。

通过 Cargo 安装：`cargo install mcp-postgres`；macOS 上可通过 Homebrew 安装：`brew tap corporatepiyush/mcp-postgres && brew install mcp-postgres`。

# CAVEATS

`unrestricted` 访问模式允许所有 SQL 操作，包括 DDL 语句和破坏性查询。连接生产数据库时请使用 `restricted` 模式。无论访问模式如何设置，都应确保 PostgreSQL 用户只拥有所需的最小权限。

# SEE ALSO

[psql](/man/psql)(1), [pg_dump](/man/pg_dump)(1)

# RESOURCES

```[Source code](https://github.com/corporatepiyush/mcp-pg-rust)```

<!-- verified: 2026-06-20 -->
