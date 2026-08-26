# TAGLINE

面向 AI 编程助手的成本与 token 可观测性仪表板

# TLDR

为最近 7 天**启动交互式仪表板**

```codeburn```

一览**今日用量**

```codeburn today```

**显示本月用量**

```codeburn month```

**生成滚动 30 天报告**

```codeburn report -p 30days```

**筛选单一提供商**（claude、codex、cursor、copilot 等）

```codeburn report --provider [claude]```

以 JSON 格式**导出原始数据**

```codeburn export --format [json] --from [2026-01-01] --to [2026-01-31]```

**发现浪费模式**并提供可直接复制的修复方法

```codeburn optimize```

通过 npx **免安装运行**

```npx codeburn today```

# SYNOPSIS

**codeburn** [_command_] [_options_]

# COMMANDS

**(default)**
> 启动交互式 TUI 仪表板（最近 7 天）。

**today**
> 显示今天的 token/成本/活动指标。

**month**
> 显示当月的指标。

**report**
> 详细文本报告；可用 **-p** 选择时间范围。

**status**
> 汇总今天与本月的单行摘要。

**export**
> 将一个或多个时间段的数据导出为 CSV 或 JSON。

**optimize**
> 扫描会话中的 11 种已知浪费模式并打印修复建议。

**compare**
> 跨模型的性能/成本并排比较。

**currency** [_CODE_]
> 设置、显示或重置显示货币（ISO 4217）。

**menubar**
> 安装 macOS 原生菜单栏伴侣应用。

# PARAMETERS

**--provider** _NAME_
> 按提供商筛选：_claude_、_codex_、_cursor_、_opencode_、_pi_、_copilot_。

**--project** _NAME_
> 按子串匹配包含某个项目（可重复）。

**--exclude** _NAME_
> 排除某个项目（可重复）。

**--format** _TYPE_
> 非交互命令的输出格式：_table_ 或 _json_。

**--from** _YYYY-MM-DD_
> 自定义窗口的开始日期。

**--to** _YYYY-MM-DD_
> 自定义窗口的结束日期。

**--refresh** _SECONDS_
> 仪表板的自动刷新间隔（默认 30，设为 0 表示禁用）。

**-p** _PERIOD_
> **report**/**optimize** 的时间范围：_today_、_week_、_30days_、_all_。

# DASHBOARD KEYS

**1–5**
> 在 Today / 7 Days / 30 Days / Month / All Time 之间切换。

**c**
> 打开模型比较视图。

**p**
> 循环切换提供商。

**o**
> 跳转到 optimize 发现结果。

**b**
> 从 compare/optimize 返回。

**q**
> 退出。

# DESCRIPTION

**codeburn** 是一款本地分析工具，它读取你的 AI 编程助手已经写入磁盘的会话文件 — 包括 **Claude Code**、**Codex**、**Cursor**、**OpenCode**、**Pi** 和 **GitHub Copilot** — 并将其转化为成本、token 和活动明细。任何数据都不会上传：定价数据来自 **LiteLLM**，汇率来自 **Frankfurter**，所有分析均针对 _~/.claude/_、_~/.cursor/_ 等目录中的文件进行。

除了原始数字之外，**codeburn optimize** 还会检查你的智能体配置中是否存在 11 种常见浪费模式（过度宽松的 hook、闲置的 MCP 服务器、重复的系统提示词等），并打印可直接复制粘贴的修复方案。**menubar** 子命令会在 macOS 上安装一个小型原生应用，让当天的支出始终可见。

# CONFIGURATION

- **货币** — 全局存储并用于所有输出，例如 _codeburn currency GBP_、_codeburn currency --reset_。
- **提供商检测** — 根据磁盘上的会话目录自动进行；必要时可用 **--provider** 覆盖。

# CAVEATS

需要 **Node.js 20+**，并且你确实在本地使用过某个受支持的工具，因为仪表板只解析磁盘上的会话数据。成本数字依赖 LiteLLM 定价目录，对新发布的模型可能存在滞后。

# HISTORY

**codeburn** 由 **AgentSeal** 创建并以 MIT 许可证发布，灵感来自更早的 **ccusage** 工具。定价数据来自 LiteLLM；汇率来自 Frankfurter。

# INSTALL

```brew: brew install codeburn```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[claude](/man/claude)(1), [codex](/man/codex)(1)
