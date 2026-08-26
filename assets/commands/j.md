# TAGLINE

用于快速目录导航的 autojump shell 函数

# TLDR

**跳转到目录**

```j [pattern]```

**跳转到子目录**

```jc [pattern]```

**在文件管理器中打开目录**

```jo [pattern]```

**显示匹配的目录**

```j -s [pattern]```

**将目录加入数据库**

```j -a [/path/to/dir]```

# SYNOPSIS

**j** [_options_] [_pattern_]

# PARAMETERS

_PATTERN_
> 要匹配的目录名模式。

**-s**
> 显示匹配的目录。

**-a** _PATH_
> 将路径添加到数据库。

**-i**
> 不区分大小写匹配。

**--help**
> 显示帮助信息。

# DESCRIPTION

**j** 是用于快速目录导航的 autojump shell 函数。它从你的 cd 习惯中学习，跳转到经常访问的目录。

该工具维护一个带权重的目录数据库。部分名称会与这个数据库进行匹配，实现快速导航。

# CAVEATS

是 autojump 的别名。需要 shell 集成。数据库随时间逐步积累。

# HISTORY

j 是 **autojump** 的默认别名，由 **William Ting** 创建，用于加快 shell 中的目录导航。

# INSTALL

```nix: nix profile install nixpkgs#j```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[autojump](/man/autojump)(1), [z](/man/z)(1), [cd](/man/cd)(1), [fasd](/man/fasd)(1)
