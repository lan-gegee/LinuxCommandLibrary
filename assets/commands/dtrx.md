# TAGLINE

智能的归档解压工具

# TLDR

**将归档解压**到专属目录

```dtrx [archive.tar.gz]```

**解压多个归档**

```dtrx [*.tar.gz]```

**列出归档内容**而不解压

```dtrx -l [archive.tar.gz]```

**解压到当前目录**而不是专属目录

```dtrx -f [archive.tar.gz]```

**递归解压嵌套的归档**

```dtrx -r [archive.tar.gz]```

**覆盖**已存在的目标目录，而不是另选名称

```dtrx -o [archive.tar.gz]```

**提取 .deb 或 .gem 的元数据**

```dtrx -m [package.deb]```

**从不询问**，采用保守的默认行为

```dtrx -n [archive.tar.gz]```

# SYNOPSIS

**dtrx** [_options_] _archive_...

# PARAMETERS

_ARCHIVE_
> 要解压的归档文件。

**-r**, **--recursive**
> 查看归档内部是否还有其他归档，并将其一并解压。

**-f**, **--flat**
> 将所有内容解压到**当前**目录，而不是专属目录。

**-o**, **--overwrite**
> 即使默认目录名已存在也直接使用并覆盖它，而不是另选名称。这**不是**输出目录选项。

**-l**, **-t**, **--list**, **--table**
> 列出内容而不解压。

**-m**, **--metadata**
> 提取 `.deb` 或 `.gem` 软件包的*元数据*而非其内容。

**--one**, **--one-entry** _MODE_
> 如何处理只包含单个文件或目录的归档：**inside**（将其包进一个以归档命名的目录；默认值）、**rename**（重命名以匹配归档名）或 **here**（原样解压到当前目录）。

**-n**, **--noninteractive**
> 从不询问；改用保守的默认行为。

**-q**, **--quiet**
> 抑制警告。使用两次可完全静默。

**-v**, **--verbose**
> 列出已解压的文件。使用两次可输出调试信息。

**--help** / **--version**
> 显示帮助，或版本与版权信息。

# DESCRIPTION

**dtrx** 是 "Do The Right Extraction"（正确地解压）的缩写，其目标是替你免去解压归档时需要做出的所有决定。

它根据文件*内容*而非文件名来识别格式，因此无需告知格式即可处理各种压缩方式的 tar、zip、rar、7z、cpio、deb、rpm、gem 等，并自动调用合适的底层工具。

它最有价值的行为是防止 **tar 炸弹**（tarbomb）：这类归档的成员没有包在顶层目录里，解压后会把文件散落得到处都是。dtrx 总是解压到单个以归档命名的目录中；如果归档本身已有一个合理的顶层目录，就直接使用而不重复嵌套。当目录名发生冲突时，dtrx 会另选新名，而不是覆盖已有内容。

它还会规范化权限：解压时会把不可读的目录或全局可写的文件修正过来。

# CAVEATS

**-o 不接受输出目录参数。** 它的含义是*覆盖*，传入 `dtrx -o mydir archive.tar.gz` 会尝试解压两个东西：该归档和一个名为 `mydir` 的文件。要解压到指定位置，请先切换目录。同样，**-m** 不保留所有权或权限；它提取的是 `.deb` 或 `.gem` 的元数据部分。

dtrx 是一个前端，自身不实现任何格式，因此只能处理系统上已安装的工具所支持的格式：如果系统上没有 `unrar` 或 `p7zip`，相应的归档会直接失败。

原项目已多年无人维护，其 Python 2 代码库迫使各发行版要么放弃它、要么自行维护 Python 3 移植版，因此可用版本因发行版而异。**atool** 覆盖的功能范围与之相近且仍在维护中。

# HISTORY

dtrx 由 **Brett Smith** 于 **2006 年**编写。那个年代 tarbomb 是真实的威胁，而且每种归档格式都需要不同的咒语——这里用 `tar xzf`，那里用 `tar xjf`，有的用 `unzip`，有的用 `unrar x`。"计算机显然可以自己搞定这些"这一前提足够有说服力，使它成为各发行版中的常客，哪怕后来 `tar` 增加了自动解压检测、让最初的问题消解了一半。

# INSTALL

```apk: sudo apk add dtrx```

```zypper: sudo zypper install dtrx```

```brew: brew install dtrx```

```nix: nix profile install nixpkgs#dtrx```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tar](/man/tar)(1), [unzip](/man/unzip)(1), [7z](/man/7z)(1), [atool](/man/atool)(1), [unar](/man/unar)(1)

# RESOURCES

```[Source code](https://github.com/dtrx-py/dtrx)```

<!-- verified: 2026-07-14 -->
