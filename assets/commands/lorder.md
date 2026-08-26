# TAGLINE

列出目标文件之间的依赖关系

# TLDR

**查找库依赖**

```lorder [*.o]```

**生成库排序**

```lorder [*.o] | tsort```

**处理指定文件**

```lorder [file1.o] [file2.o] [file3.o]```

**通过管道传给归档创建命令**

```ar cr libfoo.a $(lorder [*.o] | tsort)```

# SYNOPSIS

**lorder** _files_

# PARAMETERS

_FILES_
> 要分析的目标文件。

# DESCRIPTION

**lorder** 列出目标文件之间的依赖关系，输出成对的条目，标明哪些文件依赖哪些文件。

其输出通常通过管道传给 tsort，以确定静态库中目标文件的正确顺序。

# CAVEATS

BSD 工具，并非所有系统都可用。通常与 tsort 和 ar 配合使用。

# HISTORY

lorder 是一个传统的 **BSD** 工具，用于确定静态库中目标文件的排列顺序。

# SEE ALSO

[tsort](/man/tsort)(1), [ar](/man/ar)(1), [nm](/man/nm)(1), [ld](/man/ld)(1)
