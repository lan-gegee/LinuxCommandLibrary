# TAGLINE

复制文件和目录

# TLDR

**将文件复制到目标位置**

```cp [path/to/source.txt] [path/to/destination.txt]```

**递归复制目录**

```cp -r [path/to/source_dir] [path/to/dest_dir]```

**覆盖前交互式确认**

```cp -i [path/to/source] [path/to/dest]```

**保留权限、所有者和时间戳**

```cp -p [path/to/source] [path/to/dest]```

**归档复制（保留全部属性，递归）**

```cp -a [path/to/source_dir] [path/to/dest_dir]```

**将多个文件复制到一个目录**

```cp [file1] [file2] [file3] [path/to/dest_dir/]```

# SYNOPSIS

**cp** [_options_] [**-T**] _source_ _dest_
**cp** [_options_] _source..._ _directory_
**cp** [_options_] **-t** _directory_ _source..._

# DESCRIPTION

**cp** 用于复制文件和目录。它可以复制单个文件、把多个文件复制到目录中，或复制整个目录树。它会根据所用选项保留或修改文件属性。

该命令是 Unix 系统上文件管理的基础工具。

# PARAMETERS

**-r**, **-R**, **--recursive**
> 递归复制目录

**-i**, **--interactive**
> 覆盖前提示确认

**-f**, **--force**
> 强制覆盖

**-n**, **--no-clobber**
> 不覆盖已有文件

**-p**, **--preserve**
> 保留权限、所有者和时间戳

**-a**, **--archive**
> 归档模式（等同于 -dR --preserve=all）

**-u**, **--update**
> 仅当源文件较新时才复制

**-v**, **--verbose**
> 详细输出

**-l**, **--link**
> 创建硬链接而非复制

**-s**, **--symbolic-link**
> 创建符号链接而非复制

**-t**, **--target-directory** _DIR_
> 将所有源文件复制到 DIR 中

**-T**, **--no-target-directory**
> 将目标视为普通文件

**--backup**[=_CONTROL_]
> 备份已有文件

**-d**
> 等同于 --no-dereference --preserve=links

**--preserve**=_ATTR_LIST_
> 保留指定属性（mode,ownership,timestamps,context,links,xattr,all）

# WORKFLOW

```bash
# Copy file
cp file.txt copy.txt

# Copy to directory
cp file.txt /tmp/

# Copy multiple files
cp file1.txt file2.txt file3.txt /destination/

# Copy directory
cp -r source_dir/ destination_dir/

# Preserve attributes
cp -p original.txt copy.txt

# Archive copy (preserve everything)
cp -a directory/ backup/

# Interactive (ask before overwrite)
cp -i file.txt existing.txt

# Backup existing file
cp --backup file.txt existing.txt
```

# COPYING DIRECTORIES

```bash
# Copy directory and contents
cp -r project/ project_backup/

# Archive mode (preserve all attributes)
cp -a /data/ /backup/data/

# Update only newer files
cp -ru source/ destination/
```

# CAVEATS

不带 -r 时无法复制目录。默认会直接覆盖（为了安全请使用 -i）。同时给出 -n 和 -i 时，以最后出现的为准。-p 不一定保留所有属性（要全部保留请用 --preserve=all）。大型递归复制可能很慢。不指定 --sparse=always 时，稀疏文件可能无法高效处理。符号链接是作为链接复制还是解引用取决于所用选项。

# HISTORY

自 **1970 年代**初以来，**cp** 就一直是 Unix 的核心命令，属于最初的 Unix 工具集。

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

[mv](/man/mv)(1), [rm](/man/rm)(1), [ln](/man/ln)(1), [rsync](/man/rsync)(1), [install](/man/install)(1), [dd](/man/dd)(1)
