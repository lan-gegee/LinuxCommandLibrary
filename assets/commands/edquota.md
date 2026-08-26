# TAGLINE

磁盘配额编辑器

# TLDR

编辑**当前用户**的配额

```edquota -u $(whoami)```

编辑**特定用户**的配额

```sudo edquota -u [username]```

编辑**组**的配额

```sudo edquota -g [group]```

限定于**特定文件系统**

```sudo edquota -f [filesystem]```

编辑默认**宽限期**

```sudo edquota -t```

**复制**配额到其他用户

```sudo edquota -p [reference_user] [destination_user1] [destination_user2]```

# SYNOPSIS

**edquota** [_options_] _name_...

# DESCRIPTION

**edquota** 编辑用户、组或项目的磁盘配额。它把当前的限制和用量写入一个临时文件，在编辑器中打开它，并将你保存的内容应用回配额系统。

每一行对应一个文件系统，包含四个可编辑的数字：块的软限制和硬限制，以及 inode 的软限制和硬限制。用量列仅供参考，对其所做的任何修改都会被忽略。限制为 0 表示不设限制。

# PARAMETERS

**-u, --user**
> 编辑用户配额（默认）

**-g, --group**
> 编辑组配额

**-P, --project**
> 编辑项目配额

**-f, --filesystem** _fs_
> 将操作限定到单个文件系统

**-F, --format** _format_
> 要使用的配额格式：vfsold、vfsv0、vfsv1 或 rpc

**-t, --edit-period**
> 编辑宽限期而不是限制值

**-T, --edit-times**
> 编辑单个用户或组超出软限制的时间

**-p, --prototype** _user_
> 将原型用户或组的配额设置复制到指定用户

**-r, --remote**
> 通过 RPC 编辑远程服务器上的配额

# CONFIGURATION

**aquota.user** / **aquota.group**（位于文件系统根目录）
> 现代 vfsv0/vfsv1 格式的配额文件。较旧的 vfsold 文件系统使用 quota.user 和 quota.group。XFS 以及启用 quota 特性的 ext4 会将配额信息保存在隐藏的元数据 inode 中，不存在可见文件。

**/etc/fstab**
> 文件系统必须以 usrquota、grpquota 和/或 prjquota 挂载，配额才会生效。

# CAVEATS

必须先在文件系统上启用配额（参见 quotacheck 和 quotaon），edquota 才能发挥作用。编辑他人的配额需要 root 权限。编辑器依次从 $EDITOR、$VISUAL 中选择，最后回退到 vi。保存无法再解析的文件会使配额保持不变。

# INSTALL

```apt: sudo apt install quota```

```dnf: sudo dnf install quota```

```pacman: sudo pacman -S quota-tools```

```apk: sudo apk add quota-tools```

```zypper: sudo zypper install quota```

```nix: nix profile install nixpkgs#quota```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[quota](/man/quota)(1), [repquota](/man/repquota)(8), [quotaon](/man/quotaon)(8), [quotacheck](/man/quotacheck)(8), [setquota](/man/setquota)(8)

# RESOURCES

```[Source code](https://sourceforge.net/p/linuxquota/code/ci/master/tree/)```

```[Homepage](https://sourceforge.net/projects/linuxquota/)```

<!-- verified: 2026-07-14 -->
