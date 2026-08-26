# TAGLINE

终端下的 WebSocket 客户端和服务器

# TLDR

**连接到 WebSocket 服务器**

```websocat ws://[example.com]/socket```

**使用安全 WebSocket 连接**

```websocat wss://[example.com]/socket```

**创建 WebSocket 服务器**

```websocat -s [8080]```

**将 stdin 通过管道发送到 WebSocket**

```echo "hello" | websocat ws://[example.com]/socket```

**使用自定义请求头连接**

```websocat -H "Authorization: Bearer [token]" wss://[example.com]/socket```

传输原始数据的**二进制模式**

```websocat -b ws://[example.com]/socket```

**每行一条消息**模式

```websocat -n ws://[example.com]/socket```

**将 TCP 转发到 WebSocket**

```websocat --binary tcp-l:127.0.0.1:[8080] ws://[example.com]/socket```

# SYNOPSIS

**websocat** [_options_] _address1_ [_address2_]

# PARAMETERS

**-s**, **--server**
> 在指定端口上运行简单的 WebSocket 服务器模式。

**-b**, **--binary**
> 发送和接收二进制帧而不是文本。

**-n**, **--no-close**
> 不发送关闭帧，直接断开连接。

**-1**, **--one-message**
> 发送一条消息后退出。

**-u**, **--unidirectional**
> 只从 address1 复制到 address2。

**-U**, **--unidirectional-reverse**
> 只从 address2 复制到 address1。

**-H** _header_
> 添加自定义 HTTP 请求头。

**-E**, **--exit-on-eof**
> 当 stdin 到达 EOF 时退出。

**-t**, **--text**
> 强制文本帧模式。

**--ping-interval** _secs_
> 按间隔发送 WebSocket ping。

**--ping-timeout** _secs_
> 未收到 pong 时关闭连接。

**-k**, **--insecure**
> 接受无效的 TLS 证书。

**--origin** _url_
> 设置 Origin 请求头。

**-q**, **--quiet**
> 不显示提示性消息。

**-v**, **--verbose**
> 提高输出详细程度。

# ADDRESS TYPES

**ws://** / **wss://**
> WebSocket 客户端连接。

**tcp:** / **tcp-l:**
> TCP 客户端/监听器。

**unix:** / **unix-l:**
> Unix 套接字客户端/监听器。

**exec:**
> 执行程序并连接到其标准输入输出。

**sh-c:**
> 执行 shell 命令。

**stdio:**
> 标准输入/输出。

**mirror:**
> 将收到的消息原样回显。

**autoreconnect:**
> 自动重连的包装器。

# DESCRIPTION

**websocat** 是一款命令行 WebSocket 客户端和服务器，类似于 netcat，但面向 WebSocket 连接。它支持在各种端点之间进行双向通信，包括 WebSocket、TCP、Unix 套接字和 stdio。

基本用法是将 stdin/stdout 连接到一个 WebSocket URL。输入的行会成为 WebSocket 消息；收到的消息打印到 stdout。二进制数据请使用 **-b**，基于行的文本请使用 **-n**。

服务器模式（**-s**）创建一个适合测试的简单 WebSocket 服务器。生产环境中，可以将地址说明符组合起来，比如将 **tcp-l:** 与 **ws://** 结合进行协议转换。

地址链可以实现复杂的配置，如 WebSocket 隧道、TCP-over-WebSocket 以及命令执行。**autoreconnect:** 包装器可自动处理连接中断。

websocat 同时支持安全（wss://）和不安全（ws://）连接、用于身份验证的自定义请求头，以及保持连接存活的 ping/pong。

# CAVEATS

大消息可能需要增大缓冲区。某些功能需要特定的地址类型组合。不要在生产环境中使用 --insecure 选项。复杂的地址说明符学习曲线较陡。

# HISTORY

websocat 由 **Vitaly Shukela**（vi）创建，首次发布于 **2017 年**前后。它使用 Rust 编写，被设计为 WebSocket 操作的瑞士军刀。该工具在调试 WebSocket 服务、创建隧道和测试实时应用方面广受欢迎。目前仍在活跃开发中，不断添加适用于各种网络场景的功能。

# INSTALL

```pacman: sudo pacman -S websocat```

```apk: sudo apk add websocat```

```brew: brew install websocat```

```nix: nix profile install nixpkgs#websocat```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nc](/man/nc)(1), [curl](/man/curl)(1), [socat](/man/socat)(1)
