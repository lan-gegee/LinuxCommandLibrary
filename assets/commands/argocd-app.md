# TAGLINE

管理 Argo CD 应用

# TLDR

**列出**所有应用

```argocd app list```

**创建**新应用

```argocd app create [name] --repo [repo_url] --path [path] --dest-server [cluster_url] --dest-namespace [namespace]```

**同步**应用

```argocd app sync [name]```

**删除**应用

```argocd app delete [name]```

获取应用**详情**

```argocd app get [name]```

与 Git 进行**差异对比**

```argocd app diff [name]```

# SYNOPSIS

**argocd app** _command_ [_options_]

# DESCRIPTION

**argocd app** 管理 Argo CD 应用。应用表示从 Git 仓库同步部署的 Kubernetes 资源，每个应用将一个 Git 路径链接到一个 Kubernetes 目标。

应用可以手动或自动同步，Argo CD 会监控期望状态（Git）与实际状态（集群）之间的偏差。

# PARAMETERS

**create** _name_
> 创建新应用

**list**
> 列出所有应用

**get** _name_
> 获取应用详情

**sync** _name_
> 将应用与 Git 同步

**delete** _name_
> 删除应用

**diff** _name_
> 显示与 Git 状态的差异

**history** _name_
> 显示部署历史

**rollback** _name_ _id_
> 回滚到先前的版本

**set** _name_
> 修改应用设置

**wait** _name_
> 阻塞直到应用达到 Healthy/Synced 状态

**logs** _name_
> 流式输出应用 Pod 的日志

**--repo** _url_
> Git 仓库 URL

**--path** _path_
> 仓库内的路径

**--dest-server** _url_
> Kubernetes 集群 URL

**--dest-namespace** _ns_
> 目标命名空间

**--sync-policy** _policy_
> 同步策略（manual、automated）

# CAVEATS

应用需要预先配置好仓库和集群访问权限。生产环境使用自动同步须谨慎。修剪操作可能删除资源。

# HISTORY

应用管理是 Argo CD 的核心功能，自 **2018** 年项目创建以来一直是 GitOps 工作流的中心。

# INSTALL

```pacman: sudo pacman -S argocd```

```brew: brew install argocd```

```nix: nix profile install nixpkgs#argocd```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[argocd](/man/argocd)(1), [kubectl](/man/kubectl)(1)

# RESOURCES

```[Source code](https://github.com/argoproj/argo-cd)```

```[Documentation](https://argo-cd.readthedocs.io)```

<!-- verified: 2026-06-15 -->
