# TAGLINE

使用 CUE 的整体式 Kubernetes 平台管理器

# TLDR

**显示已安装的版本**

```holos --version```

**在当前目录初始化新平台**

```holos init platform [v1alpha5]```

**将整个平台渲染**为 deploy/ 清单

```holos render platform```

**渲染单个组件**

```holos render component [path/to/component]```

**使用其他平台目录渲染**

```holos render platform --platform [path/to/platform]```

**列出平台产生的构建计划**

```holos show buildplans```

# SYNOPSIS

**holos** _command_ [_subcommand_] [_options_]

# DESCRIPTION

**Holos** 是一个面向 Kubernetes 的配置管理工具，实现了**渲染清单模式（rendered manifests pattern）**。它不用模板化 YAML，而是用 **CUE** 描述平台及其组件；**holos** 将 CUE 规格与 **Helm** chart 和 **Kustomize** overlay 组合起来，把生成的清单写入磁盘，以便提交到 Git 并由任何 GitOps 控制器（Argo CD、Flux 等）应用。

一个平台由一个根目录组成，其中包含 **cue.mod/** 和描述 Platform 资源的生成的 **platform.gen.cue**。每个组件位于自己的目录中，并导出一个由 **holos render** 执行的 **BuildPlan**。输出是 _deploy/_ 下纯粹的 Kubernetes YAML，这使得 diff 易于审查，并将渲染与集群访问解耦。

# COMMANDS

**init platform** _version_
> 使用给定的 API 版本（如 _v1alpha5_）搭建新平台脚手架。创建 _platform/_、_cue.mod/_ 和 _platform.gen.cue_。

**render platform**
> 将平台的每个组件渲染到 _deploy/_。

**render component** _path_
> 渲染单个组件目录。

**show buildplans**
> 打印 Holos 将要执行的 BuildPlan 资源。

**generate**
> 运行代码生成器（例如从 Kubernetes CRD 重新生成 CUE schema）。

**version**
> 打印构建和 API 版本信息。

**help** [_command_]
> 显示某个命令的帮助。

# PARAMETERS

**--platform** _dir_
> 覆盖作为渲染入口的默认平台目录（_platform/_）。

**--version**
> 打印 Holos 版本后退出。

**--help**, **-h**
> 显示某个命令的帮助。

# CAVEATS

Holos 尚未发布 1.0，API 按目录区分版本（**v1alpha3**、**v1alpha4**、**v1alpha5**……）；不支持在同一平台中混用不同版本，升级通常需要重新生成 **platform.gen.cue**。如果你只熟悉 Helm/Kustomize 工作流，CUE 有一定学习曲线。该工具本身只负责渲染清单——将清单应用到集群的工作交给你的 GitOps 控制器或 **kubectl apply**。

# HISTORY

由 **Jeff McCune** 和 **holos-run** 社区于 **2023 年**发起，旨在解决大型多集群 Kubernetes 平台中纯模板化的缺陷。以 **Go** 和 **CUE** 编写，基于 **Apache 2.0** 许可证发布。通过 **Homebrew**（_brew install holos-run/tap/holos_）分发，也提供 GitHub releases 上的静态二进制文件。

# INSTALL

```zypper: sudo zypper install holos```

```nix: nix profile install nixpkgs#holos```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[helm](/man/helm)(1), [kustomize](/man/kustomize)(1), [kubectl](/man/kubectl)(1), [argocd](/man/argocd)(1)
