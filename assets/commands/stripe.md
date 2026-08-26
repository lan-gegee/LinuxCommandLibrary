# TAGLINE

Stripe 支付平台开发者 CLI

# TLDR

**登录 Stripe**

```stripe login```

**监听 webhook**

```stripe listen```

**转发到本地服务器**

```stripe listen --forward-to [localhost:3000/webhook]```

**触发测试事件**

```stripe trigger [payment_intent.succeeded]```

**列出客户**

```stripe customers list```

**创建支付意图**

```stripe payment_intents create --amount [1000] --currency [usd]```

**查看日志**

```stripe logs tail```

**打开仪表板**

```stripe open```

# SYNOPSIS

**stripe** _command_ [_subcommand_] [_options_]

# PARAMETERS

**login**
> 通过浏览器用你的 Stripe 账户对 CLI 进行身份验证。

**listen**
> 监听 webhook 事件，并可选择将其转发到本地端点。

**trigger** _EVENT_
> 触发测试 webhook 事件（例如 payment_intent.succeeded、charge.failed）。

**logs tail**
> 流式查看实时 API 请求与响应日志。

**open**
> 在默认浏览器中打开 Stripe 仪表板页面。

**status**
> 检查 Stripe API 的当前状态。

**samples**
> 下载并配置 Stripe 示例集成项目。

**get** _RESOURCE_
> 向 Stripe API 发起 GET 请求。

**post** _RESOURCE_
> 向 Stripe API 发起 POST 请求。

**--forward-to** _URL_
> 将收到的 webhook 事件转发到本地 URL（与 listen 搭配使用）。

**--api-key** _KEY_
> 为该命令使用特定的 Stripe API 密钥。

**-p**, **--project-name** _NAME_
> 针对特定项目配置运行命令（默认为 "default"）。

**--color** _on|off_
> 启用或禁用彩色输出。

**--log-level** _LEVEL_
> 设置日志详细程度级别（默认为 info）。

**-h**, **--help**
> 显示命令帮助。

**-v**, **--version**
> 显示 CLI 版本。

# DESCRIPTION

**stripe** 是 Stripe 支付平台的官方命令行界面，旨在简化支付集成的开发和测试。它提供对 Stripe API 的直接访问，让开发者无需编写代码即可创建和管理客户、支付意图和订阅等资源。

其核心特性是 webhook 监听，可在本地接收 Stripe 事件并转发给开发服务器。这免除了开发过程中对公网 URL 的需求。trigger 命令可模拟支付成功或扣款失败等特定事件，便于对 webhook 处理程序进行全面测试。

该 CLI 还提供实时日志跟踪功能用于监控 API 请求和响应，并可直接打开 Stripe 仪表板。身份验证通过 login 命令完成，它会管理 API 密钥并同时支持测试模式和生产模式。

# CAVEATS

使用前需要 Stripe 账户并通过 **stripe login** 完成身份验证。API 密钥是敏感凭据，不应共享或提交到版本控制。**listen** 命令仅在运行期间接收事件；未运行时触发的事件会丢失。Webhook 转发使用的临时签名密钥在每次会话中都会变化。除非使用测试模式的 API 密钥，资源类命令（例如 **stripe customers list**）会作用于生产数据。

# HISTORY

**Stripe CLI** 由 **Stripe** 于 **2019 年**发布，是一款旨在改善支付集成开发体验的开源工具。它以 Go 语言构建并发布于 GitHub。该 CLI 解决了在本地测试 webhook 这一常见痛点——此前需要借助 ngrok 等工具。此后它的功能扩展到 API 资源管理、日志跟踪、示例项目脚手架以及 Stripe Apps 开发支持。

# INSTALL

```brew: brew install stripe```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[curl](/man/curl)(1), [jq](/man/jq)(1)
