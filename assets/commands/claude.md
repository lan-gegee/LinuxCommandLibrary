# TAGLINE

AI 驱动的智能体编程助手 CLI

# TLDR

在当前目录**启动交互式会话**

```claude```

**以初始提示词启动**

```claude "[prompt]"```

**执行一次性命令**后退出（非交互式）

```claude -p "[prompt]"```

**继续最近一次**对话

```claude -c```

按 ID 或名称**恢复特定会话**

```claude -r "[session_id]" "[prompt]"```

向 Claude **管道输入**

```cat [file.txt] | claude -p "[analyze this code]"```

**以 JSON 输出响应**

```claude -p "[prompt]" --output-format json```

**指定其他模型**

```claude --model [opus]```

# SYNOPSIS

**claude** [_options_] [_prompt_]

**claude** **update**

**claude** **mcp** [_subcommand_]

# PARAMETERS

**-p**, **--print**
> 打印模式：处理提示词后退出，不进入交互式会话。

**-c**, **--continue**
> 继续最近一次的对话。

**-r** _ID_, **--resume** _ID_
> 按会话 ID 或名称恢复特定对话。

**-v**, **--version**
> 显示版本信息。

**--model** _MODEL_
> 指定要使用的 Claude 模型（别名：sonnet、opus、haiku，或完整模型名称）。

**--max-turns** _N_
> 非交互模式下智能体轮次的最大数量。

**--max-budget-usd** _AMOUNT_
> API 调用的最大美元金额（仅限打印模式）。

**--output-format** _FORMAT_
> 输出格式：text、json 或 stream-json。

**--input-format** _FORMAT_
> 打印模式的输入格式。

**--tools** _TOOLS_
> 限制可用的内置工具（例如 "Bash,Edit,Read"）。

**--allowedTools** _TOOLS_
> 无需提示即可执行的工具。

**--disallowedTools** _TOOLS_
> 从上下文中移除的工具。

**--permission-mode** _MODE_
> 以指定的权限模式启动（例如 plan）。

**--system-prompt** _PROMPT_
> 替换整个默认系统提示词。

**--append-system-prompt** _PROMPT_
> 在默认提示词后追加额外指令。

**--add-dir** _PATHS_
> 添加额外的工作目录。

**--mcp-config** _FILE_
> 从 JSON 配置文件加载 MCP 服务器。

**--chrome**
> 启用 Chrome 浏览器集成。

**--ide**
> 启动时自动连接到 IDE。

**--remote**
> 在 claude.ai 上创建 Web 会话。

**--teleport**
> 在本地终端中恢复 Web 会话。

**--verbose**
> 启用详细日志输出。

**--debug** _FILTER_
> 启用调试模式，可选过滤条件。

**--dangerously-skip-permissions**
> 跳过权限提示（在受信任的环境中使用时须谨慎）。

**--help**
> 显示帮助信息。

# SLASH COMMANDS

**/init**
> 初始化并为项目生成 CLAUDE.md 文件。

**/clear**
> 重置对话上下文。

**/model**
> 在可用模型之间切换。

**/compact**
> 手动压缩对话历史。

**/cost**
> 显示会话费用信息。

**/help**
> 显示可用命令和选项。

# DESCRIPTION

**Claude Code** 是 Anthropic 官方用于与 Claude AI 交互的命令行界面。它提供一个智能体编程助手，可以直接在你的开发环境中读取、写入和执行代码。

该工具有两种主要模式：适用于持续对话长时间会话的交互模式，以及适用于脚本化自动化和一次性命令的打印模式（-p）。Claude 可以浏览代码库、编辑文件、运行 shell 命令，并执行复杂的多步骤开发任务。

Claude Code 与你的终端环境集成，通过文件访问和命令执行来理解项目上下文。它跨会话维护对话历史，让你可以恢复之前的讨论。该工具支持从其他命令管道传入输入，并输出结构化的 JSON 以便与其他工具集成。

特殊语法包括用 **@** 引用文件，以及用 **!** 直接执行 shell 命令。CLI 支持 MCP（Model Context Protocol，模型上下文协议）服务器以扩展能力，并可连接 IDE 和 Chrome 以增强集成。

# CONFIGURATION

**CLAUDE.md**
> 自动从工作目录加载的项目级指令与上下文。

**~/.claude/settings.json**
> 全局用户设置，包括权限、允许的工具和默认行为。

**.claude/settings.json**
> 项目级的权限和工具配置。

# CAVEATS

需要通过 Anthropic API 密钥或有效的 Claude 订阅进行身份验证。Claude 执行的命令以你的用户权限运行。**--dangerously-skip-permissions** 选项会绕过安全提示，只应在受控的 CI/CD 环境中使用。会话持久化和 API 费用取决于实际使用情况。

# HISTORY

Claude Code 由 **Anthropic** 于 **2025 年 2 月**发布，是其开发者工具计划的一部分。它代表着向 AI 辅助开发工作流的转变，基于 Claude 的代码理解能力提供智能体的终端体验。该工具持续活跃开发，定期更新添加子代理、Chrome 集成和 MCP 支持等功能。

# INSTALL

```aur: yay -S claude```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[copilot](/man/copilot)(1), [gh](/man/gh)(1), [git](/man/git)(1)
