# TAGLINE

用于 AI 应用测试的 mock 基础设施

# TLDR

使用 fixtures **启动** mock 服务器

```npx aimock -p [4010] -f [./fixtures]```

从配置文件**启动**

```npx aimock --config [aimock.json]```

**录制**真实 API 响应作为 fixtures

```npx aimock --record --provider-openai [https://api.openai.com]```

**转换**其他工具的 fixtures

```npx aimock convert [vidaimock] [./templates/] [./fixtures/]```

用 Docker **运行**

```docker run -d -p 4010:4010 -v [./fixtures]:/fixtures ghcr.io/copilotkit/aimock -f /fixtures```

# SYNOPSIS

**npx aimock** [_options_]

**npx aimock convert** _format_ _source_ _destination_

# PARAMETERS

**-p, --port** _number_
> 监听端口（默认：4010）

**-f, --fixtures** _directory_
> fixtures 目录路径

**--config** _file_
> 从 JSON 文件加载配置

**--record**
> 启用录制模式，代理真实 API 并将响应保存为 fixtures

**--provider-openai** _url_
> 录制模式下代理用的 OpenAI provider URL

**convert** _format_ _source_ _dest_
> 转换来自其他工具（vidaimock、mockllm）的 fixtures

# DESCRIPTION

**aimock** 是用于测试 AI 应用的确定性 mock 基础设施。它可以 mock LLM API、图像生成、语音合成、转写、视频生成、MCP 工具、A2A 代理、AG-UI 事件流、向量数据库、搜索、重排序和内容审核——全部由一个软件包在一个端口上提供，且零依赖。

该工具支持 **11 家 LLM 提供商**，包括 OpenAI、Claude、Gemini、Bedrock、Azure、Vertex AI、Ollama 和 Cohere，并完整支持流式输出。**Record & Replay** 模式会代理真实 API 并把响应保存为 fixtures，实现确定性的测试回放。混沌测试能力可以模拟故障和边界情况。

aimock 每天针对真实的 provider API 运行，能在 24 小时内发现响应格式变化，保持 fixture 兼容性。它完全基于 Node.js 内建能力构建，没有任何外部依赖。

# CAVEATS

仅面向**测试环境**，不适合生产部署。通过 npx 使用需要 **Node.js**，容器化部署则需要 Docker。录制模式需要被录制提供商的有效 API 密钥。fixture 格式为 aimock 专有，可能需要从其他 mock 工具转换而来。

# HISTORY

aimock 由 **CopilotKit** 团队创建，用 **TypeScript** 编写。它的开发动机是解决 AI 应用测试的难题：单个请求可能触及多个外部服务——LLM、工具服务器、向量数据库、重排序器和审核层——aimock 提供了一个覆盖整个 agentic 技术栈的单一 mock 服务器。

# SEE ALSO

[node](/man/node)(1), [npx](/man/npx)(1), [docker](/man/docker)(1)
