# TAGLINE

包装 claude CLI 的即插即用工具，用于脚本化交互会话

# TLDR

通过包装器**运行交互式会话**

```claude-pee```

发送**一次性提示**并打印回复

```claude-pee -p "[summarize this file]"```

请求 **JSON 输出**供下游解析

```claude-pee -p "[prompt]" --output-format json```

在模型响应时流式输出**增量 JSON** 事件

```claude-pee -p "[prompt]" --output-format stream-json```

将额外标志原样**转发**给底层 claude CLI

```claude-pee --model [opus] -p "[prompt]"```

# SYNOPSIS

**claude-pee** [_options_] [**-p** _prompt_]

# DESCRIPTION

**claude-pee** 是一个 Rust 前端，包装了官方的 **claude** 命令行工具。它在伪终端（PTY）中启动 claude，分配一个全新的 **--session-id**（UUIDv4），其余标志原样转发，可选地用 **-p** 注入一次性提示，然后持续跟踪匹配的会话转录 JSONL 文件，直到助手的回复结束。

这个包装器的存在是为了让程序化脚本和 CI 流水线可以驱动 **claude**，而不消耗其编程用量额度池，同时仍享有交互式会话的语义。输出会根据 **--output-format** 以纯文本、JSON 或流式 JSON 的形式收集并打印到 stdout。

哨兵文件结合 claude 的 Stop 钩子来标记响应何时完成，使包装器能够干净退出，而不是无限轮询。

# PARAMETERS

**-p** _prompt_
> 注入一次性提示，回复完成后退出。不带 **-p** 时，包装器将 PTY 交还给用户进行交互式会话。

**--output-format** _FORMAT_
> 选择输出模式：**text**（默认）、**json** 或 **stream-json**。

**--session-id** _ID_
> 覆盖自动生成的 UUIDv4（用于关联底层 claude 转录文件）。

所有其他标志都会原样转发给 **claude**，因此 **--model**、**--add-dir**、**--allowedTools** 等选项的行为与真实 CLI 文档描述完全一致。

# CAVEATS

需要已安装 **claude** CLI 并位于 **$PATH** 中；从源码构建需 Rust **1.85+** 并执行 **cargo build --release**。由于包装器依赖 claude 的转录 JSONL 格式和 Stop 钩子行为，官方客户端未来的变更可能使其失效。这是一个社区项目，不是 Anthropic 的产品。

# HISTORY

**claude-pee** 于 **2026** 年发布，是社区对 Claude Code 交互式与编程式用法成本差异的回应，首次出现在 Hacker News 上，并从单文件 Rust 原型发展为一个小型即插即用垫片。

# INSTALL

```aur: yay -S claude```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[claude](/man/claude)(1), [jq](/man/jq)(1), [tmux](/man/tmux)(1)
