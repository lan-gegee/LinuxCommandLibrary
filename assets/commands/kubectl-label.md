# TAGLINE

为 Kubernetes 资源添加或更新标签

# TLDR

**为资源添加标签**

```kubectl label [pod/name] [key]=[value]```

**删除标签**

```kubectl label [pod/name] [key]-```

**覆盖现有标签**

```kubectl label --overwrite [pod/name] [key]=[newvalue]```

**用选择器为所有 Pod 打标签**

```kubectl label pods -l [app=myapp] [env]=[production]```

# SYNOPSIS

**kubectl** **label** _type_/_name_ _key_=_value_ [_options_]

# PARAMETERS

**--overwrite**
> 允许覆盖现有标签。

**--all**
> 选择该类型的所有资源。

**-l**, **--selector** _selector_
> 用于过滤的标签选择器。

**-n**, **--namespace** _name_
> Kubernetes 命名空间。

# DESCRIPTION

**kubectl label** 为 Kubernetes 资源（如 Pod、节点、service 和 deployment）添加、更新或移除标签。标签是键值元数据对，是整个 Kubernetes 生态中组织、分组和选择资源的主要机制。service、deployment 和网络策略中的选择器大量使用标签来确定要操作的资源。

添加标签时指定 key=value 对；删除标签时在键名后附加减号（例如 `key-`）。默认情况下，覆盖现有标签需要 --overwrite 标志，以防止意外更改。该命令可以操作单个资源、通过 --all 操作某类型的所有资源，或者操作由标签选择器匹配到的过滤集合。

# INSTALL

```apt: sudo apt install kubectl```

```pacman: sudo pacman -S kubectl```

```apk: sudo apk add kubectl```

```brew: brew install kubectl```

```nix: nix profile install nixpkgs#kubectl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kubectl-annotate](/man/kubectl-annotate)(1)
