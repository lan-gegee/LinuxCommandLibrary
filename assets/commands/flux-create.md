# TAGLINE

从命令行创建或更新 Flux 自定义资源

# TLDR

**创建 Git 源**

```flux create source git my-repo --url https://github.com/org/repo --branch main```

**创建 Kustomization** 以同步源中的路径

```flux create kustomization my-app --source my-repo --path ./k8s```

**创建 HelmRelease**

```flux create helmrelease my-release --chart mychart --source HelmRepository/myrepo```

将 YAML **导出到标准输出**而不应用到集群

```flux create source git my-repo --url https://github.com/org/repo --branch main --export```

**创建 Git 认证 Secret**

```flux create secret git my-git-secret --url https://github.com/org/repo --username user --password pass```

# SYNOPSIS

**flux** **create** _kind_ _name_ [_options_]

# DESCRIPTION

**flux create** 用于生成 Flux 自定义资源（GitRepository、Kustomization、HelmRelease、HelmRepository、Secret 等），无需手写 YAML。

默认情况下资源会被应用到集群。传入 **--export** 则改为将资源以 YAML 打印到标准输出（便于提交到 Git 或管道传给其他工具）。

它支持主要的 Flux 资源类型和许多常用配置选项。

# COMMON KINDS

**source git**, **source helm**, **source oci**
> 创建源仓库。

**kustomization**
> 定义 Kustomize 同步。

**helmrelease**
> 部署 Helm chart。

**secret git**, **secret helm**
> 创建凭据。

**image**, **receiver**, **alert**, **tenant**
> 镜像自动化、通知接收器、告警以及多租户辅助功能。

# PARAMETERS

**--export**
> 将资源以 YAML 格式导出到标准输出，而不是应用到集群。

**--interval** _duration_
> 源同步间隔（默认 `1m0s`）。

**--label** _key=value_
> 为资源设置标签（可重复 / 逗号分隔）。

**-n**, **--namespace** _ns_
> 命名空间范围（默认 `flux-system`）。

# INSTALL

```apk: sudo apk add flux```

```brew: brew install flux```

```nix: nix profile install nixpkgs#flux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[flux](/man/flux)(1), [flux-bootstrap](/man/flux-bootstrap)(1), [flux-build](/man/flux-build)(1), [flux-check](/man/flux-check)(1)

# RESOURCES

```[Source code](https://github.com/fluxcd/flux2)```

```[Documentation](https://fluxcd.io/flux/cmd/flux_create/)```

<!-- verified: 2026-07-11 -->
