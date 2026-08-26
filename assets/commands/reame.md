# TAGLINE

以 CPU 优先的本地 LLM 推理服务器，带持久化缓存

# TLDR

**列出**目录中的模型及磁盘上已有的模型

```reame list```

**下载**、自动配置并与一个模型**对话**

```reame run [qwen2.5-1.5b]```

执行一次性**提示词**

```reame run [qwen2.5-1.5b] "[Explain mmap]"```

提供 **OpenAI 兼容 API**

```reame run [qwen2.5-1.5b] --serve```

对较难的问题使用 **Conclave**（N 取最佳多数投票）

```reame run [qwen2.5-1.5b] "[question?]" --best-of [5]```

使用显式的**配置文件**运行

```reame --config [config/reame.conf] --serve```

# SYNOPSIS

**reame** [_options_]

**reame** **run** _model_ [_prompt_] [_options_]

**reame** **list**

# DESCRIPTION

**reame** 是一个构建在 **llama.cpp** 之上的 LLM 推理服务器，专为廉价的 CPU 硬件优化。其设计目标是避免重复计算：共享的提示词前缀会被快照到磁盘，已完成的生成结果会写入磁盘归档供后续请求草拟时使用，可选的投机解码则会根据实测接受率自适应调整。

**reame run** 会解析目录名称或本地 GGUF 路径，首次使用时下载到 **~/.reame/models**，并为主机自动选择线程数、KV 设置和缓存路径。**--serve** 会暴露 OpenAI 兼容的 **completions** 与 **chat/completions** 端点（支持 SSE 流式传输）、会话、指标以及健康检查端点。高级功能包括交错的多用户批处理、语法驱动的草拟、**--best-of** 共识机制（**Conclave**），以及可选的共享内存守护进程 **reame arca**。

# PARAMETERS

**list**
> 显示模型目录和本地下载情况

**run** _model_ [_prompt_]
> 对话或一次性推理；**--serve** 进入 API 模式；**--best-of** _N_ 进行多数投票

**--config** _file_
> reame 配置文件路径（模型路径、线程、缓存、服务器、投机解码等）

**--prompt** / **--max-tokens** / **--serve**
> 不通过 **run** 时直接使用的推理与服务器标志

# CONFIGURATION

INI 风格的配置节包括 **[model]**、**[memory]**（KV 量化）、**[speculative]**、**[cache]**（磁盘预算）、**[server]**（端口、API 密钥、并行用户数）以及可选的远程缓存 **[arca]**。Homebrew 用户可通过项目 tap 安装：**brew install reame**。

# CAVEATS

以 CPU 为中心；并非像 Ollama 那样的通用 GPU 或多模型管理器。效果取决于工作负载——最适合缓存能带来收益的抽取、分类和重复性领域任务。项目尚年轻，生产环境请固定版本。

# SEE ALSO

[ollama](/man/ollama)(1), [llama-cli](/man/llama-cli)(1)

# RESOURCES

```[Source code](https://github.com/swellweb/reame)```

```[Documentation](https://github.com/swellweb/reame/blob/main/docs)```

<!-- verified: 2026-07-14 -->
