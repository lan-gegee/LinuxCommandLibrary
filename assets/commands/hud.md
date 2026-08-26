# TAGLINE

面向编程智能体 CLI 的紧凑型抬头显示面板

# TLDR

**安装**到全局并配置智能体回切

```npm install -g adrida/hud-mode && hud install```

**使用默认智能体引擎启动**

```hud```

**带提示词启动**

```hud "[fix the failing CI]"```

**恢复**本目录的上一次会话

```hud -r```

**在同一个面板下驱动 Claude Code**

```hud claude "[fix the CI]"```

**驱动 Codex 并恢复上次会话**

```hud codex -r```

**设置裸 `hud` 命令使用的默认引擎**

```hud default claude```

# SYNOPSIS

**hud** [_options_] [_prompt_]

**hud** **claude**|**codex**|**opencode** [_options_] [_prompt_]

**hud** **install** | **uninstall** | **default** _engine_

# DESCRIPTION

**hud** 是一个零依赖的终端前端，面向编程智能体（**OpenCode**、**Claude Code** 和 **Codex**）。它通过各 CLI 的 JSON 事件流以无界面方式驱动它们，显示一个紧凑的仪表盘（模型、token、状态、活动），而不是不断滚动刷屏的工具调用记录。提示词输入栏在整个回合进行期间保持可写状态，后续提示会排队等待；当智能体完成时，完整的回答会连同渲染好的 markdown 一同呈现。

`/hud` 可在同一会话的这块仪表盘与引擎的完整 TUI 之间切换（具体机制因引擎而异：hook / AGENTS.md 规则 / 自定义命令）。退出完整 TUI 后会返回 hud。仪表项和偏好设置持久保存在 `~/.claude/hud/` 下。

需要 **Node.js ≥ 18**，并且 `PATH` 上至少存在 `opencode`、`claude` 或 `codex` 之一。

# PARAMETERS

**-r** [_session-id_]
> 恢复当前目录的上一次会话，或恢复指定的会话 ID。

**-m**, **--model** _model_
> 特定于引擎的模型 ID。

**-e**, **--effort** _level_
> 特定于引擎的推理力度等级。

**--danger**
> 在引擎支持的前提下跳过审批/沙箱限制。

**claude**, **codex**, **opencode**
> 选择本次运行要驱动的智能体二进制程序。

**install**
> 交互式设置：默认智能体、OpenCode 回显，以及向 Claude/Codex/OpenCode 配置写入回切接线。

**uninstall**
> 移除由 **install** 写入的 hook、技能、提示词和配置块。

**default** _engine_
> 持久保存裸 **hud** 启动时使用的引擎。

# CONFIGURATION

**~/.claude/hud/config.json**
> 默认引擎及仪表项（`/gauges`）偏好设置。

**~/.claude/hud/links/**
> 记录智能体分享过哪些 URL 的按会话台账（在支持的终端中以 OSC 8 超链接呈现）。

**~/.claude/hud/handoff.json**
> 与完整引擎 TUI 相互切换时使用的哨兵文件。

**hud install** 还会在以下位置写入引擎专属内容：`~/.claude/skills/hud/`、`~/.claude/settings.json`（hook；备份为 `.hud-backup`）、`~/.codex/prompts/hud.md`、`~/.codex/AGENTS.md` 中的一个标记区块，以及 `~/.config/opencode/commands/hud.md`。

# CAVEATS

并不是智能体 CLI 的分叉——行为取决于各引擎的无头 JSON 流和恢复 API。Codex 的回切可能采用普通的 `hud` AGENTS.md 规则，而非零 token 斜杠命令。hud 内部的权限审批功能仍在计划之中。

# HISTORY

**hud**（软件包名 **hud-mode**）是由 Tracer / adrida 作者开发的 MIT 许可终端 UI，目标是让多回合的智能体会话一目了然，同时不取代 Claude Code、Codex 或 OpenCode 本身。

# SEE ALSO

[claude](/man/claude)(1), [codex](/man/codex)(1), [opencode](/man/opencode)(1)

# RESOURCES

```[Source code](https://github.com/adrida/hud-mode)```

<!-- verified: 2026-08-06 -->
