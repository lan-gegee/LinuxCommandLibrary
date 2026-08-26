# TAGLINE

支持可插拔 LLM provider 的极简终端 AI 编码智能体

# TLDR

在当前目录**启动智能体**

```keen```

通过 npx **免全局安装运行**

```npx keen-code```

**查看已安装的版本**

```keen --version```

会话中途**切换到其他 LLM provider**（在智能体内）

```/model```

**调整扩展推理力度等级**（在智能体内）

```/thinking```

接近上下文上限时**压缩对话**（在智能体内）

```/compact```

# SYNOPSIS

**keen** [_options_]

# DESCRIPTION

**keen**（以 **keen-code** npm 软件包发布）是一个用 Go 编写的小型基于终端的编码智能体。它将 AI 模型视为通用后端，并刻意保持极小的工具面：**read_file**、**write_file**、**edit_file**、**glob**、**grep** 和 **bash**。这就是该智能体用于浏览、编辑和运行代码的全部工具箱，其设计理念是简洁优先于功能广度。

不带参数调用 **keen** 会进入一个以当前工作目录为锚点的交互式会话。智能体会读取文件、就地编辑文件，并代你执行 shell 命令，通过终端与你对话。诸如 **/model**、**/thinking** 和 **/compact** 之类的斜杠命令可以在不离开会话的情况下控制 provider 选择、推理深度和上下文压缩。

该智能体与 provider 无关：它可以驱动 Anthropic、OpenAI（包括 ChatGPT OAuth）、Google AI（Gemini）、DeepSeek、Kimi、GLM、MiniMax、Codex 以及 Go 移植版的 OpenCode。切换 provider 在运行时通过 **/model** 完成，而不是通过单独的 CLI 标志，因此一次 **keen** 安装即可覆盖所有受支持的后端。

该项目的一个显著特点是：据称仓库中的每一行代码都由 AI 智能体编写，提示词和设计决策都归档在 **.ai-interactions/** 下。

# PARAMETERS

**--version**

> 打印 **keen-code** 版本并退出。也可以通过 **npx keen-code --version** 使用，适合跳过全局安装的用户。

# SLASH COMMANDS

**/model**

> 在已配置的 LLM provider 之间切换，无需重启会话。

**/thinking**

> 为支持的 provider 调整扩展推理力度等级。

**/compact**

> 当上下文窗口占满时压缩正在进行的对话。

# INSTALLATION

**通过 npm 安装**（推荐，会将 **keen** 二进制安装到 **PATH** 中）：

```
npm install -g keen-code
```

**通过安装脚本安装**（把二进制放到 **/usr/local/bin** 或 **$HOME/.local/bin**）：

```
curl -fsSL https://raw.githubusercontent.com/mochow13/keen-code/main/scripts/install.sh | bash
```

**一次性运行**而无需安装：

```
npx keen-code
```

# CAVEATS

六工具的极简设计是有意为之，这意味着 **keen** 不提供其他智能体内置的专用辅助工具（web 抓取、结构化规划工具、子智能体）。依赖这些特性的工作流可能需要换用其他智能体。

每个 LLM provider 都必须配置自己的凭据。费用和速率限制会计入当前通过 **/model** 选定的 provider。

# HISTORY

**keen-code** 是 2026 年的项目（截至 2026 年 6 月 2 日最新版本为 v0.20.3），由 GitHub 上的 **mochow13** 以 **MIT** 许可证发布。它是受 Claude Code、Codex 和 OpenCode 启发的极简主义终端编码智能体浪潮的一部分，以限制工具面和完全由 AI 编写代码而与众不同。

# SEE ALSO

[claude](/man/claude)(1), [codex](/man/codex)(1), [paseo](/man/paseo)(1)
