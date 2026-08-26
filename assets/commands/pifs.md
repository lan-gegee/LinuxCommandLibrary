# TAGLINE

由 π 支撑的无数据 FUSE 文件系统

# TLDR

**挂载 πfs 文件系统**

```pifs -o mdd=[/path/to/metadata] [mountpoint]```

**从源码构建**

```./autogen.sh && ./configure && make && sudo make install```

# SYNOPSIS

**pifs** **-o** _mdd=metadata-directory_ [_mountpoint_]

# PARAMETERS

**-o mdd=**_path_
> πfs 存储元数据的目录（文件名及字节在 π 中的偏移量）。

_mountpoint_
> 文件系统的挂载点目录。

# DESCRIPTION

**pifs**（πfs）是一个 FUSE 用户空间文件系统，它通过定位每个字节在 π 数字中的位置而非磁盘来存储文件数据。由于 π 被猜想是正规数，任何有限的字节序列理论上都存在于它的展开之中；πfs 只记录检索每个字节所需的索引和长度。

文件被拆分为单个字节，每个字节使用 Bailey–Borwein–Plouffe 公式在 π 中查找。元数据（路径和偏移量）写入 **mdd=** 给出的目录。这个文件系统在很大程度上只是一个概念验证：即使存储小文件也极其缓慢，因为在 π 中定位任意数字序列的计算代价很高。

需要 **libfuse** 和 C 构建工具链。在基于 Debian 的系统上安装构建依赖：**autotools-dev**、**automake** 和 **libfuse-dev**。

# CAVEATS

查找性能对真实工作负载来说不切实际；项目 README 提到存储一个 400 行的文本文件可能需要几分钟。如果元数据丢失，即使数据仍然存在于 π 中，文件位置也无法恢复。更新的相关项目见 inferencefs。

# HISTORY

πfs 由 Philip L. 创建，是对"所有可能的数据早已存在于 π 中"这一想法的幽默探索，灵感来自 2001 年的一个观察：若 π 是正规数，它将包含每一个有限文件。该仓库自首次发布以来已被广泛分享。

# SEE ALSO

[fusermount](/man/fusermount)(1), [mount](/man/mount)(8)

# RESOURCES

```[Source code](https://github.com/philipl/pifs)```

<!-- verified: 2026-06-11 -->
