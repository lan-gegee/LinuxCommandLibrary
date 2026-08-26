# TAGLINE

专注于带标签资源集合的 Kubernetes 应用部署工具

# TLDR

从 YAML **部署**应用

```kapp deploy -a [my-app] -f [manifests/] -y```

**列出**集群中的应用

```kapp list```

**检查**应用资源

```kapp inspect -a [my-app]```

**删除**应用及其资源

```kapp delete -a [my-app] -y```

# SYNOPSIS

**kapp** *command* [*options*]

# DESCRIPTION

**kapp**（Carvel）将一组 Kubernetes 资源作为一个命名的"应用"部署，并通过标签跟踪归属关系。它会计算需要创建/更新/删除的资源，等待调和完成，并支持在应用前进行 diff 检查。通常与用于模板化的 **ytt** 和用于镜像解析的 **kbld** 搭配使用。

# PARAMETERS

**deploy** **-a** *name* **-f** *path*

> 部署或更新应用。**-y** 跳过确认。

**list**

> 列出应用。

**inspect** **-a** *name*

> 显示属于某应用的资源。

**delete** **-a** *name*

> 删除应用资源。

**logs** / **diff** 相关命令

> 调试辅助工具——参见 **kapp --help**。

# CAVEATS

需要可用的 **kubectl** 集群访问。基于标签的归属机制在标签被手动修改时可能产生冲突。对于 chart 生态而言，它不是 Helm 的完整替代品。

# INSTALL

```apk: sudo apk add kapp```

```brew: brew install kapp```

```nix: nix profile install nixpkgs#kapp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [ytt](/man/ytt)(1), [helm](/man/helm)(1), [kustomize](/man/kustomize)(1)

# RESOURCES

```[Source code](https://github.com/carvel-dev/kapp)```

```[Homepage](https://carvel.dev/kapp/)```

```[Documentation](https://carvel.dev/kapp/docs/)```

<!-- verified: 2026-07-19 -->
