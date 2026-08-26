# TAGLINE

DICT 协议词典客户端

# TLDR

**查询单词**定义

```dict [word]```

**在特定词典中查询**

```dict -d [wn] [word]```

**列出可用词典**

```dict -D```

**查找匹配的单词**（通配符）

```dict -m [word*]```

**使用指定服务器**

```dict -h [dict.org] [word]```

**显示数据库信息**

```dict -i [wn]```

# SYNOPSIS

**dict** [_options_] _word_

# PARAMETERS

_WORD_
> 要查询的单词或短语。

**-d** _DATABASE_
> 在指定的词典数据库中搜索。

**-D**
> 列出可用的数据库。

**-m**
> 匹配模式（查找相似的单词）。

**-s** _STRATEGY_
> 用于匹配的搜索策略。

**-S**
> 列出可用的策略。

**-h** _HOST_
> 连接到指定的 DICT 服务器。

**-p** _PORT_
> 端口号（默认：2628）。

**-i** _DATABASE_
> 显示数据库信息。

**--help**
> 显示帮助信息。

# DESCRIPTION

**dict** 是一个用于 DICT 协议词典服务器的命令行客户端。它可以访问 DICT 服务器上的各类词典和同义词库，返回释义、同义词及相关信息。

DICT 协议允许同时查询多个词典。默认公共服务器（dict.org）托管了大量词典，包括 WordNet、Jargon File 以及各种语言词典。

dict 支持多种搜索策略，包括精确匹配、前缀、后缀和正则表达式匹配。这种灵活性使得即使拼写不确定也能找到单词。

# CAVEATS

需要与 DICT 服务器的网络连接。可用词典取决于服务器。响应时间随网络状况而变化。部分词典有许可限制。

# HISTORY

dict 客户端实现了 **DICT 协议**（RFC 2229），该协议于 **1997** 年开发，作为词典服务器访问的标准。该协议旨在为通过 Internet 进行的词典查询提供通用接口。

# INSTALL

```apt: sudo apt install dict```

```brew: brew install dict```

```nix: nix profile install nixpkgs#dict```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dictd](/man/dictd)(8), [curl](/man/curl)(1), [aspell](/man/aspell)(1)

# RESOURCES

```[Homepage](http://www.dict.org)```

<!-- verified: 2026-07-11 -->
