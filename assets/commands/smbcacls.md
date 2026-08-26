# TAGLINE

管理 SMB 文件共享上的 Windows ACL

# TLDR

**显示** SMB 共享上某个文件的 **ACL**

```smbcacls //[server]/[share] [path/to/file] --user [domain\\username]%[password]```

**设置**新的 ACL

```smbcacls //[server]/[share] [path/to/file] --user [username]%[password] "ACL:[DACL]"```

**重置** ACL 并设置新值

```smbcacls //[server]/[share] [path/to/file] --user [username]%[password] "RESET" "ACL:[DACL]"```

**更改文件的所有者**

```smbcacls //[server]/[share] [path/to/file] --chown [domain\\user] --user [username]```

**递归**执行 ACL 操作

```smbcacls //[server]/[share] [path/to/dir] --recurse --user [username]```

# SYNOPSIS

**smbcacls** _//server/share_ _filename_ [_OPTIONS_]

# PARAMETERS

**-a, --add** _acl_
> 添加 ACE 条目，不修改已有条目

**-M, --modify** _acl_
> 修改指定 ACE 的权限掩码

**-D, --delete** _acl_
> 删除指定的 ACE 条目

**-S, --set** _acl_
> 用新条目替换整个 ACL

**-C, --chown** _name_
> 更改文件/目录的所有者

**-G, --chgrp** _name_
> 更改组所有权

**-I, --inherit** _allow|remove|copy_
> 启用、移除或复制继承的权限

**--recurse**
> 对目录递归应用操作

**--numeric**
> 以数字格式显示 ACL

**--sddl**
> 输入/输出使用 SDDL 格式

**--save** _file_
> 将 DACL 保存到文件以便日后恢复

**--restore** _file_
> 从保存的文件恢复 DACL

**-U, --user** _username_
> SMB 用户名（格式：user%password 或 domain\\user%password）

**-W, --workgroup** _domain_
> 设置 SMB 工作组/域

**-d, --debuglevel** _level_
> 调试详细程度（0-10）

# DESCRIPTION

**smbcacls** 操作 SMB/CIFS 文件共享上的 Windows NT 访问控制列表（ACL）。它让你可以在 Linux 命令行中查看、修改和管理远程 Windows 或 Samba 共享上的文件权限。

一个 ACL 由若干访问控制条目（ACE）组成，每条定义特定用户或组的权限。该工具支持标准的 Windows 权限操作，包括所有者变更和继承管理。

# CAVEATS

修改 ACL 需要对共享具有相应权限。ACL 格式遵循 Windows SDDL（Security Descriptor Definition Language）约定。某些操作需要对目标共享的管理员权限。域环境可能需要 Kerberos 身份验证。

# HISTORY

**smbcacls** 是 **Samba** 套件的一部分，由 **Andrew Tridgell** 自 **1992 年**起开发。Samba 为 Unix/Linux 系统提供与 Windows 的互操作性。smbcacls 工具让 Unix 管理员无需 Windows 工作站即可管理 Windows 风格的权限。

# INSTALL

```apt: sudo apt install smbclient```

```dnf: sudo dnf install samba-client```

```pacman: sudo pacman -S smbclient```

```apk: sudo apk add samba-client```

```zypper: sudo zypper install samba-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[smbclient](/man/smbclient)(1), [mount.cifs](/man/mount.cifs)(8), [getfacl](/man/getfacl)(1), [setfacl](/man/setfacl)(1)
