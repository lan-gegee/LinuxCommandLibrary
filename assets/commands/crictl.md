# TAGLINE

兼容 CRI 的容器运行时 CLI

# TLDR

**列出容器**

```crictl ps```

**列出所有容器（包括已停止的）**

```crictl ps -a```

**列出镜像**

```crictl images```

**拉取镜像**

```crictl pull [image:tag]```

**根据配置运行 pod**

```crictl runp [pod.json]```

**创建容器**

```crictl create [pod-id] [container.json] [pod.json]```

**启动容器**

```crictl start [container-id]```

**在容器中执行命令**

```crictl exec -it [container-id] [/bin/sh]```

**查看容器日志**

```crictl logs [container-id]```

**删除容器**

```crictl rm [container-id]```

**停止并删除 pod**

```crictl stopp [pod-id] && crictl rmp [pod-id]```

# SYNOPSIS

**crictl** [_global_options_] _command_ [_options_] [_arguments_]

# DESCRIPTION

**crictl** 是面向兼容 CRI 的容器运行时的命令行界面。CRI（Container Runtime Interface，容器运行时接口）是让 Kubernetes 得以配合不同容器运行时工作的插件接口。crictl 为 Kubernetes 节点提供调试与检查工具，直接与 containerd、CRI-O 或其他兼容 CRI 的运行时交互。

不同于面向通用容器管理的 docker 或 podman，crictl 专为 Kubernetes 故障排查而打造。它暴露 CRI API 操作，让集群管理员能够检查 CRI 运行时层中实际存在的 pod 沙箱、容器和镜像，从而帮助诊断 pod 调度、容器创建和镜像拉取等方面的问题。

# COMMANDS

**ps**
> 列出容器

**pods**
> 列出 pod

**images**
> 列出镜像

**pull**
> 拉取镜像

**run**
> 运行新容器

**exec**
> 在容器中执行命令

**logs**
> 查看容器日志

**attach**
> 连接到容器

**start/stop**
> 启动/停止容器

**rm**
> 删除容器

**rmi**
> 删除镜像

**runp/stopp/rmp**
> 运行/停止/删除 pod

**inspect**
> 检查容器

**inspecti**
> 检查镜像

**inspectp**
> 检查 pod

**stats**
> 容器资源使用情况

**info**
> 运行时信息

# PARAMETERS

**-r**, **--runtime-endpoint** _endpoint_
> CRI 运行时端点（例如 unix:///run/containerd/containerd.sock）。

**-i**, **--image-endpoint** _endpoint_
> CRI 镜像端点。

**--timeout** _duration_
> 连接超时秒数（默认：2）。

**--config** _path_
> 客户端配置文件的位置（默认：/etc/crictl.yaml）。

**-D**, **--debug**
> 启用调试输出。

# CONFIGURATION

**~/.crictl.yaml** or **/etc/crictl.yaml**

```yaml
runtime-endpoint: unix:///run/containerd/containerd.sock
image-endpoint: unix:///run/containerd/containerd.sock
timeout: 10
debug: false
```

# CAVEATS

必须以适当的权限运行（通常是 root）。命令语法与 docker CLI 不同。主要用于调试 Kubernetes 节点，不适合通用容器管理。命令行标志优先于环境变量，环境变量又优先于配置文件。

# HISTORY

**crictl** 属于由 **Kubernetes SIGs** 维护的 **cri-tools** 项目。它的诞生是为了给兼容 CRI 的容器运行时提供一个标准的调试排障工具，取代各运行时专有的 CLI 来检查 Kubernetes 节点。

# INSTALL

```dnf: sudo dnf install cri-tools```

```pacman: sudo pacman -S crictl```

```apk: sudo apk add cri-tools```

```zypper: sudo zypper install cri-tools```

```brew: brew install cri-tools```

```nix: nix profile install nixpkgs#cri-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [ctr](/man/ctr)(1), [podman](/man/podman)(1), [nerdctl](/man/nerdctl)(1)
