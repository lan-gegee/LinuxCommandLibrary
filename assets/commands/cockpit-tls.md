# TAGLINE

Cockpit Web 服务的 TLS 终结代理

# TLDR

在**指定端口**上服务 HTTP 请求

```cockpit-tls --port [port]```

显示**帮助**

```cockpit-tls --help```

# SYNOPSIS

**cockpit-tls** [_options_]

# DESCRIPTION

**cockpit-tls** 是一个 TLS 终结 HTTP 代理，为 Cockpit 基于 Web 的服务器管理界面处理 HTTPS 连接。它接受客户端的加密连接，终结 TLS 会话，并将解密后的 HTTP 请求转发给 cockpit-ws 处理。

默认情况下，它监听端口 9090 并使用 **/etc/cockpit/ws-certs.d/** 中的 TLS 证书。该进程被设计为以最小权限运行，只处理加密层，而将所有应用逻辑委托给 cockpit-ws。

此组件通常由 systemd 通过 **cockpit.socket** 单元管理，一般不会被直接调用。出于面向安全的关注点分离考虑，它取代了此前属于 cockpit-ws 的内置 TLS 处理功能。

# PARAMETERS

**--port** _port_
> 在指定端口而非 9090 上监听

**--help**
> 显示帮助信息

# CONFIGURATION

**/etc/cockpit/ws-certs.d/**
> 存放用于 HTTPS 连接的 TLS 证书和密钥文件的目录。

**/etc/cockpit/cockpit.conf**
> Cockpit 主配置文件，控制 Web 服务行为、来源和登录设置。

# CAVEATS

Cockpit 套件的组成部分。需要有效的 TLS 证书。通常由 systemd 管理，而非直接运行。

# SEE ALSO

[cockpit-ws](/man/cockpit-ws)(8), [cockpit-bridge](/man/cockpit-bridge)(1)

# RESOURCES

```[Source code](https://github.com/cockpit-project/cockpit)```

```[Documentation](https://cockpit-project.org/guide/latest/)```

<!-- verified: 2026-06-22 -->
