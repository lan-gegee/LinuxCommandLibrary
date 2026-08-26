# TAGLINE

Cursor 面向终端的 AI 编程代理

# TLDR

**启动交互式代理会话**

```cursor-agent```

**带初始提示词启动**

```cursor-agent "[fix the auth bug in login.ts]"```

**运行一次性提示词**并打印结果（非交互）

```cursor-agent -p "[add tests for api.js]"```

用指定模型非交互运行

```cursor-agent -p "[review changes]" --model [gpt-5]```

**恢复上一个会话**

```cursor-agent --continue```

按 ID **恢复指定对话**

```cursor-agent --resume [chat-id]```

针对复杂任务**以计划模式启动**

```cursor-agent --plan "[migrate from Redux to Zustand]"```

输出结构化 JSON 供脚本使用

```cursor-agent -p "[task]" --output-format [json]```

自动批准文件编辑（无头 CI）

```cursor-agent -p "[task]" --force --trust```

列出历史会话

```cursor-agent ls```

# SYNOPSIS

**cursor-agent** [_command_] [_options_] [_prompt_]

> 注意：Cursor CLI 安装的二进制文件通常名为 **cursor-agent**。某些发行版还会创建 `cursor` 垫片（shim）。

# COMMANDS

**agent** (default)
> 启动 AI 编程代理。附加带引号的提示词则会预填该提示词开始。

**login** / **logout** / **status** / **whoami**
> 管理身份验证。`status`（别名 `whoami`）报告当前登录用户。

**about**
> 显示版本、系统和账户信息。

**models** / **--list-models**
> 列出账户可用的模型。

**mcp**
> 管理 Model Context Protocol 服务器（安装、启用、禁用、列出）。

**acp**
> 作为 ACP 服务器运行（高级集成）。

**update**
> 将 cursor-agent 更新到最新版本。

**ls**
> 列出过去的对话会话。

**resume** [_chat-id_]
> 恢复最近的或指定的对话。

**create-chat**
> 创建新的空对话并打印其 ID。

**generate-rule**（别名 **rule**）
> 以交互方式创建新的 Cursor 规则。

**install-shell-integration** / **uninstall-shell-integration**
> 在 `~/.zshrc` 中添加或移除 cursor-agent 的集成。

# PARAMETERS

**-p**, **--print**
> 打印模式：非交互地运行提示词，流式输出响应后退出。

**--output-format** _FORMAT_
> `text`（人类可读，默认）、`json`（单个结果对象）或 `stream-json`（NDJSON 事件流）。

**--stream-partial-output**
> 输出增量的 token 差异而非完整消息。

**--model** _NAME_
> 要使用的模型（运行 `cursor-agent models` 查看当前列表）。

**--mode** _MODE_
> `agent`（默认）、`plan` 或 `ask`。

**--plan**
> `--mode plan` 的简写。

**--continue**
> 继续最近一次的会话（不带 ID 的 `--resume` 简写）。

**--resume** [_chat-id_]
> 恢复指定的对话。

**-f**, **--force**, **--yolo**
> 运行所有工具调用而不询问（被明确拒绝的除外）。

**--sandbox** _MODE_
> 沙箱行为：`enabled` 或 `disabled`。

**--trust**
> 无需提示即信任工作区（无头运行时必需）。

**--approve-mcps**
> 自动批准所有已配置的 MCP 服务器。

**--workspace** _PATH_
> 使用指定工作目录而非当前目录。

**--worktree**
> 在 `~/.cursor/worktrees` 下创建新的 Git worktree 并在其中运行。

**--api-key** _KEY_
> API 密钥（环境变量：`CURSOR_API_KEY`）。

**-H**, **--header** _"Name: Value"_
> 为请求添加自定义请求头。

**-v**, **--version**
> 打印版本号。

**-h**, **--help**
> 显示命令帮助。

# INTERACTIVE MODES

**Agent mode** — 完整工具权限（读取、编辑、运行、搜索）。
**Plan mode** — 协作设计方案；未经确认不进行编辑。
**Ask mode** — 只读探索与问答。

在会话内用 `Shift+Tab` 或斜杠命令 `/plan`、`/ask` 切换。在消息前加 `&` 可将其交给后台 Cloud Agent 处理。

# DESCRIPTION

**cursor-agent** 是 Cursor 的终端原生 AI 编程助手。它复刻了 Cursor 编辑器所用的代理循环，但运行在纯终端中，因此可以与 Vim、Neovim、Emacs、JetBrains IDE 或 CI 流水线并存。会话是持久化的且可恢复。打印模式让代理可以脚本化——将 `--output-format json` 与 Shell 工具组合，即可把代理输出通过管道传给其他程序。

CLI 与 Cursor 编辑器使用相同的订阅和模型配额。Cloud Agent（可在会话内触发）将长时间运行的任务转移到 Cursor 的服务器上执行，让本地 Shell 保持流畅。

# CAVEATS

需要有效的 Cursor 订阅。仍处于 beta 阶段——各版本之间的选项可能变化。在非交互模式下通常需要 `--force`（又名 `--yolo`），否则代理会在审批提示处卡住；在 CI 中运行时请配合 `--trust`。除非使用 `--approve-mcps`，否则 MCP 服务器需要手动批准一次。

# HISTORY

**Cursor** 由 Anysphere 于 **2022 年**创立，是 VS Code 的 AI 优先分支。**cursor-agent** CLI 于 **2025 年**推出，把同样的代理循环带到编辑器之外，使 Cursor 可以从终端和 CI 中使用。

# SEE ALSO

[claude](/man/claude)(1), [aider](/man/aider)(1), [code](/man/code)(1)
