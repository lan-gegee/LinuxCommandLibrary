# TAGLINE

备份 TeX Live 软件包

# TLDR

**备份软件包**

```tlmgr backup [package]```

**备份所有软件包**

```tlmgr backup --all```

**备份到指定目录**

```tlmgr backup --backupdir [/path/to/backup] [package]```

**清理旧备份**

```tlmgr backup --clean [days]```

# SYNOPSIS

**tlmgr backup** [_options_] [_package_...]

# PARAMETERS

**--all**
> 备份所有已安装的软件包。

**--backupdir** _dir_
> 备份目标目录。

**--clean** _n_
> 删除 n 天前的备份。

**--dry-run**
> 显示将要执行的操作。

# DESCRIPTION

**tlmgr backup** 创建 TeX Live 软件包的备份。在更新或系统更改前很有用。TeX Live Manager 的组成部分。

# SEE ALSO

[tlmgr-restore](/man/tlmgr-restore)(1), [tlmgr-update](/man/tlmgr-update)(1)
