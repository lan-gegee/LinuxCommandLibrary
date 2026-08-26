# TAGLINE

终端 TUI gRPC 客户端

# TLDR

**启动**交互式 gRPC TUI

```chiko```

使用 TLS 但跳过证书验证进行**连接**

```chiko -insecure```

使用自定义 CA 证书进行**连接**

```chiko -cacert [/path/to/ca.pem]```

使用客户端证书认证进行**连接**

```chiko -cert [/path/to/client.pem] -key [/path/to/client-key.pem]```

**设置** 30 秒连接超时

```chiko -connect-timeout 30```

# SYNOPSIS

**chiko** [_flags_]

# PARAMETERS

**-plaintext**
> 连接时使用明文 HTTP/2（不启用 TLS）。默认：true。

**-insecure**
> 跳过服务器证书和域名校验。

**-cacert** _file_
> 包含受信任根证书的文件，用于校验服务器。

**-cert** _file_
> 包含客户端证书（公钥）的文件。

**-key** _file_
> 包含客户端私钥的文件。

**-d** _data_
> 请求内容的数据。

**-allow-unknown-fields**
> 允许 JSON 请求中出现未知字段。

**-connect-timeout** _seconds_
> 等待连接的最长时间，单位秒（默认：10）。

**-keepalive-time** _seconds_
> 发送 keepalive 探测前的最长空闲时间。

**-max-time** _seconds_
> 单次操作的最长总时长，单位秒。

**-max-msg-sz** _bytes_
> 编码后响应消息的最大大小（默认：4194304）。

# DESCRIPTION

**chiko** 是一个用 Go 编写的终端用户界面，用于与 gRPC 服务交互。它将 **grpcurl** 的强大功能与可视化 TUI 的优雅体验相结合。无需记忆复杂的 grpcurl 命令语法，chiko 提供了一个交互式界面，可用于发现服务、构造请求和测试 gRPC API。

主要特性包括：智能服务器反射实现服务自动发现、内置 Bearer token 认证支持、丰富的元数据和自定义 header 支持、根据服务定义即时生成负载、用于保存和重放请求的智能书签，以及 grpcurl 命令的导入导出。

# CAVEATS

**-plaintext** 参数默认为 true，即默认连接不加密——适合本地开发，但不适用于生产服务器。gRPC 服务器必须启用服务器反射才能自动发现服务。尚不支持导入 proto 文件。处于稳定版之前的阶段（v0.x）。

# HISTORY

**chiko** 由 **Felix Angga** 开发，使用 Go 编写，采用 MIT 许可证。它的目标是成为原始 **grpcurl** 命令行工具的开发者友好型可视化替代品。可通过 Homebrew 和 Go install 安装。

# INSTALL

```brew: brew install chiko```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grpcurl](/man/grpcurl)(1), [curl](/man/curl)(1), [protoc](/man/protoc)(1)
