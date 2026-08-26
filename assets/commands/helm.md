# TAGLINE

Kubernetes 的包管理器

# TLDR

**将 chart 安装**为具名 release

```helm install [release-name] [chart]```

**使用自定义 values 文件安装**

```helm install [release-name] [chart] -f [values.yaml]```

**添加仓库**

```helm repo add [name] [url]```

**更新**仓库索引

```helm repo update```

**列出**当前命名空间中的 release

```helm list```

**将 release 升级**到新 chart 版本

```helm upgrade [release-name] [chart]```

**卸载 release**

```helm uninstall [release-name]```

**查看 chart 的可配置值**

```helm show values [chart]```

# SYNOPSIS

**helm** _command_ [_options_]

# PARAMETERS

**install** _release_ _chart_
> 将 chart 安装为具名 release。

**upgrade** _release_ _chart_
> 将 release 升级到新 chart 版本或新值。

**uninstall** _release_
> 卸载 release 及其资源。

**list**
> 列出已部署的 release。

**repo add** _name_ _url_
> 添加 chart 仓库。

**repo update**
> 更新 chart 仓库索引。

**search repo** _keyword_
> 在仓库中搜索 chart。

**show values** _chart_
> 显示 chart 的可配置值。

**template** _release_ _chart_
> 在本地渲染 chart 模板而不实际安装。

**rollback** _release_ _revision_
> 将 release 回滚到先前的修订版本。

**-n**, **--namespace** _NS_
> 操作的目标 Kubernetes 命名空间。

**-f**, **--values** _FILE_
> 指定用于 chart 配置的 values 文件。

**--set** _key=value_
> 在命令行上设置单个值。

**--dry-run**
> 模拟安装/升级而不实际应用更改。

**--wait**
> 等待所有资源就绪后再将 release 标记为成功。

# DESCRIPTION

**Helm** 是 Kubernetes 的包管理器。它管理 chart，即预先配置好的 Kubernetes 资源包。chart 用于定义、安装和升级复杂的 Kubernetes 应用。

Helm 简化了应用的部署、版本管理和升级。它使用 Go 模板针对不同环境定制部署。values 文件和 **--set** 标志可以覆盖 chart 默认值，实现特定环境的配置。

# CAVEATS

需要已配置集群访问权限的 kubectl。为保证部署的可重现性，应固定 chart 版本。Helm 3 移除了服务端 Tiller 组件，完全在客户端运行。

# HISTORY

Helm 由 **Deis** 创建，现在是 **CNCF** 毕业项目，已成为 Kubernetes 包管理的标准。

# INSTALL

```dnf: sudo dnf install helm```

```pacman: sudo pacman -S helm```

```apk: sudo apk add helm```

```zypper: sudo zypper install helm```

```brew: brew install helm```

```nix: nix profile install nixpkgs#helm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kustomize](/man/kustomize)(1)
