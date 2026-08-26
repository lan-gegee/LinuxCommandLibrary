# TAGLINE

在默认编辑器中打开资源的配置

# TLDR

**在编辑器中编辑 deployment**

```kubectl edit deployment [name]```

**编辑 Pod**

```kubectl edit pod [pod-name]```

**使用指定编辑器编辑**

```EDITOR=nano kubectl edit deployment [name]```

**以 YAML 格式编辑资源**

```kubectl edit deployment [name] -o yaml```

# SYNOPSIS

**kubectl** **edit** _type_/_name_ [_options_]

# PARAMETERS

**-o**, **--output** _format_
> 编辑格式（yaml、json）。

**-n**, **--namespace** _name_
> Kubernetes 命名空间。

**--record**
> 将命令记录在资源注解中。

# DESCRIPTION

**kubectl edit** 在你的默认编辑器中打开资源的配置。保存并退出后更改即被应用。应用前会对资源进行校验。设置 EDITOR 或 KUBE_EDITOR 环境变量可以更换编辑器。

# INSTALL

```apt: sudo apt install kubectl```

```pacman: sudo pacman -S kubectl```

```apk: sudo apk add kubectl```

```brew: brew install kubectl```

```nix: nix profile install nixpkgs#kubectl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kubectl-patch](/man/kubectl-patch)(1)
