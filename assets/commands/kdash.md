# TAGLINE

用 Rust 编写的快速 Kubernetes 终端仪表板

# TLDR

**启动 Kubernetes 仪表板**

```kdash```

**使用指定的 kubeconfig**

```kdash -c [~/.kube/config]```

**设置刷新间隔**

```kdash -t [5]```

# SYNOPSIS

**kdash** [_options_]

# PARAMETERS

**-c**, **--config** _file_
> kubeconfig 文件路径。

**-t**, **--tick-rate** _seconds_
> 刷新间隔（秒）。

**-n**, **--namespace** _name_
> 要查看的默认命名空间。

# DESCRIPTION

**kdash** 是一个用 Rust 编写的快速 Kubernetes 终端仪表板。它提供集群资源、节点指标和 Pod 状态的只读视图。资源利用率数据需要 metrics-server。使用键盘快捷键进行导航。

# CAVEATS

集群上需要部署 metrics-server 才能获取资源指标。通过 Docker 运行时，在 Minikube 或 Kind 上可能无法正常工作。

# INSTALL

```brew: brew install kdash```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [k9s](/man/k9s)(1)
