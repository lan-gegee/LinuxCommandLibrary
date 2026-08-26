# TAGLINE

底层 LFS 传输协议

# TLDR

**传输 LFS 对象**

```git lfs transfer```

# SYNOPSIS

**git lfs transfer** [_options_]

# PARAMETERS

**--help**
> 显示帮助信息。

# DESCRIPTION

**git lfs transfer** 是一个底层的 Git LFS 协议助手，实现了 Git LFS 3.0 引入的 **pure-SSH 传输协议**。当通过 **git+ssh://** 访问 Git LFS 服务器时，LFS 客户端会在远程 shell 中调用 **git lfs transfer**，以协商批量请求、交换 OID，并通过 SSH 通道流式传输对象内容——从而绕过旧版 LFS 部署所采用的基于 HTTP 的"ssh 作为认证"流程。

很少需要直接调用它；用户通常是通过 **git lfs push**、**git lfs pull**、**git lfs fetch** 或任何会实体化 LFS 对象的操作间接与该协议交互。

# CAVEATS

内部助手——由 Git LFS 通过 SSH 连接调用，而不是由用户直接使用。要求客户端和服务器都支持 pure-SSH 传输协议（双方均为 Git LFS ≥ 3.0）。

# HISTORY

git lfs transfer 是 **Git LFS** 的组成部分，实现用于大文件同步的传输协议。

# INSTALL

```nix: nix profile install nixpkgs#git-lfs-transfer```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-lfs](/man/git-lfs)(1), [git](/man/git)(1)
