# TAGLINE

将 Limine 引导加载程序菜单项与 Btrfs 快照同步

# TLDR

将 Snapper 快照同步为 **Limine 引导项**

```limine-snapper-sync```

**列出**为 Limine 管理的快照引导项

```limine-snapper-list```

显示可引导快照的**详细信息**

```limine-snapper-info```

从可引导快照**恢复**系统

```limine-snapper-restore```

运行针对新 Snapper 快照的**后台监视器**

```limine-snapper-watcher```

# SYNOPSIS

**limine-snapper-sync**

**limine-snapper-list**

**limine-snapper-info**

**limine-snapper-restore**

**limine-snapper-watcher**

# DESCRIPTION

**limine-snapper-sync** 将 Limine 引导加载程序菜单项与 Snapper 管理的 Btrfs 快照同步。这使用户可以从 Limine 引导菜单直接启动到之前的系统状态。

这套工具包含多个命令：**limine-snapper-sync** 执行手动同步，**limine-snapper-list** 显示当前可引导的快照，**limine-snapper-info** 显示详细的快照信息，**limine-snapper-restore** 从快照恢复系统，而 **limine-snapper-watcher** 实时监控快照变化。

通过 Snapper 创建或删除快照后，运行 sync 会更新 Limine 引导菜单以反映可用的还原点。

# CAVEATS

需要配置了 Snapper 进行快照管理的 Btrfs 文件系统。必须正确安装并配置 Limine 引导加载程序。从快照恢复会将系统文件回退到快照时的状态，可能丢失最近的更改。

# INSTALL

```aur: yay -S limine-snapper-sync```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[limine](/man/limine)(1), [limine-entry-tool](/man/limine-entry-tool)(1), [snapper](/man/snapper)(8), [btrfs](/man/btrfs)(8)
