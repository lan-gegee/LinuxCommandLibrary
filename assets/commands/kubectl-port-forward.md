# TAGLINE

将本地端口转发到 Pod、service 或 deployment

# TLDR

**将本地端口转发到 Pod**

```kubectl port-forward [pod-name] [8080]:[80]```

**转发到 service**

```kubectl port-forward svc/[service-name] [8080]:[80]```

**转发到 deployment**

```kubectl port-forward deployment/[name] [8080]:[80]```

**使用随机本地端口转发**

```kubectl port-forward [pod-name] :[80]```

**监听所有网络接口**

```kubectl port-forward --address [0.0.0.0] [pod-name] [8080]:[80]```

**同时转发多个端口**

```kubectl port-forward [pod-name] [5000]:[5000] [8080]:[80]```

**在指定命名空间内转发**

```kubectl port-forward -n [namespace] svc/[service-name] [8080]:[80]```

# SYNOPSIS

**kubectl** **port-forward** _type_/_name_ [_options_] [_LOCAL_PORT_:]_REMOTE_PORT_ [...]

# PARAMETERS

**--address** _addresses_
> 要监听的地址，逗号分隔（默认：localhost）。只接受 IP 地址或 localhost。

**--pod-running-timeout** _duration_
> 等待至少一个 Pod 处于运行状态的时间（默认：1m0s）

**-n**, **--namespace** _name_
> 请求的 Kubernetes 命名空间范围。

# DESCRIPTION

**kubectl port-forward** 在你本机的本地端口与 Kubernetes 集群内运行的 Pod、service 或 deployment 的端口之间创建网络隧道。发送到本地端口的流量会经由 Kubernetes API 服务器转发到目标资源，让你无需通过 LoadBalancer 或 NodePort 暴露服务即可访问集群内部服务。

这对调试、访问仪表盘、连接数据库或测试未公开暴露的服务特别有用。默认它监听 localhost，但可以使用 --address 标志绑定其他接口，例如用 0.0.0.0 在局域网内共享访问。端口映射以 LOCAL_PORT:REMOTE_PORT 的形式指定。如果省略 LOCAL_PORT，则分配一个随机的空闲端口。隧道将保持活动，直到命令被终止。

# INSTALL

```apt: sudo apt install kubectl```

```pacman: sudo pacman -S kubectl```

```apk: sudo apk add kubectl```

```brew: brew install kubectl```

```nix: nix profile install nixpkgs#kubectl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kubectl-proxy](/man/kubectl-proxy)(1), [kubectl-expose](/man/kubectl-expose)(1), [kubectl-exec](/man/kubectl-exec)(1)
