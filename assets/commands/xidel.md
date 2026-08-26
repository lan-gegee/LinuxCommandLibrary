# TAGLINE

HTML/XML/JSON 数据提取工具

# TLDR

**使用 XPath 提取**

```xidel [file.html] -e "//title"```

**从 URL 提取**

```xidel [https://example.com] -e "//h1"```

**CSS 选择器**

```xidel [file.html] --css "div.content"```

**提取 JSON**

```xidel [file.json] -e "$json/key"```

**多次提取**

```xidel [file.html] -e "//title" -e "//h1"```

**输出 JSON**

```xidel [file.html] -e "//a/@href" --output-format=json```

**跟随链接**

```xidel [url] -f "//a/@href" -e "//title"```

# SYNOPSIS

**xidel** [_-e expression_] [_--css selector_] [_options_] _input_

# PARAMETERS

**-e**, **--extract** _EXPR_
> XPath/XQuery 表达式。

**--css** _SELECTOR_
> CSS 选择器。

**-f**, **--follow** _EXPR_
> 跟随链接。

**--output-format** _FORMAT_
> 输出格式。

**--input-format** _FORMAT_
> 输入格式。

**-s**, **--silent**
> 抑制状态信息。

**--user-agent** _UA_
> 用户代理（User Agent）。

# DESCRIPTION

**xidel** 是一个命令行工具，用于从 HTML、XML 和 JSON 文档中提取和查询数据。它支持多种查询语言，包括 XPath、XQuery 和 CSS 选择器，因此无论处理本地文件还是远程 URL，都能胜任各种数据提取任务。

XPath 和 XQuery 表达式可以精确地导航文档结构，而 CSS 选择器则为熟悉 Web 开发的用户提供了熟悉的语法。对于 JSON 文档，xidel 使用基于路径的语法来遍历对象层级。可以在一次调用中组合多个提取表达式，以完成复杂的数据收集。

该工具包含链接跟随模式，可实现网络爬取：xidel 可以遍历页面上的链接，并对每个访问的页面应用提取表达式。输出可以格式化为纯文本、JSON 或其他结构化格式，便于集成到数据处理管道中。

# CAVEATS

语法复杂，有学习曲线。大文档可能较慢。可能出现编码问题。

# HISTORY

**xidel** 作为一个功能强大的命令行数据提取工具而创建。它将多种查询语言整合到一个实用程序中。

# INSTALL

```brew: brew install xidel```

```nix: nix profile install nixpkgs#xidel```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xmllint](/man/xmllint)(1), [jq](/man/jq)(1), [pup](/man/pup)(1)
