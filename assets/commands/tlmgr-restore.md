# TAGLINE

从备份恢复 TeX Live 软件包

# TLDR

**列出可用备份**

```tlmgr restore```

**恢复软件包**

```tlmgr restore [package] [revision]```

**从备份恢复全部**

```tlmgr restore --all```

# SYNOPSIS

**tlmgr restore** [_options_] [_package_ [_revision_]]

# PARAMETERS

**--all**
> 恢复所有软件包。

**--backupdir** _dir_
> 备份来源目录。

**--dry-run**
> 显示将要恢复的内容。

_revision_
> 要恢复到的特定修订版本。

# DESCRIPTION

**tlmgr restore** 从备份恢复 TeX Live 软件包。在有问题的更新之后回退到先前版本。TeX Live Manager 的组成部分。

# SEE ALSO

[tlmgr-backup](/man/tlmgr-backup)(1), [tlmgr](/man/tlmgr)(1)
