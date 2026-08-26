# TAGLINE

文件页缓存检查工具

# TLDR

显示文件的**缓存详情**

```fincore [path/to/file]```

显示**所有**可用的数据列

```fincore --output-all [path/to/file]```

显示**帮助**

```fincore [-h|--help]```

# SYNOPSIS

**fincore** [_options_] _files_

# DESCRIPTION

**fincore** 显示文件当前有多大比例已被内核页缓存保存在内存中，给出已缓存的页数和字节数。

有助于了解内存使用情况与缓存行为。

# PARAMETERS

**-n**, **--noheadings**
> 不打印标题行。

**-b**, **--bytes**
> 以字节为单位打印大小（不使用人类可读的单位）。

**-c**, **--total**
> 打印所有结果的总计值。

**-o**, **--output** _list_
> 指定要输出的列（用 _+list_ 可在默认基础上扩展）。

**--output-all**
> 显示全部可用列。

**-r**, **--raw**
> 以原始格式输出。

**-J**, **--json**
> 使用 JSON 输出格式。

**-R**, **--recursive**
> 递归进入子目录。

**-h**, **--help**
> 显示帮助。

**-V**, **--version**
> 打印版本号。

# CAVEATS

属于 util-linux。显示的是某一时刻缓存状态的快照。缓存内容会随系统活动动态变化。

# INSTALL

```apt: sudo apt install util-linux-extra```

```apk: sudo apk add util-linux-misc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fadvise](/man/fadvise)(1), [vmtouch](/man/vmtouch)(1), [free](/man/free)(1)
