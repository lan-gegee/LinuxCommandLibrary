# TAGLINE

以树状结构可视化软件包依赖关系

# TLDR

打印软件包的**依赖树**

```pactree [package]```

打印**反向**依赖（哪些软件包依赖于它）

```pactree -r [package]```

每行列出一个依赖并跳过重复项

```pactree -u [package]```

以彩色显示并包含**可选**依赖

```pactree -co [package]```

限制树的**深度**

```pactree -d [depth] [package]```

显示**帮助**

```pactree```

# SYNOPSIS

**pactree** [**-c**|**--color**] [**-d** _depth_] [**-o**|**--optional**] [**-r**|**--reverse**] [**-u**|**--unique**] _package_

# PARAMETERS

**-c, --color**
> 为输出着色以提高可读性

**-d, --depth _num_**
> 限制递归深度

**-o, --optional**
> 在树中包含可选依赖

**-r, --reverse**
> 显示反向依赖（依赖目标软件包的软件包）

**-s, --sync**
> 查询同步数据库而不是本地数据库

**-u, --unique**
> 每个依赖只列出一次，一行一个

**--config _file_**
> 使用替代的 pacman 配置

# DESCRIPTION

**pactree** 以树状结构可视化软件包依赖关系。它查询 pacman 的数据库，显示给定软件包依赖哪些软件包；使用反向选项时，则显示哪些软件包依赖于它。

该工具有助于理解软件包之间的关系、识别孤立软件包，以及规划软件包移除操作以避免破坏依赖关系。

# CAVEATS

默认只显示已安装软件包的依赖。使用 -s 标志可查询同步数据库。庞大的依赖树会产生大量输出。除非指定 -o，否则可选依赖不会显示。

# HISTORY

**pactree** 最初是一个独立脚本，后来成为官方 **pacman-contrib** 软件包的一部分。它以一种易于阅读的格式提供 pacman 标准查询选项所不具备的可视化依赖信息。

# SEE ALSO

[pacman](/man/pacman)(8), [pactrans](/man/pactrans)(1), [pkgfile](/man/pkgfile)(1)
