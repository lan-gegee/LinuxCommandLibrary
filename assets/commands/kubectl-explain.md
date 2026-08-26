# TAGLINE

显示资源和字段的文档

# TLDR

**解释资源**

```kubectl explain [pod]```

**解释字段**

```kubectl explain [pod.spec]```

**解释嵌套字段**

```kubectl explain [pod.spec.containers]```

**显示递归结构**

```kubectl explain [pod] --recursive```

**解释指定的 API 版本**

```kubectl explain [deployment] --api-version=[apps/v1]```

# SYNOPSIS

**kubectl explain** [_options_] _resource_

# PARAMETERS

_RESOURCE_
> 资源类型和可选的字段路径。

**--recursive**
> 递归显示所有字段。

**--api-version** _VERSION_
> 解释指定的 API 版本。

**--help**
> 显示帮助信息。

# DESCRIPTION

**kubectl explain** 显示资源和字段的文档。它展示 Kubernetes 对象的 schema。

该命令有助于正确编写清单。它会显示字段的类型、默认值和描述。

# CAVEATS

kubectl 的子命令。文档来自 API 服务器。因 Kubernetes 版本而异。

# HISTORY

kubectl explain 为 **Kubernetes** 资源编写提供内置的 API 文档。

# INSTALL

```apt: sudo apt install kubectl```

```pacman: sudo pacman -S kubectl```

```apk: sudo apk add kubectl```

```brew: brew install kubectl```

```nix: nix profile install nixpkgs#kubectl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kubectl-api-resources](/man/kubectl-api-resources)(1)
