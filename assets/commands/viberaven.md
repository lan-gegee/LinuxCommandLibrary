# TAGLINE

面向 AI 构建应用的生产环境上下文 CLI

# TLDR

**打开本地 Studio 驾驶舱**

```viberaven```

**将 agent 指引安装到项目配置文件**

```viberaven init --agents all```

**检查 agent 集成健康状况**

```viberaven doctor --agents```

**通过 stdio 为已连接的 agent 提供 MCP 资源**

```viberaven --mcp```

# SYNOPSIS

**viberaven** [_options_]

**viberaven** _subcommand_ [_arguments_]

# DESCRIPTION

**viberaven** 是 VibeRaven 的命令行入口。VibeRaven 是一套本地优先的工具集，在 AI 编程 agent 编辑仓库之前为其提供生产环境上下文。它将有边界的规则和技能安装到 **AGENTS.md**、**CLAUDE.md**、**.cursor/rules** 等文件中，在 **.viberaven/** 下维护生产环境记忆，并启动 Studio UI 用于查看发布 diff、提供商边界、部署证据以及与 agent 对话。

该 CLI 通过 npm 分发，通常以 **npx -y viberaven** 运行。它专注于 **route → ask → evidence → fix → verify → remember** 这一循环，将不确定的任务路由到专门技能，用于架构规划、回归分析、生产上下文和上线检查。MCP 模式暴露结构化的项目资源，使 agent 无需仅凭仓库文件猜测即可获取发布和提供商状态。

# PARAMETERS

**init**
> 将 VibeRaven 的 agent 规则和上下文文件安装到当前项目。

**--agents** _LIST_
> 指定目标 agent 环境（例如 `all`，或逗号分隔的子集）。

**--dry-run**
> 预览 **init** 的变更而不写入文件。

**doctor**
> 校验已安装的 agent 指引及集成健康状况。

**--mcp**
> 在标准输入/输出上运行 Model Context Protocol 服务器。

**validate-npm-package** _PACKAGE_
> 在将某个 npm 包添加为依赖前对其进行检查。

# CONFIGURATION

VibeRaven 将项目本地状态写入 **.viberaven/** 目录，包括 **production-context.md**、**agent-context.md** 以及可选的用于机器可读生产就绪数据的 **prp.json**。已安装的规则被包裹在 **<!-- VIBERAVEN:START -->** … **<!-- VIBERAVEN:END -->** 标记中，因此可以干净地更新或移除。

# CAVEATS

开源的 CLI 和 Studio 均为本地优先，基本使用无需登录，但特定提供商的证明（Supabase、Vercel、账单、认证）仍依赖仓库之外的凭据和控制台。VibeRaven 用于增强 agent 行为；它不能替代测试、CI 或人工的生产环境验证。

# HISTORY

VibeRaven 由 **Ohad**（ohad6k）于 2026 年创建，作为主要由 AI agent 构建的应用的任务控制工具，其公开仓库充当 agent 发现与安装入口。

# SEE ALSO

[claude](/man/claude)(1), [codex](/man/codex)(1), [npx](/man/npx)(1), [git](/man/git)(1)

# RESOURCES

```[Source code](https://github.com/ohad6k/VibeRaven)```

```[Homepage](https://viberaven.dev)```

<!-- verified: 2026-06-30 -->
