# TAGLINE

NTFS 安全数据审计工具

# TLDR

**递归审计卷上的全部安全数据**

```sudo ntfs-3g.secaudit -ar [/dev/sda1]```

**显示目录中文件的权限**

```sudo ntfs-3g.secaudit [/dev/sda1] [/path/to/directory]```

**递归显示目录中的权限**

```sudo ntfs-3g.secaudit -r [/dev/sda1] [/path/to/directory]```

**将卷和目录中的 ACL 备份到文件**

```sudo ntfs-3g.secaudit -b [/dev/sda1] [/path] > [backup.txt]```

**从备份文件恢复 ACL**

```sudo ntfs-3g.secaudit -s [/dev/sda1] < [backup.txt]```

**获取用户映射建议**

```sudo ntfs-3g.secaudit -u [/dev/sda1] [/path/to/windows/file]```

# SYNOPSIS

**ntfs-3g.secaudit** **-a**[**rv**] _volume_
**ntfs-3g.secaudit** **-b**[**v**] _volume_ [_directory_]
**ntfs-3g.secaudit** **-s**[**ev**] _volume_ [_backup-file_]
**ntfs-3g.secaudit** **-r**[**v**] _volume_ _directory_
**ntfs-3g.secaudit** **-u**[**v**] _volume_ _mounted-file_
**ntfs-3g.secaudit** **-h** _file_
**ntfs-3g.secaudit** _volume_ _directory_

# PARAMETERS

**-a**
> 审计卷上所有全局安全数据。与 -r 组合可同时扫描所有文件和目录。

**-b**
> 递归提取 NTFS ACL 到标准输出，用于备份。

**-s**
> 从备份文件或标准输入设置 NTFS ACL。与 -e 组合可同时恢复额外参数（Windows attrib）。

**-e**
> 与 -s 配合使用，设置已备份的额外参数。

**-r**
> 递归进入子目录。与 -a 配合时，检查文件与全局安全数据的关系。

**-u**
> 基于某个已挂载文件的 Windows 所有者信息，显示建议的用户映射文件。

**-h _file_**
> 以人类可读的形式显示已保存文件中的十六进制安全描述符。

**-v**
> 详细输出。使用两次可获得非常详细的输出。

# DESCRIPTION

**ntfs-3g.secaudit** 显示 NTFS 文件系统上文件的所有权和权限，并检查其一致性。它可以审计安全数据、备份和恢复 ACL，并提出用户映射建议。卷必须处于卸载状态，且必须以 root 身份运行命令。

# CAVEATS

需要 root 权限。使用前必须卸载卷。对大目录操作时应将输出重定向到文件。成功时返回 0，检测到错误时返回 1。

# HISTORY

**ntfs-3g.secaudit** 是 **ntfs-3g** 项目的一部分，为 Linux 上的 NTFS 文件系统提供安全审计和 ACL 管理功能。

# SEE ALSO

[ntfs-3g](/man/ntfs-3g)(8), [ntfs-3g.usermap](/man/ntfs-3g.usermap)(8)
