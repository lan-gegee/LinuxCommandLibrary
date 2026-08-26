# TAGLINE

命令行下朴实无华的时间记录工具集

# TLDR

**启动交互式 TUI**

```hours```

**查看时间记录报告**

```hours report```

**显示统计信息**

```hours stats```

**查看活动日志**

```hours log```

# SYNOPSIS

**hours** [_command_] [_options_]

# DESCRIPTION

**hours** 是一个极简的终端时间记录工具集。它提供一个简单的 TUI，几乎一切操作只需一两次按键即可完成，让针对任务和项目的时间记录非常快捷。

除了交互式 TUI，hours 还提供基于时间记录数据查看**报告**、**统计**和**日志**的子命令。它将所有数据存储在本地，专注于为希望在终端内记录时间的开发者提供无干扰的体验。

# CAVEATS

数据存储在本地，不会跨设备同步。不与外部时间跟踪服务集成。

# HISTORY

**hours** 由 **Dhruv Thakur**（dhth）创建，用 **Go** 编写。它是为偏好终端工作流的开发者设计的、基于 Web 的时间跟踪工具的朴素替代品。

# INSTALL

```nix: nix profile install nixpkgs#hours```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[time](/man/time)(1)
