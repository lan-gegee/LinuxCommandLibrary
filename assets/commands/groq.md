# TAGLINE

LPU 驱动的终端编程助手

# TLDR

**启动交互式聊天**会话

```groq```

使用 npx **免安装运行**

```npx groq-code-cli@latest```

**设置响应的生成温度**

```groq -t [0.7]```

**提供自定义系统消息**

```groq -s "You are a helpful coding assistant"```

**启用调试日志**写入文件

```groq -d```

为 API 请求**配置代理**

```groq --proxy [http://proxy:8080]```

# SYNOPSIS

**groq** [**-t** _temperature_] [**-s** _message_] [**-d**] [**-p** _proxy_]

# PARAMETERS

**-t**, **--temperature** _temp_
> 设置生成温度，控制响应的随机性。默认：1。

**-s**, **--system** _message_
> 为对话提供自定义系统消息。

**-d**, **--debug**
> 启用调试日志输出到 debug-agent.log。

**-p**, **--proxy** _url_
> 为 API 请求配置代理。支持 HTTP、HTTPS 和 SOCKS5 协议。

**-h**, **--help**
> 显示帮助信息。

**-V**, **--version**
> 显示版本号。

# DESCRIPTION

**groq**（Groq Code CLI）是一款由 Groq 的 LPU（Language Processing Unit）推理引擎驱动的命令行编程助手，后者以极快的响应速度著称。它提供一个基于终端的交互式界面，用于 AI 辅助的代码生成和开发任务。

该 CLI 将配置存储在主目录的 **.groq/** 文件夹中，包括 API 密钥和模型偏好。用户可以使用 **/model** 命令选择 Groq 平台上可用的不同语言模型。

代理配置遵循优先级顺序：CLI 标志（**--proxy**）优先于 **HTTPS_PROXY**，后者又优先于 **HTTP_PROXY** 环境变量。

# CONFIGURATION

**~/.groq/**
> 存储API 密钥、模型偏好和会话数据的配置目录。

# CAVEATS

需要 **GROQ_API_KEY** 环境变量或通过 **/login** 命令进行身份验证。API 用量受 Groq 的速率限制和服务条款约束。该 CLI 的安装需要 Node.js。

# HISTORY

Groq Code CLI 由 Groq 作为开源项目发布，用于向开发者展示其 LPU 推理能力。Groq 成立于 **2016 年**，开发了针对 AI 推理优化的定制张量流处理器芯片，其响应速度显著快于传统的基于 GPU 的方案。该 CLI 正是利用这一速度优势来支持交互式编程工作流。

# SEE ALSO

[claude](/man/claude)(1), [ollama](/man/ollama)(1), [anthropic](/man/anthropic)(1)
