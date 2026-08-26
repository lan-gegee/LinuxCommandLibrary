# TAGLINE

Kubernetes 终端 UI

# TLDR

**启动 k9s**

```k9s```

**在指定命名空间中启动**

```k9s -n [namespace]```

**使用指定 context 启动**

```k9s --context [context-name]```

**以只读方式启动**

```k9s --readonly```

**显示指定资源**

```k9s --command [pods|deployments|services]```

**列出所有集群资源**

```k9s --all-namespaces```

# SYNOPSIS

**k9s** [_options_]

# PARAMETERS

**-n** _NAMESPACE_
> 在指定命名空间中启动。

**--context** _NAME_
> Kubernetes context。

**--readonly**
> 只读模式。

**--command** _RESOURCE_
> 初始资源视图。

**-A**, **--all-namespaces**
> 所有命名空间。

**--help**
> 显示帮助信息。

# DESCRIPTION

**k9s** 是一个 Kubernetes 终端 UI。它提供基于键盘导航的实时集群管理。

该工具显示 Pod、Deployment、Service 等资源。它支持查看日志、exec 以及编辑资源。

# CAVEATS

需要 kubeconfig。基于终端，需要学习键盘快捷键。

# HISTORY

k9s 由 **Fernand Galiana** 创建，旨在为管理 Kubernetes 集群提供快速的终端界面。

# INSTALL

```dnf: sudo dnf install k9s```

```pacman: sudo pacman -S k9s```

```apk: sudo apk add k9s```

```zypper: sudo zypper install k9s```

```brew: brew install k9s```

```nix: nix profile install nixpkgs#k9s```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [stern](/man/stern)(1), [kubectx](/man/kubectx)(1)
