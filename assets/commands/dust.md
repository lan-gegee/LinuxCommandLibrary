# TAGLINE

直观的可视化磁盘用量分析器

# TLDR

**显示当前目录的磁盘用量**

```dust```

**带深度限制地显示磁盘用量**

```dust -d [2]```

**显示指定目录的磁盘用量**

```dust [/path/to/directory]```

**以 SI 单位显示大小**（1000 的幂）

```dust -H```

**只显示文件**（不含目录）

```dust -F```

**显示表面大小**而非磁盘用量

```dust -s```

**反转排序顺序**（最小在前）

```dust -r```

**显示磁盘用量**但不带百分比条

```dust -p```

# SYNOPSIS

**dust** [_options_] [_paths_...]

# DESCRIPTION

**dust**（du + rust）是一个现代、直观的磁盘用量分析器，以树状结构展示目录和文件的大小。它提供带有百分比条的可视化呈现，便于快速识别大文件和大目录。

与传统 du 不同，dust 以树状格式显示结果并附带直观的大小指示，自动限制深度以保证输出可读。它默认最大的条目排在最前，还包含一个显示相对大小的百分比列。

该工具用 Rust 编写以追求性能，借助并行处理高效处理大型目录树。

# PARAMETERS

**-d** _n_, **--depth** _n_
> 最大显示深度。

**-n** _num_
> 显示的条目数量。

**-r**, **--reverse**
> 反转排序顺序。

**-s**, **--apparent-size**
> 显示表面大小而非磁盘用量。

**-f**
> 显示文件数量而非大小。

**-H**, **--si**
> 以 SI 单位打印大小（1000 的幂而非 1024）。

**-p**, **--no-percent-bars**
> 隐藏百分比条。

**-c**, **--no-colors**
> 禁用彩色输出。

**-b**, **--no-bars**
> 完全隐藏条形图。

**-D**, **--only-dir**
> 只显示目录，不显示文件。

**-F**, **--only-file**
> 只显示文件，不显示目录。

**-e** _regex_, **--filter** _regex_
> 按正则表达式过滤。

**-v** _regex_, **--invert-filter** _regex_
> 排除匹配正则表达式的条目。

**-X**, **--ignore-directory** _name_
> 忽略指定的目录。

**-x**, **--one-filesystem**
> 不跨出单一文件系统。

**-j**, **--threads** _n_
> 使用的线程数。

**-z** _size_, **--min-size** _size_
> 最小显示大小（如 1M）。

# CAVEATS

由于块大小与表面大小的差异，结果可能与 du 不同。非常大的目录树扫描起来可能耗时较长。要获得最佳可视化效果，需要支持颜色的终端。符号链接默认不被跟随。

# HISTORY

**dust** 由 **Andy Boot** 于 **2018 年**创建，是基于 Rust 的 du 替代品，可视化效果更好。它的设计初衷是解决人们对 du 输出格式的常见抱怨以及解读结果的困难。作为用 Rust 重写传统 Unix 工具浪潮的一部分，该项目广受欢迎。

# INSTALL

```apt: sudo apt install du-dust```

```dnf: sudo dnf install du-dust```

```pacman: sudo pacman -S dust```

```apk: sudo apk add dust```

```zypper: sudo zypper install dust```

```brew: brew install dust```

```nix: nix profile install nixpkgs#dust```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[du](/man/du)(1), [ncdu](/man/ncdu)(1), [duf](/man/duf)(1), [df](/man/df)(1), [tree](/man/tree)(1)
