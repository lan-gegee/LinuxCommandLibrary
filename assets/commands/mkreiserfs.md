# TAGLINE

创建 ReiserFS 文件系统

# TLDR

**创建 ReiserFS 文件系统**

```mkreiserfs [/dev/sdb1]```

**强制创建**

```mkreiserfs -f [/dev/sdb1]```

**设置卷标**

```mkreiserfs -l "[label]" [/dev/sdb1]```

**设置 UUID**

```mkreiserfs -u [uuid] [/dev/sdb1]```

**安静模式**

```mkreiserfs -q [/dev/sdb1]```

# SYNOPSIS

**mkreiserfs** [_options_] _device_

# PARAMETERS

_DEVICE_
> 要格式化的块设备。

**-f**
> 强制创建。

**-l** _LABEL_
> 卷标。

**-u** _UUID_
> 设置 UUID。

**-q**
> 安静模式。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mkreiserfs** 创建 ReiserFS 文件系统。ReiserFS 是一款日志文件系统。

该工具将分区格式化为 ReiserFS。以高效处理小文件著称。

# CAVEATS

ReiserFS 已属遗留技术。建议改用 ext4 或 btrfs。会销毁现有数据。

# HISTORY

mkreiserfs 是 **ReiserFS** 工具的一部分，ReiserFS 是由 Hans Reiser 创建的一款日志文件系统。

# INSTALL

```apt: sudo apt install reiserfsprogs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mkfs](/man/mkfs)(8)
