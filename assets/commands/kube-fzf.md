# TAGLINE

为 Kubernetes 提供模糊查找命令

# TLDR

**交互式选择 Pod**

```findpod```

**跟踪 Pod 日志**

```tailpod```

**进入 Pod 执行命令**

```execpod```

**描述 Pod**

```describepod```

**端口转发**

```pfpod```

# SYNOPSIS

Commands: **findpod**, **tailpod**, **execpod**, **describepod**, **pfpod**

# PARAMETERS

**findpod**
> 模糊查找并选择 Pod。

**tailpod**
> 通过模糊选择跟踪日志。

**execpod**
> 以交互方式进入 Pod 执行命令。

**describepod**
> 描述所选的 Pod。

**pfpod**
> 对所选的 Pod 进行端口转发。

# DESCRIPTION

**kube-fzf** 是一组 Shell 函数，它将常用的 kubectl 操作与 fzf 模糊查找相结合，用于交互式选择 Kubernetes 资源。无需手动输入确切的 Pod 名称或从 `kubectl get pods` 输出中复制名称，kube-fzf 会呈现一个可搜索、可筛选的资源列表，并对选中的条目执行相应的 kubectl 命令。

该软件包提供了多个专用命令：`findpod` 用于定位和选择 Pod，`tailpod` 用于流式查看日志，`execpod` 用于在容器内打开 Shell 会话，`describepod` 用于查看 Pod 详情，`pfpod` 用于建立端口转发。每个命令都会查询当前的 Kubernetes 上下文和命名空间，通过 fzf 的交互式界面展示匹配的 Pod，并将所选内容直接传递给相应的 kubectl 子命令。

# CAVEATS

需要安装 fzf。属于 Shell 函数。kubectl 必须可用。

# HISTORY

kube-fzf 将 **fzf** 模糊查找器与 kubectl 相结合，用于交互式选择 Kubernetes 资源。

# INSTALL

```aur: yay -S kube-fzf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [fzf](/man/fzf)(1), [k9s](/man/k9s)(1)
