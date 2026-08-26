# TAGLINE

用于自主完成任务的 AI 智能体循环编排器

# TLDR

**使用 PRD 文件运行 Ralph**

```ralph-tui run --prd [./prd.json]```

**在 AI 辅助下创建 PRD**

```ralph-tui create-prd --chat```

**初始设置**

```ralph-tui setup```

# SYNOPSIS

**ralph-tui** _command_ [_options_]

# DESCRIPTION

**ralph-tui** 是一个终端 UI，用于编排 AI 编程智能体自主完成任务列表。它将你的 AI 编程助手（Claude Code、OpenCode、Gemini CLI 等）接入你的任务跟踪器并循环运行——选择优先级最高的任务、构建提示词、执行智能体、检测是否完成，然后重复此过程直到所有任务完成。

# CAVEATS

需要已安装并配置好某个 AI 编程智能体（如 Claude Code）。

# HISTORY

**ralph-tui** 由 **subsy** 创建，使用 **TypeScript** 编写。

# INSTALL

```aur: yay -S ralph-tui```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[claude](/man/claude)(1)
