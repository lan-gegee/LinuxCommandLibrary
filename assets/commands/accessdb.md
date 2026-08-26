# TAGLINE

以可读形式转储 man-db 数据库

# TLDR

**转储** man-db 数据库内容

```accessdb```

转储**指定的**数据库文件

```accessdb [/var/cache/man/index.db]```

显示**调试**信息

```accessdb -d [database_path]```

# SYNOPSIS

**accessdb** [_-d_] [_database_]

# DESCRIPTION

**accessdb** 是一个实用工具，它把 man-db 数据库的内容以人类可读的格式转储到标准输出。数据库包含手册页的索引信息，包括它们的位置、名称、描述和时间戳。

该工具主要用于调试 man-db 问题、验证手册页是否被正确索引，或者了解手册页缓存系统的工作原理。

# PARAMETERS

**-d**, **--debug**
> 打印调试信息

**database**
> 数据库文件的路径（默认为系统 man-db 位置）

# CAVEATS

数据库格式为 man-db 特有，可能随版本变化。该工具主要用于调试；普通用户很少需要直接与数据库交互。必须先用 **mandb** 构建数据库才能访问。

# HISTORY

**accessdb** 属于 **man-db** 软件包，该软件包最初由 John W. Eaton 编写，后来由 Colin Watson 维护。man-db 项目始于 **1994** 年，用以取代旧的 man 软件包，引入了数据库缓存以加快手册页查找速度。

# INSTALL

```apt: sudo apt install man-db```

```dnf: sudo dnf install man-db```

```pacman: sudo pacman -S man-db```

```apk: sudo apk add man-db```

```brew: brew install man-db```

```nix: nix profile install nixpkgs#man-db```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[man](/man/man)(1), [mandb](/man/mandb)(8), [whatis](/man/whatis)(1), [apropos](/man/apropos)(1)

# RESOURCES

```[Source code](https://gitlab.com/man-db/man-db)```

```[Homepage](https://man-db.gitlab.io/man-db/)```

<!-- verified: 2026-06-10 -->
