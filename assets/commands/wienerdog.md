# TAGLINE

为 Claude Code 和 Codex CLI 提供基于文件的记忆、技能与夜间例行任务

# TLDR

**初始化** Wienerdog（先用 dry-run 预览）

```npx wienerdog@latest init --dry-run```

```npx wienerdog@latest init```

```npx wienerdog@latest init --yes```

**检查**安装健康状况和安全门控

```wienerdog doctor```

```wienerdog safety```

从身份笔记**同步**会话摘要

```wienerdog sync```

立即**运行**一次 dream 整理任务

```wienerdog dream```

**批准**拟议的身份笔记修改

```wienerdog memory approve```

**移除** Wienerdog 安装的所有内容

```wienerdog uninstall```

# SYNOPSIS

**wienerdog** _command_ [_options_]

# DESCRIPTION

**wienerdog** 会安装一个纯文件的"记忆库"以及相关技能/钩子，使编程智能体（**Claude Code** 和 **Codex CLI**）共享同一份配置和长期笔记。它不运行守护进程，也不会外传数据：布局是位于 **~/.wienerdog** 下的 markdown 文件和配置，由你已经在用的 AI 工具来解读。

**init** 创建核心结构、检测智能体，并可通过一次访谈用同一个记忆库（Obsidian 风格的 PARA）填写 **CLAUDE.md** / **AGENTS.md**。计划任务 **dream** 会将近期会话整理进记忆（每晚最多一个 git commit），并可提出身份笔记的修改建议，这些修改只有在执行 **wienerdog memory approve** 后才会生效。可选的 Google Workspace 访问和目录例行任务使用操作系统调度器（launchd / systemd / Task Scheduler），并在每次运行前进行验证。

需要 **Node.js ≥ 18**。典型安装方式：**npx wienerdog@latest init**，或上游的 **install.sh** 引导脚本，或 **npm i -g wienerdog**。当前状态为 **0.x**；在 1.0 之前文件格式仍可能变化。

# PARAMETERS

**init** [**--dry-run**] [**--yes**]
> 创建 **~/.wienerdog**，检测 AI 工具，并设置技能/钩子。**--dry-run** 只打印计划而不写入。

**adopt**
> 让 Wienerdog 采用现有的记忆库目录，而不是新建一个。

**sync**
> 从记忆库的身份笔记重新渲染会话摘要（手动编辑 **config.yaml** 后计划任务需要重新授权时，也可用它修复）。

**update**
> 将 Wienerdog 更新到最新发布版本，无需单独的 npm 流程。

**dream**
> 将近期会话整理进记忆库（与夜间任务做同样的事）。

**schedule**
> 添加、移除或列出计划任务（dream 和可选的例行任务）。

**run-job**
> 立即运行某个计划任务（由 OS 调度器调用）。

**doctor**
> 检查现有安装是否存在问题。

**alerts**
> 列出任务警报；通过输入确认来静音已读警报。

**uninstall**
> 移除 Wienerdog 创建的文件（撤销安装）。

**gws**
> 通过本地能力代理使用 Google Workspace 辅助功能（读取 Gmail/日历/云端硬盘；起草邮件）。

**grant**
> 授权某个例行任务发送邮件（需输入确认）。

**memory**
> 批准身份笔记的修改，使其注入下一个会话（需输入确认）。

**safety**
> 显示哪些敏感操作被允许或阻止。

**--dry-run**
> 全局选项：显示将会发生什么；不做任何更改（在支持的地方）。

**--yes**
> 全局选项：跳过确认提示（在支持的地方）。

# CONFIGURATION

**~/.wienerdog**
> 核心安装根目录：记忆库、技能、钩子和配置。**uninstall** 会移除 Wienerdog 写入的内容。

**config.yaml**（安装树内）
> 运行时/调度配置。在 **wienerdog sync** 之外的编辑可能使计划任务进入失败关闭状态，直到重新授权。

**CLAUDE.md** / **AGENTS.md**
> 由共享记忆库访谈和记忆笔记生成的智能体身份摘要。

# CAVEATS

依赖已安装的 Claude Code 和/或 Codex CLI，且设置后需重启才能加载技能。密钥清理是尽力而为。计划的完整性检查可检测两次同步之间的漂移；它们不是 OS 级的恶意软件防御。项目处于 1.0 之前阶段；请将安装后的文件布局视为公共 API。

# HISTORY

**Wienerdog** 是一个开源（MIT）npm 包，它把智能体的记忆和例行任务视为受版本控制的文件，而不是个人 AI 守护进程。上游地址：**github.com/wienerdog-ai/wienerdog**。

# SEE ALSO

[claude](/man/claude)(1), [codex](/man/codex)(1), [npx](/man/npx)(1), [npm](/man/npm)(1), [node](/man/node)(1)

# RESOURCES

```[Source code](https://github.com/wienerdog-ai/wienerdog)```

```[Homepage](https://www.npmjs.com/package/wienerdog)```

<!-- verified: 2026-08-02 -->
