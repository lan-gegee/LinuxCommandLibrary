# TAGLINE

Augment Code 出品的 AI 智能体编码 CLI

# TLDR

在当前目录**启动交互式会话**

```auggie```

**以初始提示词**启动

```auggie "[prompt]"```

**运行一次性命令**并输出到 stdout

```auggie --print "[prompt]"```

**继续最近一次**对话

```auggie --continue```

按 ID **恢复指定会话**

```auggie --resume [session_id]```

**使用指定模型**

```auggie --model [sonnet4.5]```

**管道输入**并以非交互方式运行

```cat [file.txt] | auggie --print "[analyze this code]"```

本次会话**禁用特定工具**

```auggie --remove-tool [web-fetch]```

# SYNOPSIS

**auggie** [_options_] [_prompt_]

**auggie** **login** | **logout**

**auggie** **models** **list**

**auggie** **session** **list** | **continue** | **resume** [_id_] | **share**

**auggie** **mcp** **add** | **add-json** | **list** | **remove**

**auggie** **tools** **list** | **add** | **remove**

**auggie** **rules** **list**

**auggie** **command** [_command-name_] | **help**

**auggie** **plugin** **marketplace** **add** | **list** | **update** | **remove**

**auggie** **plugin** **list** | **enable** | **disable** | **reload**

# PARAMETERS

**--print**, **-p**
> 运行一次提示词并将结果打印到 stdout 后退出。适合 CI/CD 流水线和脚本自动化。

**--quiet**
> 只返回最终输出，抑制中间消息和进度指示。

**--compact**
> 将工具调用、结果和响应压缩为单行输出。

**--output-format** _FORMAT_
> print 模式的输出格式（如 json）。

**--continue**, **-c**
> 恢复最近一次对话会话。

**--resume** _ID_
> 按 ID 或 ID 前缀恢复指定会话。

**-f**
> 将会话列表过滤为仅当前工作空间。

**--dont-save-session**
> 跳过保存本次会话的对话历史。

**--delete-saved-sessions**
> 删除所有已保存的会话。

**--model** _NAME_
> 选择要使用的模型。支持短名称（如 sonnet4.5）。

**--instruction** _TEXT_
> 为交互模式提供初始指令。

**--instruction-file** _PATH_
> 从文件加载初始指令。

**--workspace-root** _PATH_
> 设置工作空间根目录。

**--rules** _PATH_
> 从文件追加额外规则。

**--remove-tool** _NAME_
> 本次会话禁用特定工具。可重复使用。

**--permission** _SETTING_
> 在运行时配置工具权限。

**--max-turns** _N_
> 限制 print 模式下智能体的迭代次数。

**--enhance-prompt**
> 发送给智能体之前自动优化提示词（非交互模式）。

**--image** _PATH_
> 在提示词中附加图片。

**--shell** _SHELL_
> 设置用于执行命令的 Shell。

**--startup-script** _PATH_
> 指定 Shell 启动脚本。

**--mcp**
> 将 auggie 作为 MCP 工具服务器运行。

**--mcp-config** _PATH_
> 从 JSON 文件或内联 JSON 字符串加载 MCP 服务器配置。

**--mcp-auto-workspace**
> 在 MCP 模式下启用工作空间自动发现。

**-w** _PATH_
> 指定要预索引的工作空间目录。

**--log-file** _PATH_
> 在 MCP 模式下启用错误日志写入文件（默认：/tmp/augment-log.txt）。

**--acp**
> 启用 Agent Client Protocol 支持，以便与外部编辑器集成。

**--allow-indexing**
> 允许在 ACP 模式下进行代码库索引。

**--augment-session-json** _JSON_
> 以 JSON 形式提供认证会话。

**--help**, **-h**
> 显示帮助信息。

**--version**
> 显示已安装的版本。

# DESCRIPTION

**auggie** 是 Augment Code 打造的基于终端的 AI 编码智能体。它利用 Augment 的 Context Engine 对代码库进行深层语义理解，超越简单的文本匹配，能够把握大型仓库中的项目结构、依赖关系和代码之间的关联。

该工具有两种主要运行模式。交互模式提供完整的 TUI，具备实时流式输出、可视化进度指示、Vim 风格按键绑定以及可观察的工具执行过程。非交互模式（--print）面向脚本化自动化，适用于 CI/CD 流水线、代码评审流程和无头环境。

auggie 支持面向专项任务的子智能体，如安全审计、测试编写和数据分析，并可并行执行多个智能体。会话是持久化的且可恢复，允许跨终端会话延续对话，或通过 /share 命令与队友共享。

CLI 集成了 Model Context Protocol（MCP）服务器，可扩展连接 GitHub、Linear 和 Jira 等服务。它自身也可以作为 MCP 服务器运行，从而与其他工具集成。支持多个 AI 模型，用户可通过 --model 标志或 TUI 中的 Option+M 快捷键切换模型。

自定义斜杠命令可在 .augment/commands/ 或 ~/.augment/commands/ 目录中以 markdown 文件形式定义，为代码评审、bug 修复、安全分析等任务提供可复用的提示词。~/.augment/rules/ 下的用户级规则和工作区规则可针对每个项目定制智能体行为。

插件系统允许通过市场扩展功能；智能体技能框架则遵循 agentskills.io 规范，从 SKILL.md 文件加载专业领域知识。

# CONFIGURATION

**~/.augment/settings.json**
> 全局用户设置，包括 MCP 服务器配置、工具权限、模型偏好、自动更新行为和默认 Shell。

**.augment/commands/**
> 项目级自定义斜杠命令，以带 frontmatter 的 markdown 文件存放。

**~/.augment/commands/**
> 用户级自定义斜杠命令，在所有项目中可用。

**~/.augment/rules/**
> 用户级规则，用于全局定制智能体行为。

**.augment/.agents/**
> 通过 SKILL.md 和 AGENTS.md 文件发现技能与智能体的目录。

# CAVEATS

需要 Node.js 22 或更高版本。首次使用前必须通过 auggie login 完成认证，且需要有效的 Augment 订阅。CLI 默认自动更新；可通过 autoUpdate 设置或 AUGMENT_DISABLE_AUTO_UPDATE 环境变量禁用。本软件为专有软件，采用 Augment Computing, Inc. 的自定义许可证授权。

# HISTORY

**Augment Code** 于 **2025 年 7 月 31 日**宣布 **auggie** 并以 beta 版上线，企业客户即刻可用，团队和个人用户分阶段开放。GitHub 仓库创建于 **2025 年 9 月**。到 **0.7.0** 版时，CLI 去掉了 beta 标签并正式发布。开发节奏很快，MCP 服务器支持、Agent Client Protocol 集成、会话共享、并行工具调用、插件市场和智能体技能等特性在多次发布中陆续加入。该工具是 Augment Code 更大平台的一部分，平台还包括 VS Code 和 JetBrains IDE 扩展。

# SEE ALSO

[claude](/man/claude)(1), [copilot](/man/copilot)(1), [aider](/man/aider)(1), [codex](/man/codex)(1), [opencode](/man/opencode)(1), [grok](/man/grok)(1)
