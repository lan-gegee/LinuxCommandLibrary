# TAGLINE

从文件或命令行输入创建 Kubernetes 资源

# TLDR

**从文件创建资源**

```kubectl create -f [manifest.yaml]```

**创建命名空间**

```kubectl create namespace [name]```

**创建 secret**

```kubectl create secret generic [name] --from-literal=[key]=[value]```

**从文件创建 configmap**

```kubectl create configmap [name] --from-file=[path]```

**创建 deployment**

```kubectl create deployment [name] --image=[image:tag]```

# SYNOPSIS

**kubectl** **create** _resource_ [_options_]

# PARAMETERS

**-f**, **--filename** _file_
> 从文件或 URL 创建。

**namespace** _name_
> 创建命名空间。

**deployment** _name_
> 创建 deployment。

**secret** _type_ _name_
> 创建 secret。

**configmap** _name_
> 创建 configmap。

**--dry-run** _mode_
> 只预览而不创建（client、server）。

**-o**, **--output** _format_
> 输出格式。

# DESCRIPTION

**kubectl create** 从文件或命令行输入创建 Kubernetes 资源。与 apply 不同，如果资源已存在，create 将失败。支持创建多种资源类型，包括 deployment、service、secret 和 configmap。

# INSTALL

```apt: sudo apt install kubectl```

```pacman: sudo pacman -S kubectl```

```apk: sudo apk add kubectl```

```brew: brew install kubectl```

```nix: nix profile install nixpkgs#kubectl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kubectl-apply](/man/kubectl-apply)(1)
