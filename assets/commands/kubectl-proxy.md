# TAGLINE

运行一个指向 Kubernetes API 服务器的代理

# TLDR

**启动 API 代理**

```kubectl proxy```

**在指定端口上运行代理**

```kubectl proxy --port=[8001]```

**允许外部访问**

```kubectl proxy --address=[0.0.0.0] --accept-hosts='.*'```

**代理特定的 API 路径**

```kubectl proxy --api-prefix=/api/```

# SYNOPSIS

**kubectl** **proxy** [_options_]

# PARAMETERS

**--port** _port_
> 代理运行的端口。

**--address** _address_
> 要绑定的地址。

**--accept-hosts** _regex_
> 接受请求来源的主机。

**--api-prefix** _prefix_
> 代理的 API 前缀。

# DESCRIPTION

**kubectl proxy** 运行一个指向 Kubernetes API 服务器的代理。它负责处理身份验证，让你无需直接暴露服务即可访问 API 和服务。默认端口为 8001。

# INSTALL

```apt: sudo apt install kubectl```

```pacman: sudo pacman -S kubectl```

```apk: sudo apk add kubectl```

```brew: brew install kubectl```

```nix: nix profile install nixpkgs#kubectl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kubectl-port-forward](/man/kubectl-port-forward)(1)
