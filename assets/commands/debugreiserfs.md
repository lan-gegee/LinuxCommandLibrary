# TAGLINE

ReiserFS 文件系统调试工具

# TLDR

**显示超级块**信息

```debugreiserfs [/dev/sda1]```

**转储文件系统树**

```debugreiserfs -d [/dev/sda1]```

**打印日志内容**

```debugreiserfs -j [/dev/sda1]```

**显示块**信息

```debugreiserfs -1 [block_number] [/dev/sda1]```

**扫描 reiserfs** 文件系统

```debugreiserfs -S [/dev/sda1]```

**解包元数据**到目录

```debugreiserfs -u [/output/dir] [/dev/sda1]```

# SYNOPSIS

**debugreiserfs** [_options_] _device_

# PARAMETERS

_DEVICE_
> 要检查的 ReiserFS 文件系统设备。

**-d**
> 转储文件系统树。

**-j**
> 打印日志内容。

**-J**
> 仅打印日志头。

**-1** _BLOCK_
> 打印特定块的信息。

**-S**
> 在分区中扫描 reiserfs 文件系统。

**-u** _DIR_
> 解包元数据到目录。

**-p**
> 以十六进制打印条目内容。

**-q**
> 安静模式。

# DESCRIPTION

**debugreiserfs** 是 ReiserFS 文件系统的调试工具。它可以在不挂载文件系统的情况下显示其内部结构，包括超级块、日志和 B+ 树节点。

该工具对诊断 ReiserFS 问题、理解文件系统结构和恢复数据很有价值。它可以转储整个文件系统树、检查特定块，并提取元数据进行分析。

debugreiserfs 在未挂载的文件系统上工作，提供了正常文件系统操作无法触及的 ReiserFS 内部底层访问能力。

# CAVEATS

仅适用于 ReiserFS（v3）文件系统。为保证结果一致，检查期间设备不应处于挂载状态。在大文件系统上某些操作可能耗时较长。不支持 Reiser4。

# HISTORY

debugreiserfs 是 **reiserfsprogs** 软件包的一部分。ReiserFS 由 **Hans Reiser** 和 Namesys 创建，随 Linux 2.4.1（**2001 年**）引入，是主线的内核中包含的首个日志文件系统。

# INSTALL

```apt: sudo apt install reiserfsprogs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[debugfs](/man/debugfs)(8)
