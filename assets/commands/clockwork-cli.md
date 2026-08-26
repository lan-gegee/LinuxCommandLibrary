# TAGLINE

Clockwork PHP 性能分析器的命令行监控工具

# TLDR

**监控当前项目的 Clockwork 日志**

```clockwork-cli```

**监控多个项目的日志**

```clockwork-cli [/www/*]```

# SYNOPSIS

**clockwork-cli** [_path_...]

# DESCRIPTION

**clockwork-cli** 是 Clockwork（一款 PHP 调试与性能分析工具）的命令行界面。它读取 Clockwork 服务端库为 Laravel、Slim 等 PHP 框架请求写下的 JSON 请求数据，并在终端中直接呈现一个不断更新的近期 HTTP 请求交互列表，无需浏览器扩展。

不带参数运行时，它监控当前项目的 Clockwork 日志。传入一个或多个路径（例如 `/www/*` 这样的 glob）可同时监控多个项目。每个请求都显示一个热键，你可以借此深入查看其数据库查询、日志条目、时间线及其他记录的数据。

# CONTROLS

**hotkey** (first character shown)
> 查看对应 HTTP 请求的详细信息

**Backspace**
> 显示最近 10 分钟内的请求

**Escape**
> 退出应用程序

# CAVEATS

需要在被分析（profiling）的 PHP 应用中安装并启用 Clockwork 服务端库，以便请求元数据被写入 clockwork-cli 所读取的存储目录。

# SEE ALSO

[php](/man/php)(1), [artisan](/man/artisan)(1)

# RESOURCES

```[Source code](https://github.com/ptrofimov/clockwork-cli)```

<!-- verified: 2026-06-22 -->
