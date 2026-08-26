# TAGLINE

面向 Kubernetes 的 GitOps 持续交付 CLI

# TLDR

**登录** Argo CD 服务器

```argocd login [argocd.example.com]```

**列出**应用

```argocd app list```

**创建**应用

```argocd app create [app-name] --repo [https://github.com/user/repo] --path [k8s/] --dest-server [https://kubernetes.default.svc]```

**同步**应用

```argocd app sync [app-name]```

**获取**应用详情

```argocd app get [app-name]```

# SYNOPSIS

**argocd** _command_ [_options_]

# DESCRIPTION

**argocd** 是 Argo CD 的 CLI。Argo CD 是面向 Kubernetes 的声明式 GitOps 持续交付工具，该 CLI 通过 Argo CD 服务器管理应用、集群、仓库和项目。

该工具支持 GitOps 工作流，即以 Git 仓库作为 Kubernetes 应用定义的唯一事实来源。

# PARAMETERS

**login** _server_
> 向 Argo CD 服务器进行身份验证

**app** _command_
> 应用管理命令

**cluster** _command_
> 集群管理命令

**repo** _command_
> 仓库管理命令

**proj** _command_
> 项目管理命令

**account** _command_
> 账户管理命令

**--server** _url_
> Argo CD 服务器地址

**--auth-token** _token_
> 身份验证令牌

**--grpc-web**
> 使用 gRPC-Web 通信

**--insecure**
> 跳过 TLS 验证

# CONFIGURATION

**~/.config/argocd/config**
> 存储 Argo CD 服务器的身份验证上下文，包括服务器地址和身份验证令牌。

# CAVEATS

需要运行中的 Argo CD 服务器。服务器必须能访问 Git 仓库和 Kubernetes 集群。RBAC 控制对应用的访问。

# HISTORY

**Argo CD** 由 Intuit 创建并于 **2018** 年开源。它成为 CNCF 孵化项目，确立了其作为 Kubernetes 领先 GitOps 解决方案的地位。

# INSTALL

```pacman: sudo pacman -S argocd```

```brew: brew install argocd```

```nix: nix profile install nixpkgs#argocd```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[kubectl](/man/kubectl)(1), [helm](/man/helm)(1), [flux](/man/flux)(1)

# RESOURCES

```[Source code](https://github.com/argoproj/argo-cd)```

```[Documentation](https://argo-cd.readthedocs.io)```

<!-- verified: 2026-06-15 -->
