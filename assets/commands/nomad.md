# TAGLINE

HashiCorp 出品的工作负载编排器

# TLDR

**启动开发代理**

```nomad agent -dev```

**运行一个作业**

```nomad job run [job.nomad]```

**显示作业状态**

```nomad job status [job_name]```

**停止一个作业**

```nomad job stop [job_name]```

**列出正在运行的作业**

```nomad job status```

**显示节点状态**

```nomad node status```

**查看分配（allocation）日志**

```nomad alloc logs [alloc_id]```

# SYNOPSIS

**nomad** [_options_] _command_ [_args_]

# DESCRIPTION

**nomad** 是 HashiCorp 出品的工作负载编排器。它可以在集群中部署和管理应用，支持容器、虚拟机和独立可执行文件。

该工具提供调度、服务发现和滚动更新。它与 Consul 和 Vault 集成，提供服务网格和密钥管理能力。

# PARAMETERS

**agent**
> 运行 Nomad 代理。

**job run** _file_
> 提交一个作业。

**job plan** _file_
> 试运行一个作业并显示调度影响。

**job status** [_job_]
> 作业状态。

**job stop** _job_
> 停止一个作业。

**node status**
> 节点信息。

**alloc status** _id_
> 分配详情。

**alloc logs** _id_
> 分配日志。

**server members**
> 服务器集群信息。

**-dev**
> 开发模式。

**-address** _addr_
> Nomad API 地址（默认：http://127.0.0.1:4646）。

**-region** _region_
> 要查询的区域。

**-namespace** _ns_
> 目标命名空间。

**-token** _token_
> 要使用的 ACL 令牌。

# CAVEATS

搭建集群需要规划。生产环境需要 ACL。资源限制很重要。服务发现建议使用 Consul。

# HISTORY

**Nomad** 由 **HashiCorp** 于 **2015 年**发布，作为 Kubernetes 在工作负载调度上更简单的替代方案。它专注于运维简洁性，同时支持容器之外的多种工作负载类型。

# INSTALL

```pacman: sudo pacman -S nomad```

```nix: nix profile install nixpkgs#nomad```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[consul](/man/consul)(1), [vault](/man/vault)(1), [docker](/man/docker)(1), [kubectl](/man/kubectl)(1)
