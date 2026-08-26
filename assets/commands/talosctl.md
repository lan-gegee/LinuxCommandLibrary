# TAGLINE

管理 Talos Linux Kubernetes 节点

# TLDR

**生成配置**

```talosctl gen config [cluster-name] [https://endpoint:6443]```

**应用配置**

```talosctl apply-config --nodes [192.168.1.10] --file [controlplane.yaml]```

引导启动集群

```talosctl bootstrap --nodes [192.168.1.10]```

获取集群信息

```talosctl --nodes [192.168.1.10] dashboard```

显示服务

```talosctl --nodes [192.168.1.10] services```

查看日志

```talosctl --nodes [192.168.1.10] logs [kubelet]```

获取 kubeconfig

```talosctl kubeconfig --nodes [192.168.1.10]```

# SYNOPSIS

**talosctl** [_--nodes nodes_] [_--endpoints endpoints_] _command_ [_options_]

# PARAMETERS

**--nodes** _NODES_
> 目标节点。

**--endpoints** _ENDPOINTS_
> API 端点。

**-n** _NODE_
> 单个节点。

**--talosconfig** _FILE_
> 配置文件。

# COMMANDS

**gen config** - 生成配置
**apply-config** - 应用到节点
**bootstrap** - 引导启动 etcd
**kubeconfig** - 获取 kubeconfig
**dashboard** - 节点仪表盘
**services** - 列出服务
**logs** - 查看日志

# DESCRIPTION

**talosctl** 是管理 Talos Linux 的命令行工具。Talos Linux 是专为运行 Kubernetes 打造的最小化、不可变操作系统。它为 Talos 节点提供完整的生命周期管理，从最初的配置生成一直到日常的集群运维。

**gen config** 命令为控制平面节点和工作节点创建机器配置文件，包括安全集群通信所需的证书和密钥。**apply-config** 命令把这些配置推送到节点，**bootstrap** 则在第一个控制平面节点上初始化 etcd 集群以启动 Kubernetes 集群。

在日常运维方面，talosctl 提供用于监控节点健康和资源使用的 **dashboard**、用于检查系统服务运行状态的 **services**，以及用于查看服务输出的 **logs**。**kubeconfig** 命令检索集群凭据供 kubectl 使用。所有与节点的通信都使用 talosconfig 文件中配置的双向 TLS 认证。

# CONFIGURATION

**~/.talos/config**
> 默认的 talosconfig 文件，包含用于向 Talos 节点认证的集群端点、节点地址和 TLS 凭据

**--talosconfig** _FILE_
> 通过命令行标志覆盖默认配置文件的位置

**TALOSCONFIG**
> 用于指定备用 talosconfig 文件路径的环境变量

# CAVEATS

Talos 专用工具。节点必须是 Talos。需要 API 访问权限。

# HISTORY

**Talos** 由 **Sidero Labs** 创建，是一个最小化的不可变 Kubernetes 操作系统。talosctl 提供完整的生命周期管理。

# INSTALL

```pacman: sudo pacman -S talosctl```

```zypper: sudo zypper install talosctl```

```brew: brew install talosctl```

```nix: nix profile install nixpkgs#talosctl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [docker](/man/docker)(1)
