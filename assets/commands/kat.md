# TAGLINE

Kubernetes 清单的 TUI 与基于规则的渲染引擎

# TLDR

**渲染并查看**当前目录中的清单

```kat```

**使用指定的 profile 渲染**

```kat -p [profile_name]```

# SYNOPSIS

**kat** [**-p** _profile_] [_options_]

# DESCRIPTION

**kat** 是一个面向 Kubernetes 清单的 TUI 与基于规则的渲染引擎。它让你可以直接在 shell 中渲染、过滤和审阅 **Helm** 或 **Kustomize** 清单，在文件变化时自动重载并标记错误，从而简化 chart 和清单的开发。

核心功能包括：基于 profile 的清单生成、使用 **kubeconform** 和 **kyverno** 的自动校验、带 diff 可视化的实时重载、渲染前/后钩子、用于自定义命令的插件系统，以及 Chroma 主题支持。

# CAVEATS

需要安装 Helm 和/或 Kustomize 才能渲染。校验工具（kubeconform、kyverno）是可选的但推荐安装。

# HISTORY

**kat** 为 Kubernetes 工程师和 DevOps 团队设计，旨在通过提供持久、可导航的渲染资源视图和即时反馈，消除清单开发中的上下文切换。

# INSTALL

```aur: yay -S kat```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [helm](/man/helm)(1), [kustomize](/man/kustomize)(1)
