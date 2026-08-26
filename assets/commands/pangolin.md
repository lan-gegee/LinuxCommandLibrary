# TAGLINE

带内置身份验证的自托管隧道反向代理

# TLDR

**使用 ID 和密钥连接 Pangolin 服务器**

```pangolin --id [client_id] --secret [client_secret] --endpoint [https://pangolin.example.com]```

**开启调试日志进行连接**

```pangolin --id [client_id] --secret [client_secret] --endpoint [https://pangolin.example.com] --log-level DEBUG```

**显示帮助**

```pangolin --help```

# SYNOPSIS

**pangolin** [_options_]

# PARAMETERS

**--id** _ID_
> 用于身份验证的客户端标识符。

**--secret** _SECRET_
> 用于身份验证的客户端密钥。

**--endpoint** _URL_
> Pangolin 服务器的端点 URL。

**--log-level** _LEVEL_
> 设置日志级别（例如 DEBUG）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**Pangolin** 是一个自托管的隧道反向代理服务器，内置身份与访问管理。它通过配套客户端 **Newt** 建立 WireGuard 隧道，无需复杂的网络配置即可安全地对外暴露私有资源。Pangolin 可以作为 Cloudflare Tunnels 和 Ngrok 的替代方案。

# CAVEATS

需要一个正在运行的 Pangolin 服务器组件。客户端 ID 和密钥必须先在服务器上完成配置。配套的隧道客户端名为 Newt。

# SEE ALSO

[ssh](/man/ssh)(1), [ngrok](/man/ngrok)(1)
