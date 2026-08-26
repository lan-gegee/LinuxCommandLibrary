# TAGLINE

为 deployment、replica set 创建 Horizontal Pod Autoscaler

# TLDR

**为 deployment 创建 HPA**

```kubectl autoscale deployment [name] --min=[2] --max=[10] --cpu-percent=[80]```

**自动扩缩 replication controller**

```kubectl autoscale rc [name] --max=[5]```

**以指定名称创建 HPA**

```kubectl autoscale deployment [name] --name=[hpa-name] --max=[10]```

# SYNOPSIS

**kubectl** **autoscale** _type_ _name_ [_options_]

# PARAMETERS

**--min** _count_
> 最小副本数。

**--max** _count_
> 最大副本数。

**--cpu-percent** _percent_
> 目标 CPU 使用率百分比。

**--name** _name_
> HPA 资源的名称。

**-n**, **--namespace** _name_
> Kubernetes 命名空间。

# DESCRIPTION

**kubectl autoscale** 为 deployment、replica set 或 replication controller 创建 Horizontal Pod Autoscaler（HPA）。根据 CPU 使用率或自定义指标自动伸缩 Pod 数量。

# INSTALL

```apt: sudo apt install kubectl```

```pacman: sudo pacman -S kubectl```

```apk: sudo apk add kubectl```

```brew: brew install kubectl```

```nix: nix profile install nixpkgs#kubectl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kubectl-scale](/man/kubectl-scale)(1)
