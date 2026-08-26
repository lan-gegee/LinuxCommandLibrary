# TAGLINE

在终端中浏览 Hacker News（haxor-news）

# TLDR

**显示热门帖子**

```hn top```

**显示最新帖子**

```hn new [20]```

**显示最佳帖子**

```hn best```

**显示 Ask HN 帖子**

```hn ask```

**显示 Show HN 帖子**

```hn show```

**按列表编号查看帖子的链接内容或评论**

```hn view [1]```

**查看某帖子的全部评论，并通过分页器输出**

```hn view [8] -c | less -r```

**按关键字过滤每月的 "who is hiring" 帖子**

```hn hiring "[(?i)(Node|JavaScript).*(remote)]"```

# SYNOPSIS

**hn** _command_ [_params_] [_options_]

**haxor-news**

# COMMANDS

**top**, **best**, **new**, **ask**, **show**, **jobs**, **onion** [_limit_]
> 列出对应类别的帖子（默认数量：10；onion 默认：全部）。

**view** _#_ [_options_]
> 查看列表中某个帖子链接的网页内容，配合 **-c** 可查看其评论。

**hiring** [_regex_] [_post_id_]
> 过滤最新（或指定）的每月 "who is hiring" 帖子。

**freelance** [_regex_] [_post_id_]
> 过滤最新（或指定）的每月自由职业者信息帖子。

**user** _user_id_
> 显示用户的资料信息。

**help**
> 显示用法帮助。

# PARAMETERS

**-c**, **--comments**
> 显示所查看帖子的全部评论。

**-cu**, **--comments_unseen**
> 只显示之前未看过的评论（以 **[!]** 标记）。

**-cr**, **--comments_recent**
> 只显示最近 60 分钟内发表的评论。

**-cq**, **--comments_regex_query** _regex_
> 只显示匹配某个正则表达式的评论。

**-ch**, **--comments_hide**
> 隐藏（而非折叠）不匹配过滤条件的评论。

**-b**, **--browser**
> 在默认浏览器而非终端中打开链接内容或评论。

# DESCRIPTION

**hn** 是 **haxor-news** 提供的命令行客户端。haxor-news 是一个把 Hacker News 带到终端的 Python 工具，无需离开命令行即可使用。它可以列出并翻阅 Top、Best、New、Ask、Show、Jobs 以及愚人节 "Onion" 帖子，查看帖子的链接内容（渲染为可读文本）或完整评论树，并将大量评论筛选为未读、最近或匹配正则表达式的部分。

输出可以管道传给分页器、重定向到文件，或与其他命令行工具组合使用。直接运行不带参数的 **haxor-news** 命令（而不是 **hn**）会启动一个可选的、带自动补全的交互式提示符，使用相同的 **hn** _command_ 语法。

# CAVEATS

需要联网；数据通过 **haxor** Python 库来自 Hacker News 的 Firebase/Algolia API。该项目自 2010 年代中期以来几乎无更新，但其只读浏览命令仍然可用。

# HISTORY

**haxor-news** 由 **Donne Martin** 创建，于 **2015 年**首次发布，基于 Kenneth Reitz 的 **requests**、Aaron Swartz 的 **html2text** 以及 **click** 和 **prompt_toolkit** 库构建。

# SEE ALSO

[rtv](/man/rtv)(1), [tuir](/man/tuir)(1), [w3m](/man/w3m)(1)

# RESOURCES

```[Source code](https://github.com/donnemartin/haxor-news)```

<!-- verified: 2026-07-19 -->
