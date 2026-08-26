# TAGLINE

cron 任务监控服务的 CLI 工具

# TLDR

**同步 cron 任务到 Cronitor**

```cronitor sync```

**带监控地执行命令**

```cronitor exec [monitor-key] -- [command]```

**列出所有 cron 任务**

```cronitor list```

**查看监控器状态**

```cronitor status```

**发送遥测 ping**

```cronitor ping [monitor-key]```

**启动 Web 控制台**

```cronitor dash```

**配置 API 密钥**

```cronitor configure --api-key [key]```

# SYNOPSIS

**cronitor** [_global_options_] _command_ [_options_]

# DESCRIPTION

**cronitor** 是 Cronitor 的配套 CLI。Cronitor 是一项基于云的 cron 任务与定时任务监控服务。该工具监控 cron 任务的执行情况，跟踪时间与频率，并在任务失败、错过调度或运行超时时发送警报。

CLI 会自动把系统中的 cron 任务同步到 Cronitor 服务，包装命令执行以发送遥测 ping，并提供查看任务状态的控制台。它通过确保问题得到及时通知，帮助团队维护定时维护任务、备份和自动化流程的可靠性。

# COMMANDS

**sync**
> 将 cron 任务同步到 Cronitor

**exec**
> 带监控地执行命令

**list**
> 列出并搜索 cron 任务

**ping**
> 发送遥测 ping

**status**
> 查看监控器状态

**dash**
> 启动 Web 控制台

**configure**
> 保存配置

**select**
> 以交互方式选择要运行的 cron 任务

**activity**
> 查看监控器活动

**shell**
> 运行类 cron 的 shell

**update**
> 更新到最新版本

# GLOBAL OPTIONS

**-k**, **--api-key** _key_
> Cronitor API 密钥

**-c**, **--config** _file_
> 配置文件路径

**--env** _name_
> Cronitor 环境

**-n**, **--hostname** _name_
> 主机标识符

**-u**, **--users** _list_
> 逗号分隔的用户列表

**-p**, **--ping-api-key** _key_
> 遥测事件 API 密钥

**-v**, **--verbose**
> 详细输出

**-l**, **--log** _file_
> 调试日志文件

# CONFIGURATION

**~/.config/cronitor/cronitor.json**
> 用户配置文件，包含 API 密钥、环境、主机名等设置。

# CAVEATS

需要 Cronitor 账户和 API 密钥。监控系统级 crontab 时需使用 sudo。内置 MCP 服务器，可用于 AI 工具集成。

# SEE ALSO

[cron](/man/cron)(8), [crontab](/man/crontab)(1)
