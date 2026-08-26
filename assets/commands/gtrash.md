# TAGLINE

功能丰富的回收站 CLI 管理器与安全的 rm 替代品

# TLDR

**将文件移入回收站**而不是删除

```gtrash put [path/to/file1] [path/to/file2]```

**列出回收站中的文件**

```gtrash find```

**使用 TUI 交互式恢复文件**

```gtrash restore```

从回收站中**永久删除匹配模式的文件**

```gtrash find --rm "[pattern]"```

**显示回收站摘要**及大小

```gtrash summary```

**清理回收站中的旧文件**

```gtrash prune --day [30]```

# SYNOPSIS

**gtrash** _command_ [_options_] [_arguments_]

# DESCRIPTION

**gtrash** 是一款功能丰富的回收站 CLI 管理器，可作为更安全的 **rm** 替代品。它不通过 unlink 系统调用永久删除文件，而是使用 rename 系统调用将其移入系统回收站，从而方便恢复。它遵循 **FreeDesktop.org 回收站规范**，因此与桌面环境的回收站实现以及其他工具（如 **gio trash** 和 **trash-cli**）兼容。

其主要特性包括：用于快速浏览的目录大小缓存、共同删除文件的成组恢复、用于选择要恢复文件的交互式 TUI，以及对带有独立卷回收站目录的外置驱动器的支持。

# PARAMETERS

**put**
> 将文件移入回收站

**find**
> 列出回收站中的文件（支持 --rm 永久删除匹配项）

**restore**
> 使用 TUI 交互式地从回收站恢复文件

**summary**
> 显示回收站大小摘要

**prune**
> 移除回收站中的旧文件

**--day** _N_
> 与 prune 配合，指定以天为单位的时限阈值

**--rm**
> 与 find 配合，永久删除匹配的文件

# CAVEATS

移入回收站的文件在被清理或永久删除之前仍占用磁盘空间。回收操作所用的 rename 系统调用只在同一文件系统内有效；跨文件系统的移动需要进行复制。使用 **--rm** 永久删除不可逆，与 rm 类似。

# HISTORY

**gtrash** 由 **umlx5h** 创建，旨在同时替代 **rm** 和现有回收站管理器，是一个现代且功能丰富的工具。它用 **Go** 编写，以单个静态二进制文件分发。

# INSTALL

```brew: brew install gtrash```

```nix: nix profile install nixpkgs#gtrash```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rm](/man/rm)(1), [trash-cli](/man/trash-cli)(1)
