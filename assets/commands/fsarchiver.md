# TAGLINE

文件系统备份与恢复工具

# TLDR

将文件系统**保存到归档**

```sudo fsarchiver savefs [archive.fsa] [/dev/sda1]```

**从归档恢复文件系统**

```sudo fsarchiver restfs [archive.fsa] id=0,dest=[/dev/sda1]```

**保存多个文件系统**

```sudo fsarchiver savefs [archive.fsa] [/dev/sda1] [/dev/sda2]```

**列出归档内容**

```fsarchiver archinfo [archive.fsa]```

以压缩方式**保存**

```sudo fsarchiver savefs -z9 [archive.fsa] [/dev/sda1]```

以加密方式**保存**

```sudo fsarchiver savefs -c [password] [archive.fsa] [/dev/sda1]```

# SYNOPSIS

**fsarchiver** _command_ [_options_] _archive_ [_filesystem_...]

# PARAMETERS

**savefs**
> 将文件系统保存到归档。

**restfs**
> 从归档恢复文件系统。

**archinfo**
> 显示归档信息。

**probe**
> 显示检测到的文件系统。

**-z** _level_
> 压缩级别（0-9）。

**-j** _jobs_
> 并行压缩任务数。

**-c** _password_
> 加密归档。

**-v**
> 详细输出。

**-A**
> 允许恢复到更小的文件系统。

# DESCRIPTION

**fsarchiver** 将文件系统保存到归档文件或从中恢复。与 tar 不同，它会保留文件系统属性、ACL 和扩展属性，并且可以恢复到不同大小的分区。

该工具在文件系统层面工作，只保存已使用的块。它支持 ext2/3/4、XFS、Btrfs、NTFS 等文件系统，并可选压缩和加密。

# CAVEATS

要获得可靠的备份，必须先卸载文件系统。只要目标支持相应特性，就可以跨不同文件系统类型恢复。恢复可能会改变 UUID。归档带有校验和保护，可检测损坏。

# HISTORY

fsarchiver 由 **Francois Dupoux** 创建，是 partimage 等分区镜像工具更灵活的替代方案。它的设计目标是通过在文件系统层面工作来克服块级备份的局限。

# INSTALL

```apt: sudo apt install fsarchiver```

```dnf: sudo dnf install fsarchiver```

```pacman: sudo pacman -S fsarchiver```

```apk: sudo apk add fsarchiver```

```zypper: sudo zypper install fsarchiver```

```nix: nix profile install nixpkgs#fsarchiver```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[partclone](/man/partclone)(8), [tar](/man/tar)(1), [dd](/man/dd)(1), [rsync](/man/rsync)(1)

# RESOURCES

```[Source code](https://github.com/fdupoux/fsarchiver)```

```[Homepage](https://www.fsarchiver.org/)```

<!-- verified: 2026-07-15 -->
