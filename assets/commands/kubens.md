# TAGLINE

切换默认的 Kubernetes 命名空间

# TLDR

**列出命名空间**

```kubens```

**切换命名空间**

```kubens [namespace]```

**切换到上一个**

```kubens -```

**显示当前命名空间**

```kubens -c```

# SYNOPSIS

**kubens** [_options_] [_namespace_]

# PARAMETERS

_NAMESPACE_
> 要切换到的命名空间。

**-**
> 切换到上一个命名空间。

**-c**
> 显示当前命名空间。

**--help**
> 显示帮助信息。

# DESCRIPTION

**kubens** 是一个快速切换当前上下文中默认 Kubernetes 命名空间的工具。它会修改 kubeconfig 中的 namespace 字段，使后续的 kubectl 命令直接作用于选定的命名空间，无需每次都加 `-n` 标志。

不带参数调用时，该工具会列出所有可用的命名空间，并支持通过 fzf 集成进行交互式模糊选择。它还可以用 `-` 切换回上一个活动的命名空间。作为 kubectx 的配套工具设计，kubens 补全了高效浏览多集群、多命名空间 Kubernetes 环境的工作流。

# CAVEATS

第三方工具。会修改 kubeconfig。与 kubectx 配合使用。

# HISTORY

kubens 由 **Ahmet Alp Balkan** 与 kubectx 一同创建，用于简化 Kubernetes 命名空间的切换。

# INSTALL

```apt: sudo apt install kubectx```

```pacman: sudo pacman -S kubectx```

```apk: sudo apk add kubectx```

```zypper: sudo zypper install kubectx```

```brew: brew install kubectx```

```nix: nix profile install nixpkgs#kubectx```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kubectx](/man/kubectx)(1), [kubectl-config](/man/kubectl-config)(1)
