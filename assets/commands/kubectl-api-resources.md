# TAGLINE

列出 Kubernetes 集群中所有可用的资源类型

# TLDR

**列出所有 API 资源**

```kubectl api-resources```

**仅列出命名空间级资源**

```kubectl api-resources --namespaced=true```

**列出特定 API 组的资源**

```kubectl api-resources --api-group=[apps]```

**显示资源短名称**

```kubectl api-resources -o wide```

**列出资源支持的动词**

```kubectl api-resources --verbs=[list,get]```

# SYNOPSIS

**kubectl** **api-resources** [_options_]

# PARAMETERS

**--namespaced** _bool_
> 过滤命名空间级/集群级资源。

**--api-group** _group_
> 按 API 组过滤。

**--verbs** _verbs_
> 按支持的动词过滤。

**-o** _format_
> 输出格式（wide、name）。

# DESCRIPTION

**kubectl api-resources** 列出 Kubernetes 集群中所有可用的资源类型。显示资源名称、短名称、API 组以及是否属于命名空间级。有助于发现可用的资源类型。

# INSTALL

```apt: sudo apt install kubectl```

```pacman: sudo pacman -S kubectl```

```apk: sudo apk add kubectl```

```brew: brew install kubectl```

```nix: nix profile install nixpkgs#kubectl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kubectl-api-versions](/man/kubectl-api-versions)(1)
