# TAGLINE

检查授权权限

# TLDR

**检查操作是否被允许**

```kubectl auth can-i [create] [pods]```

**以指定用户身份检查**

```kubectl auth can-i [delete] [deployments] --as [user@example.com]```

**在命名空间内检查**

```kubectl auth can-i [get] [secrets] -n [namespace]```

**列出所有权限**

```kubectl auth can-i --list```

**检查所有命名空间**

```kubectl auth can-i [get] [pods] --all-namespaces```

**调和 RBAC**

```kubectl auth reconcile -f [rbac.yaml]```

# SYNOPSIS

**kubectl auth** _subcommand_ [_options_]

# PARAMETERS

**can-i** _VERB_ _RESOURCE_
> 检查授权。

**reconcile**
> 调和 RBAC 规则。

**--as** _USER_
> 模拟用户身份。

**--as-group** _GROUP_
> 模拟组身份。

**--list**
> 列出所有权限。

**-n** _NAMESPACE_
> 目标命名空间。

**--help**
> 显示帮助信息。

# DESCRIPTION

**kubectl auth** 用于检查授权权限。它验证用户和服务账户可以执行哪些操作。

该命令用于测试 RBAC 策略，对调试访问问题和审计权限很有用。

# CAVEATS

kubectl 的子命令。显示 RBAC 结果。可能无法反映所有策略。

# HISTORY

kubectl auth 为 **Kubernetes** 提供 RBAC 策略的授权检查和访问调试功能。

# INSTALL

```apt: sudo apt install kubectl```

```pacman: sudo pacman -S kubectl```

```apk: sudo apk add kubectl```

```brew: brew install kubectl```

```nix: nix profile install nixpkgs#kubectl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kubectl-config](/man/kubectl-config)(1)
