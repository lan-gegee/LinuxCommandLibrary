# TAGLINE

列出 Kubernetes 集群中所有可用的 API 版本

# TLDR

**列出所有 API 版本**

```kubectl api-versions```

# SYNOPSIS

**kubectl** **api-versions**

# DESCRIPTION

**kubectl api-versions** 列出 Kubernetes 集群中所有可用的 API 版本。以 group/version 格式显示每个可用的 API。在编写清单时有助于确定支持哪些 API 版本。

# INSTALL

```apt: sudo apt install kubectl```

```pacman: sudo pacman -S kubectl```

```apk: sudo apk add kubectl```

```brew: brew install kubectl```

```nix: nix profile install nixpkgs#kubectl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kubectl-api-resources](/man/kubectl-api-resources)(1)
