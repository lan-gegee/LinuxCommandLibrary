# TAGLINE

检查并分叉持久化智能体工作流日志

# TLDR

**列出**日志存储目录中的运行记录

```kassette list --storage file:[.kassette]```

显示某次运行的**状态**

```kassette status [runId] --storage file:[.kassette]```

**导出**日志条目（可选指定偏移量）

```kassette dump [runId] --storage file:[.kassette]
kassette dump [runId] --offset [N] --storage file:[.kassette]```

从日志前缀**分叉**出新的运行

```kassette fork [srcRunId] --from-offset [N] --storage file:[.kassette]```

使用 **S3 兼容**存储

```kassette list --storage s3://[bucket]/[prefix]]```

# SYNOPSIS

**kassette** _command_ [_options_] [_args_]

# DESCRIPTION

**kassette** 是来自 **@usekassette/cli** 的 CLI，用于操作 kassette 持久化库写入的日志。Kassette 将智能体工作流步骤记录在只追加的 JSONL 日志中，这样重试时可以重放已完成的工作，而不必重新运行昂贵的 LLM 调用和副作用操作。

该库嵌入在你的进程中（没有独立服务器）。CLI 帮助人类和智能体针对文件系统或 S3 后端存储执行 **list**、**status**、**dump** 和 **fork** 操作。日志是纯文本，适合配合 **jq** 使用和离线检查。

# PARAMETERS

**list**
> 列出所选存储中的运行记录

**status** _runId_
> 概括运行状态（success、suspended、error 等）

**dump** _runId_ [**--offset** _N_]
> 打印日志条目

**fork** _srcRunId_ **--from-offset** _N_
> 创建一个新的运行，先重放日志前缀再继续实际执行

**--storage** _file:path_|_s3://bucket[/prefix]_
> 选择后端；使用 **s3://** 需安装 **@usekassette/s3**

# CAVEATS

核心产品是可嵌入的库；CLI 用于检查和分叉，本身不用于运行工作流。**s3://** 需要可选的 S3 软件包。重放的前提是工作流代码仍与日志结构匹配——请谨慎使用版本控制和步骤重命名。

# SEE ALSO

[jq](/man/jq)(1)

# RESOURCES

```[Source code](https://github.com/lostinpatterns/kassette)```

```[Homepage](https://lostinpatterns.github.io/kassette/)```

```[Documentation](https://lostinpatterns.github.io/kassette/docs/quickstart)```

<!-- verified: 2026-07-14 -->
