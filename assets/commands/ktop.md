# TAGLINE

类 top 的 Kubernetes 集群监控工具

# TLDR

**监控当前 Kubernetes 集群**

```ktop```

**监控指定命名空间**

```ktop -n [namespace]```

**使用指定的 kubeconfig**

```ktop --kubeconfig [path/to/config]```

**使用指定的上下文**

```ktop --context [context-name]```

**监控所有命名空间**

```ktop -A```

# SYNOPSIS

**ktop** [_options_]

# PARAMETERS

**-n**, **--namespace** _NAME_
> 要监控的命名空间（默认：全部或当前上下文）。

**-A**, **--all-namespaces**
> 显示所有命名空间中的 Pod。

**--kubeconfig** _PATH_
> kubeconfig 文件路径。

**--context** _NAME_
> 要使用的 Kubernetes 上下文。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ktop** 是一款面向 Kubernetes 集群的终端 UI 监控工具，类似于 Linux 上的 **htop**。它实时可视化集群资源使用情况，包括跨节点和 Pod 的 CPU、内存、磁盘和 GPU。

TUI 显示集群概览（总资源和聚合利用率）、每个节点的指标（CPU、内存、Pod 数量），以及可排序的 Pod 列表（含资源消耗和重启次数）。指标默认每 2 秒更新一次。

# CAVEATS

需要可用的 kubectl 配置，且集群中部署了 metrics-server。GPU 监控需要相应的驱动和设备插件。

# HISTORY

**ktop** 由 **Vladimir Vivien** (vladimirvivien) 创建，使用 **Go** 编写。它的灵感来自 **top** 和 **htop** 等经典 Unix 监控工具，并针对 Kubernetes 集群监控进行了改造。

# INSTALL

```zypper: sudo zypper install ktop```

```brew: brew install ktop```

```nix: nix profile install nixpkgs#ktop```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [k9s](/man/k9s)(1), [htop](/man/htop)(1)
