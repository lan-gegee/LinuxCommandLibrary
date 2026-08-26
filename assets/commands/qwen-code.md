# TAGLINE

阿里巴巴出品的 AI 智能体编程助手

# TLDR

**启动交互式会话**

```qwen```

**以无头模式和提示词运行**

```qwen -p "[explain this codebase]"```

在查询中**引用本地文件**

```qwen``` 然后 ```@[src/main.ts] [explain this file]```

**配置身份验证**

```qwen``` 然后 ```/auth```

**显示会话统计信息**

```qwen``` 然后 ```/stats```

**压缩对话历史以节省 token**

```qwen``` 然后 ```/compress```

# SYNOPSIS

**qwen** [_options_]

# PARAMETERS

**-p** _PROMPT_
> 以提供的提示词在无头模式下运行

# IN-SESSION COMMANDS

**/help**
> 显示可用命令

**/auth**
> 配置身份验证方式

**/clear**
> 清除对话历史

**/compress**
> 压缩历史以节省 token

**/stats**
> 显示当前会话信息

**/bug**
> 提交缺陷报告

**/exit**, **/quit**
> 退出应用程序

# KEYBOARD SHORTCUTS

**Ctrl+C**
> 取消当前操作

**Ctrl+D**
> 空行时退出

**Up/Down**
> 浏览命令历史

**@**_filepath_
> 在查询中引用本地文件

# DESCRIPTION

**Qwen Code** 是阿里巴巴推出的开源终端 AI 编程智能体，针对 Qwen3-Coder 模型优化。它借助智能体编程能力帮助开发者理解大型代码库、自动化繁琐工作并加快交付速度。

该项目使用 TypeScript 构建，从 Gemini CLI 分支而来，体验相似，但可接入任何支持 OpenAI completions API 的模型。功能包括 Skills、SubAgents 和用于完整智能体工作流的 Plan Mode。该工具支持超越普通上下文窗口的深度代码理解，以及 PR 处理、变基和格式化等工作流自动化。

身份验证方式包括 Qwen OAuth（每天 2000 次免费请求）或 OpenAI 兼容 API。另有面向 VS Code、Zed 和 JetBrains 的 IDE 集成。

# CAVEATS

需要通过 Qwen OAuth 或 OpenAI 兼容 API 密钥进行身份验证。可为自定义服务商设置环境变量 **OPENAI_API_KEY**、**OPENAI_BASE_URL** 和 **OPENAI_MODEL**。0.5.0 版本支持在单个终端中运行四个并发实例。

# HISTORY

Qwen Code 由 **阿里巴巴** 于 **2025 年 7 月**随 Qwen3-Coder 模型一同发布。旗舰模型为 Qwen3-Coder-480B-A35B-Instruct，这是一款 4800 亿参数、350 亿激活参数的混合专家（MoE）模型，原生支持 256K 上下文，外推后可达 1M token。该工具已在 GitHub 上开源。

# INSTALL

```pacman: sudo pacman -S qwen-code```

```brew: brew install qwen-code```

```nix: nix profile install nixpkgs#qwen-code```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gemini](/man/gemini)(1), [claude](/man/claude)(1), [opencode](/man/opencode)(1), [aider](/man/aider)(1)
