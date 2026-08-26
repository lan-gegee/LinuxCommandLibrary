# TAGLINE

用于 NAT 穿透的高速反向代理

# TLDR

**启动 frp 客户端**

```frpc -c [frpc.toml]```

**启动 frp 服务端**

```frps -c [frps.toml]```

**校验客户端配置**

```frpc verify -c [frpc.toml]```

**不重启即重载客户端配置**

```frpc reload -c [frpc.toml]```

**显示代理状态**

```frpc status -c [frpc.toml]```

# SYNOPSIS

**frpc** | **frps** [_command_] [_options_]

# COMMANDS

**reload**
> 不重启进程即可热重载客户端配置。

**verify**
> 校验配置文件语法后退出。

**status**
> 输出客户端定义的所有代理的状态。

**stop**
> 通过管理 API 停止正在运行的 frpc 实例。

# PARAMETERS

**-c**, **--config** _FILE_
> 配置文件路径（TOML、YAML 或 JSON）。

**-L**, **--log_level** _LEVEL_
> 日志级别（trace、debug、info、warn、error）。

**-t**, **--token** _TOKEN_
> 客户端与服务端共享的认证令牌。

**-s**, **--server_addr** _ADDR_
> frps 服务器地址（仅 frpc）。

**-v**, **--version**
> 输出版本信息。

**-h**, **--help**
> 显示帮助信息。

# CONFIGURATION

**frpc.toml**
> 客户端配置：定义服务器连接、认证令牌，以及要对外暴露的服务的代理定义。

**frps.toml**
> 服务端配置：指定绑定端口、仪表盘设置、认证令牌和连接数限制。

# DESCRIPTION

**frp**（fast reverse proxy）将位于 NAT 或防火墙之后的本地服务器暴露到互联网。它由内网中的客户端（**frpc**）和公网主机上的服务端（**frps**）组成。

该工具支持 TCP、UDP、HTTP、HTTPS、STCP、SUDP 和 XTCP 协议，并具备加密、压缩、多路复用和认证等特性。它可用于远程访问内部服务、SSH 隧道、Web 应用以及点对点连接。

自 v0.52.0 起，frp 支持 **TOML**、**YAML** 和 **JSON** 配置格式。旧的 **INI** 格式已被弃用，计划移除。

frp 是 ngrok 等服务的自托管替代方案。

# CAVEATS

需要一台可从公网访问的服务器。每个暴露的服务都需要在客户端配置中有自己的代理条目。安全性依赖于强共享令牌和 TLS 配置。INI 配置已弃用，请迁移到 TOML。

# HISTORY

**frp** 由 **fatedier** 创建，是商业反向代理服务的开源替代品。它以 Go 编写，为开发者和系统管理员提供自托管的隧道服务。

# INSTALL

```nix: nix profile install nixpkgs#frp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[frpc](/man/frpc)(1), [frps](/man/frps)(1), [ngrok](/man/ngrok)(1)
