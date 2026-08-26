# TAGLINE

为 Kubernetes 资源添加或更新注解

# TLDR

**为资源添加注解**

```kubectl annotate [pod/mypod] [key]=[value]```

**删除注解**

```kubectl annotate [pod/mypod] [key]-```

**覆盖现有注解**

```kubectl annotate --overwrite [pod/mypod] [key]=[newvalue]```

**为命名空间中的所有 Pod 添加注解**

```kubectl annotate pods --all [key]=[value]```

# SYNOPSIS

**kubectl** **annotate** [_type_/_name_] _key_=_value_ [_options_]

# PARAMETERS

**--overwrite**
> 允许覆盖现有注解。

**--all**
> 选择指定类型的所有资源。

**--selector** _selector_
> 用于过滤的标签选择器。

**-n**, **--namespace** _name_
> Kubernetes 命名空间。

# DESCRIPTION

**kubectl annotate** 为 Kubernetes 资源添加或更新注解。注解是用于存储元数据的键值对。与标签不同，注解不用于选择资源，而是供工具和库使用。

# INSTALL

```apt: sudo apt install kubectl```

```pacman: sudo pacman -S kubectl```

```apk: sudo apk add kubectl```

```brew: brew install kubectl```

```nix: nix profile install nixpkgs#kubectl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kubectl-label](/man/kubectl-label)(1)
