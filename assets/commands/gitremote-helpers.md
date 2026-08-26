# TAGLINE

Git 远程助手传输接口文档

# TLDR

**文档参考**

```man gitremote-helpers```

# SYNOPSIS

**git remote-**_transport_ _repository_ [_URL_]

# DESCRIPTION

**gitremote-helpers** 是 Git 中远程助手接口的文档。远程助手是 Git 调用的独立程序，用于处理 Git 原生不支持的协议或系统的远程仓库传输。

Git 通过基于行的协议与助手的标准输入/输出通信：助手首先响应 `capabilities` 命令声明自己支持的功能（`fetch`、`push`、`import`、`export`、`connect`、`option` 等），然后按需处理 `list`、`fetch` 和 `push` 命令。内置助手包括 `git-remote-http`、`git-remote-https` 和 `git-remote-ftp`；针对 Mercurial（`git-remote-hg`）和 Bazaar（`git-remote-bzr`）等系统也存在第三方助手。

当远程 URL 以 `<transport>::` 为前缀（例如 `hg::https://example.com/repo`）或使用了没有内置传输实现的协议时，Git 会通过在 `PATH` 中查找名为 `git-remote-<transport>` 的可执行文件来自动调用助手。

# CAVEATS

这是协议文档，不是可运行的命令。助手由 Git 根据远程 URL 协议自动调用；通常不需要直接调用 `git remote-*`。实现自定义传输后端时才会用到。

# HISTORY

远程助手接口加入 **Git** 是为了提供可扩展的传输机制，让 Git 无需修改自身即可桥接到其他版本控制系统。

# SEE ALSO

[git-remote](/man/git-remote)(1), [git-remote-ext](/man/git-remote-ext)(1)

# RESOURCES

```[Documentation](https://git-scm.com/docs/gitremote-helpers)```

<!-- verified: 2026-07-17 -->
