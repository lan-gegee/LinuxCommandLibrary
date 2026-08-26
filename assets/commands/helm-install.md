# TAGLINE

将 Helm chart 部署到 Kubernetes 集群，创建新的 release

# TLDR

**安装 chart**

```helm install [release-name] [chart]```

**从软件仓库安装**

```helm install [my-nginx] bitnami/nginx```

**使用自定义 values 文件安装**

```helm install [release] [chart] -f [values.yaml]```

**使用内联值安装**

```helm install [release] [chart] --set [key]=[value]```

**在指定命名空间中安装**

```helm install [release] [chart] -n [namespace]```

**安装并等待 pod 就绪**

```helm install [release] [chart] --wait```

**试运行而不实际安装**

```helm install [release] [chart] --dry-run```

# SYNOPSIS

**helm** **install** [_name_] _chart_ [_options_]

# PARAMETERS

**-f**, **--values** _file_
> 自定义 values YAML 文件。

**--set** _key_=_value_
> 在命令行上内联覆盖值。

**-n**, **--namespace** _namespace_
> 目标命名空间。

**--wait**
> 等待 pod 就绪。

**--timeout** _duration_
> 命令超时时间（默认 5m0s）。

**--dry-run**
> 模拟执行而不实际安装。

**--create-namespace**
> 若命名空间不存在则创建。

# DESCRIPTION

**helm install** 将 Helm chart 部署到 Kubernetes 集群，创建一个新的 release。chart 包含运行应用所需的全部资源定义。Helm 会跟踪 release，便于使用 **helm upgrade** 进行升级和使用 **helm rollback** 进行回滚。使用 **--wait** 可在完成前等待所有 pod 就绪。

# INSTALL

```dnf: sudo dnf install helm```

```pacman: sudo pacman -S helm```

```apk: sudo apk add helm```

```zypper: sudo zypper install helm```

```brew: brew install helm```

```nix: nix profile install nixpkgs#helm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[helm](/man/helm)(1), [kubectl](/man/kubectl)(1)
