# TAGLINE

在 Pod 中运行的容器内执行命令

# TLDR

**在 Pod 中执行命令**

```kubectl exec [pod-name] -- [command]```

**打开交互式 Shell**

```kubectl exec -it [pod-name] -- /bin/sh```

**在指定容器中执行**

```kubectl exec [pod-name] -c [container] -- [command]```

**在 Pod 中执行 bash**

```kubectl exec -it [pod-name] -- /bin/bash```

# SYNOPSIS

**kubectl** **exec** [_options_] _pod-name_ **--** _command_ [_args_...]

# PARAMETERS

**-c**, **--container** _name_
> 多容器 Pod 中的容器名称。

**-i**, **--stdin**
> 将 stdin 传递给容器。

**-t**, **--tty**
> 分配 TTY。

**-n**, **--namespace** _name_
> Kubernetes 命名空间。

# DESCRIPTION

**kubectl exec** 直接在运行中的 Kubernetes Pod 所包含的容器内执行命令，功能类似于 `docker exec`。它通过 Kubernetes API 服务器和 kubelet 建立到容器运行时环境的连接，让你可以检查文件、运行诊断或打开交互式 Shell 会话。

双横线（--) 用于分隔 kubectl 的标志与要传给容器的命令及其参数，这是必需的。结合 -i（stdin）和 -t（tty）标志使用时，它可以提供完全交互式的终端会话。对于包含多个容器的 Pod，-c 标志让你指定要操作哪个容器。

# INSTALL

```apt: sudo apt install kubectl```

```pacman: sudo pacman -S kubectl```

```apk: sudo apk add kubectl```

```brew: brew install kubectl```

```nix: nix profile install nixpkgs#kubectl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kubectl-attach](/man/kubectl-attach)(1)
