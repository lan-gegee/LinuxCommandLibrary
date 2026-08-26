# TAGLINE

Hetzner Cloud 的命令行界面

# TLDR

**列出服务器**

```hcloud server list```

**创建服务器**

```hcloud server create --name [myserver] --type [cx22] --image [ubuntu-24.04]```

**SSH 连接到服务器**

```hcloud server ssh [myserver]```

**删除服务器**

```hcloud server delete [myserver]```

**列出镜像**

```hcloud image list```

**创建快照**

```hcloud server create-image [myserver] --type snapshot```

# SYNOPSIS

**hcloud** [_global-options_] _command_ _subcommand_ [_options_]

# PARAMETERS

_COMMAND_
> 要执行的资源或子命令。

**server**
> 管理云服务器。

**image**
> 管理服务器镜像和快照。

**volume**
> 管理块存储卷。

**network**
> 管理私有网络。

**firewall**
> 管理防火墙及规则。

**load-balancer**
> 管理负载均衡器。

**ssh-key**
> 管理 SSH 密钥。

**certificate**
> 管理 TLS 证书。

**context**
> 管理 CLI 上下文（项目/API 令牌配置档案）。

**config**
> 管理本地 CLI 配置。

**--context** _name_
> 使用指定的上下文而不是当前激活的上下文。

**-o**, **--output** _format_
> 输出格式：table、json 或 yaml。

**--debug**
> 启用调试输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**hcloud** 是 Hetzner Cloud 的命令行界面，用于管理云服务器、镜像、卷和网络。

该工具提供对 Hetzner Cloud 基础设施的完整控制，支持以自动化和脚本方式管理云资源。

# CAVEATS

需要 API 令牌。仅适用于 Hetzner Cloud。某些操作会产生费用。

# HISTORY

hcloud 由 **Hetzner** 开发，是其云平台的官方 CLI。

# INSTALL

```apt: sudo apt install hcloud-cli```

```dnf: sudo dnf install hcloud```

```pacman: sudo pacman -S hcloud```

```apk: sudo apk add hcloud```

```zypper: sudo zypper install hcloud-cli```

```brew: brew install hcloud```

```nix: nix profile install nixpkgs#hcloud```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[doctl](/man/doctl)(1), [aws](/man/aws)(1), [gcloud](/man/gcloud)(1)

# RESOURCES

```[Source code](https://github.com/hetznercloud/cli)```
```[Documentation](https://github.com/hetznercloud/cli/blob/main/docs/reference/manual/hcloud.md)```
```[Homepage](https://www.hetzner.com/cloud)```

<!-- verified: 2026-07-17 -->
