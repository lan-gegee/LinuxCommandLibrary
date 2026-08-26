# TAGLINE

AI 驱动的终端编码助手

# TLDR

**在当前目录启动交互式会话**

```copilot```

**以初始提示启动**

```copilot "[prompt]"```

**运行一次性命令**后退出（非交互）

```copilot -p "[prompt]"```

**继续最近一次**对话

```copilot --continue```

**按 ID 恢复指定会话**

```copilot --resume```

**在提示中引用特定文件**

```copilot "Explain @[path/to/file.js]"```

**直接运行 shell 命令**而不调用模型

```copilot "![git status]"```

# SYNOPSIS

**copilot** [_options_] [_prompt_]

# PARAMETERS

**-p**, **--prompt**
> 打印模式：处理提示后退出，不进入交互式会话。

**--continue**
> 继续最近关闭的本地会话。

**--resume**
> 循环切换并恢复本地与远程的交互式会话。

**--allow-all-paths**
> 对 shell 命令禁用路径校验。

**--allow-all-urls**
> 对外部访问禁用 URL 校验。

**--allow-url** _domain_
> 预先批准特定域名的网络访问（例如 --allow-url github.com）。

**--agent** _agent-name_
> 指定会话要使用的自定义 agent。

# SLASH COMMANDS

**/login**
> 登录 GitHub 进行身份验证。

**/add-dir** _path_
> 手动添加受信任目录。

**/cwd** _path_
> 切换工作目录而无需结束会话。

**/delegate** _prompt_
> 将当前会话移交给 GitHub 上的 Copilot 编码 agent。

**/agent**
> 从可用的自定义 agent 中选择。

**/model**
> 从可用模型中选择（Claude Sonnet 4.5、Claude Sonnet 4、GPT-5、GPT-5 mini、GPT-4.1）。

**/mcp add**
> 添加新的 MCP 服务器。

**/usage**
> 查看会话统计和 token 用量明细。

**/context**
> 显示当前 token 使用情况的可视化概览。

**/compact**
> 手动压缩对话历史。

**/feedback**
> 提交反馈、缺陷报告或功能建议。

**?**
> 显示可用的命令和选项。

# DESCRIPTION

**GitHub Copilot CLI** 将 AI 驱动的编码辅助直接带到你的终端，让你能用自然语言对话来构建、调试和理解代码。它以 agent 式编码助手的形态工作，能够在你的开发环境中读取、编写和执行代码。

该工具有两种主要模式：用于持续对话的长时间交互模式，以及用于脚本自动化和一次性命令的程序化模式（-p）。Copilot 可以浏览代码库、编辑文件、运行 shell 命令，并完成复杂的多步骤开发任务。

特殊语法包括用 **@** 引用文件（例如 @src/app.js），以及用 **!** 直接执行 shell 命令而不调用模型。该 CLI 支持路径的 Tab 补全，并在多个会话之间保留对话历史。

# CAVEATS

需要有效的 **GitHub Copilot 订阅**。组织或企业管理员可以禁用 Copilot CLI 的访问。**--allow-all-paths** 和 **--allow-all-urls** 标志会绕过安全提示，应谨慎使用。对 PowerShell 的原生 Windows 支持仍属实验性；推荐使用 WSL。

# HISTORY

GitHub Copilot CLI 由 **GitHub** 于 **2024** 年发布，是其 Copilot AI 助手的延伸。它最初作为 shell 命令建议工具推出，在 **2025** 年演变为完整的 agent 式编码助手。到 **2026 年 1 月**，它增加了增强的 agent、上下文管理、MCP 服务器集成，以及扩展的模型选择，包括 GPT-5 和 Claude Sonnet 4.5。

# INSTALL

```brew: brew install copilot```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gh](/man/gh)(1), [claude](/man/claude)(1), [git](/man/git)(1)

# RESOURCES

```[Source code](https://github.com/github/copilot-cli)```

```[Documentation](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/use-copilot-cli)```

<!-- verified: 2026-06-23 -->
