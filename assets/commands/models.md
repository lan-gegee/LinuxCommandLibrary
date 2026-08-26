# TAGLINE

用于浏览 LLM 模型和编程智能体的 CLI 与 TUI

# TLDR

**启动交互式 TUI**

```models```

**列出所有模型**

```models list```

**跨提供商搜索模型**

```models search "[query]"```

**查看某个模型**的详细信息

```models show [provider/model-id]```

**列出提供商**

```models providers```

**查看编程智能体状态**

```agents status```

# SYNOPSIS

**models** [_subcommand_] [_options_]

**agents** [_subcommand_] [_options_]

# SUBCOMMANDS

**list**
> 列出可用模型。

**show** _MODEL_
> 显示特定模型的详细信息。

**search** _QUERY_
> 在所有提供商中搜索模型。

**providers**
> 列出模型提供商。

**benchmarks** _list_|_show_
> 浏览已发布的基准测试结果。

**status** _list_|_show_|_sources_
> 查看被跟踪的数据源及其状态。

**link**
> 为模型创建符号链接别名。

# DESCRIPTION

**models** 是一个快速的 CLI 和 TUI，用于在终端中浏览 LLM 模型并跟踪编程智能体的动态。它聚合来自 models.dev 的数据，让你可以浏览和筛选 AI 模型提供商、跨多个提供商搜索、查看上下文长度限制、定价和能力、复制模型 ID，并把数据导出为 JSON。

与之配套的 **agents** 命令维护着一份精选的编程智能体列表，能检测已安装的版本，并跟踪 GitHub 上的星标、发布和更新情况等指标。

# CAVEATS

需要联网以获取模型数据。定价和可用性可能随时变化，恕不另行通知。

# HISTORY

**models** 由 **arimxyer** 创建，使用 **Rust** 编写。

# INSTALL

```brew: brew install models```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[claude](/man/claude)(1), [ollama](/man/ollama)(1)
