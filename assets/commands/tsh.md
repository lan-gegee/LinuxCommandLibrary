# TAGLINE

Teleport 统一基础设施访问客户端

# TLDR

**登录 Teleport 集群**

```tsh login --proxy=[teleport.example.com] --user=[username]```

**列出可用的 SSH 服务器**

```tsh ls```

**SSH 连接到服务器**

```tsh ssh [user]@[hostname]```

**列出 Kubernetes 集群**

```tsh kube ls```

**连接 Kubernetes 集群**

```tsh kube login [cluster-name]```

**列出可用的数据库**

```tsh db ls```

**连接数据库**

```tsh db connect [database-name]```

**列出活动会话**

```tsh sessions ls```

**从集群登出**

```tsh logout```

# SYNOPSIS

**tsh** [_global-options_] _command_ [_command-options_] [_args_...]

# COMMANDS

**login**
> 向 Teleport 集群进行身份验证。

**logout**
> 结束会话并移除凭据。

**status**
> 显示当前登录状态。

**ls**
> 列出可用的 SSH 服务器。

**ssh** _[user@]host_
> 与服务器建立 SSH 会话。

**scp** _src_ _dest_
> 安全复制文件。

**join** _session-id_
> 加入一个活动会话。

**play** _session-id_
> 回放已录制的会话。

**sessions ls**
> 列出活动会话。

**kube** ls|login|credentials
> 管理 Kubernetes 访问。

**db** ls|login|connect|logout
> 管理数据库访问。

**apps** ls|login|logout
> 管理应用访问。

**request** create|ls|show|review
> 管理访问请求。

**config**
> 为原生 SSH 客户端生成 SSH 配置。

**version**
> 显示版本信息。

# PARAMETERS

**--proxy** _address_
> Teleport 代理服务地址。

**--user** _username_
> Teleport 用户名。

**--login** _os-user_
> SSH 登录使用的远程 OS 用户名。

**--ttl** _duration_
> 会话凭据的有效期（TTL）。默认：12h。

**--identity** _file_
> 身份文件路径。

**--auth** _connector_
> 身份验证连接器名称。

**--insecure**
> 跳过 TLS 证书校验。

**--debug**
> 启用详细的调试日志。

**--jumphost**, **-J** _host_
> SSH 跳板机。

**--cert-format** _format_
> 证书格式：standard 或 kubernetes。

**--skip-version-check**
> 跳过客户端/服务器版本兼容性检查。

# DESCRIPTION

**tsh** 是 Teleport 的客户端 CLI，用于访问受 Teleport 保护的基础设施。它为 SSH 服务器、Kubernetes 集群、数据库和 Web 应用提供统一访问，并内置审计日志与访问控制。

通过 **login** 完成身份验证后，凭据存储在 **~/.tsh** 中并自动过期（默认 12 小时）。证书支持短期访问，符合零信任原则。

对于 SSH 访问，可以使用 **ssh** 命令，或用 **tsh config** 生成原生 SSH 配置供标准 ssh 客户端使用。会话录制功能支持通过 **play** 进行审计回放。

通过 **kube login** 访问 Kubernetes 时会配置 kubectl 凭据。通过 **db connect** 访问数据库时，可建立经过身份验证的连接，支持 PostgreSQL、MySQL、MongoDB 等数据库。

访问请求支持带有审批流程的即时权限提升。对需要更高权限的资源，使用 **request create** 创建请求。

# CAVEATS

需要管理员配置的 Teleport 集群访问权限。部分资源需要基于角色的授权或审批。证书 TTL 限制了会话时长。不应在生产环境使用 --insecure 选项。

# HISTORY

Teleport 由 **Gravitational**（现名 Teleport）于 **2016 年**创建，旨在提供带审计日志和基于身份的访问控制的安全基础设施访问。该项目遵循 BeyondCorp/零信任原则实现基于证书的身份验证。Teleport 将核心产品开源，此后逐步扩展到 Kubernetes、数据库和应用领域。

# INSTALL

```aur: yay -S tsh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ssh](/man/ssh)(1), [kubectl](/man/kubectl)(1)
