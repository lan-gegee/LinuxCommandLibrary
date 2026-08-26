# TAGLINE

显示客户端和服务器版本

# TLDR

**显示版本**

```kubectl version```

**仅客户端版本**

```kubectl version --client```

**以 JSON 格式输出**

```kubectl version -o json```

**以 YAML 格式输出**

```kubectl version -o yaml```

**短格式**

```kubectl version --short```

# SYNOPSIS

**kubectl version** [_options_]

# PARAMETERS

**--client**
> 仅显示客户端版本。

**-o** _FORMAT_
> 输出格式（json、yaml）。

**--short**
> 简短的输出格式。

**--help**
> 显示帮助信息。

# DESCRIPTION

**kubectl version** 显示客户端和服务器版本。它显示 kubectl 与 Kubernetes API 服务器的版本。

该命令用于验证版本兼容性。客户端与服务器的小版本号相差不应超过一个。

# CAVEATS

kubectl 的子命令。服务器版本需要集群访问权限。版本偏差（skew）很重要。

# HISTORY

kubectl version 为 **Kubernetes** 兼容性验证提供版本检查功能。

# INSTALL

```apt: sudo apt install kubectl```

```pacman: sudo pacman -S kubectl```

```apk: sudo apk add kubectl```

```brew: brew install kubectl```

```nix: nix profile install nixpkgs#kubectl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kubectl-cluster-info](/man/kubectl-cluster-info)(1)
