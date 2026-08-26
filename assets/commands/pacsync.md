# TAGLINE

将 pacman 软件包数据库与远程仓库同步

# TLDR

更新**所有**同步数据库

```sudo pacsync```

更新**指定的**仓库

```sudo pacsync [repo1] [repo2]```

即使已是最新也**强制**更新

```sudo pacsync --force```

使用指定的**配置**文件

```sudo pacsync --config [path/to/pacman.conf]```

仅当数据库**确实被更新**时才返回真

```sudo pacsync --updated```

# SYNOPSIS

**pacsync** [**--config** _file_] [**--dbpath** _path_] [**--force**] [**--updated**] [_repository_...]

# PARAMETERS

**--config _file_**
> 使用替代的 pacman 配置文件

**--dbpath _path_**
> 使用替代的数据库位置

**--force**
> 即使已是最新也强制同步数据库

**--updated**
> 仅当数据库确实被更新时才成功退出

**--help**
> 显示帮助信息

# DESCRIPTION

**pacsync** 将 pacman 软件包数据库与远程仓库同步。它是 pacutils 实用工具集的一部分，为 pacman 提供增强功能。

不带参数运行时，它会更新所有已配置的同步数据库。可以将仓库名称作为参数来针对特定仓库。--updated 标志对需要知道是否确实有更新的脚本很有用。

# CAVEATS

更新系统数据库需要 root 权限。仓库和镜像设置沿用 pacman 的配置。属于 pacutils 软件包的一部分，默认不安装。

# HISTORY

**pacsync** 由 **Andrew Gregory** 创建，是 pacman 辅助工具集 **pacutils** 的一部分。与直接调用 pacman 相比，它为数据库同步提供了更简单的接口。

# SEE ALSO

[pacman](/man/pacman)(8), [pactrans](/man/pactrans)(1), [pacinstall](/man/pacinstall)(1)
