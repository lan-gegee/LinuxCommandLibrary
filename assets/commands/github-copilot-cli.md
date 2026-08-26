# TAGLINE

面向 shell 命令的 AI 命令行助手

# TLDR

**启动交互式 Copilot 智能体**

```gh copilot```

以非交互方式运行一次性提示词

```gh copilot -p "[how do I rebase onto main?]"```

**选择特定模型**

```gh copilot --model [claude-sonnet-4.5]```

**移除内置的 Copilot 二进制文件**

```gh copilot --remove```

# SYNOPSIS

**gh copilot** [_options_] [_prompt_]

# PARAMETERS

**-p**, **--prompt** _TEXT_
> 运行一次性提示词并输出响应。

**--model** _MODEL_
> 选择 Copilot 使用的 LLM 模型。

**--allow-tool** _TOOL_, **--deny-tool** _TOOL_, **--allow-all-tools**
> 针对智能体内置工具的逐工具执行策略。

**--banner**
> 强制显示启动横幅（在脚本中很有用）。

**--experimental**
> 启用实验性功能。

**--remove**
> 卸载由 **gh** 管理的独立 **copilot** 二进制文件。

# SLASH COMMANDS (interactive mode)

**/login**
> 进行 GitHub Copilot 身份验证。

**/model**
> 切换当前使用的模型。

**/lsp**
> 配置语言服务器协议（LSP）集成。

**/feedback**
> 向 GitHub 发送反馈。

# DESCRIPTION

**gh copilot**（此前是带有 **suggest** 和 **explain** 子命令的扩展）现在是一个轻量启动器，用于下载并运行独立的 **copilot** 二进制文件——GitHub 的智能体编程助手。旧的 **suggest**/**explain**/**config**/**alias** 子命令已被弃用；请直接调用 **copilot** 进入交互式智能体会话，或在脚本中通过 **-p** 使用。

该工具支持多种 shell 和命令行工具，提供可复制或直接执行的交互式建议。

# CAVEATS

需要 GitHub Copilot 订阅。需要联网。建议不一定总是准确，执行前请仔细检查命令。注意命令数据的隐私问题。

# HISTORY

GitHub Copilot for code 取得成功后，GitHub Copilot CLI 作为 GitHub CLI 扩展发布。它将 AI 辅助从代码编辑器延伸到了命令行。

# INSTALL

```nix: nix profile install nixpkgs#github-copilot-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gh](/man/gh)(1), [tldr](/man/tldr)(1), [man](/man/man)(1)
