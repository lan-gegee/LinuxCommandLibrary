# TAGLINE

基于本地 tmux 的编程智能体元调度器

# TLDR

**配置**带 Telegram 远程控制的 relaymux

```relaymux setup --telegram --telegram-bot-token '[token]'```

**检查**服务状态

```relaymux status```

在仓库上**启动**一个智能体

```relaymux launch --repo [~/code/my-app] --agent [claude] --name [fix-tests] --prompt "[Fix the failing tests]"```

**发送**测试通知

```relaymux notify --from [test] --reply-mode telegram --message "[hello]"```

# SYNOPSIS

**relaymux** _subcommand_ [_options_]

# DESCRIPTION

**relaymux** 是一款轻量级的本地元调度器，它在可见的 **tmux** 会话中运行命令行编程智能体，同时让你可以远程监控它们并回复。每次智能体运行都在你的机器上拥有自己的 tmux 标签页，因此工作始终保留在本地且可随时查看；Telegram 则充当状态更新和提示词的远程控制通道。

它编排现有的智能体 CLI（例如 **claude**、**codex** 或 **pi**）而不是取代它们，适合在手机上启动并监督长时间运行的智能体任务。

# SUBCOMMANDS

**setup**
> 初始化配置，包括 Telegram 集成。

**status**
> 报告 relaymux 服务和正在运行的智能体的状态。

**launch**
> 在给定仓库上带提示词启动一次智能体运行。

**notify**
> 通过配置的回复渠道发送手动通知。

**db**
> 执行数据库操作（需要系统 **sqlite3** CLI）。

# PARAMETERS

**--telegram**
> 启用 Telegram 集成（与 **setup** 配合使用）。

**--telegram-bot-token** _token_
> Telegram 机器人认证令牌。

**--repo** _path_
> 智能体运行所在的仓库或工作区路径。

**--agent** _name_
> 要启动的智能体 CLI（例如 **claude**、**codex** 或 **pi**）。

**--name** _name_
> 本次智能体运行的标签。

**--prompt** _text_
> 传递给智能体的任务指令。

**--from** _source_
> 通知来源标签（与 **notify** 配合使用）。

**--reply-mode** _channel_
> 回复渠道，例如 **telegram**。

**--message** _text_
> 通知正文（与 **notify** 配合使用）。

# CAVEATS

需要 Node.js 20+、npm、**tmux** 以及要驱动的本地智能体 CLI。数据库操作需要 PATH 中存在系统的 **sqlite3** 命令。

# HISTORY

**relaymux** 使用 TypeScript 编写，以 MIT 许可证发布。它于 2026 年发布，旨在远程监督本地编程智能体，而无需将控制权交给托管服务。

# SEE ALSO

[tmux](/man/tmux)(1), [screen](/man/screen)(1), [zellij](/man/zellij)(1), [claude](/man/claude)(1)

# RESOURCES

```[Source code](https://github.com/mupt-ai/relaymux)```

<!-- verified: 2026-06-19 -->
