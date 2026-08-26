# TAGLINE

用于服务器管理的 Cockpit Web 服务

# TLDR

启用 **SSH 认证**启动

```cockpit-ws --local-ssh```

在**指定端口**上启动 HTTP 服务器

```cockpit-ws --port [port]```

**绑定**到特定 IP 地址

```cockpit-ws --address [ip_address]```

以**无 TLS 模式**启动

```cockpit-ws --no-tls```

# SYNOPSIS

**cockpit-ws** [_options_]

# DESCRIPTION

**cockpit-ws** 是 Cockpit 的 Web 服务，负责浏览器应用与 cockpit-bridge 等各类配置工具之间的通信。它提供 Web 界面并处理认证。

默认情况下，它绑定到 0.0.0.0 并要求 TLS。

# PARAMETERS

**--local-ssh**
> 在 127.0.0.1:22 上启用 SSH 认证

**--port** _port_
> 在指定端口上监听

**--address** _address_
> 绑定到特定 IP 地址（默认：0.0.0.0）

**--no-tls**
> 在无 TLS 加密的情况下运行

**--help**
> 显示帮助信息

# CAVEATS

Cockpit 套件的组成部分。不带 TLS 运行并不安全，只应在反向代理之后使用。通常由 systemd 管理。

# HISTORY

**Cockpit** 由 Red Hat 开发，是一个基于 Web 的服务器管理界面，为传统的命令行管理方式提供了现代化替代方案。

# INSTALL

```dnf: sudo dnf install cockpit-ws```

```zypper: sudo zypper install cockpit-ws```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cockpit-bridge](/man/cockpit-bridge)(1), [cockpit-tls](/man/cockpit-tls)(8)

# RESOURCES

```[Source code](https://github.com/cockpit-project/cockpit)```

```[Documentation](https://cockpit-project.org/guide/latest/)```

<!-- verified: 2026-06-22 -->
