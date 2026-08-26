# TAGLINE

用户友好的 TUI 套接字统计工具

# TLDR

**查看活动的套接字连接**

```neoss```

**通过 npm 全局安装 neoss**

```npm install -g neoss```

# SYNOPSIS

**neoss**

# DESCRIPTION

**neoss** 是一个用户友好的 TUI 工具，提供详细的 TCP 和 UDP 套接字统计。它旨在用清晰简洁的终端界面取代基本用法下的 **ss** 命令，支持对结果进行排序、刷新和浏览。

TUI 会显示正在使用的套接字及其各自的统计信息，包括本地和远程地址、状态以及相关进程。你可以选中任意数据点来查看其含义的解释。

# CAVEATS

获取完整的进程信息需要提权（sudo）。安装需要 Node.js 和 npm。可通过 `npm install -g neoss` 作为 npm 软件包安装。

# HISTORY

**neoss** 由 **PabloLec** 创建，使用 **TypeScript** 编写。

# INSTALL

```aur: yay -S neoss```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ss](/man/ss)(8), [netstat](/man/netstat)(8)
