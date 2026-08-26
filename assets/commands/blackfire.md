# TAGLINE

分析 PHP 应用性能

# TLDR

**分析一个 PHP 脚本**

```blackfire run php [script.php]```

**带参数分析**

```blackfire run php [script.php] --arg1 [value]```

**通过 curl 分析 HTTP 请求**

```blackfire curl [https://example.com/page]```

**分析到指定环境**

```blackfire --env=[ENV_UUID] run php [script.php]```

**以 JSON 输出**分析结果

```blackfire --json run php [script.php]```

**静默分析**（不显示 URL）

```blackfire -q run php [script.php]```

**分析 Symfony 控制台命令**

```blackfire run php bin/console [command:name]```

# SYNOPSIS

**blackfire** [_options_] _subcommand_ [_arguments_]

# DESCRIPTION

**blackfire** 是 Blackfire 性能分析器的 CLI 工具，后者是面向 PHP 应用的性能管理方案。它可分析 PHP 脚本、HTTP 请求和 Web 应用，找出性能瓶颈。

该工具与 Blackfire.io 云服务集成，提供详细的火焰图、调用图和性能建议。可以对多次分析结果进行比较，跟踪性能随时间的变化。

# SUBCOMMANDS

**run**
> 分析 PHP CLI 脚本或命令

**curl**
> 分析 HTTP 请求（使用系统 curl）

**upload**
> 将分析结果上传到 Blackfire.io

**client:config**
> 配置客户端凭证

**agent:config**
> 配置 agent 设置

# PARAMETERS

**--env** _uuid_
> 分析结果所属的目标环境 UUID

**--json**
> 以 JSON 格式输出分析结果

**-q, --quiet**
> 抑制输出（不显示分析结果的 URL）

**--samples** _n_
> 采集的样本数量

**--title** _text_
> 为分析结果设置标题

**--external-id** _id_
> 为分析结果设置外部标识符

**--ignore-exit-status**
> 忽略被分析命令的非零退出状态

# CONFIGURATION

**/etc/blackfire/agent**
> Blackfire agent 配置，包括服务器凭证和套接字设置。

**~/.blackfire.ini**
> 客户端配置，包含用于身份验证的客户端 ID 和令牌。

# CAVEATS

需要 Blackfire 账户以及正确配置的凭证（BLACKFIRE_CLIENT_ID 和 BLACKFIRE_CLIENT_TOKEN）。必须安装 Blackfire PHP 扩展才能进行分析。**curl** 子命令要求系统已安装 curl。

# HISTORY

Blackfire 由 **SensioLabs**（Symfony 背后的公司）创建，于 **2014 年**作为商业性能分析方案发布。它由开源的 xhprof 分析器演化而来，为 PHP 应用提供持续的性能监控。

# INSTALL

```nix: nix profile install nixpkgs#blackfire```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[php](/man/php)(1), [curl](/man/curl)(1)
