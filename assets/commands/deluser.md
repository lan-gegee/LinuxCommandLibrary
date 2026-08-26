# TAGLINE

从系统中移除用户

# TLDR

**移除**一个用户

```sudo deluser [username]```

移除用户及其**主目录**

```sudo deluser --remove-home [username]```

移除用户、**备份文件**并删除主目录

```sudo deluser --backup-to [path/to/backup_directory] --remove-home [username]```

移除用户及其**所有所属文件**

```sudo deluser --remove-all-files [username]```

将用户从某个**组中移除**

```sudo deluser [username] [group]```

# SYNOPSIS

**deluser** [_options_] _user_ [_group_]

# DESCRIPTION

**deluser** 用于从系统中删除用户。它可以选择同时删除用户的主目录、邮件 spool 和其他文件。它是 userdel 在 Debian/Ubuntu 上的对应命令。

同时给出用户名和组名时，它只把该用户从组中移除，而不删除用户账户。

# PARAMETERS

**--remove-home**
> 删除用户的主目录

**--remove-all-files**
> 删除该用户拥有的所有文件

**--backup**
> 删除前先备份文件

**--backup-to** _dir_
> 备份的目标目录

**--system**
> 仅当为系统用户时才删除

# CONFIGURATION

**/etc/deluser.conf**
> 控制默认行为，包括是否删除主目录以及备份设置。

# CAVEATS

需要 root 权限。删除重要用户时请使用 --backup。目标用户必须未登录。非 Debian 系统请改用 userdel。

# SEE ALSO

[userdel](/man/userdel)(8), [adduser](/man/adduser)(8), [delgroup](/man/delgroup)(8)

# RESOURCES

```[Source code](https://salsa.debian.org/debian/adduser)```

```[Documentation](https://manpages.debian.org/deluser.8)```

<!-- verified: 2026-07-11 -->
