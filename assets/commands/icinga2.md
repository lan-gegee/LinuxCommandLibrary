# TAGLINE

检查主机和服务可用性的监控系统

# TLDR

**检查配置**

```icinga2 daemon -C```

**启动 Icinga 2**

```sudo systemctl start icinga2```

**重载配置**

```sudo systemctl reload icinga2```

**显示功能特性**

```icinga2 feature list```

**启用功能特性**

```sudo icinga2 feature enable [api]```

**列出对象**

```icinga2 object list --type Host```

# SYNOPSIS

**icinga2** _command_ [_options_]

# PARAMETERS

**daemon** [**-C**]
> 运行守护进程（或使用 -C 检查配置）。

**feature** _subcommand_
> 管理功能特性（list、enable、disable）。

**object** _subcommand_
> 对象管理（list）。

**node** _subcommand_
> 节点/集群管理。

**pki** _subcommand_
> PKI/证书管理。

**console**
> 打开调试控制台。

**--version**
> 显示版本。

# DESCRIPTION

**Icinga 2** 是一个监控系统，用于检查主机和服务的可用性。它支持分布式监控和高级配置，并可与多种后端集成。

Icinga 2 使用领域特定语言（DSL）进行配置，支持模板、apply 规则，以及通过 API 进行运行时修改。

# FEATURES

- 主机与服务监控
- 分布式/集群部署
- REST API
- Graphite/InfluxDB 集成
- 通知系统
- 性能数据

# CAVEATS

配置语法与 Icinga 1/Nagios 不同。集群部署需要 PKI。大型部署需要调优。Web 界面（Icinga Web 2）需单独安装。

# HISTORY

Icinga 于 **2009 年**因项目治理分歧从 **Nagios** 分叉而来。发布于 **2014 年**的 Icinga 2 是一次完全重写，采用现代架构和全新的配置语言。

# INSTALL

```apt: sudo apt install icinga2-bin```

```apk: sudo apk add icinga2```

```zypper: sudo zypper install icinga2-bin```

```nix: nix profile install nixpkgs#icinga2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nagios](/man/nagios)(8), [prometheus](/man/prometheus)(1)
