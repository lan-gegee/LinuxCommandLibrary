# TAGLINE

免费、本地、开源的 LLM 成本分析工具

# TLDR

**分析** LLM 使用日志，查看将调用路由到更便宜模型可节省的成本

```frugon analyze ./logs.jsonl```

通过代理垫片在本地**捕获** LLM 调用以生成日志

```frugon capture --out ./logs.jsonl```

对内置示例数据**运行**演示分析

```frugon analyze --demo```

**列出**可作为路由候选的可用模型

```frugon models```

**生成**可分享的 HTML 或 Markdown 分析报告

```frugon analyze ./logs.jsonl --report savings.html```

通过 pipx **安装**以便长期使用

```pipx install frugon```

# SYNOPSIS

**frugon** <command> [options]

# DESCRIPTION

Frugon 是一个本地优先的工具，它分析你真实的 LLM API 调用日志（OpenAI 兼容的 JSONL 格式），准确展示你的开销去向，以及把简单的调用路由到更便宜的模型、同时把复杂的调用留给更强模型能节省多少钱。

它完全在你的机器上运行：任何日志或密钥都不会发送到别处。它在本地使用分词器和最新的定价数据。可选的 `--measure` 模式会使用你自己的 provider 密钥（直连，绝不经过 Frugon）针对候选模型采样你的流量，以给出质量估计。

Frugon 还可以作为透明本地代理（`frugon capture`），在原样转发请求给真实 provider 的同时记录调用日志。

# COMMANDS

**analyze** [file]
> 分析 JSONL 日志文件（或 `--demo`）并给出路由建议。

**capture**
> 运行本地代理，将请求/响应记录到 JSONL 文件。

**models** [filter]
> 列出可用于 `--candidates` 的模型及其定价/质量层级。

**update**
> 刷新本地定价和质量数据。

**pricing**, **quality**
> 查看本地定价和质量数据集。

# PARAMETERS

**analyze**
> `--candidates` 供路由考虑的模型的逗号分隔列表
> `--measure` 采样真实流量进行质量比较（需要 `pip install 'frugon[measure]'` 及 provider 密钥）
> `--judge` 与 `--measure` 配合时对候选质量打分
> `--report` 报告输出路径（.html 或 .md）
> `--demo` 使用内置示例数据而非文件
> `--verbose` 输出更多核算细节

**capture**
> `--out` 输出的 JSONL 文件（默认 capture.jsonl）
> `--port` 监听端口（默认 8787）
> `--upstream` 覆盖转发目标
> `--proxy` 允许上游调用走环境中的 HTTP(S)_PROXY（默认忽略，保证密钥直连）
> `--verbose` 每个捕获的调用输出一行日志

# CAVEATS

- 日志必须是特定的 JSONL 结构（model + request/response + 可选 usage）。
- `--measure` 会向你的 provider 发起真实 API 调用并产生相应费用。
- 质量层级只是估计；在生产流量切换前务必用 `--measure --judge` 在你的数据上验证。
- 路由建议是离线计算的结果；它们不会自动修改你的应用。

# SEE ALSO

[pipx](/man/pipx)(1), [uvx](/man/uvx)(1)

# RESOURCES

```[Source code](https://github.com/Rodiun/frugon)```

```[Homepage](https://frugon.rodiun.io)```

```[Documentation](https://github.com/Rodiun/frugon#readme)```

<!-- verified: 2026-07-11 -->
