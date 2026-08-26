# TAGLINE

等待服务变为可用

# TLDR

**等待 TCP 端口**接受连接

```wait4x tcp [localhost:8080]```

**等待 HTTP 端点**返回特定状态码

```wait4x http [https://api.example.com/health] --expect-status-code [200]```

**并行等待多个服务**

```wait4x tcp [127.0.0.1:5432] [127.0.0.1:6379] [127.0.0.1:27017]```

**等待某个服务就绪后执行命令**

```wait4x tcp [localhost:3306] -- [./start-app.sh]```

**等待 DNS 记录**解析成功

```wait4x dns A [example.com] --expected-ip [93.184.216.34]```

**等待 PostgreSQL** 就绪

```wait4x postgresql 'postgres://[user]:[password]@[localhost]:5432/[mydb]?sslmode=disable'```

**等待 Redis** 并校验键

```wait4x redis redis://[localhost]:6379 --expect-key "[status]=^ready$"```

**等待某服务变为不可用**

```wait4x tcp [localhost:8080] --invert-check```

# SYNOPSIS

**wait4x** _command_ [_options_] [_targets_] [**--** _command_]

# SUBCOMMANDS

**tcp** _address..._
> 等待 TCP 端口接受连接。

**http** _url..._
> 等待 HTTP 端点并验证响应。

**dns** _type_ _name_
> 等待 DNS 记录解析（A、AAAA、CNAME、MX、NS、TXT）。

**mysql** _dsn_
> 等待 MySQL 数据库就绪。

**postgresql** _dsn_
> 等待 PostgreSQL 可用。

**mongodb** _uri_
> 等待 MongoDB 连接。

**redis** _uri_
> 等待 Redis 可用，可选键检查。

**rabbitmq** _uri_
> 等待 RabbitMQ 消息代理。

**kafka** _uri..._
> 等待 Kafka broker 就绪。

**influxdb** _url_
> 等待 InfluxDB 服务。

**temporal** _subcommand_
> 等待 Temporal 工作流引擎（server 或 worker）。

**exec** _command_
> 执行 shell 命令并检查退出码。

# PARAMETERS

**--timeout** _duration_
> 最长等待时间（例如 30s）。

**--interval** _duration_
> 检查频率（默认：1s）。

**--invert-check**
> 反转为等待服务变为不可用。

**--backoff-policy** _policy_
> 重试策略（例如 exponential）。

**--backoff-exponential-coefficient** _n_
> 每次重试的倍增系数（例如 2.0）。

**--backoff-exponential-max-interval** _duration_
> 重试之间的最大间隔。

**--expect-status-code** _code_
> 期望的 HTTP 响应状态码（http 子命令）。

**--expect-body-regex** _pattern_
> 在 HTTP 响应正文中匹配的模式。

**--expect-body-json** _path_
> 使用 GJSON 语法的 JSON 路径校验。

**--expect-body-xpath** _expression_
> 对 HTML/XML 响应求值的 XPath 表达式。

**--expect-header** _header=value_
> 期望的 HTTP 响应头。

**--request-header** _header_
> 自定义 HTTP 请求头（可重复使用）。

**--expect-key** _key_
> 期望存在的 Redis 键，可选带值正则（key=regex）。

**--expect-table** _table_
> 期望存在的数据库表（mysql/postgresql 子命令）。

**--expected-ip** _ip_
> DNS A/AAAA 记录期望的 IP 地址。

**--expected-domain** _domain_
> DNS CNAME/MX 记录期望的域名。

**-n** _server_
> 要查询的 DNS 域名服务器。

# DESCRIPTION

**wait4x** 是一款轻量级、零依赖的工具，用于等待服务达到就绪状态。它支持 TCP、HTTP、DNS，以及与数据库和消息代理的直接集成，包括 MySQL、PostgreSQL、MongoDB、Redis、RabbitMQ、Kafka、InfluxDB 和 Temporal。

可以指定多个目标并行检查服务。**--invert-check** 标志反转逻辑，改为等待服务变为不可用。检查成功后，可以通过追加 **--** 加命令来执行任意命令。

wait4x 支持可配置的超时时间、重试间隔和指数退避策略，适用于 CI/CD 流水线、容器编排、部署脚本以及本地开发环境。

# CAVEATS

数据库和消息代理的连接字符串以命令行参数形式传递，可能在进程列表中暴露凭据。生产环境请使用环境变量或密钥管理。该工具超时后以非零状态退出，脚本应相应处理这种情况。

# HISTORY

**wait4x** 的定位是 shell 等待脚本及 **wait-for-it**、**dockerize** 等工具的现代单二进制替代品。它使用 **Go** 编写，从简单的 TCP/HTTP 检查扩展到对常见数据库和消息代理的原生协议支持。该项目持续维护中，可通过 Homebrew、Alpine 软件包、AUR、NixOS 和 Docker 获取。

# INSTALL

```apk: sudo apk add wait4x```

```zypper: sudo zypper install wait4x```

```brew: brew install wait4x```

```nix: nix profile install nixpkgs#wait4x```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nc](/man/nc)(1), [curl](/man/curl)(1), [timeout](/man/timeout)(1)
