# TAGLINE

找出未被任何 Pod 引用的 Kubernetes Secret

# TLDR

**检测集群中未使用的 Secret**

```k8s-unused-secret-detector```

**检查指定命名空间**

```k8s-unused-secret-detector -n [namespace]```

**检测并删除命名空间中未使用的 Secret**

```k8s-unused-secret-detector -n [namespace] | kubectl delete secret -n [namespace]```

# SYNOPSIS

**k8s-unused-secret-detector** [_options_]

# PARAMETERS

**-n** _namespace_
> 检查指定的命名空间。

**--context** _context_
> 指定要使用的 kubectl context。

# DESCRIPTION

**k8s-unused-secret-detector** 检测不再被任何资源引用的未使用 Kubernetes Secret。它把 Secret 名称输出到 stdout，可以通过管道传给 kubectl 进行删除。注意：该项目已归档，不再维护；可以考虑改用 [kubectl-reap](https://github.com/micnncim/kubectl-reap)。

# SEE ALSO

[kubectl](/man/kubectl)(1), [k9s](/man/k9s)(1)
