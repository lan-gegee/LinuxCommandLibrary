# TAGLINE

获取 AI 编程助手更新日志的工具

# TLDR

**显示最新的 Claude Code 更新日志**

```aic claude```

**列出一个工具的所有可用版本**

```aic codex --list```

**显示指定版本**的更新日志

```aic gemini --version [0.1.0]```

**以 JSON 格式输出**更新日志

```aic claude --json```

**显示最近 24 小时内的所有发布**

```aic latest```

**显示所有受跟踪工具的状态概览**

```aic status```

# SYNOPSIS

**aic** [_command_] [_options_]

# PARAMETERS

**-j**, **--json**
> 以 JSON 格式输出

**-m**, **--md**
> 以 Markdown 格式输出

**-l**, **--list**
> 列出所有可用版本

**-p**, **--pick**
> 交互式版本选择器

**--version** _ver_
> 获取指定版本

**-w**, **--web**
> 在浏览器中打开更新日志

**-h**, **--help**
> 显示帮助文档

# DESCRIPTION

**aic** 是一个命令行工具，用于获取并展示流行 AI 编程助手的发行说明和更新日志。它将来自多个来源的更新日志信息聚合到统一的界面中，支持 Claude Code、Codex CLI、OpenCode、Gemini CLI、Copilot CLI、Kimi CLI、Qwen Code 和 Goose 等工具。

aic 用 Go 编写，支持多种输出格式（文本、JSON、Markdown）、交互式版本选择、浏览器集成、已安装版本检测，以及一个全面的状态仪表板，可展示所有受跟踪工具的发布频率。

# CAVEATS

需要联网才能从上游来源获取更新日志。可用工具及其更新日志格式取决于各项目的发布内容。

# SEE ALSO

[gh](/man/gh)(1)
