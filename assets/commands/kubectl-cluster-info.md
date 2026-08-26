# TAGLINE

显示控制平面和集群服务的地址

# TLDR

**显示集群信息**

```kubectl cluster-info```

**显示详细的集群信息**

```kubectl cluster-info dump```

**将集群信息转储到目录**

```kubectl cluster-info dump --output-directory=[path]```

**转储指定的命名空间**

```kubectl cluster-info dump --namespaces=[default],[kube-system]```

# SYNOPSIS

**kubectl** **cluster-info** [_subcommand_] [_options_]

# PARAMETERS

**dump**
> 转储集群状态用于调试。

**--output-directory** _path_
> 转储文件的目录。

**--namespaces** _list_
> 要包含在转储中的命名空间。

**--all-namespaces**
> 包含所有命名空间。

# DESCRIPTION

**kubectl cluster-info** 显示控制平面和集群服务的地址。dump 子命令收集用于调试的集群状态信息，包括所有 Pod 的日志和集群元数据。

# CAVEATS

需要具有集群访问权限的有效 kubeconfig。对于拥有大量 Pod 的集群，dump 子命令可能产生非常大的输出。使用 `--namespaces` 限制范围。转储输出可能包含环境变量和密钥等敏感信息。

# INSTALL

```apt: sudo apt install kubectl```

```pacman: sudo pacman -S kubectl```

```apk: sudo apk add kubectl```

```brew: brew install kubectl```

```nix: nix profile install nixpkgs#kubectl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kubectl-get](/man/kubectl-get)(1)
