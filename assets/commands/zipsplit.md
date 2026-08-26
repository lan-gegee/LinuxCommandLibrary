# TAGLINE

将 ZIP 归档分割为更小的部分

# TLDR

**分割**归档

```zipsplit [path/to/archive.zip]```

按**大小**限制分割

```zipsplit -n [size] [path/to/archive.zip]```

在每个分卷之间**暂停**

```zipsplit -p -n [size] [path/to/archive.zip]```

输出到**目录**

```zipsplit -b [path/to/output_directory] -n [size] [path/to/archive.zip]```

# SYNOPSIS

**zipsplit** [_OPTIONS_] _ZIPFILE_

# PARAMETERS

**-n** _SIZE_
> 每个分割归档的最大字节数

**-p**
> 在创建每个分卷之间暂停

**-b** _PATH_
> 分割归档的输出目录

**-t**
> 报告将创建多少个文件而不实际创建

**-r** _ROOM_
> 在第一个磁盘上预留额外字节的空间（默认：0）

**-s**
> 即使需要更多 zip 文件也执行顺序分割

**-i**
> 创建索引文件（zipsplit.idx），并将其大小计入第一个 zip 文件

**-h**
> 显示简短帮助信息

**-v**
> 显示版本信息

**-L**
> 显示软件许可证

# DESCRIPTION

**zipsplit** 将 ZIP 归档分割为更小的 ZIP 归档。若未通过 **-n** 指定，默认大小限制为 36000 字节。

输出文件基于原始文件名以数字后缀命名。

# CAVEATS

超过大小限制的单个文件无法跨归档拆分。提取完整的归档内容需要所有分卷。

# INSTALL

```apt: sudo apt install zip```

```dnf: sudo dnf install zip```

```pacman: sudo pacman -S zip```

```apk: sudo apk add zip```

```zypper: sudo zypper install zip```

```brew: brew install zip```

```nix: nix profile install nixpkgs#zip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[zip](/man/zip)(1), [unzip](/man/unzip)(1), [split](/man/split)(1), [zipcloak](/man/zipcloak)(1), [zipnote](/man/zipnote)(1)
