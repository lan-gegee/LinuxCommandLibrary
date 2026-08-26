# TAGLINE

从命令行管理 Kubernetes Secret

# TLDR

**列出 Secret**

```k8sec list```

**获取 Secret 值**

```k8sec get [secret-name]```

**设置 Secret**

```k8sec set [secret-name] [key=value]```

**删除 Secret 键**

```k8sec unset [secret-name] [key]```

**在命名空间中列出**

```k8sec list -n [namespace]```

**以环境变量形式导出 Secret**

```k8sec dump [secret-name]```

# SYNOPSIS

**k8sec** _command_ [_options_]

# PARAMETERS

**list**
> 列出 Secret。

**get** _NAME_
> 获取 Secret 值。

**set** _NAME_ _KEY=VALUE_
> 设置 Secret 键。

**unset** _NAME_ _KEY_
> 移除 Secret 键。

**dump** _NAME_
> 导出为环境变量。

**-n** _NAMESPACE_
> Kubernetes 命名空间。

**--help**
> 显示帮助信息。

# DESCRIPTION

**k8sec** 从命令行管理 Kubernetes Secret。它简化了 Secret 值的查看和编辑。

该工具会自动解码 base64。相比 kubectl，它为 Secret 管理提供了更简单的接口。

# CAVEATS

需要 kubeconfig。Secret 以 base64 存储。请考虑 RBAC 权限。

# HISTORY

k8sec 的创建目的是通过更直观的命令行界面简化 Kubernetes Secret 管理。

# SEE ALSO

[kubectl](/man/kubectl)(1), [kubeseal](/man/kubeseal)(1), [vault](/man/vault)(1)
