# TAGLINE

为文献数据库创建倒排索引

# TLDR

**构建文献索引**

```indxbib [database.bib]```

**为多个文件建立索引**

```indxbib [file1.bib] [file2.bib]```

**指定输出索引基名**

```indxbib -o [index] [database.bib]```

**设置常用词文件**

```indxbib -c [common.txt] [database.bib]```

# SYNOPSIS

**indxbib** [_options_] _file_...

# PARAMETERS

**-o** _NAME_
> 输出索引的基名。

**-c** _FILE_
> 要忽略的常用词文件。

**-h** _N_
> 建立索引的最小词长。

**-i** _STRING_
> 索引键中要忽略的字符。

**-l** _N_
> 每条记录的最大键数。

**--help**
> 显示帮助信息。

# DESCRIPTION

**indxbib** 为文献数据库创建倒排索引。这些索引可供 lkbib 和 refer 进行快速查找。

该工具处理 refer 格式的文献文件。生成的索引文件扩展名为 .ia、.ib、.ic。

# CAVEATS

属于 groff 的一部分，只能处理 refer 格式的文件。索引文件为二进制格式。

# HISTORY

indxbib 是 **groff** 文档排版系统的一部分，源自传统的 Unix refer 工具。

# INSTALL

```apt: sudo apt install groff```

```dnf: sudo dnf install groff```

```pacman: sudo pacman -S groff```

```apk: sudo apk add groff```

```zypper: sudo zypper install groff```

```brew: brew install groff```

```nix: nix profile install nixpkgs#groff```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[refer](/man/refer)(1), [lkbib](/man/lkbib)(1), [lookbib](/man/lookbib)(1), [groff](/man/groff)(1)
