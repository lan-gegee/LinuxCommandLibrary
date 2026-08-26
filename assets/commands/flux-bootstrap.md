# TAGLINE

使用 GitOps 在 Kubernetes 集群上引导安装 Flux

# TLDR

使用 GitHub 仓库（个人账户）**引导安装 Flux**

```flux bootstrap github --owner [username] --repository [repo] --path [clusters/my-cluster] --personal```

**使用 GitLab 引导安装**

```flux bootstrap gitlab --owner [group] --repository [repo] --path [clusters/my-cluster]```

通过 SSH **从通用 Git 仓库引导安装**

```flux bootstrap git --url ssh://git@example.com/repo.git --branch main --path ./clusters/my-cluster```

# SYNOPSIS

**flux** **bootstrap** _provider_ [_options_]

# DESCRIPTION

**flux bootstrap** 通过将必要的清单推送到 Git 仓库并配置集群从该仓库同步，从而在 Kubernetes 集群上安装 Flux。这会建立 GitOps 控制平面（source-controller、kustomize-controller、helm-controller、notification-controller 等）。

它支持 GitHub、GitLab、Gitea、Bitbucket Server 以及通用 Git 仓库。该命令会创建 `flux-system` 命名空间、所需的 Secret，以及让 Flux 自身保持最新的初始 GitRepository + Kustomization。

引导完成后，集群即可通过 Git 进行声明式管理。

# PARAMETERS

各提供者通用的选项：

**--owner** _name_
> GitHub/GitLab 所有者或组织。

**--repository** _name_
> 仓库名称。

**--path** _path_
> 清单在仓库中的路径（例如 `clusters/my-cluster`）。

**--branch** _branch_
> Git 分支（默认 `main`）。

**--personal**
> 使用个人访问令牌而不是组织应用。

**--private-key-file** _file_
> SSH 私钥路径。

**--components** _list_
> 要安装的组件列表（逗号分隔）（默认包括 source、kustomize、helm 和 notification 控制器）。

**--components-extra** _list_
> 额外的组件（例如 `image-reflector-controller,image-automation-controller`）。

**--token-auth**
> 使用个人访问令牌而不是 SSH 部署密钥。

还存在其他特定于提供者的选项（参见 `flux bootstrap --help`）。

# CAVEATS

引导过程需要一个具备集群管理员权限且可用的 `kubectl` 上下文，以及相应的 Git 凭据。仓库必须已存在（或者在使用受支持的提供者时由该命令创建）。

# INSTALL

```apk: sudo apk add flux```

```brew: brew install flux```

```nix: nix profile install nixpkgs#flux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[flux](/man/flux)(1), [flux-check](/man/flux-check)(1), [flux-create](/man/flux-create)(1)

# RESOURCES

```[Source code](https://github.com/fluxcd/flux2)```

```[Documentation](https://fluxcd.io/flux/cmd/flux_bootstrap/)```

<!-- verified: 2026-07-11 -->
