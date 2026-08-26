# TAGLINE

快速的磁盘用量分析器和开发者清理 TUI

# TLDR

**扫描当前目录**

```mcdu```

**扫描指定路径**

```mcdu [path/to/directory]```

# SYNOPSIS

**mcdu** [_options_] [_path_]

# DESCRIPTION

**mcdu** 是一个快速、现代的磁盘用量分析器，带有 TUI 界面。它按大小对目录排序并提供色彩编码的可视化，支持 vim 风格导航。它能搜索 **18 种以上生态系统**中的构建产物和缓存，包括 node_modules、Cargo target 和 Docker 构建产物。

在 macOS 上，它可以检测 ~/Library 中的孤立应用数据。为了安全删除，它支持试运行、双重确认和 JSON 审计日志。

# CAVEATS

删除构建产物后需要重新构建这些项目。删除前请使用试运行模式预览。

# HISTORY

**mcdu** 由 **mikalv** 创建，用 **Rust** 编写。

# INSTALL

```aur: yay -S mcdu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ncdu](/man/ncdu)(1), [du](/man/du)(1), [kondo](/man/kondo)(1)
