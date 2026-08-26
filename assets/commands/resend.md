# TAGLINE

用于发送邮件和管理 Webhook 的电子邮件 API CLI

# TLDR

向你的 Resend 账户进行**身份验证**

```resend login```

**发送邮件**，包含主题和正文

```resend emails send --from [sender@example.com] --to [recipient@example.com] --subject "[Hello]" --text "[Message body]"```

**检查 API 密钥**并验证域名就绪状态

```resend doctor```

**启动本地 webhook** 监听器

```resend webhooks listen```

为生产环境事件**创建 webhook**

```resend webhooks create```

以 HTML 正文**发送邮件**

```resend emails send --from [sender@example.com] --to [recipient@example.com] --subject "[Hello]" --html "[<h1>Hello</h1>]"```

# SYNOPSIS

**resend** _command_ [_options_]

# PARAMETERS

**login**
> 通过浏览器向你的 Resend 账户进行身份验证。

**doctor**
> 验证 API 密钥有效性、列出已验证域名并检查就绪状态。

**emails send**
> 发送邮件，指定发件人、收件人、主题和正文。

**webhooks listen**
> 在 4318 端口启动本地服务器，捕获并显示传入的 webhook 事件。

**webhooks create**
> 为生产环境注册新的 webhook 端点。

**--from** _address_
> 发件人邮箱地址。

**--to** _address_
> 收件人邮箱地址。

**--subject** _text_
> 邮件主题行。

**--text** _body_
> 纯文本邮件正文。

**--html** _body_
> HTML 邮件正文。

**--forward-to** _url_
> 将 webhook 负载转发到本地服务器，保留签名头。

**--version**
> 显示版本信息。

**--help**
> 显示可用命令与选项。

# DESCRIPTION

**resend** 是 Resend 电子邮件 API 的官方 CLI。它支持直接从终端发送事务性邮件、管理 webhook 以及诊断账户配置。该 CLI 面向开发者、CI/CD 流水线和 AI 智能体工作流设计。

在非交互模式下，输出格式为 JSON 并提供一致的退出码，适合脚本编写和自动化。错误包含结构化的 **message** 和 **code** 字段，便于程序化处理。

webhook 监听器（**resend webhooks listen**）会创建一个本地开发服务器，捕获传入的事件并将其流式输出到终端，便于在不部署到生产环境的情况下测试邮件事件处理器。

# CAVEATS

需要 Resend 账户和 API 密钥进行身份验证。发送邮件需要已验证的域名。webhook 监听器需要 Tailscale 才能在开发期间将本地端口暴露到互联网。CLI 在非交互模式下输出 JSON，在交互模式下输出人类可读的文本。

# HISTORY

**Resend** 由 **Zeno Rocha** 创立，是一个面向开发者的现代电子邮件 API，可作为传统事务性邮件服务的替代品。该 CLI 用于补充 REST API 和 SDK，提供基于终端的所有核心邮件操作。它使用 **TypeScript** 编写，通过 npm 和 Homebrew 分发。

# SEE ALSO

[mail](/man/mail)(1), [sendmail](/man/sendmail)(1), [curl](/man/curl)(1)
