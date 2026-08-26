# TAGLINE

受 k9s 启发的 Kubernetes API 终端用户界面（TUI）

# TLDR

使用默认 kubeconfig 和上下文**启动 b4n**

```b4n```

以指定的资源类型**启动**

```b4n [pods]```

使用指定的 kubeconfig 上下文

```b4n --context [my-cluster]```

启动时**聚焦指定的命名空间**

```b4n --namespace [kube-system]```

以覆盖所有命名空间的**集群级视图**启动

```b4n --all-namespaces```

使用自定义的 kubeconfig 文件

```b4n --kube-config [path/to/kubeconfig]```

**跳过 TLS 证书校验**

```b4n --insecure```

# SYNOPSIS

**b4n** [_options_] [_resource_]

# PARAMETERS

**--kube-config** _path_
> kubeconfig 文件的路径。默认为 **$HOME/.kube/config**。也可以通过 **KUBECONFIG** 环境变量设置。

**--context** _name_
> 要使用的 kubeconfig 文件中的 Kubernetes 上下文。

**-n**, **--namespace** _name_
> 启动时聚焦的命名空间。

**-A**, **--all-namespaces**
> 以显示所有命名空间资源的集群级视图启动。

**--insecure**
> 连接集群时跳过 TLS 证书校验。

**-V**, **--version**
> 输出版本信息。

**-h**, **--help**
> 输出帮助信息。

# DESCRIPTION

**b4n** 是一个用于管理 Kubernetes 集群的交互式终端用户界面，使用 Rust 编写，基于 **kube-rs** 和 **ratatui** 库。它提供键盘驱动的界面，让你无需离开终端就能执行常见的 Kubernetes 操作。

TUI 支持对 Kubernetes 资源的完整 CRUD 操作。用户可以通过交互式界面列出、创建、编辑和删除资源。其他能力包括：用 **e** 查看资源事件、用 **l** 流式查看 Pod 和容器日志、用 **s** 在容器内启动交互式 shell 会话、用 **y** 查看资源 YAML、用 **x** 解码 Secret、用 **f** 配置端口转发。

导航依靠通过 **:** 或 **>** 唤出的命令面板，此外还有专用按键用于选择命名空间（**左方向键**）和资源类型（**右方向键**）。可以用 **/** 过滤资源，用 **Alt+[0-9]** 对列排序。用 **Space** 选中资源，确认后按 **Ctrl+D** 删除。鼠标支持可通过 **Ctrl+N** 开关。

命令面板支持配置别名以便快速访问资源。默认别名包括 **pp** 对应 pods、**svc** 对应 services、**cm** 对应 configmaps、**ds** 对应 daemonsets、**ns** 对应 namespaces、**pvc** 对应 persistentvolumeclaims、**sts** 对应 statefulsets 等。

# CONFIGURATION

配置存储在 **$HOME/.b4n/** 中，结构如下：

**config.yaml**
> 主应用设置，包括日志偏好、鼠标支持、活动主题、各上下文专属的高亮颜色、资源别名以及自定义键绑定。若文件缺失会自动生成默认值。

**themes/**
> 存放 YAML 格式 TUI 主题文件的目录。首次运行时会自动生成默认主题。

**history.yaml**
> 按 Kubernetes 上下文保存过滤和搜索历史，以及最近使用的命名空间和资源类型。

**logs/**
> 用于调试的每日应用日志文件。

**config.yaml** 中的关键配置项包括 **logs.lines**（获取的日志行数，默认 800）、**logs.timestamps**（日志中显示时间戳，默认 true）、**mouse**（启用鼠标支持，默认 true）、**theme**（活动主题名称）、**contexts**（各集群的高亮颜色）、**aliases**（命令面板快捷方式）和 **key_bindings**（自定义键位映射，支持 Ctrl、Alt 和功能键）。

# CAVEATS

需要有效的 kubeconfig 文件以及到 Kubernetes 集群的网络访问。为了 UI 渲染正常，建议使用带有 Nerd Font 符号的终端字体（如 Cascadia Code）。从源码构建需要 Rust 1.88 或更新版本。该项目正在积极开发中，最初主要是作为一个 Rust 学习练习而创建。

# INSTALL

```zypper: sudo zypper install b4n```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[k9s](/man/k9s)(1), [kubectl](/man/kubectl)(1), [helm](/man/helm)(1)
