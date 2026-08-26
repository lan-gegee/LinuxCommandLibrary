# TAGLINE

从系统中移除组

# TLDR

**删除一个组**

```sudo delgroup [groupname]```

**将用户从组中移除**

```sudo delgroup [username] [groupname]```

**删除系统组**

```sudo delgroup --system [groupname]```

**仅在组为空时删除**

```sudo delgroup --only-if-empty [groupname]```

# SYNOPSIS

**delgroup** [_options_] _group_

**delgroup** [_options_] _user_ _group_

# DESCRIPTION

**delgroup** 用于从系统中删除组，或将用户从某个组中移除。它是 groupdel 在 Debian/Ubuntu 上的对应命令，并带有额外的安全保护。

只给组名时会直接删除该组；同时给出用户名和组名时，则把该用户从这个组中移除，而不删除组本身。

# PARAMETERS

**--system**
> 仅当目标为系统组时才执行操作（否则失败）。也会影响 adduser 中的创建逻辑。

**--only-if-empty**
> 仅当组没有成员时才移除。

**--backup**
> 备份被删除的文件（供 deluser 使用；保留于此以保持对称）。

**--backup-to** _dir_
> 将备份放到 _dir_ 目录而不是当前目录。

**--remove-home**
> （deluser）删除用户的主目录。此处列出仅供参考。

**--group**
> 即使给定了用户名也强制按组处理。避免调用含义含糊不清。

**-q**, **--quiet**
> 抑制提示性消息。

**-v**, **--verbose**
> 输出更详细的进度信息。

**--conf** _FILE_
> 使用其他 `deluser.conf` 配置文件。

**--help**
> 显示帮助信息。

**--version**
> 显示版本。

# CONFIGURATION

**/etc/deluser.conf**
> 控制 deluser 与 delgroup 操作的默认行为。

# CAVEATS

需要 root 权限。用户仍存在时无法删除其主组。被删组的所属文件仍保留数字 GID。这是 Debian/Ubuntu 特有的命令。

# HISTORY

**delgroup** 是 **adduser** 软件包的一部分，为 **Debian** Linux 创建，目的是提供比底层命令更友好的用户/组管理。它包装了 groupdel 和 gpasswd，并增加了检查和配置选项。

# SEE ALSO

[groupdel](/man/groupdel)(1), [deluser](/man/deluser)(1), [addgroup](/man/addgroup)(1), [gpasswd](/man/gpasswd)(1)
