# TAGLINE

用于便携式 LLM 推理的单文件可执行程序

# TLDR

**运行一个 llamafile（在终端启动聊天，并在 8080 端口启动服务器）**

```./[model].llamafile```

**以纯服务器模式运行**

```./[model].llamafile --server```

**以 CLI 模式运行并附带提示词**

```./[model].llamafile --cli -p "[prompt]"```

**运行交互式聊天模式**

```./[model].llamafile --chat```

**加载外部模型权重**

```llamafile -m [path/to/model.gguf]```

**设置上下文大小和线程数**

```./[model].llamafile -c [8192] -t [8] -p "[prompt]"```

**在指定的主机和端口上运行服务器**

```./[model].llamafile --server --host [0.0.0.0] --port [8080]```

**将层卸载到 GPU 并设置温度**

```./[model].llamafile -ngl [999] --temp [0.7] -p "[prompt]"```

# SYNOPSIS

**llamafile** [_options_]

# PARAMETERS

**-m** _model_
> 模型权重文件的路径（当权重未内嵌于 llamafile 时使用）。

**-p** _prompt_
> 输入的提示词文本。

**--cli**
> 以 CLI 模式运行，回答单个提示词。

**--chat**
> 运行带斜杠命令的交互式聊天模式。

**--server**
> 启动带 Web UI 的 HTTP 服务器模式。

**-c** _size_
> 以 token 为单位的上下文窗口大小。

**-t** _threads_
> 用于计算的线程数。

**-n** _count_
> 生成的最大 token 数量。

**-ngl** _n_
> 卸载到 GPU 的层数。

**--host** _addr_
> 服务器监听地址（默认：127.0.0.1）。

**--port** _port_
> 服务器端口（默认：8080）。

**--temp** _value_
> 采样温度（越高越随机）。

**--top-k** _n_
> Top-k 采样（默认：40）。

**--top-p** _value_
> Top-p 核采样（默认：0.95）。

**--seed** _n_
> 用于输出可复现的随机种子。

**--grammar** _grammar_
> 应用 BNF 文法来约束输出格式。

**--mmproj** _file_
> 视觉模型的多模态投影模型权重。

**--image** _file_
> 多模态模型的图像文件输入。

**--jinja**
> 为聊天模板启用 Jinja 模板支持。

**-e**
> 启用提示词评估。

# DESCRIPTION

**llamafile** 是一种单文件可执行程序，它将 llama.cpp 与模型打包在一起，实现便携式 LLM 推理。基于 Cosmopolitan Libc 构建，同一个文件可以在 Linux、macOS、Windows、FreeBSD、NetBSD 和 OpenBSD 上直接运行，无需安装。

默认情况下，llamafile 会同时启动一个终端聊天机器人和一个在 8080 端口提供 Web UI 的 HTTP 服务器。它也可以在专用的 CLI、聊天或服务器模式下运行。

# CAVEATS

文件体积可能很大（数 GB）。Unix 系统上需要执行 chmod +x。Apple Silicon 可能需要代码签名。模型采用内存映射以提高效率。

# HISTORY

llamafile 由 **Mozilla** 的 **Justine Tunney** 于 **2023 年**创建，将 Cosmopolitan Libc 的通用二进制格式与 llama.cpp 相结合。

# INSTALL

```aur: yay -S llamafile```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[llama.cpp](/man/llama.cpp)(1), [ollama](/man/ollama)(1)
