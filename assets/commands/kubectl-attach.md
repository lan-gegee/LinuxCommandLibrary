# TAGLINE

连接到 Pod 中正在运行的容器

# TLDR

**连接到运行中的 Pod**

```kubectl attach [pod-name]```

**连接到 Pod 中的指定容器**

```kubectl attach [pod-name] -c [container-name]```

**带 TTY 的交互式连接**

```kubectl attach [pod-name] -c [container-name] -i -t```

**连接到副本集的第一个 Pod**

```kubectl attach rs/[nginx]```

**在指定命名空间内连接**

```kubectl attach [pod-name] -n [namespace]```

# SYNOPSIS

**kubectl attach** (_POD_ | _TYPE/NAME_) [**-c** _CONTAINER_] [_options_]

# PARAMETERS

**-c**, **--container** _name_
> 容器名称。如果省略，则使用 `kubectl.kubernetes.io/default-container` 注解或 Pod 中的第一个容器。

**-i**, **--stdin**
> 将 stdin 传递给容器。

**-t**, **--tty**
> stdin 是 TTY（分配一个终端）。

**-q**, **--quiet**
> 只输出远程会话的内容。

**--pod-running-timeout** _duration_
> 等待至少一个 Pod 处于运行状态的时间（默认：1m0s）。

**-n**, **--namespace** _name_
> 请求的命名空间范围。

**--context** _name_
> 要使用的 kubeconfig 上下文。

**--kubeconfig** _path_
> kubeconfig 文件的路径。

# DESCRIPTION

**kubectl attach** 将你的终端连接到容器内已在运行的进程的 stdin/stdout/stderr 流。与会在容器中启动新进程的 **kubectl exec** 不同，**attach** 挂接到容器的 PID 1（镜像或 Pod 规格中定义的主命令），因此你看到的输出与容器的日志流相同，并且在进程以打开 stdin 的方式启动时可以向其发送输入。

当容器以交互式命令启动时（例如用 `kubectl run -it` 创建的 Pod），请同时使用 **-i -t** 以获得完整的交互式 Shell 体验。要连接多容器 Pod 中的特定容器，请传入 **-c**。使用转义序列 **Ctrl-P Ctrl-Q** 分离连接，让进程继续运行。

# CAVEATS

目标容器必须以打开 stdin 的方式启动（Pod 规格中的 **stdin: true** 或 `kubectl run` 的 **-i**），输入才能被传递。attach 不会重启进程；用 Ctrl-C 不当地关闭连接可能会向进程发送信号。每个容器流同时只有一个 attach 会话是可靠的。

# INSTALL

```apt: sudo apt install kubectl```

```pacman: sudo pacman -S kubectl```

```apk: sudo apk add kubectl```

```brew: brew install kubectl```

```nix: nix profile install nixpkgs#kubectl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kubectl-exec](/man/kubectl-exec)(1), [kubectl-logs](/man/kubectl-logs)(1), [kubectl-run](/man/kubectl-run)(1)
