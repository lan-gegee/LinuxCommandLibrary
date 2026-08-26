# TAGLINE

交换两个文件路径的工具

# TLDR

**交换**两个文件的路径

```exch [path/to/file1] [path/to/file2]```

# SYNOPSIS

**exch** _file1_ _file2_

# PARAMETERS

_file1_
> 要交换的第一个文件

_file2_
> 要交换的第二个文件

# DESCRIPTION

**exch** 以原子方式交换两个路径。操作完成后，file1 指向原先位于 file2 路径的内容，反之亦然。它是 **renameat2**(2) 系统调用中 **RENAME_EXCHANGE** 标志的一个轻量封装。

属于 **util-linux** 软件包。适用于快速交换配置文件、符号链接或备份，无需借助中间临时名称。

# CAVEATS

两个文件都必须存在。与三步式的 mv 操作不同，这种交换是原子的（不存在任何一个名称缺失的时间窗口）。它依赖支持 RENAME_EXCHANGE 的 **renameat2**(2)，因此仅限 Linux，且两个路径必须位于同一文件系统上。该命令在 util-linux 2.41 中加入。

# INSTALL

```apt: sudo apt install util-linux-extra```

```apk: sudo apk add util-linux-misc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mv](/man/mv)(1), [cp](/man/cp)(1), [rename](/man/rename)(1)

# RESOURCES

```[Source code](https://github.com/util-linux/util-linux)```

```[Documentation](https://man7.org/linux/man-pages/man1/exch.1.html)```

<!-- verified: 2026-07-15 -->
