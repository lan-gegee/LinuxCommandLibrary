# TAGLINE

极速的 Kubernetes 米勒列式 TUI

# TLDR

使用默认 kubeconfig **启动**

```lfk```

**打开特定的 context 和命名空间**

```lfk --context [my-cluster] -n [kube-system]```

**使用自定义 kubeconfig 文件**

```lfk --kubeconfig [/path/to/kubeconfig]```

通过环境变量**合并多个 kubeconfig**

```KUBECONFIG=[/path/to/c1]:[/path/to/c2] lfk```

**加载某个目录下的所有 kubeconfig**

```lfk --kubeconfig-dir [/path/to/configs/]```

# SYNOPSIS

**lfk** [_options_]

# PARAMETERS

**--context** _name_
> 以给定的 Kubernetes context 启动。

**-n** _namespace_, **--namespace** _namespace_
> 在给定的命名空间中打开。

**--kubeconfig** _file_
> 用给定文件覆盖 **KUBECONFIG**（支持冒号分隔的多个路径）。

**--kubeconfig-dir** _dir_
> 将 _dir_ 下的每个文件都当作 kubeconfig 并全部加载。

**--read-only**
> 以只读模式启动；所有修改性操作均被禁用。

**--theme** _name_
> 选择一款内置配色主题（运行时可按 **T** 切换）。

**--help**
> 打印内置帮助后退出。

# KEY BINDINGS

**h / Left**, **l / Right**
> 在 Miller 布局中向上一列或向下一列移动。

**j / Down**, **k / Up**
> 在当前列内移动光标。

**gg / Home**, **G / End**
> 跳转到列表顶部或底部。

**Enter**
> 全屏查看所选资源的 YAML。

**f**
> 过滤当前列表。

**/**
> 增量搜索并跳转。

**Space**
> 切换多选状态，用于批量操作。

**x**
> 打开操作菜单（日志、exec、debug、扩缩容、删除、端口转发等）。

**Ctrl+R**
> 在运行时切换只读模式。

**T**
> 循环切换内置配色主题。

**?**
> 显示帮助界面。

# DESCRIPTION

**lfk** 是一个键盘驱动的终端用户界面，用于浏览和操作 **Kubernetes** 集群，其灵感来自 **yazi** 文件管理器。它以三列式的 **Miller columns**（米勒列）布局呈现资源（context → 资源类型 → 资源 → 所属资源 → 容器），让运维人员全程不离开键盘就能从集群一路下钻到具体的日志行。

除了浏览之外，**lfk** 还支持 Kubernetes CLI 日常所需的操作：跟踪 **logs**、**exec** 进入容器、运行 **kubectl debug**、伸缩工作负载、删除资源以及为服务做端口转发。**多集群**和**多 context**工作流是一等公民：标签页和快速切换器让你在单个会话内的多个集群之间自由跳转。可选集成还涵盖 **Helm** releases、**ArgoCD** 应用、**KEDA** scaler 和 **External Secrets**。

内置的 **Prometheus** 告警视图可以在展示资源的同时呈现与之相关的触发中的告警。该程序用 Go 编写，以单个静态可执行文件的形式发行。

# CONFIGURATION

**~/.config/lfk/config.yaml**
> 用户配置：主题、搜索缩写、默认 context、按键绑定。

**~/.config/lfk/keys.yaml**
> 自定义按键绑定覆盖。

**KUBECONFIG** / **KUBECONFIG_DIR**
> 与 **kubectl** 用法一致的环境变量。

# CAVEATS

需要安装 **kubectl** 并确保其在 **PATH** 中可用。**helm** 和 **trivy** 是可选依赖，缺失时相应的集成将被禁用。所有修改性操作都有确认提示把关；**--read-only** 标志和 **Ctrl+R** 切换为生产集群提供了额外的安全网。

# HISTORY

**lfk** 由 **Janos Miko** 创建，于 **2024 年**首次发布在 GitHub 上。它借鉴了 **yazi** 的资源列表/预览人机工学以及 **k9s** 的键盘操作速度，目标是让 SRE 能更快地在*"问题出在哪里"*与*"日志里写了什么"*之间往返。

# INSTALL

```nix: nix profile install nixpkgs#lfk```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [k9s](/man/k9s)(1), [helm](/man/helm)(1), [yazi](/man/yazi)(1)
