# TAGLINE

面向流式数据的交互式 grep

# TLDR

交互式**过滤流式 Kubernetes 日志**

```stern --context kind etcd |& sig```

重新执行并过滤一条命令

```sig --cmd "[stern --context kind etcd]"```

交互式搜索静态文件

```cat [README.md] |& sig```

# SYNOPSIS

**sig** [_options_]

# DESCRIPTION

**sig** 是一个交互式 grep 工具，可以实时过滤流式数据。它与管道输入配合良好，例如 Kubernetes 日志或 WebSocket 数据。它包含一种归档模式，会缓冲最近的条目以便向后搜索，同时支持流式和静态文件输入。

# HISTORY

**sig** 由 **ynqa** 创建，使用 **Rust** 编写。

# INSTALL

```pacman: sudo pacman -S sig```

```nix: nix profile install nixpkgs#sig```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grep](/man/grep)(1), [ripgrep](/man/ripgrep)(1), [fzf](/man/fzf)(1)
