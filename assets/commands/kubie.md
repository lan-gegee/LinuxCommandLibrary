# TAGLINE

使用隔离的 Shell 管理 Kubernetes 上下文

# TLDR

**切换上下文**

```kubie ctx [context]```

**切换命名空间**

```kubie ns [namespace]```

**列出上下文**

```kubie ctx```

**列出命名空间**

```kubie ns```

**在上下文中生成 Shell**

```kubie ctx [context] -n [namespace]```

**执行一条命令**（在特定上下文中，无需生成 Shell）

```kubie exec [context] [namespace] -- [kubectl get pods]```

**显示当前上下文信息**

```kubie info ctx```

**退出 kubie Shell**

```exit```

# SYNOPSIS

**kubie** _command_ [_options_]

# PARAMETERS

**ctx** [_CONTEXT_]
> 切换或列出上下文。

**ns** [_NAMESPACE_]
> 切换或列出命名空间。

**-n** _NAMESPACE_
> 指定命名空间。

**exec** _CONTEXT_ _NAMESPACE_ **--** _CMD_
> 在上下文中执行命令，而不生成 Shell。

**info** _ITEM_
> 显示当前上下文（ctx）或命名空间（ns）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**kubie** 是一个 Kubernetes 上下文和命名空间管理器，它把每次上下文切换隔离在各自的 Shell 会话中。与修改全局 kubeconfig 状态的 kubectx 不同，kubie 会生成一个新的子 Shell，其环境变量指向一份临时 kubeconfig，因此每个终端窗口都可以独立地针对不同的集群和命名空间进行操作，互不干扰。

这种隔离模型避免了多集群工作流中的常见错误来源：在一个终端里切换上下文，却意外影响到另一个终端中正在运行的命令。Kubie 还可以列出可用的上下文和命名空间、针对特定上下文执行一次性命令，并与 fzf 集成以实现交互式选择。它用 Rust 编写，启动迅速且开销极小。

# CAVEATS

每次上下文切换都会生成一个子 Shell，因此深度嵌套的切换会增加 Shell 层级。需要能够访问 kubeconfig 文件。如果安装了 fzf，则支持交互式选择。

# HISTORY

kubie 的诞生是为了提供隔离的上下文管理，避免全局上下文切换带来的种种问题。

# INSTALL

```pacman: sudo pacman -S kubie```

```apk: sudo apk add kubie```

```zypper: sudo zypper install kubie```

```brew: brew install kubie```

```nix: nix profile install nixpkgs#kubie```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kubectx](/man/kubectx)(1), [kubens](/man/kubens)(1)
