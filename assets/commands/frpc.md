# TAGLINE

高速反向代理客户端

# TLDR

**启动 frp 客户端**

```frpc -c [frpc.ini]```

**校验配置**

```frpc verify -c [frpc.ini]```

**重载配置**

```frpc reload -c [frpc.ini]```

**显示状态**

```frpc status -c [frpc.ini]```

**显示版本**

```frpc -v```

# SYNOPSIS

**frpc** [_command_] [_options_]

# PARAMETERS

_COMMAND_
> 操作：verify、reload、status。

**-c** _FILE_
> 配置文件路径。

**verify**
> 校验配置文件。

**reload**
> 不重启进程即重载配置。

**status**
> 显示代理状态。

**-v**, **--version**
> 显示版本。

**--help**
> 显示帮助信息。

# CONFIGURATION

**frpc.ini**
> 客户端配置文件，指定服务器地址、认证令牌，以及每个要通过隧道暴露的服务的代理定义。

# DESCRIPTION

**frpc** 是 frp（fast reverse proxy）的客户端组件。它运行在内网中，与 frps 服务器建立连接，为要暴露的服务创建隧道。

配置可为 TCP、UDP、HTTP 和 HTTPS 服务定义代理。客户端维持持久连接并处理重连。一个客户端可以同时暴露多个服务。

frpc 让你可以通过公网上的 frps 服务器访问内部服务。

# CAVEATS

需要有正在运行的 frps 服务器。配置必须与服务端匹配。需要网络连通性。

# HISTORY

frpc 是开源反向代理项目 **frp** 的一部分。它提供穿过 NAT 与防火墙建立隧道所需的客户端功能。

# INSTALL

```apk: sudo apk add frp```

```brew: brew install frpc```

```nix: nix profile install nixpkgs#frp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[frps](/man/frps)(1), [frp](/man/frp)(1), [ssh](/man/ssh)(1)

# RESOURCES

```[Source code](https://github.com/fatedier/frp)```

```[Documentation](https://gofrp.org/en/docs/)```

<!-- verified: 2026-07-15 -->
