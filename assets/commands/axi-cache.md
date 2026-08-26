# TAGLINE

面向 Debian 的快速索引软件包搜索工具

# TLDR

**搜索**软件包名称与描述

```axi-cache search [keyword]```

**显示**上次搜索的更多结果

```axi-cache more```

用额外的关键词细化**上一次搜索**

```axi-cache again [keyword]```

**显示**软件包详情

```axi-cache show [package-name]```

# SYNOPSIS

**axi-cache** [_options_] _command_ [_args_]

# DESCRIPTION

**axi-cache** 是一款面向 Debian 系系统的快速软件包搜索工具，基于 apt-xapian-index。它利用预构建的 Xapian 索引对软件包名称和描述进行快速全文搜索，支持相关度排序和 debtags。

在全文搜索方面，该工具比 apt-cache 快得多，同时还封装了多个 apt-cache 前端命令。

# PARAMETERS

**search** _terms_
> 对软件包名称和描述开始一次新的搜索。

**again** _terms_
> 重复上一次搜索，可选择追加查询词。

**last**
> 再次显示上一次搜索的结果。

**more** [_count_]
> 显示上一次搜索的更多词条或结果。

**info**
> 打印关于 apt-xapian-index 环境的信息。

**show** _package_
> apt-cache show 的前端；显示软件包记录。

**showpkg** _package_
> apt-cache showpkg 的前端。

**depends** _package_
> apt-cache depends 的前端。

**rdepends** _package_
> apt-cache rdepends 的前端；显示反向依赖。

**policy** _package_
> apt-cache policy 的前端。

**madison** _package_
> apt-cache madison 的前端。

# FEATURES

- 索引化全文搜索
- 支持 debtags 的过滤
- 相关度排序
- 快速的查询响应
- apt-cache 前端命令

# CAVEATS

需要安装并更新 apt-xapian-index。必须重建索引（update-apt-xapian-index）才能反映新加入的软件包。它不搜索文件内容；如需此功能请使用 apt-file。并非所有基于 Debian 的发行版都提供此工具。

# HISTORY

**axi-cache** 由 Enrico Zini 于 **2007** 年前后作为 apt-xapian-index 项目的一部分开发，旨在借助 Xapian 全文搜索引擎提供更快的软件包搜索。

# SEE ALSO

[apt-cache](/man/apt-cache)(1), [apt-file](/man/apt-file)(1), [aptitude](/man/aptitude)(8)

# RESOURCES

```[Source code](https://salsa.debian.org/debian/apt-xapian-index)```

```[Homepage](https://tracker.debian.org/pkg/apt-xapian-index)```

<!-- verified: 2026-06-18 -->
