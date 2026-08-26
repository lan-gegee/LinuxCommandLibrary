# TAGLINE

按关键字搜索 man page 描述

# TLDR

**按关键字搜索** man page

```apropos [keyword]```

以**精确匹配**方式搜索

```apropos -e [keyword]```

在**特定章节**中搜索

```apropos -s [1,8] [keyword]```

使用**正则表达式**搜索

```apropos -r "[network.*config]"```

**匹配所有**关键字（AND）

```apropos -a [keyword1] [keyword2]```

# SYNOPSIS

**apropos** [_-e_] [_-r_] [_-s sections_] [_-l_] _keyword_

# DESCRIPTION

**apropos** 在 man page 名称和简短描述中搜索关键字，当你不知道命令的确切名称时，它可以帮助你找到相关的命令。

搜索查询由 mandb 构建的 whatis 数据库。默认情况下，每个关键字都被视为正则表达式。多个关键字之间是 OR 关系；使用 **-a** 可要求全部匹配。

# PARAMETERS

**-e**, **--exact**
> 搜索与关键字完全匹配的结果

**-r**, **--regex**
> 将每个关键字解释为正则表达式。这是默认行为。

**-w**, **--wildcard**
> 将关键字解释为 Shell 通配符模式

**-s** _list_, **--sections** _list_
> 只在指定的手册章节中搜索

**-l**, **--long**
> 不将输出裁剪到终端宽度。

**-a**, **--and**
> 要求所有关键字都匹配

# CAVEATS

搜索结果依赖 whatis 数据库保持最新。如果刚安装了新软件包，请运行 **mandb** 更新。某些 man page 的描述可能写得比较差。

# HISTORY

**apropos** 从 Unix 早期版本起就是系统的一部分，帮助用户发现相关命令。它等价于 **man -k**。

# INSTALL

```apt: sudo apt install man-db```

```dnf: sudo dnf install man-db```

```pacman: sudo pacman -S man-db```

```apk: sudo apk add mandoc-apropos```

```brew: brew install man-db```

```nix: nix profile install nixpkgs#man-db```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[man](/man/man)(1), [whatis](/man/whatis)(1), [mandb](/man/mandb)(8)
