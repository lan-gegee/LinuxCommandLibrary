# TAGLINE

交互式 JSON 查看器和处理器

# TLDR

**交互式 JSON 查看器**

```cat [data.json] | fx```

**应用转换**

```cat [data.json] | fx '.items'```

**用表达式过滤**

```cat [data.json] | fx '.[] | select(.active)'```

**选取多个字段**

```cat [data.json] | fx '.name' '.age'```

**格式化输出**

```cat [data.json] | fx .```

# SYNOPSIS

**fx** [_options_] [_expressions_...]

# PARAMETERS

_EXPRESSIONS_
> 点号路径或 fx 表达式语法。

**.**
> 美化输出 JSON。

**-r**, **--raw**
> 输出原始字符串。

**-s**, **--slurp**
> 读取多个 JSON 对象。

**--help**
> 显示帮助信息。

# DESCRIPTION

**fx** 是一个用 Go 编写的命令行 JSON 处理工具，支持交互式浏览。它提供类似 jq 的过滤功能，并使用自己的表达式语法实现灵活的数据操作。

在交互模式下，fx 以可导航的树形视图展示 JSON 数据。表达式模式允许将数据通过管道进行转换。多个表达式可以串联使用。

fx 可处理流式 JSON、对象操作和数据提取。

# CAVEATS

大文件在交互模式下可能较慢。JavaScript 表达式有学习曲线。语法与 jq 不同。

# HISTORY

fx 的定位是一款现代 JSON 工具，将交互式探索与基于 JavaScript 的处理相结合，为熟悉 JavaScript 的开发者提供 jq 之外的另一种选择。

# INSTALL

```pacman: sudo pacman -S fx```

```apk: sudo apk add fx```

```zypper: sudo zypper install fx```

```brew: brew install fx```

```nix: nix profile install nixpkgs#fx```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jq](/man/jq)(1), [gron](/man/gron)(1), [jless](/man/jless)(1)
