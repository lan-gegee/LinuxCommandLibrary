# TAGLINE

支持端到端加密的轻量级实时终端聊天工具

# TLDR

**以交互方式启动聊天服务器**

```marchat-server --interactive```

**启用管理面板启动服务器**

```marchat-server --admin-panel```

**以命名用户身份连接服务器**

```marchat-client --server [ws://host:8080/ws] --username [name]```

**以管理员身份连接**

```marchat-client --server [ws://host:8080/ws] --admin --admin-key [key]```

**显示服务器诊断信息**

```marchat-server --doctor```

# SYNOPSIS

**marchat-server** [_options_]

**marchat-client** [_options_]

# PARAMETERS

**--interactive**
> 未设置环境变量时，为服务器提供引导式设置提示。

**--admin-panel**
> 在服务器上启用终端内的管理界面。

**--web-panel**
> 在服务器上启用基于 Web 的管理界面。

**--config-dir** _PATH_
> 覆盖默认配置目录。

**--doctor**
> 以文本格式显示服务器诊断信息。

**--doctor-json**
> 以 JSON 格式显示服务器诊断信息。

**--username** _NAME_
> 设置连接时使用的客户端用户名。

**--server** _URL_
> 要连接的服务器 WebSocket 地址（如 `ws://localhost:8080/ws`）。

**--admin**
> 以管理员权限连接。

**--admin-key** _KEY_
> 管理员认证密钥。

**--skip-tls-verify**
> 跳过 TLS 证书验证（使用自签名证书时有用）。

# DESCRIPTION

**marchat** 是一个自托管的终端群聊应用，具备实时 WebSocket 消息传递、可选的端到端加密、插件系统、文件共享、管理面板和代码片段支持。TUI 客户端使用 Bubble Tea 构建，数据存储在 SQLite 中。

服务器通过标志或环境变量进行配置（`MARCHAT_PORT`、`MARCHAT_ADMIN_KEY`、`MARCHAT_GLOBAL_E2E_KEY` 等）。端到端加密采用 X25519/ChaCha20-Poly1305。插件系统支持社区开发的扩展，可用于 ANSI 图片分享、文本过滤器和自定义命令。

# CAVEATS

需要自行运行服务器实例。端到端加密是可选功能，必须通过 `MARCHAT_GLOBAL_E2E_KEY` 显式启用。不带参数运行任一二进制文件都会启动交互式配置提示。

# HISTORY

**marchat** 由 **Cod-e-Codes** 创建，使用 **Go** 语言编写。

# SEE ALSO

[irssi](/man/irssi)(1), [weechat](/man/weechat)(1)
