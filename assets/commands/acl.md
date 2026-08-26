# TAGLINE

细粒度文件权限管理

# TLDR

**查看文件的 ACL**

```getfacl [path/to/file]```

**为特定用户设置读写权限**

```setfacl -m u:[username]:rw [path/to/file]```

**为组设置权限**

```setfacl -m g:[groupname]:rx [path/to/directory]```

**移除用户的 ACL 条目**

```setfacl -x u:[username] [path/to/file]```

**移除文件的所有 ACL 条目**

```setfacl -b [path/to/file]```

**为目录中新文件设置默认 ACL**

```setfacl -d -m u:[username]:rwx [path/to/directory]```

对目录**递归应用 ACL**

```setfacl -R -m u:[username]:rx [path/to/directory]```

**将 ACL 从一个文件复制到另一个**

```getfacl [source_file] | setfacl --set-file=- [target_file]```

# SYNOPSIS

**getfacl** [_options_] _file_...

**setfacl** [_options_] _acl_spec_ _file_...

# PARAMETERS

**-m** _acl_spec_
> 通过添加或更新条目来修改 ACL。

**-x** _acl_spec_
> 移除指定的 ACL 条目。

**-b**
> 移除所有扩展 ACL 条目。

**-d**
> 将操作应用于默认 ACL（针对目录）。

**-R**
> 递归应用于目录及其内容。

**-k**
> 移除默认 ACL。

**--set** _acl_spec_
> 用指定的条目替换整个 ACL。

**--set-file** _file_
> 从文件读取 ACL 条目（用 **-** 表示标准输入）。

**-n**
> 不重新计算有效权限掩码。

# DESCRIPTION

**访问控制列表（ACL）**扩展了传统的 Unix 权限模型，允许在单个文件或目录上为多个用户和组设置细粒度权限。标准权限只支持所有者、组和其他人三类，而 ACL 可以为任意数量的具名用户和组指定不同的访问权限。

**getfacl** 命令显示 ACL 条目，**setfacl** 命令修改它们。ACL 条目的格式为 **type:name:permissions**，其中 type 为 **u**（用户）、**g**（组）、**o**（其他）或 **m**（掩码），name 标识用户或组，permissions 是 **r**（读）、**w**（写）、**x**（执行）的组合。

目录上的默认 ACL 决定在其中创建的新文件的初始 ACL。ACL 掩码条目限制了授予具名用户和组的有效权限。

# CAVEATS

并非所有文件系统都支持 ACL；ext4、XFS 和 Btrfs 在以 ACL 支持挂载时支持。某些备份和归档工具可能不会保留 ACL。带 ACL 的文件会在 **ls -l** 输出的权限位后显示一个 **+**。NFSv4 使用与 POSIX ACL 不同的 ACL 模型。

# HISTORY

POSIX ACL 于 **20 世纪 90 年代**作为 POSIX 1003.1e 草案标准的一部分开发，该草案最终被撤回但已被广泛实现。Linux 的 ACL 支持在 **2.6** 版本（2003 年）加入内核。该规范旨在提供跨 Unix 系统的可移植 ACL 接口，但具体实现细节因操作系统而异。

# INSTALL

```dnf: sudo dnf install acl```

```pacman: sudo pacman -S acl```

```zypper: sudo zypper install acl```

```brew: brew install acl```

```nix: nix profile install nixpkgs#acl```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[chmod](/man/chmod)(1), [chown](/man/chown)(1), [getfacl](/man/getfacl)(1), [setfacl](/man/setfacl)(1), [ls](/man/ls)(1)

# RESOURCES

```[Source code](https://git.savannah.nongnu.org/cgit/acl.git)```

```[Homepage](https://savannah.nongnu.org/projects/acl/)```

<!-- verified: 2026-06-10 -->
