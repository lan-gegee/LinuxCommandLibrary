# TAGLINE

Go 语言编写的高速源码搜索工具

# TLDR

**搜索模式**

```pt [pattern]```

**在特定目录中搜索**

```pt [pattern] [path]```

**搜索特定文件类型**

```pt --type=[go] [pattern]```

**不区分大小写搜索**

```pt -i [pattern]```

**只显示文件名**

```pt -l [pattern]```

# SYNOPSIS

**pt** [_options_] _pattern_ [_path_]

# PARAMETERS

_PATTERN_
> 搜索模式。

_PATH_
> 搜索路径。

**-i**
> 不区分大小写。

**-l**
> 只显示文件。

**--type** _TYPE_
> 文件类型过滤。

**-w**
> 整词匹配。

**-C** _N_
> 上下文行数。

# DESCRIPTION

**pt**（Platinum Searcher）是用 Go 编写的快速代码搜索工具，类似于 **ag**（The Silver Searcher）和 **ack**。它递归搜索目录树中的文本模式，自动跳过 **.gitignore** 和其他 VCS 忽略文件中列出的文件。

该工具专为大型项目中的源码搜索而设计。它支持按文件类型过滤、整词边界匹配以及匹配项周围的上下文显示。得益于 Go 的单二进制静态编译特性，它具有良好的跨平台支持。

# CAVEATS

使用 Go 编写。遵循 .gitignore 规则。

# HISTORY

pt 是用 Go 编写的**快速代码搜索**工具。

# INSTALL

```apk: sudo apk add tcl-lib```

```brew: brew install pt```

```nix: nix profile install nixpkgs#pt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ag](/man/ag)(1), [rg](/man/rg)(1), [grep](/man/grep)(1)
