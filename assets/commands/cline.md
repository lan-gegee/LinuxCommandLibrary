# TAGLINE

面向终端的模型无关 AI 编程代理

# TLDR

在当前目录**启动交互式会话**

```cline```

**带提示词运行任务**

```cline "[fix the login bug]"```

**以完全自主模式运行**（无交互式界面）

```cline -y "[refactor auth module]"```

与 AI 提供商**完成身份验证设置**

```cline auth -p [anthropic] -k [sk-ant-api-xxxxx]```

**以计划模式运行**，在执行前预览变更

```cline -p "[add unit tests for auth]"```

在无头模式下向 cline **管道传入上下文**

```cat [error.log] | cline -y "[explain these errors]"```

# SYNOPSIS

**cline** [_options_] [_prompt_]

**cline** **auth** [_options_]

**cline** **config**

**cline** **history** [_options_]

**cline** **update**

# PARAMETERS

**-y**, **--yolo**
> 以完全自主模式运行，没有交互式界面。输出流式写入 stdout。

**-a**, **--act**
> 以执行模式运行（直接实施变更）。

**-p**, **--plan**
> 以计划模式运行（先预览变更再执行）。

**-m**, **--model** _MODEL_
> 指定要使用的模型。

**-i**, **--images** _PATHS_
> 在提示词中附加图片文件。

**--json**
> 流式输出结构化 JSON，便于程序化处理。

**--thinking**
> 启用扩展思考模式。

**--timeout** _SECONDS_
> 为任务设置超时时间。

**--continue**
> 继续最近的任务。

**--acp**
> 以符合 ACP（Agent Client Protocol）的代理身份运行，用于编辑器集成。

**--config** _PATH_
> 自定义配置目录。

**-c**, **--cwd** _PATH_
> 设置工作目录。

**-v**, **--verbose**
> 显示详细输出。

**--help**
> 显示帮助信息。

# SUBCOMMANDS

**auth**
> 设置与 AI 提供商的身份验证。用 **-p** 指定提供商、**-k** 指定 API 密钥、**-m** 指定模型 ID、**-b** 指定基础 URL。

**config**
> 用于设置、规则、工作流和钩子的交互式配置界面。

**history**
> 浏览任务历史。用 **-n** 限制数量、**-p** 指定页码。

**update**
> 安装最新版本的 CLI。

**version**
> 显示已安装的版本号。

# DESCRIPTION

**cline** 是一个在终端中工作的 AI 编程代理，支持多种 AI 模型提供商，包括 OpenAI、Anthropic、Google、AWS Bedrock、Ollama 以及任何 OpenAI 兼容的 API。它可以读写文件、执行终端命令，并自主完成多步骤开发任务。

该工具有两种主要模式：交互模式（在终端中运行时的默认模式）和无头模式（通过 **-y**/**--yolo** 或管道输入/输出激活）。无头模式专为自动化、CI/CD 流水线和脚本设计。

Cline 起源于一个 VS Code 扩展，后来扩展出 CLI 接口，使其可以从任何终端环境使用。它采用模型无关架构，允许用户选择偏好的 AI 后端。**--acp** 选项启用 Agent Client Protocol，可与 JetBrains、Zed、Neovim 和 Emacs 等编辑器集成。

# CAVEATS

云端模型提供商需要 API 密钥。通过 Ollama 使用本地模型需要单独安装并下载模型。token 用量和 API 费用因提供商和模型而异。首次使用前请运行 **cline auth** 配置提供商。

# HISTORY

Cline 最初于 **2024 年**以 **Claude Dev** 之名作为 Visual Studio Code 扩展创建，后更名为 Cline 以体现其模型无关的设计。它迅速成长为最受欢迎的开源 AI 编程工具之一。**Cline CLI 2.0** 于 **2026 年 2 月**发布，围绕终端优先的工作流重建了整个代理，增加了无头模式和 ACP 支持。

# INSTALL

```brew: brew install cline```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[claude](/man/claude)(1), [aider](/man/aider)(1), [codex](/man/codex)(1), [copilot](/man/copilot)(1)
