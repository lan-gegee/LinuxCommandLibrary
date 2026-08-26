# TAGLINE

在目录树中查找文件

# TLDR

**按名称查找**文件

```find [path] -name "[*.txt]"```

**查找目录**

```find [path] -type d -name "[dirname]"```

**查找并删除**

```find [path] -name "[*.tmp]" -delete```

**按修改时间查找**

```find [path] -mtime -[7]```

**查找并对结果执行**命令

```find [path] -name "[*.log]" -exec rm {} \;```

**以自定义格式打印**输出

```find [path] -printf "[%p %s bytes\n]"```

# SYNOPSIS

**find** [_path_...] [_expression_]

# PARAMETERS

_PATH_
> 起始目录（默认：当前目录）。

**-name** _PATTERN_
> 匹配文件名模式（glob）。

**-iname** _PATTERN_
> 不区分大小写的名称匹配。

**-type** _TYPE_
> 文件类型：f（文件）、d（目录）、l（链接）。

**-mtime** _N_
> N 天前修改过。

**-size** _N_
> 文件大小（c 字节、k KB、M MB）。

**-exec** _CMD_ **{}** **\;**
> 对查到的结果执行命令。

**-delete**
> 删除匹配的文件。

**-maxdepth** _N_
> 最大目录深度。

**-printf** _FORMAT_
> 为每个匹配项按自定义格式打印（例如 %p 路径、%f 文件名、%s 大小、%t 时间）。除非包含 \n，否则不会换行。

**--help**
> 显示帮助信息。

# DESCRIPTION

**find** 在目录树中搜索满足条件的文件。它是 Unix 上最强大的实用工具之一，通过 -exec 把查找与文件操作结合起来。

该工具从左到右对表达式求值，遇到 -a（与）和 -o（或）时进行短路处理。-print、-delete、-exec 等动作会作用于匹配到的条目。

find 的灵活性足以应对复杂查询，可以把名称模式、时间戳、大小、权限和所有者等条件组合起来。

# CAVEATS

glob 模式必须加引号。-delete 会立即执行且不请求确认。复杂表达式需要仔细安排先后顺序。

# HISTORY

find 出现于 **Unix Version 5**（1974 年）。它至今仍是标准的文件查找工具，尽管 fd 等现代替代品针对常见场景提供了更简单的语法。

# INSTALL

```apt: sudo apt install findutils```

```dnf: sudo dnf install findutils```

```pacman: sudo pacman -S findutils```

```apk: sudo apk add findutils```

```zypper: sudo zypper install findutils```

```brew: brew install findutils```

```nix: nix profile install nixpkgs#findutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fd](/man/fd)(1), [locate](/man/locate)(1), [xargs](/man/xargs)(1)
