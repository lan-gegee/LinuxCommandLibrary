# TAGLINE

轻量级 Kubernetes 发行版

# TLDR

**启动 server**

```sudo k3s server```

**以 agent 身份加入**

```sudo k3s agent --server [https://server:6443] --token [token]```

**获取 kubeconfig**

```sudo k3s kubectl config view```

**运行 kubectl 命令**

```k3s kubectl get pods```

**禁用组件后启动**

```sudo k3s server --disable traefik```

**查看 token**

```sudo cat /var/lib/rancher/k3s/server/node-token```

# SYNOPSIS

**k3s** _command_ [_options_]

# PARAMETERS

**server**
> 启动控制平面。

**agent**
> 启动工作节点。

**kubectl**
> 运行 kubectl 命令。

**--server** _URL_
> agent 使用的服务器 URL。

**--token** _TOKEN_
> 加入集群的 token。

**--disable** _COMPONENT_
> 禁用组件。

**--help**
> 显示帮助信息。

# DESCRIPTION

**K3s** 是一个轻量级 Kubernetes 发行版。它能以极少的资源运行完整的 Kubernetes 集群。

该工具把 Kubernetes、containerd 和 Flannel 打包成单个二进制文件。它面向边缘计算、IoT 和开发场景设计。

# CAVEATS

简化的 Kubernetes，单一二进制文件，默认使用 sqlite3。

# HISTORY

K3s 由 **Rancher Labs** 于 2019 年创建，是一个经过认证的轻量级 Kubernetes 发行版。

# INSTALL

```apk: sudo apk add k3s```

```nix: nix profile install nixpkgs#k3s```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [k3d](/man/k3d)(1), [crictl](/man/crictl)(1)
