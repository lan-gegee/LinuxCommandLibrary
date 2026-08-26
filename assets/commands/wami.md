# TAGLINE

搜索并推荐软件工具

# TLDR

按排序搜索**所有**类别

```wami -a -S [asc|desc] -s [search_string]```

按排序搜索 **GitHub**

```wami -a -S desc --github [search_string]```

列出**主题**

```wami --list-topics [search_string]```

搜索**渗透测试**工具

```wami -S desc -s pentest credential default```

# SYNOPSIS

**wami** [_OPTIONS_] [_SEARCH_...]

# PARAMETERS

**-a, --show-all**
> 显示展开的结果

**-S, --sort** _ORDER_
> 对结果排序（asc 或 desc）

**-s, --search-all**
> 搜索所有类别

**--github**
> 搜索 GitHub

**--list-topics**
> 列出匹配的主题

# DESCRIPTION

**wami** 是一款为任务推荐合适程序的开源工具。它搜索一个精选数据库和 GitHub，以找到符合指定条件的工具。

该工具特别适合查找安全与渗透测试工具，但也适用于一般性的软件发现。

# CAVEATS

GitHub 搜索需要联网。结果取决于数据库覆盖范围。搜索质量因关键词的具体程度而异。

# SEE ALSO

[apt-cache](/man/apt-cache)(8)
