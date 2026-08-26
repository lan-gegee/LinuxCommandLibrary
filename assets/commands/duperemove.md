# TAGLINE

文件系统 extent 去重工具

# TLDR

搜索**重复的 extent**

```duperemove -r [path/to/directory]```

在 Btrfs 或 XFS 上执行**去重**

```duperemove -r -d [path/to/directory]```

使用**哈希文件**持久化结果

```duperemove -r -d --hashfile=[path/to/hashfile] [path/to/directory]```

限制**线程数**

```duperemove -r -d --hashfile=[path/to/hashfile] --io-threads=[n] --cpu-threads=[n] [path/to/directory]```

# SYNOPSIS

**duperemove** [_options_] _paths_...

# DESCRIPTION

**duperemove** 查找重复的文件系统 extent，并可选地将它们调度去重。在 Btrfs 和 XFS 这类文件系统上，相同的数据块可以在多个文件之间共享，从而节省磁盘空间。

extent 是为文件分配的一段连续存储区域。

# PARAMETERS

**-r**
> 递归处理目录

**-d**
> 去重（将重复内容调度去重）

**--hashfile** _file_
> 将哈希存入文件以便复用

**--io-threads** _n_
> I/O 线程数

**--cpu-threads** _n_
> 用于哈希比较的 CPU 线程数

**-h**
> 以人类可读格式打印大小

**-v**
> 详细输出

**--dedupe-options=**_OPTIONS_
> 逗号分隔的去重选项（如 partial、same）

**-b** _SIZE_
> 计算哈希的块大小（默认：128K）

# CAVEATS

只适用于支持 extent 级去重的文件系统（Btrfs、XFS）。去重由内核通过 `FIDEDUPERANGE` ioctl 完成。强烈建议在大数据集上使用哈希文件，因为它能减少内存占用并支持跨运行增量扫描。不加 `-d` 时，工具只报告重复而不去重。只读文件也可以被去重，因为去重在文件系统层面操作。

# INSTALL

```apt: sudo apt install duperemove```

```dnf: sudo dnf install duperemove```

```pacman: sudo pacman -S duperemove```

```apk: sudo apk add duperemove```

```zypper: sudo zypper install duperemove```

```nix: nix profile install nixpkgs#duperemove```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[btrfs](/man/btrfs)(8), [fdupes](/man/fdupes)(1), [rmlint](/man/rmlint)(1)
