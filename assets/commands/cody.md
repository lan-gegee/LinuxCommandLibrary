# TAGLINE

Sourcegraph Cody AI 编码助手 CLI

# TLDR

**通过网页浏览器登录**

```cody auth login --web```

**发送聊天消息**

```cody chat -m "[Explain React hooks]"```

**就本地文件提问**

```cody chat --context-file [src/app.ts] -m "[Are there code smells here?]"```

**使用远程仓库作为上下文**

```cody chat --context-repo [github.com/owner/repo] -m "[question]"```

**根据 git diff 生成提交信息**

```git diff | cody chat --stdin -m "Write a commit message for this diff"```

**查看身份验证状态**

```cody auth whoami```

# SYNOPSIS

**cody** _command_ [_options_]

# PARAMETERS

**-m**, **--message** _text_
> 要发送给 Cody 的消息。

**--context-file** _path_
> 将本地文件作为查询上下文一并纳入。

**--context-repo** _repository_
> 将远程仓库作为上下文纳入（例如 github.com/owner/repo）。

**--stdin**
> 从标准输入读取内容。

**--model** _model_
> 指定 LLM 模型（例如 claude-3.5-sonnet）。

**auth login** [**--web**]
> 与 Sourcegraph 进行身份验证。使用 **--web** 通过浏览器登录。

**auth logout**
> 登出并删除已存储的访问令牌。

**auth whoami**
> 显示当前身份验证状态和账户信息。

**chat** [**-m** _message_]
> 向 Cody AI 助手发送消息。

# DESCRIPTION

**cody** 是 Sourcegraph 的 Cody AI 编码助手的命令行接口。它让你在终端中使用与 Cody IDE 扩展相同的 AI 技术，直接从命令行完成代码理解、生成和分析。

该 CLI 支持结合本地文件（通过 **--context-file**）或远程仓库（通过 **--context-repo**）进行上下文查询，使 Cody 能根据你的代码库给出更准确、更相关的回答。

标准输入集成可实现强大的工作流自动化：将 git diff 管道传入以生成提交信息、将代码输出传入以进行分析，或将日志传入以获得调试辅助。多种输入方式可在一次查询中组合使用。

身份验证凭据安全地存储在操作系统的凭据管理器中。也可以改用 **SRC_ENDPOINT** 和 **SRC_ACCESS_TOKEN** 环境变量，以便在 CI/CD 流水线或临时环境中使用。

# CAVEATS

需要 Node.js v20 或更新版本。该 CLI 目前标记为实验性功能，且需要 Sourcegraph Enterprise 账户。自 **2025 年 7 月**起，Cody Free 和 Pro 方案已停止提供，官方引导用户转向 Amp（ampcode.com）作为替代。

# HISTORY

Cody 由 **Sourcegraph** 开发，该公司成立于 **2013 年**，专注于代码智能与搜索工具。Cody 于 **2023 年**推出，是一款 AI 编码助手，借助 Sourcegraph 的代码图技术实现更强的上下文感知能力。CLI 的发布是为了补充 IDE 扩展，支持基于终端和脚本的 AI 辅助工作流。

# SEE ALSO

[claude](/man/claude)(1), [gh](/man/gh)(1), [copilot](/man/copilot)(1)
