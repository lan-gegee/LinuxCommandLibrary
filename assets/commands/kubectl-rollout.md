# TAGLINE

管理 deployment、daemonset 和 statefulset 的发布过程

# TLDR

**检查 deployment 的发布状态**

```kubectl rollout status deployment/[name]```

**带超时地监视发布状态**

```kubectl rollout status deployment/[name] --timeout=[5m]```

**查看发布历史**

```kubectl rollout history deployment/[name]```

**查看特定修订版本的详情**

```kubectl rollout history deployment/[name] --revision=[3]```

**撤销回上一个修订版本**

```kubectl rollout undo deployment/[name]```

**回滚到特定修订版本**

```kubectl rollout undo deployment/[name] --to-revision=[2]```

**暂停发布**

```kubectl rollout pause deployment/[name]```

**恢复已暂停的发布**

```kubectl rollout resume deployment/[name]```

**在不更改模板的情况下重启 deployment 中的所有 Pod**

```kubectl rollout restart deployment/[name]```

**重启匹配标签选择器的 deployment**

```kubectl rollout restart deployment --selector=[app=nginx]```

# SYNOPSIS

**kubectl rollout** _SUBCOMMAND_ [_options_]

# PARAMETERS

**history** _TYPE/NAME_
> 查看发布的修订历史。

**pause** _TYPE/NAME_
> 将给定资源标记为已暂停。

**restart** _TYPE/NAME_
> 触发所有 Pod 的滚动重启。

**resume** _TYPE/NAME_
> 恢复已暂停的发布。

**status** _TYPE/NAME_
> 显示发布状态。

**undo** _TYPE/NAME_
> 撤销上一次发布。

**--revision** _N_
> 为 history 或 status 固定到特定修订版本。

**--to-revision** _N_
> undo 的目标修订版本（默认 0 表示上一个版本）。

**--timeout** _DURATION_
> 结束状态监视前的等待时间（例如 5m）。

**-w**, **--watch**
> 持续监视发布状态直至完成（默认 true）。

**-f**, **--filename** _FILE_
> 标识资源的文件名、目录或 URL。

**-l**, **--selector** _SELECTOR_
> 用于过滤资源的标签选择器。

**-R**, **--recursive**
> 递归处理 -f 使用的目录。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**kubectl rollout** 管理 Kubernetes 工作负载滚动更新的生命周期，包括 deployment、daemonset 和 statefulset。它提供多个子命令，用于监视进行中的发布的进度、检查修订历史，以及在发现问题后触发回滚到之前的版本。

该命令还支持暂停和恢复发布，这适用于金丝雀式的部署场景——在允许更新继续之前先验证部分更新。`restart` 子命令在不更改 Pod 模板的情况下触发所有 Pod 的新一轮滚动重启，有助于让 Pod 重新加载 ConfigMap 或 Secret 的更改。每次发布都会被记录为一个编号修订版本，从而支持用 --to-revision 进行精确回滚。

# CAVEATS

只对 deployment、daemonset 和 statefulset 有效。修订历史的深度由 `.spec.revisionHistoryLimit` 字段控制（默认 10）。暂停发布会同时阻止回滚和新的发布，直到恢复为止。`restart` 子命令不会更改 Pod 模板；它通过更新一个注解来触发新的发布。

# HISTORY

自 **Kubernetes** 早期版本起，kubectl rollout 就是 **kubectl** 的一部分，为工作负载的发布提供声明式的生命周期管理。

# INSTALL

```apt: sudo apt install kubectl```

```pacman: sudo pacman -S kubectl```

```apk: sudo apk add kubectl```

```brew: brew install kubectl```

```nix: nix profile install nixpkgs#kubectl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kubectl-apply](/man/kubectl-apply)(1), [kubectl-set](/man/kubectl-set)(1), [kubectl-get](/man/kubectl-get)(1), [kubectl-scale](/man/kubectl-scale)(1)
