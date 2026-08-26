# TAGLINE

高速反向代理服务端

# TLDR

**启动 frp 服务端**

```frps -c [frps.toml]```

**校验配置**

```frps verify -c [frps.toml]```

使用默认值启动**简单服务端**

```frps --bind_port [7000]```

**显示版本**

```frps -v```

# SYNOPSIS

**frps** [_command_] [_options_]

# PARAMETERS

_COMMAND_
> 操作：verify。

**-c** _FILE_
> 配置文件路径。

**--bind_port** _PORT_
> 用于客户端连接的绑定端口。

**--dashboard_port** _PORT_
> Web 仪表盘端口。

**--token** _STRING_
> 认证令牌。

**verify**
> 校验配置文件。

**--help**
> 显示帮助信息。

# CONFIGURATION

**frps.toml**
> 服务端配置文件（自 frp v0.52 起为 TOML；早期版本使用 INI 和 YAML），控制绑定端口、仪表盘设置、认证要求和连接策略。

# DESCRIPTION

**frps** 是 frp（fast reverse proxy）的服务端组件。它运行在公网服务器上，接受来自 frpc 客户端的连接，并将流量路由到被暴露的内部服务。

服务端负责管理客户端认证、代理路由和端口分配。Web 仪表盘提供监控功能。多个客户端可以连接到同一个服务器。

frps 为访问由 frpc 客户端暴露的服务提供公网入口。

# CAVEATS

需要有开放端口且可从公网访问的服务器。安全性取决于认证配置。资源消耗随连接数增长。

# HISTORY

frps 是 **frp** 的一部分，为该反向代理系统提供服务端功能。它让你能够自建隧道基础设施，作为商业服务的替代方案。

# INSTALL

```apk: sudo apk add frp```

```brew: brew install frps```

```nix: nix profile install nixpkgs#frp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[frpc](/man/frpc)(1), [frp](/man/frp)(1), [nginx](/man/nginx)(1)
