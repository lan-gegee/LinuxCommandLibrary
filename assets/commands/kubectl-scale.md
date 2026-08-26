# TAGLINE

为 deployment、replica set 或 replication controller 设置新的大小

# TLDR

**伸缩 deployment 副本数**

```kubectl scale deployment [name] --replicas=[3]```

**伸缩多个 deployment**

```kubectl scale deployment [name1] [name2] --replicas=[3]```

**带当前副本数前置条件伸缩**

```kubectl scale deployment [name] --current-replicas=[2] --replicas=[3]```

**从文件伸缩**

```kubectl scale -f [manifest.yaml] --replicas=[5]```

# SYNOPSIS

**kubectl** **scale** _type_ _name_ **--replicas=**_count_ [_options_]

# PARAMETERS

**--replicas** _count_
> 目标副本数。

**--current-replicas** _count_
> 当前副本数的前置条件。

**-f**, **--filename** _file_
> 要伸缩的资源文件。

**--timeout** _duration_
> 伸缩操作的超时时间。

# DESCRIPTION

**kubectl scale** 调整 deployment、replica set、replication controller 和 statefulset 的副本数，让你可以按需增加或减少运行中的 Pod 实例数量。更改立即生效，Kubernetes 控制器管理器会将实际状态调和至期望的副本数。

该命令支持一个前置条件标志（--current-replicas），当当前副本数与期望值不匹配时伸缩操作将失败，这有助于防止自动化工作流中的竞态条件。你还可以对清单文件中定义的资源进行伸缩，并在单次调用中将操作应用到多个资源。

# INSTALL

```apt: sudo apt install kubectl```

```pacman: sudo pacman -S kubectl```

```apk: sudo apk add kubectl```

```brew: brew install kubectl```

```nix: nix profile install nixpkgs#kubectl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kubectl-autoscale](/man/kubectl-autoscale)(1)
