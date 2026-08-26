# TAGLINE

查找并删除重复文件

# TLDR

在目录中**查找重复文件**

```fdupes [/path/to/directory]```

**递归查找重复文件**

```fdupes -r [/path/to/directory]```

**交互式删除重复文件**

```fdupes -d [/path/to/directory]```

**删除重复文件**并自动保留第一个文件

```fdupes -dN [/path/to/directory]```

**显示重复文件的大小**

```fdupes -S [/path/to/directory]```

**汇总**重复文件统计信息

```fdupes -m [/path/to/directory]```

**比较多个目录**

```fdupes [/path/dir1] [/path/dir2]```

只在指定的目录之间**查找重复文件**

```fdupes -r [/path/original] [/path/copy]```

# SYNOPSIS

**fdupes** [_options_] _directory_...

# DESCRIPTION

**fdupes** 通过比较文件大小和 MD5 签名来识别指定目录中的重复文件，随后再进行逐字节比较加以确认。它将重复文件分组，便于审查或自动删除。

该工具先比较文件大小，然后计算部分和完整的 MD5 哈希，最后执行逐字节比较以确保准确性。这种多阶段方法兼顾了速度和准确性。

fdupes 可跨多个目录操作，找出目录内部及目录之间的重复文件。适用于清理备份副本、照片库以及回收磁盘空间。

# PARAMETERS

**-r**, **--recurse**
> 递归搜索目录。

**-R**, **--recurse:**
> 仅对其后的目录递归。

**-d**, **--delete**
> 提示选择要删除的文件。

**-N**, **--noprompt**
> 与 -d 配合，不经提示直接删除。

**-S**, **--size**
> 显示重复文件的大小。

**-m**, **--summarize**
> 显示汇总统计。

**-1**, **--sameline**
> 将每组列在单行上。

**-n**, **--noempty**
> 排除空文件。

**-H**, **--hardlinks**
> 将硬链接视为重复文件。

**-f**, **--omitfirst**
> 省略每组中的第一个文件。

**-q**, **--quiet**
> 安静模式（用于 -d 操作）。

**-i**, **--reverse**
> 反转顺序（删除第一个文件）。

**-L**, **--linkhard**
> 用硬链接替换重复文件。

# CAVEATS

对大文件的逐字节比较可能较慢。删除操作不可逆。硬链接模式会改变文件之间的关系。跨不同文件系统无法进行硬链接比较。

# HISTORY

**fdupes** 由 **Adrian Lopez** 于 **1999 年**创建，是一款用于查找重复文件的工具。多年来它一直得到维护和增强，成为类 Unix 系统上检测重复文件的标准工具。该工具影响了众多类似的实用程序，至今仍被广泛用于磁盘清理工作。

# INSTALL

```apt: sudo apt install fdupes```

```dnf: sudo dnf install fdupes```

```pacman: sudo pacman -S fdupes```

```apk: sudo apk add fdupes```

```zypper: sudo zypper install fdupes```

```brew: brew install fdupes```

```nix: nix profile install nixpkgs#fdupes```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rmlint](/man/rmlint)(1), [find](/man/find)(1), [md5sum](/man/md5sum)(1), [diff](/man/diff)(1)

# RESOURCES

```[Source code](https://github.com/adrianlopezroche/fdupes)```

<!-- verified: 2026-07-15 -->
