# TAGLINE

显示 man page 的简要描述

# TLDR

显示 man page 中的**描述**

```whatis [command]```

不在行尾**截断描述**

```whatis -l [command]```

显示匹配**通配符**的命令描述

```whatis -w net*```

用**正则表达式**搜索 man page 描述

```whatis -r 'wish[0-9]\.[0-9]'```

以**指定语言**显示描述

```whatis -L en [command]```

# SYNOPSIS

**whatis** [**-dlv**] [**-r** | **-w**] [**-s** _list_] [**-m** _system_] [**-M** _path_] [**-L** _locale_] _name_...

# PARAMETERS

**-d**, **--debug**
> 启用调试模式

**-l**, **--long**
> 不将输出裁剪到终端宽度

**-r**, **--regex**
> 将 name 解释为正则表达式

**-w**, **--wildcard**
> 将 name 解释为 shell 通配符模式

**-s** _list_, **--sections=**_list_
> 只搜索指定的手册章节

**-m** _system_, **--systems=**_system_
> 搜索其他系统的 man page

**-M** _path_, **--manpath=**_path_
> 设置手册页搜索路径

**-L** _locale_, **--locale=**_locale_
> 设置搜索使用的 locale

**-v**, **--verbose**
> 打印详细的警告消息

# DESCRIPTION

**whatis** 搜索手册页名称，并显示匹配的 man page NAME 区中的简要描述。它查询 whatis 数据库——一个由 **mandb** 构建的手册页描述缓存。

该命令适合快速了解某个命令的用途而无需阅读完整手册页。可以一次查询多个命令，且支持模式匹配以搜索一组相关命令。

# CAVEATS

需要已构建的 whatis 数据库（通常由 mandb 自动完成）。数据库过期时结果可能不完整。必要时使用 **mandb** 重建数据库。

# HISTORY

源自 **BSD Unix**，是 man page 系统的一部分。引入 whatis 数据库是为了加快查找速度，避免扫描全部 man page。在现代系统上由 **mandb** 维护该数据库，取代了较旧的 **makewhatis** 实现。

# INSTALL

```apt: sudo apt install man-db```

```dnf: sudo dnf install man-db```

```pacman: sudo pacman -S man-db```

```apk: sudo apk add mandoc-apropos```

```brew: brew install man-db```

```nix: nix profile install nixpkgs#man-db```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[man](/man/man)(1), [apropos](/man/apropos)(1), [whereis](/man/whereis)(1), [mandb](/man/mandb)(8)
