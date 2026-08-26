# TAGLINE

带策略与支出控制的自托管 LLM 路由器

# TLDR

**初始化**提供商、模型角色和 API 密钥

```millwright init```

**启动**路由网关

```millwright serve```

**查看支出**汇总和团队排行

```millwright spend```

**查看**模型与提供商构成

```millwright models```

按 trace id **解释**路由决策

```millwright trace [trace-id]```

在终端中实时查看**支出与**模型活动

```millwright top```

从运行中的网关**分析**成本

```millwright analyze --url [http://127.0.0.1:8080] --key [$MILLWRIGHT_OPERATOR_KEY] --since [30d] --report [analysis.html]```

**打印**版本与构建元数据

```millwright version```

# SYNOPSIS

**millwright** _command_ [_options_]

# DESCRIPTION

**millwright** 是一个自托管 LLM 路由器，位于 AI 应用与模型提供商之间。它接受 OpenAI Chat Completions 和 Anthropic Messages 请求，然后将每个请求路由到 OpenAI 兼容 API、Anthropic 或 Amazon Bedrock。

你将模型分配到 **cheap**、**mid** 和 **frontier** 三种角色。Millwright 会选择解析后的角色所允许的、预估成本最低的健康路由。通过会话 ID，它维护独立的角色作用域亲和通道，使并发的 cheap/mid/frontier 流量可以复用温热的提示词缓存，而不会串行化智能体工作。

它是一个路由器，而不是智能体编排器：不会生成智能体、调度任务、检查提示词或改写上下文。路由决策可通过响应头、追踪记录以及可选的用量账本进行检查（默认 SQLite；生产环境用 PostgreSQL）。

以单个 Rust 二进制文件发布，并支持 Docker Compose。提供商凭据保存在环境变量中；独立的工作负载密钥和操作员密钥分别控制推理访问和管理访问。

# PARAMETERS

**init**
> 以交互式（或参数驱动）方式设置提供商、角色、定价和密钥。写入 policy/models 配置和环境变量引用（不写入原始提供商密钥）。常用参数：**--non-interactive**、**--provider**、**--cheap**、**--mid**、**--frontier**、**--cache-ttl**、**--team**、**--force**。

**serve**
> 运行路由器 HTTP 网关（默认本地 URL 为 **http://localhost:8080**）。

**spend** [**--url** _url_] [**--key** _key_] [**--json**]
> 从管理 API 获取总支出、缓存读取率及各团队明细。

**models** [**--url** _url_] [**--key** _key_] [**--json**]
> 从账本获取模型与提供商构成。

**trace** _trace-id_ [**--url** _url_] [**--key** _key_] [**--json**]
> 解释一次路由决策（包括被拒绝的备选方案）。Trace id 出现在 **x-millwright-trace-id** 中。

**top** [**--url** _url_] [**--key** _key_]
> 在终端实时显示支出和模型活动。

**analyze** [_options_]
> 分析在线账本或本地 JSONL 成本数据。生成 HTML/Markdown 报告和带模式版本的 JSON。关键参数：**--url**、**--key**、**--input**、**--input-format**、**--since**、**--until**、**--catalog**、**--candidates**、**--report**、**--json-out**。

**healthcheck**
> 探测本地网关，用于容器健康检查。

**version**
> 打印版本和构建元数据（也可用 **--version** / **-v**）。

网关客户端默认值：**--url** 回退到 **MILLWRIGHT_URL** 或 **http://localhost:8080**；**--key** 依次回退到 **MILLWRIGHT_OPERATOR_KEY**，再回退到 **MILLWRIGHT_API_KEY**。

# CAVEATS

从源码构建需要较新的 Rust 工具链（项目固定使用 **rustc** 1.97+）。必须先配置提供商 API 密钥和操作员密钥才能进行有效路由；`millwright init` 只存储机密的环境变量*名称*，而不存储机密本身。跨协议翻译支持文档化的文本与工具子集，遇到不支持的形状会拒绝请求，而不会静默丢弃数据。

# HISTORY

**Millwright** 是 Northwood Systems 的 Apache-2.0 开源项目。版本 **0.1.0** 专注于确定性的基于角色的路由、缓存感知的亲和性，以及自托管 LLM 网关的本地支出可见性。

# SEE ALSO

[curl](/man/curl)(1), [docker](/man/docker)(1), [docker-compose](/man/docker-compose)(1), [ollama](/man/ollama)(1), [caddy](/man/caddy)(1)

# RESOURCES

```[Source code](https://github.com/Northwood-Systems/millwright)```

```[Homepage](https://northwoodsystems.ai/research/projects/millwright/docs)```

```[Documentation](https://github.com/Northwood-Systems/millwright/tree/main/docs)```

<!-- verified: 2026-07-23 -->
