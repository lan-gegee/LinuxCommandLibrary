# TAGLINE

快速切换 Kubernetes 上下文

# TLDR

**列出上下文**

```kubectx```

**切换上下文**

```kubectx [context-name]```

**切换到上一个**

```kubectx -```

**删除上下文**

```kubectx -d [context-name]```

**重命名上下文**

```kubectx [new-name]=[old-name]```

**显示当前上下文**

```kubectx -c```

# SYNOPSIS

**kubectx** [_options_] [_context_]

# PARAMETERS

_CONTEXT_
> 要切换到的上下文。

**-**
> 切换到上一个上下文。

**-c**
> 显示当前上下文。

**-d** _NAME_
> 删除上下文。

**--help**
> 显示帮助信息。

# DESCRIPTION

**kubectx** 是一个用于在 kubeconfig 文件中定义的多个 Kubernetes 上下文之间快速切换的工具。相比运行 `kubectl config use-context`，它将上下文切换简化为一条命令，速度更快；并且在未提供参数时支持通过 fzf 集成进行交互式模糊选择。

该工具可以列出所有可用上下文、切换到指定的上下文或用 `-` 切换回上一个活动的上下文，还支持重命名和删除上下文。在管理多个集群时它特别有用，因为它省去了原本需要在开发、预发布和生产环境之间导航时输入冗长 kubectl config 命令的麻烦。

# CAVEATS

第三方工具。需单独安装。配合 kubeconfig 工作。

# HISTORY

kubectx 由 **Ahmet Alp Balkan** 创建，用于简化 Kubernetes 上下文管理。

# INSTALL

```apt: sudo apt install kubectx```

```pacman: sudo pacman -S kubectx```

```apk: sudo apk add kubectx```

```zypper: sudo zypper install kubectx```

```brew: brew install kubectx```

```nix: nix profile install nixpkgs#kubectx```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kubens](/man/kubens)(1), [kubectl-config](/man/kubectl-config)(1)
