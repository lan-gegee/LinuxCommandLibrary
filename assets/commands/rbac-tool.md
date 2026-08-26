# TAGLINE

分析并可视化 Kubernetes RBAC 策略

# TLDR

**显示谁能对资源执行某个操作**

```rbac-tool who-can [get] [pods]```

**将 RBAC 可视化为 HTML**

```rbac-tool viz --outformat html > [rbac.html]```

**查找分配给特定主体的角色**

```rbac-tool lookup -e [user@example.com]```

**列出主体的策略规则**

```rbac-tool policy-rules -e [system:serviceaccount:default:.*]```

**分析 RBAC 的风险配置**

```rbac-tool analysis```

**从审计事件生成 ClusterRole**

```rbac-tool auditgen -f [audit.log]```

**显示当前用户的权限**

```rbac-tool whoami```

# SYNOPSIS

**rbac-tool** _command_ [_options_]

# COMMANDS

**analysis**
> 检查 RBAC 权限，识别权限过大的主体和有风险的配置。

**viz**
> 生成 RBAC 关系的可视化表示（DOT 或 HTML）。

**who-can** _verb_ _kind_|_kind/name_|_url_
> 查找所有有权对某资源执行给定操作的主体。

**lookup**
> 列出分配给指定用户、服务账号或组的 Role 和 ClusterRole。

**policy-rules**
> 列出与给定主体关联的 RBAC 策略规则。

**generate** | **gen**
> 生成具有明确权限的 Role 或 ClusterRole。

**auditgen**
> 从 Kubernetes 审计事件生成 RBAC 策略。

**show**
> 生成一个包含集群全部可用权限的 ClusterRole。

**whoami**
> 显示 API server 所看到的当前已认证主体。

**version**
> 打印 rbac-tool 版本。

# PARAMETERS

**--outformat** _FORMAT_
> 输出格式。对于 **viz**：`dot` 或 `html`。对于数据类命令：`json`、`yaml`、`table`。

**-e** _REGEX_
> 作为正则表达式的主体过滤器（与 **lookup**、**policy-rules** 配合使用）。

**--config** _FILE_
> 自定义分析规则集文件（与 **analysis** 配合使用）。

**--cluster-context** _NAME_
> 要使用的 kubeconfig 上下文。

**--exclude-namespaces** _LIST_
> 以逗号分隔的命名空间列表，从可视化中排除。

**--generated-type** _TYPE_
> Role 或 ClusterRole（与 **generate** 配合使用）。

**--allowed-verbs** _LIST_
> 要包含在生成的角色中的动词。

**--allowed-groups** _LIST_
> 要包含在生成的角色中的 API 组。

**--deny-resources** _LIST_
> 要从生成的角色中排除的资源。

**--for-groups** _LIST_
> 与 **show** 命令配合使用的 API 组。

**-f** _PATH_|_URL_
> 审计事件的来源文件、目录或 HTTP URL（与 **auditgen** 配合使用）。

# CONFIGURATION

**~/.kube/config**
> 用于连接目标集群的默认 kubeconfig。

# DESCRIPTION

**rbac-tool** 用于分析和可视化 Kubernetes RBAC（基于角色的访问控制）配置。它帮助管理员理解谁可以做什么、识别权限过大的主体、生成最小权限策略，并可视化角色/主体关系图。

`viz` 命令可生成 Graphviz DOT 图或交互式 HTML 页面。`policy-rules` 和 `lookup` 接受正则表达式，便于查询大型集群。

# CAVEATS

需要可用的 kubeconfig。某些命令需要 cluster-admin 权限才能枚举所有角色和绑定。生成的策略在应用前应先审查。

# HISTORY

**rbac-tool** 由 **Alcide**（现已并入 Rapid7）开发，以 Apache 2.0 许可证发布。它旨在帮助 Kubernetes 管理员理解和管理复杂的 RBAC 配置。

# SEE ALSO

[kubectl](/man/kubectl)(1), [kubeaudit](/man/kubeaudit)(1)
