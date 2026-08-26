# TAGLINE

创建文件并更新时间戳

# TLDR

**创建新的空文件**

```touch [file]```

**创建多个文件**

```touch [file1] [file2] [file3]```

将访问和修改时间**更新**为当前时间

```touch [existing_file]```

**设置指定的修改时间**

```touch -t [[CC]YY]MMDDhhmm[.ss] [file]```

**从另一个文件设置时间**

```touch -r [reference_file] [file]```

**只更改访问时间**

```touch -a [file]```

**只更改修改时间**

```touch -m [file]```

文件不存在时**不创建文件**

```touch -c [file]```

# SYNOPSIS

**touch** [_options_] _file_...

# PARAMETERS

**-a**
> 只更改访问时间

**-m**
> 只更改修改时间

**-c**, **--no-create**
> 文件不存在时不创建

**-d** _string_, **--date**=_string_
> 解析字符串并用其代替当前时间

**-r** _file_, **--reference**=_file_
> 使用参考文件的时间

**-t** _stamp_
> 使用时间戳 [[CC]YY]MMDDhhmm[.ss] 代替当前时间

**-h**, **--no-dereference**
> 作用于符号链接本身而非所引用的文件

**--time**=_WORD_
> 更改指定的时间：_access_、_atime_、_use_ 等同于 **-a**；_modify_、_mtime_ 等同于 **-m**

**-f**
> 被忽略；仅为兼容 BSD 版本的 touch 而保留

# DESCRIPTION

**touch** 更新文件的访问和修改时间戳。如果文件不存在，touch 会创建一个空文件（除非指定了 **-c** 或 **-h**）。

常见用途包括创建空文件、更新时间戳以触发 make 重新构建，以及为测试或归档目的设置特定时间。

时间可以多种格式指定：用 **-t** 指定精确的时间戳，用 **-d** 指定人类可读的字符串（"yesterday"、"2 hours ago"），或用 **-r** 从另一个文件复制时间。

不带 **-a** 或 **-m** 时，访问时间（atime）和修改时间（mtime）都会被更新。当时间戳变化时，变更时间（ctime）始终由内核更新。

# DATE STRING EXAMPLES

```touch -d "2024-01-15 10:30:00" file```
```touch -d "yesterday" file```
```touch -d "2 weeks ago" file```
```touch -d "next monday" file```

# CAVEATS

创建文件需要对该目录有写权限。更新时间戳需要对文件有写权限或为其所有者。

某些文件系统以 **noatime** 或 **relatime** 方式挂载，这会影响访问时间的记录方式。这对 touch 没有影响，但可能影响依赖 atime 的程序。

Touch 无法更改 ctime（inode 变更时间）；当元数据变化时，它总是由内核设置为当前时间。

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

[stat](/man/stat)(1), [date](/man/date)(1), [ls](/man/ls)(1), [mkdir](/man/mkdir)(1), [chmod](/man/chmod)(1)
