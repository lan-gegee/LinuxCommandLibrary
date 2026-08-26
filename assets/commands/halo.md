# TAGLINE

基于 RLM 的 AI 智能体执行轨迹分析器

# TLDR

使用诊断提示词**分析轨迹文件**

```halo [traces.jsonl] -p "[Diagnose errors and suggest fixes]"```

为分析运行**指定模型**

```halo [traces.jsonl] -p "[prompt]" --model [gpt-5.4-mini]```

**指向 OpenAI 兼容的 API 提供方**

```halo [traces.jsonl] -p "[prompt]" --base-url [https://openrouter.ai/api/v1]```

为 HALO 运行本身**输出遥测数据**

```halo [traces.jsonl] -p "[prompt]" --telemetry```

# SYNOPSIS

**halo** _TRACE_PATH_ **--prompt** _TEXT_ [_options_]

**halo** _TRACE_PATH_ **-p** _TEXT_ [_options_]

# DESCRIPTION

**halo** 是 HALO 引擎的命令行前端。HALO 引擎是一个围绕 **RLM**（Recursive Language Models，递归语言模型）构建的递归结构化轨迹分析器。它可以摄取来自智能体框架的 OpenTelemetry 兼容 JSONL 执行轨迹，跨多次运行分解失败原因，并生成系统性问题报告，而不是过度拟合单条坏轨迹。

该 CLI 将用户提示词连同轨迹文件一起发送给一个根智能体，根智能体可以派生子智能体、总结长上下文并综合各项发现。输出旨在反馈给 **claude** 或 **cursor** 等编程智能体，以便迭代改进框架提示词、工具和防护措施。另有独立的桌面应用和托管服务，但 **halo** 是从 **halo-engine** Python 软件包安装的本地可脚本化入口。

# PARAMETERS

**--prompt**, **-p** _TEXT_
> 必需的用户提示词，描述要在轨迹中查找的内容。

**--model**, **-m** _MODEL_
> 用于根智能体和子智能体调用的模型（默认 `gpt-5.4-mini`）。

**--synthesis-model** _MODEL_
> 用于轨迹摘要的更廉价模型（默认为 **--model**）。

**--compaction-model** _MODEL_
> 用于上下文压缩的更廉价模型（默认为 **--model**）。

**--max-depth** _N_
> 子智能体的最大递归深度（默认 2）。

**--max-turns** _N_
> 每个智能体的最大轮次（默认 20）。

**--max-parallel** _N_
> 最大并发子智能体数（默认 10）。

**--base-url** _URL_
> OpenAI 兼容 API 的基础 URL。

**--api-key** _KEY_
> 服务提供方的 API 密钥（回退到 **OPENAI_API_KEY**）。

**--header**, **-H** _NAME:VALUE_
> 额外的请求头；可重复使用。

**--temperature** _N_
> 传递给模型的采样温度。

**--max-output-tokens** _N_
> 传递给模型的最大输出 token 数。

**--telemetry**
> 为 HALO 自身的 LLM 和工具活动输出 OpenInference 遥测数据。

# CONFIGURATION

**OPENAI_API_KEY**
> 所配置服务提供方的默认凭据。

**OPENAI_BASE_URL**
> 未设置 **--base-url** 时使用的默认 API 基础 URL。

**CATALYST_OTLP_TOKEN**
> 启用 **--telemetry** 时，通过 OTLP 将 span 上传到 inference.net Catalyst。

# CAVEATS

**halo** 需要有效的 API 密钥以及对所选模型的服务访问权限。轨迹文件必须是由已集成框架生成的 OpenTelemetry 兼容格式的 JSONL 文件。分析成本随轨迹大小、递归深度和模型选择而增长；在大规模运行时建议使用更小的模型进行综合与压缩。

# HISTORY

HALO 由 **Context Labs**（inference.net）于 2026 年开发，是一种基于生产轨迹改进智能体框架的方法论和引擎。**halo** CLI 随 PyPI 上的开源 **halo-engine** 软件包一同发布。

# INSTALL

```nix: nix profile install nixpkgs#halo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[claude](/man/claude)(1), [codex](/man/codex)(1), [jq](/man/jq)(1)

# RESOURCES

```[Source code](https://github.com/context-labs/HALO)```

```[Homepage](https://inference.net/products/halo)```

```[Documentation](https://docs.inference.net)```

<!-- verified: 2026-06-30 -->
