# TAGLINE

管理数据库集群的防火墙规则

# TLDR

**列出防火墙规则**

```doctl databases firewalls list [cluster_id]```

**为 IP 添加防火墙规则**

```doctl databases firewalls append [cluster_id] --rule ip_addr:[ip]```

**为 droplet 添加防火墙规则**

```doctl databases firewalls append [cluster_id] --rule droplet:[droplet_id]```

**移除防火墙规则**

```doctl databases firewalls remove [cluster_id] [rule_uuid]```

# SYNOPSIS

**doctl** **databases** **firewalls** _command_ [_options_]

# SUBCOMMANDS

**list**
> 列出防火墙规则。

**append**
> 添加防火墙规则。

**remove**
> 移除防火墙规则。

# DESCRIPTION

**doctl databases firewalls** 管理 DigitalOcean 托管数据库集群的可信来源（防火墙规则）。规则控制哪些 IP、droplet、Kubernetes 集群或标签可以建立连接。

出于安全考虑，托管数据库集群默认拒绝所有入站连接。防火墙规则用于显式允许来自特定来源的访问。你可以授权单个 IP 地址、整个 droplet、Kubernetes 集群，或由标签标识的资源。这样既能安全地访问数据库，又能阻止未授权连接。

规则可以添加、列出和移除，以适应不断变化的基础设施需求。每条规则由一个 UUID 标识，便于管理操作。

# INSTALL

```dnf: sudo dnf install doctl```

```pacman: sudo pacman -S doctl```

```apk: sudo apk add doctl```

```brew: brew install doctl```

```nix: nix profile install nixpkgs#doctl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[doctl-databases](/man/doctl-databases)(1)
