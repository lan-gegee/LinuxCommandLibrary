# TAGLINE

用于文件搜索的类 SQL 查询语言

# TLDR

**按名称查找文件**

```fselect name from [/path] where name = '[*.txt]'```

**查找大文件**

```fselect name, size from [/path] where size > [1g]```

**按扩展名查找**

```fselect name from [/path] where ext = '[jpg]'```

**查找最近的文件**

```fselect name, modified from [/path] where modified > [yesterday]```

**显示图片尺寸**

```fselect name, width, height from [/path] where ext = '[png]'```

# SYNOPSIS

**fselect** _fields_ **from** _paths_ [**where** _conditions_] [_options_]

# PARAMETERS

_FIELDS_
> 要输出的列：name、size、modified、ext、width 等。

_PATHS_
> 要搜索的目录。

_CONDITIONS_
> 过滤表达式。

**where**
> 引出过滤条件。

**order by** _FIELD_
> 对结果排序。

**limit** _N_
> 限制输出数量。

**--help**
> 显示帮助信息。

# DESCRIPTION

**fselect** 使用类 SQL 语法查找和查询文件。它把文件系统当作数据库，用熟悉的 SQL 语法选择属性并按条件过滤。

该工具可提取大小、日期、权限等元数据；对图片和音频还能提取尺寸与标签。count 和 sum 等聚合函数可用于结果之上。

fselect 弥合了 find 的强大与 SQL 的易读之间的鸿沟。

# CAVEATS

复杂查询在大目录上可能较慢。某些字段需要读取文件内容。SQL 语法存在一些限制。

# HISTORY

fselect 的创建目的是为文件搜索提供直观的查询语言。它将数据库查询概念应用到文件系统操作上，实现熟悉而强大的搜索。

# INSTALL

```brew: brew install fselect```

```nix: nix profile install nixpkgs#fselect```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[find](/man/find)(1), [fd](/man/fd)(1), [locate](/man/locate)(1)

# RESOURCES

```[Source code](https://github.com/jhspetersson/fselect)```

<!-- verified: 2026-07-15 -->
