# TAGLINE

用硬链接整合重复文件

# TLDR

对目录中的重复文件建立硬链接（先进行 dry-run）

```hardlink --dry-run /path/to/directory```

在一个或多个目录中对重复文件建立硬链接

```hardlink /path/to/dir1 /path/to/dir2```

建立硬链接并输出详细信息

```hardlink --verbose /path/to/directory```

仅考虑大于最小大小的文件

```hardlink --minimum-size 1M /path/to/directory```

# SYNOPSIS

**hardlink** [_options_] _directory_...

# PARAMETERS

**-n**, **--dry-run**  
> 不实际链接文件，只打印将会执行的操作

**-v**, **--verbose**  
> 打印更多正在执行的操作的信息

**-s**, **--minimum-size** _size_  
> 只对大于 _size_ 的文件建立硬链接（支持 K、M、G 后缀）

**-x**, **--exclude** _pattern_  
> 跳过匹配给定 glob 模式的文件（可重复）

**-i**, **--include** _pattern_  
> 只考虑匹配给定 glob 模式的文件

**-f**, **--force**  
> 即使跨越不同文件系统也强制链接（危险）

# DESCRIPTION

**hardlink** 在给定目录中查找内容相同的文件，并用指向剩余那份文件的硬链接替换其余副本。当相同内容存在于多处时（常见于备份、软件包缓存、构建产物等），这样可以节省磁盘空间。

该工具在链接之前会比较文件内容（而不只是名称或大小）。默认行为是安全的：它不会跨越文件系统边界，也会拒绝链接不完全相同的文件。

硬链接是指向同一 inode 的目录条目。删除其中一个名称并不影响其他名称；只有当最后一个链接被删除时数据才会被移除。因此 hardlink 特别适合对大型静态数据集做去重。

# CAVEATS

- 硬链接只能在同一文件系统内创建。
- 剩余的那份副本会保留原文件的权限和所有权。
- 对活动中的构建目录或数据库目录运行 hardlink 时，如果扫描期间文件被修改，可能出现意外结果。
- 一些备份工具和版本控制系统没有考虑硬链接的存在，可能表现异常。

# INSTALL

```apt: sudo apt install util-linux```

```dnf: sudo dnf install util-linux```

```pacman: sudo pacman -S util-linux```

```apk: sudo apk add util-linux-misc```

```zypper: sudo zypper install util-linux```

```brew: brew install util-linux```

```nix: nix profile install nixpkgs#util-linux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cp](/man/cp)(1), [ln](/man/ln)(1), [find](/man/find)(1), [fdupes](/man/fdupes)(1), [rdfind](/man/rdfind)(1)
