# TAGLINE

面向复杂多文件任务的 AI 编程智能体

# TLDR

**启动交互式 REPL**

```plandex```

**描述任务或提问**

```plandex tell "[add a cancel button to the left of the submit button]"```

**将文件加载到上下文**

```plandex load [path/to/file.py]```

**将待定更改应用到项目文件**

```plandex apply```

**应用更改并提交到 git**

```plandex tell -a -c "[fix the authentication bug]"```

**查看计划历史**

```plandex log```

**回退到之前的步骤**

```plandex rewind [commit_hash]```

**使用简写别名**

```pdx tell "[your prompt]"```

# SYNOPSIS

**plandex** [_command_] [_options_]

**pdx** [_command_] [_options_]

# PARAMETERS

**tell**, **t**
> 描述任务、提问或聊天

**load**, **l**
> 将文件、目录、URL、笔记或管道数据加载到上下文

**apply**, **ap**
> 将计划中的更改应用到项目文件

**rewind**
> 回退到计划历史中的上一步

**log**
> 查看计划的变更历史

# TELL OPTIONS

**-f** _FILE_
> 从文件读取提示词

**-a**, **--apply**
> 生成后自动应用更改

**-c**, **--commit**
> 与 --apply 配合使用时将更改提交到 git

**--auto-load-context**
> 使用项目地图自动加载上下文

# DESCRIPTION

**Plandex** 是一个开源 AI 编程智能体，面向大型项目和真实任务设计。它可以规划并执行跨越多步骤、涉及数十个文件的复杂编码任务，可直接处理多达 200 万 token 的上下文。

该工具采用累积式 diff 审查沙箱，AI 生成的更改会与项目文件保持隔离，直到你准备好再应用。这使回滚和调试变得容易。Plandex 支持多种 AI 提供商，包括 Anthropic、OpenAI、Google 以及开源模型。

其主要特性包括终端命令的自动调试、基于 tree-sitter 的快速项目地图生成（支持 30 多种语言），以及从全自动到逐步审查的可配置自主级别。REPL 模式为命令和文件加载提供模糊自动补全。

# CONFIGURATION

**~/.plandex-home/**
> Plandex 的数据目录，存放计划、上下文和设置。

**OPENAI_API_KEY**
> OpenAI 模型的 API 密钥。

**ANTHROPIC_API_KEY**
> Anthropic Claude 模型的 API 密钥。

# CAVEATS

Windows 仅能通过 WSL 使用；该工具无法在 CMD 或 PowerShell 中运行。需要所支持提供商的 API 密钥。大上下文操作可能消耗大量 token。由于采用沙箱机制，更改在被应用之前不会立即反映到项目文件中。

# HISTORY

Plandex 由 **Dane Schneider** 于 **2024 年**在旧金山创立。开源版本于 **2024 年 4 月**发布。Schneider 此前创立了 EnvkeyConfig（YC W18）。该项目在 GitHub 上获得了超过 14,000 颗星，旨在解决大型代码库上 AI 辅助开发的难题。

# SEE ALSO

[claude](/man/claude)(1), [aider](/man/aider)(1), [codex](/man/codex)(1), [opencode](/man/opencode)(1)
