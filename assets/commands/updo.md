# TAGLINE

支持告警的网站在线状态监控 CLI

# TLDR

**监控一个网站**

```updo monitor [https://example.com]```

**以自定义刷新间隔和超时进行监控**

```updo monitor --refresh [10] --timeout [5] [https://example.com]```

**配合 Slack webhook 告警进行监控**

```updo monitor --webhook-url "[https://hooks.slack.com/...]" [https://example.com]```

# SYNOPSIS

**updo** **monitor** [_options_] _URL_...

# PARAMETERS

**--refresh** _seconds_
> 刷新间隔，单位为秒（默认：5）。

**--timeout** _seconds_
> 请求超时时间，单位为秒（默认：10）。

**--count** _n_
> 执行检查的次数（0 表示无限次，也是默认值）。

**--webhook-url** _url_
> 用于告警的 Webhook URL（Slack 或 Discord）。

**--assert-text** _text_
> 用于校验每次检查的预期响应正文文本。

**--simple**
> 打印纯文本输出而非交互式 TUI。

# DESCRIPTION

**updo** 是一款用于监控网站在线状态和性能的命令行工具。它提供实时指标，包括响应时间、SSL 证书到期时间和在线率百分比。支持多目标监控、跨区域的 AWS Lambda 部署、Prometheus 与 Grafana 集成，以及面向 Slack 和 Discord 的 webhook 告警。

# HISTORY

**updo** 由 **Owloops** 创建，使用 **Go** 语言编写。

# INSTALL

```aur: yay -S updo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ping](/man/ping)(1), [curl](/man/curl)(1), [httpstat](/man/httpstat)(1)
