# TAGLINE

以比例指标报告内存使用情况

# TLDR

**显示**当前用户进程的内存使用情况

```smem```

**显示**每个用户的内存使用情况

```smem --users```

按用户名**过滤**

```smem --userfilter [username]```

**显示**系统级内存信息

```smem --system```

按 PSS（比例集大小）**排序**

```smem --sort pss```

以**百分比**显示

```smem --percent```

# SYNOPSIS

**smem** [_options_]

# PARAMETERS

**--users**
> 显示每个用户的内存使用情况

**--userfilter _user_**
> 按用户名过滤

**--system**
> 显示系统级内存信息

**-c, --columns _columns_**
> 指定输出列

**-s, --sort _column_**
> 按指定列排序

**-r, --reverse**
> 反转排序顺序

**-k, --kilounits**
> 以 KB 为单位显示大小

**-m, --megaunits**
> 以 MB 为单位显示大小

**-p, --percent**
> 显示百分比

**-t, --totals**
> 显示总计

# DESCRIPTION

**smem** 报告内存使用情况，重点在于比例集大小（PSS），对于有共享内存的系统来说，这是比 RSS 更有意义的指标。PSS 会将共享内存按比例分摊到共享它的各个进程上。

该工具通过统计共享库和内存映射文件，提供准确的内存使用分析，因此特别适合用来了解每个进程的实际内存消耗。

# CAVEATS

需要对 **/proc/[pid]/smaps** 的读取权限（查看所有进程通常需要 root）。在进程很多的系统上 PSS 计算可能较慢。内核必须启用 CONFIG_PROC_PAGE_MONITOR。

# INSTALL

```dnf: sudo dnf install cfitsio```

```pacman: sudo pacman -S cfitsio```

```apk: sudo apk add cfitsio```

```zypper: sudo zypper install cfitsio```

```brew: brew install cfitsio```

```nix: nix profile install nixpkgs#cfitsio```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ps](/man/ps)(1), [top](/man/top)(1), [free](/man/free)(1), [pmap](/man/pmap)(1)
