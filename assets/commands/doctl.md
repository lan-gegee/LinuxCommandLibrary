# TAGLINE

DigitalOcean 官方命令行界面

# TLDR

**向** DigitalOcean **进行身份验证**

```doctl auth init```

**列出所有 Droplet**

```doctl compute droplet list```

**创建 Droplet**

```doctl compute droplet create [name] --size [s-1vcpu-1gb] --image [ubuntu-22-04-x64] --region [nyc1]```

**删除 Droplet**

```doctl compute droplet delete [droplet_id]```

**列出 Kubernetes 集群**

```doctl kubernetes cluster list```

**获取 kubeconfig**

```doctl kubernetes cluster kubeconfig save [cluster_name]```

**列出可用区域**

```doctl compute region list```

**列出所有数据库**

```doctl databases list```

**列出 Spaces**（对象存储桶）

```doctl spaces list```

**创建容器镜像仓库**

```doctl registry create [name]```

**列出 SSH 密钥**

```doctl compute ssh-key list```

**以 JSON 格式输出**

```doctl compute droplet list --output json```

# SYNOPSIS

**doctl** _command_ [_subcommand_] [_options_]

# PARAMETERS

_COMMAND_
> 资源类型：account、auth、compute、apps、databases、kubernetes、monitoring、projects、registry、serverless、spaces、vpcs 等。

**auth** **init**
> 使用 API 令牌进行身份验证。

**auth** **list**
> 列出可用的身份验证上下文。

**compute** **droplet** _ACTION_
> 管理 Droplet（创建、列出、删除、查询等）。

**compute** **volume** _ACTION_
> 管理块存储卷。

**compute** **domain** _ACTION_
> 管理 DNS 域名和记录。

**compute** **firewall** _ACTION_
> 管理云防火墙。

**compute** **load-balancer** _ACTION_
> 管理负载均衡器。

**kubernetes** **cluster** _ACTION_
> 管理 Kubernetes 集群。

**apps** _ACTION_
> 管理 App Platform 应用。

**databases** _ACTION_
> 管理托管数据库集群。

**spaces** _ACTION_
> 管理 Spaces 对象存储。

**registry** _ACTION_
> 管理容器镜像仓库。

**serverless** _ACTION_
> 管理 Serverless 函数。

**monitoring** _ACTION_
> 管理监控警报策略和在线状态检查。

**projects** _ACTION_
> 组织资源并将其分配到项目。

**--access-token** _TOKEN_
> DigitalOcean API 令牌。覆盖配置文件和 DIGITALOCEAN_ACCESS_TOKEN。

**--output** _FORMAT_
> 输出格式：text、json。

**--format** _COLUMNS_
> 表格输出中要显示的列的列表，以逗号分隔。

**--context** _NAME_
> 使用指定的身份验证上下文。

**--trace**
> 执行命令时显示网络活动日志。

**--verbose**
> 启用详细输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**doctl** 是 DigitalOcean 官方的命令行界面，可用于访问所有 DigitalOcean 服务，包括 Droplets、Kubernetes、App Platform、数据库等。

该工具支持基础设施自动化、CI/CD 集成，以及通过脚本管理 DigitalOcean 资源。它支持多个身份验证上下文，便于管理不同的账号或团队。

doctl 与 DigitalOcean API 的功能一一对应，让你无需使用 Web 控制台即可从命令行完全掌控云资源。

# CAVEATS

需要 DigitalOcean 账号和 API 令牌。某些操作可能产生费用。部分操作不可逆。API 请求受速率限制约束。

# HISTORY

doctl 由 **DigitalOcean** 开发，是其云平台的官方 CLI。它提供对 DigitalOcean 服务的编程式访问，支持 DevOps 工作流和基础设施即代码实践。

# INSTALL

```dnf: sudo dnf install doctl```

```pacman: sudo pacman -S doctl```

```apk: sudo apk add doctl```

```brew: brew install doctl```

```nix: nix profile install nixpkgs#doctl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [terraform](/man/terraform)(1), [aws](/man/aws)(1), [gcloud](/man/gcloud)(1)
