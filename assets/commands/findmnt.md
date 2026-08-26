# TAGLINE

查询和校验已挂载的文件系统

# TLDR

**列出**所有已挂载的文件系统

```findmnt```

按**设备**搜索

```findmnt /dev/sdb1```

按**挂载点**搜索

```findmnt /```

按**类型**过滤

```findmnt -t ext4,btrfs```

像 df 一样显示**磁盘用量**

```findmnt -D```

按**标签**查找

```findmnt LABEL=BigStorage```

以 **JSON** 格式输出

```findmnt --json```

**校验** fstab

```findmnt -x --verbose```

# SYNOPSIS

**findmnt** [_OPTIONS_] [_device_|_mountpoint_]

# DESCRIPTION

**findmnt** 列出所有已挂载的文件系统，也可以按设备、挂载点、标签或 UUID 搜索某个文件系统。它还能检查挂载表以及 fstab 配置中有无错误。

# PARAMETERS

**-t, --types** _list_
> 只显示指定类型的文件系统

**-o, --output** _list_
> 定义输出的列

**-l, --list**
> 使用列表形式的输出格式

**-D, --df**
> 模仿 df 的输出（显示空间使用情况）

**-x, --verify**
> 校验挂载表内容

**-n, --noheadings**
> 不打印列标题

**-r, --raw**
> 使用原始输出格式

**-J, --json**
> 使用 JSON 输出格式

**-f, --first-only**
> 只打印第一个匹配的文件系统

**-s, --fstab**
> 在 /etc/fstab 中搜索而不是 /proc/self/mountinfo

**-S, --source** _spec_
> 显式指定挂载来源（设备、LABEL=、UUID= 等）

**-M, --mountpoint** _path_
> 显式指定挂载点文件或目录

**-T, --target** _path_
> 查找给定路径（任意文件或目录）所在的文件系统

**-p, --poll**[=_list_]
> 监视 /proc/self/mountinfo 的变化（动作：mount、umount、remount、move）

**-R, --submounts**
> 递归打印所选文件系统的全部子挂载

**LABEL=**_label_
> 按文件系统标签搜索

**UUID=**_uuid_
> 按文件系统 UUID 搜索

# CAVEATS

verify 选项只负责检查配置错误，不会真正挂载任何东西。输出格式在不同系统和内核版本之间可能有差异。

# HISTORY

**findmnt** 是 **util-linux** 软件包的一部分，用于在 Linux 系统上查询挂载信息。

# INSTALL

```apt: sudo apt install util-linux```

```dnf: sudo dnf install util-linux```

```pacman: sudo pacman -S util-linux```

```apk: sudo apk add findmnt```

```zypper: sudo zypper install util-linux```

```brew: brew install util-linux```

```nix: nix profile install nixpkgs#util-linux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mount](/man/mount)(8), [umount](/man/umount)(8), [df](/man/df)(1), [lsblk](/man/lsblk)(8), [blkid](/man/blkid)(8), [mountpoint](/man/mountpoint)(1)
