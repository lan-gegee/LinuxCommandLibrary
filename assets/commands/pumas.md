# TAGLINE

Apple Silicon 功耗监视器

# TLDR

**启动功耗监视 TUI**

```sudo pumas```

**以 JSON 流式输出指标**

```sudo pumas --json```

# SYNOPSIS

**pumas** [_options_]

# PARAMETERS

**--json**
> 以 JSON 形式将指标流式输出到 stdout，而不是运行 TUI。

# DESCRIPTION

**pumas** 是一个受 nvtop 启发的命令行工具，用于监控 Apple Silicon Mac 的功耗和性能指标。它有两种运行模式：TUI 模式显示利用率和功耗的全局指标，JSON 模式则便于将指标通过管道传给 jq 等工具或构建 Prometheus exporter。它使用 macOS 的 powermetrics 工具和 sysinfo crate。

# CAVEATS

需要 **sudo**，因为底层的 powermetrics 工具需要 root 权限。仅支持 Apple Silicon Mac。

# HISTORY

**pumas** 由 **graelo** 创建，使用 **Rust** 编写。

# SEE ALSO

[htop](/man/htop)(1), [macmon](/man/macmon)(1), [nvtop](/man/nvtop)(1)
