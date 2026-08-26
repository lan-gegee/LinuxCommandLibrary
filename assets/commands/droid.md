# TAGLINE

Factory.ai 终端编程智能体

# TLDR

**启动交互式会话**

```droid```

**非交互式执行单个提示词**（默认只读）

```droid exec "[analyze the auth system and propose a plan]"```

**允许安全的文件编辑**

```droid exec --auto low "[add JSDoc comments to all functions]"```

**完全自主**，包括提交和推送

```droid exec --auto high "[fix the bug, run tests, commit and push]"```

**从文件读取提示词**

```droid exec -f [prompt.txt]```

**获取 JSON 输出**供脚本使用

```droid exec -o json "[your prompt]"```

**继续已有会话**

```droid exec -s [session_id] "[keep going]"```

**在隔离的 git worktree 中工作**

```droid exec --worktree "[refactor the parser]"```

# SYNOPSIS

**droid** [_options_]

**droid** **exec** [_options_] [_prompt_]

**droid** _subcommand_ [_options_]

# COMMANDS

**droid**
> 启动交互式 REPL。

**exec**
> 非交互式运行任务。这是脚本化的入口。

**search**, **find**
> 跨本地会话搜索：消息、文档和工具结果。

**mcp**
> 管理模型上下文协议服务器。

**plugin**
> 安装、卸载和更新插件，并管理插件市场。

**computer**
> 注册和管理自带机器（Bring-Your-Own-Machine）计算机。

**daemon**
> 运行 Factory 守护进程服务器。

**update**
> 将 CLI 更新到最新版本。

# EXEC OPTIONS

**--auto** _LEVEL_
> 自主级别：**low**、**medium** 或 **high**。省略则智能体保持只读。

**-f**, **--file** _PATH_
> 从文件读取提示词。

**-m**, **--model** _ID_
> 选择特定模型。

**-r**, **--reasoning-effort** _LEVEL_
> 覆盖推理力度：`off`、`none`、`low`、`medium` 或 `high`。

**-o**, **--output-format** _FORMAT_
> 输出格式：`text`（默认）、`json`、`stream-json` 或 `stream-jsonrpc`。

**--input-format** _FORMAT_
> 输入格式。`stream-jsonrpc` 支持多轮会话。

**-s**, **--session-id** _ID_
> 继续已有会话。

**--fork**
> 将已有会话分叉为新副本并恢复之。

**-w**, **--worktree**
> 在隔离的 git worktree 中运行会话，工作树保持原样。

**--cwd** _PATH_
> 在指定的工作目录中执行。

**--use-spec**
> 以规格模式启动：先规划再执行。

**--spec-model** _ID_ / **--spec-reasoning-effort** _LEVEL_
> 为规划阶段使用不同的模型或推理力度。

**--enabled-tools** _IDS_ / **--disabled-tools** _IDS_ / **--list-tools**
> 强制启用工具、本次运行禁用工具，或列出可用工具后退出。

**--mission**
> 以 mission 模式运行，编排多个智能体。**--worker-model** 和 **--validator-model** 及其配套的 reasoning-effort 标志控制各子智能体。

**--append-system-prompt** _TEXT_ / **--append-system-prompt-file** _PATH_
> 向系统提示词追加自定义指令。

**--tag** _TAG_
> 附加会话标签。可重复使用。

**--skip-permissions-unsafe**
> 跳过所有权限提示。危险；参见 CAVEATS。

**-v**, **--version** / **-h**, **--help**
> 打印版本号或显示帮助。

# CONFIGURATION

**.factory/droids/**
> 自定义子智能体定义，为带 YAML frontmatter 的 markdown 文件。

# DESCRIPTION

**droid** 是 Factory.ai 面向终端的编程智能体。它有两种运行形态：交互式 REPL，以及 **droid exec**——后者接收提示词、持续工作直到任务完成然后退出，这使它可以在脚本和 CI 中使用。

权限是分级而非全有全无的。不指定 **--auto** 时，智能体实际上只读：它可以查看代码库并产出计划，但不能修改代码。**--auto low** 允许文件编辑，仅此而已。**--auto medium** 额外自动批准可逆操作，比如安装依赖和运行测试，但执行任何有风险的操作前仍会询问。**--auto high** 则移交一切，包括提交和推送。合理的做法是在陌生仓库上先从 low 开始，看看智能体实际打算改动什么，等信任建立后再提高级别。

**--use-spec** 反转了流程：智能体先撰写规格说明，然后再据此实现，还可通过 **--spec-model** 为规划步骤选用更强的模型。**--mission** 更进一步，编排多个智能体并在 worker 与 validator 角色之间分工。

自定义子智能体（"Custom Droids"）是 `.factory/droids/` 下带 YAML frontmatter 的 markdown 文件，因此仓库可以随代码一起分发自己的专用智能体。

# CAVEATS

**--skip-permissions-unsafe** 会禁用所有安全检查，包括破坏性命令前的确认。它面向用完即弃的容器；在你珍视的机器上运行它，或在环境变量里带着有效凭据运行它，正是其名字所警告的那种错误。

**--auto high** 可以改写历史、强制推送并不加询问地运行任意命令。将它与对共享分支有推送权限的会话组合是实实在在的风险，而 **--worktree** 是低成本的缓解手段，因为它把智能体的更改与你的工作树隔离开来。

该工具需要 Factory.ai 账户，提示词、代码上下文和工具结果会被发送到 Factory 的服务及底层模型提供方。这对专有代码有明显影响，将其指向私有仓库之前值得对照你所在组织的政策审视一番。

# HISTORY

**droid** 是 **Factory.ai** 的 CLI，这家公司打造的智能体工具面向企业工程团队而非个人开发者——这一点体现在它对会话管理、worktree 隔离、多智能体 mission 和模型选择的强调上。它是 2024 年以来涌现的一众终端编程智能体中的一员，与 Claude Code、Codex CLI、Aider 等并列。

# SEE ALSO

[claude](/man/claude)(1), [codex](/man/codex)(1), [aider](/man/aider)(1), [opencode](/man/opencode)(1), [gemini](/man/gemini)(1)

# RESOURCES

```[Homepage](https://factory.ai)```

```[Documentation](https://docs.factory.ai/reference/cli-reference)```

<!-- verified: 2026-07-14 -->
