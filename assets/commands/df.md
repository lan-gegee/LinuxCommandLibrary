# TAGLINE

查看已挂载文件系统的磁盘空间使用情况

# TLDR

显示**所有文件系统**及其磁盘使用量

```df```

以**人类可读**的形式显示文件系统

```df -h```

显示**指定路径**所在文件系统的信息

```df [path/to/file_or_directory]```

包含**空闲 inode** 的统计

```df -i```

显示文件系统但排除**特定类型**

```df -x squashfs -x tmpfs```

显示**文件系统类型**

```df -T```

# SYNOPSIS

**df** [_-h_] [_-i_] [_-T_] [_-x type_] [_file_...]

# DESCRIPTION

**df**（disk free）显示文件系统上的可用磁盘空间。默认情况下，它列出所有已挂载的文件系统，包括总容量、已用空间、可用空间和使用百分比。

# PARAMETERS

**-h, --human-readable**
> 以人类可读格式（K、M、G）输出大小

**-H, --si**
> 以 1000（而非 1024）为底数计算大小

**-i, --inodes**
> 显示 inode 信息而不是块使用情况

**-T, --print-type**
> 输出文件系统类型

**-t, --type type**
> 只列出指定类型的文件系统

**-x, --exclude-type type**
> 排除指定类型的文件系统

**-a, --all**
> 包含虚拟文件系统

**-l, --local**
> 只列出本地文件系统

**--total**
> 附加一行总计

**-P, --portability**
> 使用 POSIX 输出格式

# CAVEATS

由于文件系统开销和保留空间，显示的大小可能与实际文件大小不一致。某些文件系统为 root 保留了空间，普通用户看不到这部分可用空间。

# HISTORY

属于 **GNU Coreutils** 的一部分。df 命令起源于 **1971 年**的 **Version 1 AT&T UNIX**。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```apk: sudo apk add coreutils```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[du](/man/du)(1), [lsblk](/man/lsblk)(8), [mount](/man/mount)(8)

# RESOURCES

```[Homepage](https://www.gnu.org/software/coreutils/)```

```[Documentation](https://www.gnu.org/software/coreutils/manual/html_node/df-invocation.html)```

<!-- verified: 2026-07-11 -->
