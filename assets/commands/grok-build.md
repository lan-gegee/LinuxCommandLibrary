# TAGLINE

xAI 官方的终端原生智能体编程 CLI

# TLDR

在当前目录**启动交互式会话**

```grok```

**执行一次性命令**后退出（无头模式）

```grok -p "[prompt]"```

**流式输出结构化结果**以便脚本处理

```grok -p "[prompt]" --output-format streaming-json```

**检查 Grok 在当前目录发现了什么**

```grok inspect```

在无头模式下**选择特定模型**

```grok -m [model-id]```

通过环境变量**提供 xAI 凭据**

```export GROK_CODE_XAI_API_KEY="xai-..."```

# SYNOPSIS

**grok** [_options_] [_prompt_]

**grok** **inspect**

# PARAMETERS

**-p**, **--prompt** _text_
> 以无头模式运行：执行单个提示词后退出。适用于脚本、CI/CD 管道、GitHub Actions 或定时任务中。

**-m**, **--model** _model_
> 选择本次会话使用的模型。

**--output-format** _format_
> 设置响应格式（例如 _streaming-json_），用于无头模式下机器可读的输出。

# DESCRIPTION

**Grok Build** 是 xAI 的第一方命令行编码智能体，面向专业软件工程、应用开发和工作流自动化而构建。默认情况下它以终端 TUI 形式运行，也可以以无头模式进行自动化操作。

它内置 **plan 模式**：智能体提出完整计划，可在任何执行开始前被批准、评论或重写。计划获批后，每处修改都以清晰的 diff 呈现。对于较大的任务，Grok Build 会把工作委派给**并行子智能体**，还可以选择让它们在各自的 git worktree 中启动。

Grok Build 是 **ACP 优先**的，并且刻意兼容 Anthropic Skills 格式，因此为 Claude Code 编写的技能几乎无需修改即可使用。它开箱即支持 **MCP**，现有的服务器（数据库连接器、GitHub 集成、自定义工具）无需改动即可接入。

# CONFIGURATION

**AGENTS.md**
> 项目级智能体指令，自动从工作目录加载。与 Claude Code 的 CLAUDE.md 兼容。

**GROK_CODE_XAI_API_KEY**
> 保存 xAI API 密钥的环境变量。在未通过浏览器流程认证时使用。

**自定义模型配置**
> 可以在用户配置中用模型 id、基础 URL、显示名称和环境变量键引用来定义模型，然后将其设为默认或在 TUI 中通过 _/model_ 选择。

# SLASH COMMANDS

**/model** _name_
> 在 TUI 内切换当前使用的模型。

# CAVEATS

Grok Build 目前处于**早期测试（beta）阶段**，仅向 **SuperGrok Heavy** 订阅者开放。请预期存在粗糙之处：部分命令尚不可用、错误处理不完整，子智能体协调偶尔出现回退。对于生产环境的 CI/CD 管道，在 Grok Build 正式发布前建议使用成熟工具；用于探索和业余项目则没有问题。首次启动会打开浏览器进行身份验证，除非已通过环境变量设置了 API 密钥。

# HISTORY

xAI 于 **2026 年 5 月**以早期测试形式发布了 **Grok Build**，与 Claude Code 和 Codex CLI 一同进入智能体 CLI 领域。它通过一条 curl 管道 bash 脚本（_x.ai/cli/install.sh_）安装，自带 plan 模式、集成 worktree 的并行子智能体、MCP 支持和 Anthropic-Skills 兼容性，定位为其基于 Web 的 Grok 编程工具在终端原生的对应产品。

# INSTALL

```zypper: sudo zypper install grok-build```

```nix: nix profile install nixpkgs#grok-build```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grok](/man/grok)(1), [claude](/man/claude)(1), [copilot](/man/copilot)(1), [gh](/man/gh)(1)
