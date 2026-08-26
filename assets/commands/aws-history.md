# TAGLINE

回顾和检查过去的 CLI 命令执行记录。

# TLDR

**列出最近的 CLI 命令历史**

```aws history list```

**查看特定命令的详细信息**

```aws history show [command-id]```

**启用 CLI 历史**记录

```aws configure set cli_history enabled```

# SYNOPSIS

**aws history** _command_ [_options_]

# DESCRIPTION

**aws history** 提供对历次执行的 AWS CLI 命令历史的访问，可用于调试和审计目的，回顾过去的命令、其参数、发出的 API 调用以及收到的响应。

必须在 **~/.aws/config** 文件中设置 **cli_history = enabled** 才会启用历史记录。启用后，CLI 会记录所有命令调用以便日后检查。

# COMMANDS

**list**
> 显示先前执行命令的列表，包括其 ID、时间戳、参数和返回码

**show**
> 显示特定命令执行的详细信息，包括 API 调用和响应

# PARAMETERS

**--debug**
> 启用调试日志

**--output**
> 输出格式（json、text、table）

**--query**
> 用于筛选结果的 JMESPath 查询

**--profile**
> 使用指定的命名配置文件

# CAVEATS

历史记录存储在本地，不会跨机器同步。启用历史可能会在存储的记录中暴露敏感数据。历史数据库会随时间不断增大，应定期清理。历史只记录 CLI 命令，不记录 SDK 或控制台操作。

# HISTORY

**aws history** 命令于 **AWS CLI version 2** 中引入，旨在提供更好的调试和审计能力。它取代了手动记录 CLI 操作的做法，并与 CLI 的结构化输出系统集成。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-configure](/man/aws-configure)(1)

# RESOURCES

```[Source code](https://github.com/aws/aws-cli)```

```[Homepage](https://aws.amazon.com/cli/)```

```[Documentation](https://docs.aws.amazon.com/cli/latest/reference/history/index.html)```

<!-- verified: 2026-06-18 -->
