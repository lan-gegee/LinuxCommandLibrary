# TAGLINE

无需模板即可自定义 Kubernetes YAML 配置

# TLDR

从当前目录**构建 kustomization**

```kustomize build .```

从指定目录**构建**

```kustomize build [path/to/overlay]```

从 Git 仓库**构建**

```kustomize build [https://github.com/org/repo//path]```

在当前目录**新建 kustomization**

```kustomize create```

自动检测资源并**创建**

```kustomize create --autodetect```

**编辑**以添加资源

```kustomize edit add resource [deployment.yaml]```

**编辑**以设置命名空间

```kustomize edit set namespace [my-namespace]```

**编辑**以设置镜像标签

```kustomize edit set image [nginx:1.25]```

# SYNOPSIS

**kustomize** _command_ [_options_]

# COMMANDS

**build** [_path_]
> 从目录或 URL 构建 kustomization 目标并输出到标准输出。

**create**
> 在当前目录创建新的 kustomization.yaml。

**edit**
> 编辑现有的 kustomization.yaml 文件。

**cfg**
> 用于读取和写入配置的命令。

**fn**
> 针对配置运行函数的命令。

**completion** _shell_
> 生成 Shell 补全脚本。

**version**
> 打印 kustomize 版本。

**help**
> 查看任意命令的帮助信息。

# PARAMETERS

**--enable-helm**
> 启用 Helm chart inflator 生成器。

**--enable-alpha-plugins**
> 启用 alpha 版 kustomize 插件。

**--as-current-user**
> 使用命令执行者的 uid 和 gid。

**--load-restrictor** _value_
> 控制文件加载：LoadRestrictionsRootOnly 或 LoadRestrictionsNone。

**-o**, **--output** _path_
> 将输出写入文件而非标准输出。

**--stack-trace**
> 出错时打印堆栈跟踪。

**-h**, **--help**
> 显示帮助信息。

# EDIT SUBCOMMANDS

**edit add resource** _file_
> 向 kustomization 添加资源。

**edit add patch** _file_
> 添加补丁文件。

**edit set namespace** _name_
> 为所有资源设置命名空间。

**edit set image** _name:tag_
> 设置或覆盖镜像标签。

**edit set replicas** _name=count_
> 为某个 Deployment 设置副本数。

**edit add label** _key:value_
> 为所有资源添加标签。

**edit add annotation** _key:value_
> 为所有资源添加注解。

# DESCRIPTION

**kustomize** 无需模板即可自定义 Kubernetes YAML 配置。它通过 **kustomization.yaml** 文件以声明式方式指定基础资源，以及叠加在其上的修改项，例如补丁、标签、命名空间和镜像标签。

该工具遵循 base/overlay 模式：base 存放公共资源，overlay 则针对特定环境（开发、预发布、生产）进行定制。这种做法既避免了重复，又保留了各环境间的差异。

Kustomize 自 v1.14 起内置于 kubectl，形式为 **kubectl kustomize** 和 **kubectl apply -k**。独立 CLI 提供最新特性，建议在高级用例中使用。

关键概念包括 **resources**（要纳入的 YAML 文件）、**patches**（策略合并补丁或 JSON 补丁）、**configMapGenerator** 与 **secretGenerator**（从文件生成 ConfigMap/Secret），以及 **vars**（变量替换）。

# CAVEATS

内置于 kubectl 的版本可能落后于独立 CLI。部分功能需要 **--enable-helm** 或 **--enable-alpha-plugins** 标志。与 Helm 等模板工具相比，变量替换存在一定局限。

# HISTORY

Kustomize 由 **Kubernetes SIG CLI** 团队于 **2017 年**前后开始开发，是一种无模板的 Kubernetes 配置管理方案。它在 **1.14 版本（2019 年）**中被集成进 kubectl。该项目强调声明式配置，秉承 Kubernetes 期望状态管理的理念。

# INSTALL

```apt: sudo apt install kustomize```

```dnf: sudo dnf install kustomize```

```pacman: sudo pacman -S kustomize```

```apk: sudo apk add kustomize```

```zypper: sudo zypper install kustomize```

```brew: brew install kustomize```

```nix: nix profile install nixpkgs#kustomize```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [helm](/man/helm)(1), [k9s](/man/k9s)(1)
