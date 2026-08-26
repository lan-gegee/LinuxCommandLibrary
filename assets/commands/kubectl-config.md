# TAGLINE

管理 kubeconfig 文件：集群、用户和上下文

# TLDR

**查看**合并后的 kubeconfig

```kubectl config view```

**查看包含密钥的原始** kubeconfig

```kubectl config view --raw```

**显示当前上下文**

```kubectl config current-context```

**列出上下文**

```kubectl config get-contexts```

**切换上下文**

```kubectl config use-context [context-name]```

为当前上下文**设置默认命名空间**

```kubectl config set-context --current --namespace=[namespace]```

**添加一个集群**条目

```kubectl config set-cluster [name] --server=[https://api.example.com]```

**删除上下文**

```kubectl config delete-context [context-name]```

# SYNOPSIS

**kubectl config** _SUBCOMMAND_ [_options_]

# PARAMETERS

**view**
> 显示合并后的 kubeconfig。使用 **--raw** 包含凭据，使用 **--minify** 只显示当前上下文，使用 **-o** 指定其他输出格式。

**current-context**
> 打印当前上下文。

**use-context** _NAME_
> 在 kubeconfig 中设置当前上下文。

**get-contexts** [_NAME_]
> 列出一个或全部上下文。

**set-context** _NAME_ | **--current**
> 创建或修改上下文。使用 **--current** 更新活动上下文（通常与 **--namespace** 一起使用）。

**rename-context** _OLD_ _NEW_
> 重命名上下文。

**delete-context** _NAME_
> 移除一个上下文。

**get-clusters**
> 列出 kubeconfig 中定义的集群。

**set-cluster** _NAME_ [**--server**=_URL_] [**--certificate-authority**=_FILE_] [**--insecure-skip-tls-verify**]
> 创建或修改集群条目。

**delete-cluster** _NAME_
> 移除一个集群条目。

**get-users**
> 列出 kubeconfig 中定义的用户。

**set-credentials** _NAME_ [**--token**=_BEARER_] [**--client-certificate**=_FILE_] [**--client-key**=_FILE_] [**--username**=_USER_ **--password**=_PASS_]
> 创建或修改用户条目。

**delete-user** _NAME_
> 移除一个用户条目。

**set** _PROPERTY_ _VALUE_
> 设置 kubeconfig 中的单个值（点号路径）。

**unset** _PROPERTY_
> 取消设置单个值。

**--kubeconfig** _FILE_
> 操作指定的 kubeconfig 文件，而不是默认的查找链。

**--help**
> 显示帮助信息。

# DESCRIPTION

**kubectl config** 管理 **kubeconfig** 文件，其中存储着与 Kubernetes 集群交互所需的连接详情、凭据和偏好设置。一个 kubeconfig 定义三个列表式部分：**clusters**、**users** 和 **contexts**，其中每个上下文绑定一个集群、一个用户和一个可选的默认命名空间。

默认情况下 kubectl 读取 `~/.kube/config`。加载顺序为：显式的 **--kubeconfig** 标志，其次是 **KUBECONFIG** 环境变量中以冒号分隔的多个路径，最后是 `~/.kube/config`。当 **KUBECONFIG** 列出多个文件时，它们会按顺序合并，冲突时以靠前的文件为准。

这些子命令让你可以查看合并后的视图、在不同上下文之间切换以面向不同的集群、设置每个上下文的默认值（如命名空间），以及添加或移除集群、用户和上下文条目。

# CAVEATS

**kubectl config view** 默认会隐去凭据；当你确实需要密钥内容时使用 **--raw**（并小心处理输出）。**kubectl config** 是 **kubectl** 的子命令：它只编辑 kubeconfig 文件，不与集群通信。对于交互式的上下文和命名空间切换，许多用户更倾向于使用 **kubectx** 和 **kubens**。

# HISTORY

**kubectl config** 自 **Kubernetes** 早期版本起便随 **kubectl** 一同发布，并固化了整个生态（kubectl、client-go、Helm、kustomize 等）使用的 kubeconfig 格式。

# INSTALL

```apt: sudo apt install kubectl```

```pacman: sudo pacman -S kubectl```

```apk: sudo apk add kubectl```

```brew: brew install kubectl```

```nix: nix profile install nixpkgs#kubectl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kubectx](/man/kubectx)(1), [kubens](/man/kubens)(1)
