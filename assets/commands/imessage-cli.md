# TAGLINE

通过第三方 API 发送和管理 iMessage 的提供商中立 CLI

# TLDR

通过已配置的提供商**发送文本消息**

```imessage-cli send --provider blooio --to +15551234567 --text 'Hello'```

**列出可用提供商**及其能力

```imessage-cli provider list```

**保存命名连接**（凭据存入操作系统钥匙串）

```imessage-cli connection add support --provider blooio```

**使用已保存的连接发送**

```imessage-cli send --connection support --to +15551234567 --text 'Hello'```

**以机器可读的 JSON 输出进行发送演练**

```imessage-cli send --provider blooio --to +15551234567 --text 'Hello' --dry-run --json```

**显示 send 命令的代理输入模式**

```imessage-cli schema send --json```

**全局安装**（需要 Node.js 20.19+、22.13+ 或 24+）

```npm install --global imessage-cli```

# SYNOPSIS

**imessage-cli** \<command\> [_options_]

# DESCRIPTION

**imessage-cli** 是一个命令行界面，用于通过提供商中立的 API 进行 iMessage 风格的消息传递。它是 **imessage-sdk** 项目的一部分，面向本地用户和 AI 代理。它不直接与 Apple 的 Messages.app 或 iCloud 通信，而是经由官方内置的提供商（如 **blooio**、**photon** 和 **sendblue**）路由，每个提供商都需要各自的账户和凭据。

命令涵盖发送消息（文本、回复、附件）、读取会话和消息、表情回应、输入状态指示、附件下载以及特定于提供商的扩展功能。输入可以是命令行选项或经过校验的 JSON（**--input** / stdin）。使用 **--json** 时，成功结果输出到 stdout，结构化错误输出到 stderr，并为自动化提供稳定的退出码。

凭据可以作为命名连接存储在操作系统的凭据存储中（macOS 钥匙串、Windows 凭据管理器、Linux Secret Service），也可以通过环境变量提供，或作为一次性选项传入。对于当前进程，环境变量和选项值会覆盖已保存的连接，且不会被写回磁盘。实验性的本地签名 webhook 服务器（**webhook serve --experimental**）可以以 JSON Lines 格式发出规范化事件，供代理流水线使用。

# PARAMETERS

**send**
> 发送消息。常用选项：**--provider**、**--connection**、**--to**、**--conversation**、**--text**、**--reply-to**、**--image**、**--video**、**--file**、**--input**、**--dry-run**、**--json**。

**provider list** / **provider show** _name_
> 列出内置提供商，或显示某个提供商的规范化能力。

**connection add** / **list** / **show** / **doctor** / **remove**
> 管理命名保存的连接和基于钥匙串的凭据。

**schema** [_command_]
> 输出面向代理的输入模式。

**webhook serve**
> 实验性的本地签名 webhook 接收器（需要 **--experimental**）。

**completion** _shell_
> 生成 Shell 补全脚本（**bash**、**zsh**、**fish**、**powershell**）。

**--json**
> 以机器可读格式输出成功/错误对象。

**--help**
> 显示 CLI 或子命令的帮助信息。

# CAVEATS

需要第三方提供商账户和 API 凭据；它不是通过本地 Mac 免费桥接个人 iMessage 的工具。根据提供商不同，群组消息可能被禁用。各提供商的限制不同（例如 Blooio 要求附件使用公开 URL；Sendblue 每条消息只允许一个附件）。本地附件在每个命令中的总大小限制为 100 MiB。在命令行上传递机密信息可能使其暴露在进程列表和 Shell 历史记录中——建议改用保存的连接或环境变量。在没有 Secret Service 守护进程的无头 Linux 上，基于钥匙串的连接可能仅限当前会话有效。webhook 服务器是实验性功能，并非生产级队列或高可用端点。

# HISTORY

**imessage-cli** 由 **jmisilo** 作为 **imessage-sdk** monorepo 的一部分发布。SDK 核心、各提供商、Chat SDK 适配器和 CLI 是在提供商中立会话 API 下可独立安装的软件包。

# SEE ALSO

[wacli](/man/wacli)(1), [matrix-commander](/man/matrix-commander)(1), [curl](/man/curl)(1)

# RESOURCES

```[Source code](https://github.com/jmisilo/imessage-sdk)```

```[Homepage](https://imessage-sdk.dev)```

```[Documentation](https://github.com/jmisilo/imessage-sdk/blob/main/packages/cli/README.md)```

<!-- verified: 2026-07-20 -->
