# TAGLINE

面向终端的 TUI gRPC 客户端

# TLDR

**启动 gRPC 客户端**

```wireman```

**启用服务器反射**（在 UI 内的选择选项卡上）

```Ctrl+r```

# SYNOPSIS

**wireman**

# DESCRIPTION

**WireMan** 是一个用 Rust 编写的基于终端的 gRPC 客户端。它从配置文件读取 .proto 文件，并提供 TUI 用于发送请求、浏览服务和方法以及查看响应。

该客户端支持服务器反射、服务器端流、头部和元数据管理、通过 shell 脚本按环境加载令牌，以及将请求导出为 **grpcurl** 命令。请求历史会在会话之间持久保存。

# CONFIGURATION

**~/.config/wireman/wireman.toml**
> 主配置文件，指定 proto 文件路径、地址、默认头部和历史设置。

# KEY BINDINGS

**Tab**
> 在选择、请求、响应和头部各选项卡之间切换。

**Ctrl+r**
> 启用服务器反射模式（在选择选项卡上）。

**Enter**
> 发送请求或确认选择。

**?**
> 显示应用内帮助。

# CAVEATS

需要一个指向本地 .proto 文件或启用了反射的服务器的配置文件。某些高级 gRPC 功能（如客户端流）的 UI 支持可能有限。

# HISTORY

**wireman** 由 **preiter93** 创建，使用 Rust 编写。它面向偏好键盘驱动的终端工作流而非 Postman 或 BloomRPC 等 GUI 工具的开发者。

# INSTALL

```pacman: sudo pacman -S wireman```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grpcurl](/man/grpcurl)(1), [curl](/man/curl)(1), [protoc](/man/protoc)(1)
