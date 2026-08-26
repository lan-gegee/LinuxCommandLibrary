# TAGLINE

从命令行设置磁盘配额

# TLDR

为用户**设置配额**（含软限制和硬限制）

```sudo setquota -u [username] [block-soft] [block-hard] [inode-soft] [inode-hard] [/path/to/filesystem]```

为组**设置配额**

```sudo setquota -g [groupname] [block-soft] [block-hard] [inode-soft] [inode-hard] [/path/to/filesystem]```

将一个用户的配额设置**复制**到另一个用户

```sudo setquota -u -p [prototype_user] [target_user] [/path/to/filesystem]```

在所有启用了配额的文件系统上**设置配额**

```sudo setquota -a -u [username] [block-soft] [block-hard] [inode-soft] [inode-hard]```

为用户**设置宽限时间**

```sudo setquota -t -u [block-grace] [inode-grace] [/path/to/filesystem]```

从批量输入**设置配额**

```echo "[username] [block-soft] [block-hard] [inode-soft] [inode-hard]" | sudo setquota -b [/path/to/filesystem]```

# SYNOPSIS

**setquota** [**-u**|**-g**|**-P**] [_options_] _name_ _block-softlimit_ _block-hardlimit_ _inode-softlimit_ _inode-hardlimit_ _filesystem_

**setquota** [**-u**|**-g**|**-P**] **-p** _protoname_ _name_ _filesystem_

**setquota** **-t** [**-u**|**-g**|**-P**] _block-grace_ _inode-grace_ _filesystem_

**setquota** **-T** [**-u**|**-g**|**-P**] _name_ _block-time_ _inode-time_ _filesystem_

# PARAMETERS

**-u**, **--user**
> 为指定用户设置用户配额。这是默认行为。

**-g**, **--group**
> 为指定组设置组配额。

**-P**, **--project**
> 为指定项目设置项目配额。

**-p**, **--prototype** _protoname_
> 从原型用户、组或项目复制配额设置。

**-b**, **--batch**
> 从标准输入读取配额信息。格式：name block-softlimit block-hardlimit inode-softlimit inode-hardlimit。

**-t**, **--edit-period**
> 为用户、组或项目设置宽限时间（秒）。

**-T**, **--edit-times**
> 修改单个用户在软限制生效后的剩余时间。

**-a**, **--all**
> 应用于 /etc/mtab 中列出的所有启用了配额的文件系统。

**-F**, **--format** _quotaformat_
> 指定配额格式：**vfsold**、**vfsv0**、**vfsv1**、**rpc** 或 **xfs**。

**-r**, **--remote**
> 使用 rpc.rquotad 编辑远程配额。

# DESCRIPTION

**setquota** 是一个命令行配额编辑器，用于在文件系统上为用户、组或项目设置磁盘配额。与交互式的 **edquota** 命令不同，setquota 允许在单条命令中完成配额配置，适合脚本和自动化场景。

配额可以同时限制磁盘空间用量（块）和文件数量（inode）。每种限制都有软限制（可暂时超出）和硬限制（绝对上限）。超出软限制后宽限期开始计时，期满后软限制将变为硬限制。

块限制通常以千字节为单位，但可能因配额格式而异。如果给定的是数字而非用户名，则会被视为 UID/GID/项目 ID。

# CAVEATS

需要 root 权限。文件系统必须已启用配额支持并用 **quotacheck** 初始化了配额文件。更改立即生效，无需重新挂载。并非所有配额格式都支持所有特性。

# HISTORY

**setquota** 属于 Linux Diskquota Tools 项目。磁盘配额自 20 世纪 80 年代起就是 Unix 系统的一部分，最早出现在 BSD Unix 中。Linux 配额系统由这些早期实现演化而来，现代工具支持多种配额格式，包括 XFS 原生配额和 NFS 远程配额。

# INSTALL

```apt: sudo apt install quota```

```dnf: sudo dnf install quota```

```pacman: sudo pacman -S quota-tools```

```apk: sudo apk add quota-tools```

```zypper: sudo zypper install quota```

```nix: nix profile install nixpkgs#quota```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[quota](/man/quota)(1), [edquota](/man/edquota)(8), [repquota](/man/repquota)(8), [quotacheck](/man/quotacheck)(8), [quotaon](/man/quotaon)(8)
