# TAGLINE

声明式磁盘分区管理

# TLDR

**自动扩展**分区

```systemd-repart```

**试运行**（仅查看变更）

```systemd-repart --dry-run yes```

将根分区扩展到**指定大小**

```systemd-repart --size 10G --root /```

# SYNOPSIS

**systemd-repart** [_OPTIONS_] [_DEVICE_]

# PARAMETERS

**--dry-run=** _BOOL_
> 显示将要执行的操作但不实际应用变更

**--size=** _SIZE_
> 操作的目标大小

**--root=** _PATH_
> 在指定的根目录上操作

**--definitions=** _PATH_
> 使用指定目录中的配置

# DESCRIPTION

**systemd-repart** 依据 `/usr/lib/repart.d/` 和 `/etc/repart.d/` 中的配置文件自动扩展和添加分区。它读取声明式的分区定义并将其应用到磁盘上。

此工具只修改分区表，不调整文件系统大小。扩展分区之后请使用 `systemd-growfs` 来扩展文件系统。

# CAVEATS

只修改分区表，不修改文件系统。配置文件以声明式方式描述期望的分区布局。应用更改前请先用试运行模式预览。主要为基于镜像的系统设计。

# HISTORY

**systemd-repart** 通过支持声明式分区管理来助力基于镜像的操作系统部署，让系统能够在首次启动时自动配置磁盘布局。

# INSTALL

```apt: sudo apt install systemd-repart```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemd-growfs](/man/systemd-growfs)(8), [repart.d](/man/repart.d)(5), [fdisk](/man/fdisk)(8)
