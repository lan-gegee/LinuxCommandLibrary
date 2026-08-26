# TAGLINE

从终端搜索 Arch Linux Wiki

# TLDR

**搜索 Arch Wiki**

```arch-wiki [search_term]```

**搜索并在浏览器中打开结果**

```arch-wiki -o [search_term]```

**以特定语言搜索**

```arch-wiki -l [de] [search_term]```

**显示不带格式化的原始搜索结果**

```arch-wiki -r [search_term]```

**限制结果数量**

```arch-wiki -n [10] [search_term]```

# SYNOPSIS

**arch-wiki** [_options_] _search_term_

# PARAMETERS

**-o**, **--open**
> 在默认网页浏览器中打开第一个结果。

**-l**, **--lang** _code_
> 以特定语言搜索（如 de、es、fr、ja）。

**-n**, **--number** _count_
> 限制返回的结果数量。

**-r**, **--raw**
> 输出不带颜色格式的原始结果。

**-h**, **--help**
> 显示帮助信息。

**-v**, **--version**
> 显示版本信息。

# DESCRIPTION

**arch-wiki** 是一个命令行工具，可直接在终端中搜索 Arch Linux Wiki。它查询 wiki 的 API 并展示带标题和 URL 的结果，让你无需离开命令行即可快速访问文档。

Arch Wiki 以其全面且维护良好的文档而闻名，内容不仅涵盖 Arch Linux，还包括一般性 Linux 主题。该工具让你在进行系统管理和故障排查时能快速访问这一知识库。

结果默认以语法高亮显示，便于浏览。**-o** 标志会立即打开最上方的结果，适合你明确知道要找什么的情况。

# CAVEATS

需要有效的互联网连接。该工具查询 wiki API，因此结果取决于 wiki 的搜索索引。某些文章的名称可能与预期不同；如果初次搜索结果不理想，请尝试其他关键词。

# HISTORY

**arch-wiki** 工具的开发目的是提供对 Arch Wiki 的快速终端访问——它是 Linux 领域最全面的文档资源之一。Arch Wiki 本身于 **2002** 年随 Arch Linux 一同建立，如今已收录数千篇文章，涵盖适用于众多 Linux 发行版的软件配置、故障排查和最佳实践。

# SEE ALSO

[man](/man/man)(1), [tldr](/man/tldr)(1)
