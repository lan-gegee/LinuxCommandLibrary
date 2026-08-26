# TAGLINE

用于发送链路、指标和日志的 OpenTelemetry 命令行工具

# TLDR

为命令**发送 span**

```otel-cli exec --service [my-app] --name [build] -- [make]```

**手动发出服务器 span**

```otel-cli span --service [api] --name [handle-request]```

**状态**/配置检查

```otel-cli status```

# SYNOPSIS

**otel-cli** *command* [*options*]

# DESCRIPTION

**otel-cli** 是 OpenTelemetry 的命令行客户端。用 **otel-cli exec** 包裹进程，可在构建和脚本周围创建 span；也可以直接发出 span/事件，构建基于 Shell 的可观测性管道。OTLP 端点可通过环境变量（如 **OTEL_EXPORTER_OTLP_ENDPOINT**）或标志进行配置。

# PARAMETERS

**exec** **--** *command*...

> 在一个 span 内运行命令。

**span**

> 创建/结束带属性的 span。

**status**

> 显示配置/连接状态。

**--service** *name* / **--name** *span*

> 通用的身份标识属性。

厂商专属的导出器以及 W3C traceparent 传播辅助功能请参见 **otel-cli --help**。

# CAVEATS

需要可达的 OpenTelemetry collector 或后端。端点配置错误时会静默丢弃遥测数据。时钟偏差会影响 span 计时。

# INSTALL

```brew: brew install otel-cli```

```nix: nix profile install nixpkgs#otel-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[curl](/man/curl)(1), [time](/man/time)(1)

# RESOURCES

```[Source code](https://github.com/equinix-labs/otel-cli)```

<!-- verified: 2026-07-19 -->
