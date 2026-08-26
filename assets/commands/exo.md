# TAGLINE

Exoscale 云服务的命令行界面

# TLDR

**配置 CLI 凭据**

```exo config add```

**列出计算实例**

```exo compute instance list```

**在指定可用区创建计算实例**

```exo compute instance create [name] --zone [ch-gva-2]```

**SSH 登录某个实例**

```exo compute instance ssh [instance_name]```

**列出 IAM API 密钥**

```exo iam api-key list```

**列出对象存储桶**

```exo storage list```

**显示当前账户限额**

```exo limits```

# SYNOPSIS

**exo** _command_ [_subcommand_] [_options_]

# PARAMETERS

_COMMAND_
> 服务：compute、iam、storage、dns 等。

**compute** _SUBCOMMAND_
> 管理计算资源（实例、安全组、负载均衡器、SKS 集群等）。

**dbaas** _SUBCOMMAND_
> 管理数据库即服务（DBaaS）实例。

**dns** _SUBCOMMAND_
> 管理 DNS 区域和记录。

**iam** _SUBCOMMAND_
> 身份与访问管理（API 密钥、角色、组织策略）。

**storage** _SUBCOMMAND_
> 对象存储操作（存储桶、上传、下载）。

**config** _SUBCOMMAND_
> 管理 CLI 配置和凭据。

**zone**
> 列出可用区。

**limits**
> 显示当前账户的资源限额。

**status**
> 显示 Exoscale 平台状态。

**version**
> 输出 CLI 版本。

**--help**
> 显示帮助信息。

# CONFIGURATION

**~/.config/exoscale/exoscale.toml**
> 存储 API 凭据以及默认的可用区/账户设置。

# DESCRIPTION

**exo** 是 Exoscale（一家欧洲云计算提供商）的命令行界面。它管理计算实例、存储、DNS 以及其他云资源。

该工具为所有 Exoscale 服务提供命令，包括 SKS（Kubernetes）、DBaaS、专用推理和网络。配置中保存用于身份验证的 API 凭据。

exo 让你无需 Web 控制台即可实现基础设施的自动化与管理。

# CAVEATS

需要 Exoscale 账户和 API 密钥。某些操作可能产生费用。可用性因可用区而异。部分功能需要特定订阅。

# HISTORY

exo 是 **Exoscale** 的官方 CLI。Exoscale 是一家成立于 **2011 年**的瑞士云服务商，提供符合 GDPR 的云基础设施，专注于欧洲数据主权。

# INSTALL

```dnf: sudo dnf install exo```

```pacman: sudo pacman -S exo```

```apk: sudo apk add exoscale```

```nix: nix profile install nixpkgs#exo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aws](/man/aws)(1), [gcloud](/man/gcloud)(1), [az](/man/az)(1), [doctl](/man/doctl)(1)
