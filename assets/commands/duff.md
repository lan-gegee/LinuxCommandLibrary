# TAGLINE

重复文件查找器

# TLDR

**在目录中查找重复文件**

```duff [directory]```

**递归查找重复文件**

```duff -r [directory]```

**比较来自多个目录的文件**

```duff -r [dir1] [dir2] [dir3]```

**逐字节比较**，而不只是比较摘要值

```duff -rt [directory]```

**排除空文件**（它们彼此全都相同）

```duff -rz [directory]```

递归搜索时**包含隐藏文件**

```duff -ra [directory]```

**只输出多余的副本**，便于管道接入删除操作

```duff -re [directory]```

**使用更强的摘要算法**

```duff -r -d [sha256] [directory]```

# SYNOPSIS

**duff** [_options_] [_file_...]

# PARAMETERS

**-r**
> 递归搜索给定目录。不加该选项时，duff 只查看点名给出的文件。

**-a**
> 递归搜索时包含隐藏文件和目录。

**-e**
> 多余模式（excess）：每组重复簇中除一个文件外全部输出，并省略组头。这是接入 `xargs rm` 管道时使用的形式。

**-t**
> 彻底模式（thorough）：大小相同时逐字节比较，而不是信赖摘要值。

**-d** _function_
> 摘要算法：`sha1`（默认）、`sha256`、`sha384` 或 `sha512`。

**-z**
> 不把空文件报告为彼此的重复。

**-p**
> 物理模式：将指向同一文件的硬链接视为不同文件，而不是重复。

**-H** / **-L** / **-P**
> 只跟随命令行中给出的符号链接；跟随所有符号链接；或不跟随任何符号链接。默认为 **-P**，三者互相覆盖。

**-l** _limit_
> 超过该最小文件大小时，duff 改为抽样而非读取整个文件。默认为零。这是一个**大小阈值**，不是结果数量的上限。

**-f** _format_
> 自定义重复簇头部，可用转义符如 `%n`（文件数）、`%s`（大小）、`%d`（摘要）、`%i`（簇序号）。

**-q**
> 安静模式：抑制警告和错误消息。

**-0**
> 从标准输入读取文件名时期望以 null 结尾，而不是以换行分隔。

# DESCRIPTION

**duff**（Duplicate File Finder）通过比较文件大小和内容来识别重复文件。它将内容完全相同的文件分组，因此适合查找并清除冗余文件以释放磁盘空间。

该工具先按大小分组，再用校验和比较内容，必要时进行逐字节比较。输出以空行分隔各组重复文件。

# OUTPUT FORMAT

```
file1.txt
file2.txt

another1.jpg
another2.jpg
another3.jpg
```

每一簇内的文件内容完全相同。

# CAVEATS

**duff 默认不递归。** `duff mydir` 只检查这个目录条目本身，什么也找不到；你几乎总是需要 **-r**。递归模式下隐藏文件同样会被跳过，除非给出 **-a**，所以一次"没有发现重复"的报告可能根本没找过那些地方。

不加 **-t** 时，是否重复由**摘要值**决定，而不是比较字节本身。SHA-1 碰撞不是你会偶然遇到的事情，但这个保证是概率性的而非绝对的，**-t** 以速度为代价把它升级为确定。`-l` 让保证更弱：超过指定大小的文件 duff 改用抽样而非完整哈希，速度快但偶尔出错。

duff 从不删除任何东西，这正是它的优点。预期的用法是通过管道接 **-e**，它对每个重复簇输出除一个之外的所有副本：

```duff -re [directory] | xargs -d '\n' rm --```

执行前请先读一遍输出。空文件彼此全都相同，不加 **-z** 时会被一并扫走；默认情况下指向同一 inode 的硬链接也会被报告为重复，尽管删掉其中一个释放不了任何空间：**-p** 可以避免这一点。

# HISTORY

duff 由 **Camilla Löwy** 编写，是一个小巧快速的 Unix 重复文件查找工具。它的方法是经典套路：先按大小分组，再按摘要分组，只有明确要求时才回退到逐字节比较，这意味着绝大多数候选文件从未被完整读取。该项目早已归于沉寂，如今大多数人改用 **jdupes**——fdupes 的一个维护活跃且快得多的后继者。

# INSTALL

```apt: sudo apt install duff```

```dnf: sudo dnf install duff```

```brew: brew install duff```

```nix: nix profile install nixpkgs#duff```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fdupes](/man/fdupes)(1), [rdfind](/man/rdfind)(1), [jdupes](/man/jdupes)(1), [rmlint](/man/rmlint)(1), [find](/man/find)(1)

# RESOURCES

```[Source code](https://github.com/elmindreda/duff)```

<!-- verified: 2026-07-14 -->
