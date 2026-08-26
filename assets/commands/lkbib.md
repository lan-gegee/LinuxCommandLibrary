# TAGLINE

搜索文献目录数据库

# TLDR

**搜索文献数据库**

```lkbib [keyword]```

**搜索特定数据库**

```lkbib -p [database] [keyword]```

**搜索多个关键词**

```lkbib [keyword1] [keyword2]```

**不区分大小写搜索**

```lkbib -i [keyword]```

# SYNOPSIS

**lkbib** [_options_] _keys_

# PARAMETERS

_KEYS_
> 搜索关键词。

**-p** _DATABASE_
> 文献数据库文件。

**-i**
> 不区分大小写搜索。

**-n** _NUM_
> 最大结果数。

**--help**
> 显示帮助信息。

# DESCRIPTION

**lkbib** 搜索文献目录数据库。它在 refer 风格的数据库中查找与关键词匹配的参考文献。

该工具是 groff 的一部分，配合 refer 用于文档中的引文格式化。

# CAVEATS

是 groff 软件包的一部分。使用 refer 数据库格式。主要用于学术场景。

# HISTORY

lkbib 是 **groff** 文本排版系统的组成部分，为 refer 预处理器提供文献检索功能。

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

[refer](/man/refer)(1), [lookbib](/man/lookbib)(1), [groff](/man/groff)(1)
