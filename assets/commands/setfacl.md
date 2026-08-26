# TAGLINE

设置文件访问控制列表

# TLDR

为用户设置**读/写**权限

```setfacl -m u:username:rw path/to/file```

为目录中的新文件设置**默认 ACL**

```setfacl -d -m u::rw path/to/directory```

**移除**特定用户的 ACL

```setfacl -x u:username path/to/file```

移除**所有**扩展 ACL 条目

```setfacl -b path/to/file```

以**递归**方式将 ACL 应用于目录

```setfacl -R -m u:username:rx path/to/directory```

将一个文件的 ACL **复制**到另一个文件

```getfacl file1 | setfacl --set-file=- file2```

通过 ACL 设置**组**权限

```setfacl -m g:groupname:r path/to/file```

# SYNOPSIS

**setfacl** [_-bkndRLPvh_] [{_-m_|_-x_} _acl_spec_] [{_-M_|_-X_} _acl_file_] _file_...

# DESCRIPTION

**setfacl** 设置文件和目录的访问控制列表（ACL）。ACL 在传统的 Unix 所有者/组/其他权限模型之外提供细粒度的访问控制，可为单个用户和组指定特定权限。

# PARAMETERS

**-m, --modify**
> 使用指定条目修改 ACL。

**-x, --remove**
> 移除指定的 ACL 条目。

**-M, --modify-file**
> 从文件中读取要修改的 ACL 条目。

**-X, --remove-file**
> 从文件中读取要移除的 ACL 条目。

**-b, --remove-all**
> 移除所有扩展 ACL 条目。

**-k, --remove-default**
> 移除默认 ACL。

**-d, --default**
> 将操作应用于默认 ACL。

**-n, --no-mask**
> 不重新计算有效权限掩码。

**--mask**
> 强制重新计算有效权限掩码。

**-R, --recursive**
> 递归地应用操作。

**-L, --logical**
> 跟随指向目录的符号链接（与 -R 一起使用）。

**-P, --physical**
> 不跟随符号链接（与 -R 一起使用）。

**--restore=file**
> 从 getfacl 备份恢复权限。

**--test**
> 测试模式——列出结果 ACL 但不做修改。

# ACL ENTRY FORMAT

**u[ser]:uid:perms**: Named user or owner permissions
**g[roup]:gid:perms**: Named group or owning group permissions
**m[ask]:perms**: Effective rights mask
**o[ther]:perms**: Permissions for others

Permissions: r (read), w (write), x (execute), or numeric (4, 2, 1).

# CAVEATS

有效权限掩码会限制授予具名用户/组的权限。某些文件系统（如 FAT、不支持 ACL 的 NFS）不支持 ACL。修改前请用 **getfacl** 备份 ACL。默认 ACL 仅适用于目录内新建的文件。

# HISTORY

**setfacl** 是 **acl** 软件包的一部分，实现 POSIX 访问控制列表（POSIX 1003.1e draft 17）。ACL 扩展了标准的 Unix 权限模型。

# INSTALL

```apt: sudo apt install acl```

```dnf: sudo dnf install acl```

```pacman: sudo pacman -S acl```

```apk: sudo apk add acl```

```zypper: sudo zypper install acl```

```brew: brew install acl```

```nix: nix profile install nixpkgs#acl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[getfacl](/man/getfacl)(1), [chmod](/man/chmod)(1), [umask](/man/umask)(1), [acl](/man/acl)(5)
