# TAGLINE

彩色的磁盘用量树状可视化工具

# TLDR

显示当前目录的**图形化树状图**

```dutree```

显示**指定目录**

```dutree [path/to/directory]```

**聚合**小于阈值的条目

```dutree -a [10]M```

显示子目录至**指定深度**

```dutree -d [2]```

**跳过目录**以快速概览

```dutree -f```

**排除隐藏**文件

```dutree -H```

**排除**匹配模式的文件

```dutree -x "*.log"```

仅显示总大小的**汇总**

```dutree -s```

# SYNOPSIS

**dutree** [_options_] [_path_]

# DESCRIPTION

**dutree** 是一个磁盘用量分析器，以彩色层级树的形式呈现文件系统信息。与传统 du 的输出不同，dutree 提供直观的可视化呈现，一眼就能找出占用空间的目录。

该工具用颜色编码和树枝结构展示目录与其内容的关系，文件大小醒目地显示出来。它可以把低于可配置阈值的细小条目聚合起来，让输出保持简洁、聚焦于最大的空间消耗者。

dutree 用 Rust 编写以追求性能，能高效处理大型目录树。可用 **-d** 限制深度，避免输出过多。它特别适合快速的空间审查和寻找适合清理的目录。

# PARAMETERS

**-a**, **--aggr** _size_
> 聚合小于指定大小的条目（如 1K、10M、1G）。

**-d**, **--depth** _n_
> 最大显示的目录深度。

**-f**, **--files-only**
> 跳过目录，只显示文件。

**-H**, **--no-hidden**
> 排除隐藏文件和目录。

**-x**, **--exclude** _pattern_
> 排除匹配 glob 模式的文件。

**-s**, **--summary**
> 只显示总大小。

**-b**, **--bytes**
> 打印原始字节数而非人类可读格式。

# CAVEATS

要获得最佳可视化效果，需要支持颜色的终端。大型目录扫描可能耗时。

# INSTALL

```brew: brew install dutree```

```nix: nix profile install nixpkgs#dutree```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[du](/man/du)(1), [dust](/man/dust)(1), [ncdu](/man/ncdu)(1), [tree](/man/tree)(1)
