# TAGLINE

面向 Kubernetes 的 Helm chart 声明式部署工具

# TLDR

**应用** **helmfile.yaml** 中的期望状态

```helmfile apply```

**同步** release 使其符合声明（安装缺失的、升级变更的）

```helmfile sync```

在应用前**比较**待执行的变更

```helmfile diff```

**销毁** helmfile 中定义的所有 release

```helmfile destroy```

对 helmfile 及其引用的 chart 执行**静态检查**

```helmfile lint```

**生成**新的项目脚手架

```helmfile create [my-project]```

# SYNOPSIS

**helmfile** [_global_options_] **apply** | **sync** | **diff** | **destroy** | **lint** | **template** | **build** | **list** | **status** | **delete** | **init** | **create** [_command_options_]

# PARAMETERS

**-f**, **--file** _path_
> helmfile 的路径（默认：**helmfile.yaml**）。可重复使用。

**-e**, **--environment** _name_
> 分层 values 所用的环境名称（例如 **staging**、**production**）。

**--selector** _label=value_
> 将操作限制在匹配标签选择器的 release 上。

**-l**, **--selector** _label=value_
> **--selector** 的别名。

**-n**, **--namespace** _namespace_
> 覆盖 Kubernetes 命名空间。

**--kube-context** _context_
> 要使用的 Kubernetes context。

**--debug**
> 启用详细的调试输出。

**--quiet**
> 抑制非必要的输出。

**--no-color**
> 禁用 ANSI 颜色代码。

# DESCRIPTION

**helmfile** 是一种将 Helm chart 部署到 Kubernetes 的声明式规范。你可以在 YAML 中描述仓库、release、values 和钩子（通常是 **helmfile.yaml**），将该文件纳入版本控制，然后运行 **helmfile apply** 或 **helmfile sync**，使集群收敛到声明的状态。

该可执行文件将 chart 操作委托给 **helm**，并在使用 **diff** 子命令时依赖 **helm-diff** 插件。安装后先运行一次 **helmfile init** 以安装所需的插件。

Helmfile 支持模块化的 helmfile（从 Git 或 S3 导入共享片段）、按环境分层的 values、在安装前对渲染后的清单应用 JSON 补丁和 strategic-merge 补丁，以及将 Helm chart 与原生 Kubernetes 清单和 Kustomize base 混合使用。release 可以声明依赖关系，Helmfile 会按正确顺序安装它们。

常见工作流：用 **helmfile diff** 预览变更；用 **helmfile apply** 一步完成安装和升级；用 **helmfile template** 或 **helmfile build** 为 Argo CD 等 GitOps 工具渲染清单；用 **helmfile destroy** 拆除该文件管理的所有 release。

# CONFIGURATION

**helmfile.yaml**
> 主声明式规范。定义 **repositories**、**releases**、可选的 **environments**、**helmDefaults** 和 **templates**。

**helmfile.d/**
> 存放额外 YAML 片段的目录，这些片段会合并进主规范。

**.helmfile/**
> 操作过程中创建的可选本地状态与缓存目录。

**helmfile init**
> 安装 **helm-diff** 插件及 Helmfile 依赖的其他组件。

# CAVEATS

Helmfile v1.x 相较 v0.x 引入了破坏性变更；升级旧项目前请查阅 v1 迁移指南。**helm** 和 **helm-diff** 必须单独安装，并与所用的 Helmfile 版本保持兼容。**diff** 子命令需要可正常工作的 **helm-diff** 插件。

# INSTALL

```pacman: sudo pacman -S helmfile```

```zypper: sudo zypper install helmfile```

```brew: brew install helmfile```

```nix: nix profile install nixpkgs#helmfile```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[helm](/man/helm)(1), [helm-install](/man/helm-install)(1), [kubectl](/man/kubectl)(1)
