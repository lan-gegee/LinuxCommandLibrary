# TAGLINE

AI 编程代理访问过什么的本地取证报告

# TLDR

**扫描**本地 Claude Code 会话日志并打开 HTML 报告

```npx confessor```

扫描**聊天导出** zip 或目录

```npx confessor [~/Downloads/chatgpt-export.zip]
npx confessor [~/Downloads/claude-export.zip]```

将报告写入指定**路径**并跳过打开浏览器

```npx confessor --out [report.html] --no-open```

输出 **JSON** 并在高严重性发现时使 CI 失败

```npx confessor --json --fail-on [high]```

# SYNOPSIS

**confessor** [_options_] [_export-path_]

# DESCRIPTION

**confessor** 从磁盘上已有的日志中重建 AI 编程代理的行为轨迹——主要是 **~/.claude/projects** 下的 Claude Code 会话 JSONL——并生成一份离线 HTML 报告。它会列出被读取或写入的文件、进入工具结果的密钥、网络或 MCP 出口，以及**暴露路径**：同一会话中先有敏感读取、随后出现对外活动的情况。

同一引擎还能扫描 ChatGPT、Claude.ai 和 Gemini Takeout 导出数据中的粘贴密钥和敏感话题。检测基于规则模式（不使用机器学习）。密钥在存储前会被遮蔽。该工具自身**零网络调用**，除 Node 之外**零运行时依赖**。

# PARAMETERS

**--out** _file_
> 报告输出路径（默认 HTML 文件名）

**--no-open**
> 不在浏览器中打开报告

**--json**
> 机器可读输出

**--quiet**
> 减少日志输出

**--fail-on** _critical_|_high_|_medium_
> 若发现达到或超过指定严重级别则以非零值退出（用于 CI）

# CAVEATS

暴露路径只是调查线索，并非泄密证据。代理行为重建目前仅针对 Claude Code 日志格式；其他代理可能无法完全支持。仅限事后追溯——不会拦截实时会话。

# SEE ALSO

[claude](/man/claude)(1)

# RESOURCES

```[Source code](https://github.com/ninjahawk/Confessor)```

```[Homepage](https://ninjahawk.github.io/Confessor/)```

<!-- verified: 2026-07-14 -->
