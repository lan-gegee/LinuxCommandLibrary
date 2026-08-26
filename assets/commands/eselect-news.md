# TAGLINE

Gentoo 新闻条目阅读器和管理器

# TLDR

**列出**新闻条目

```eselect news list```

只列出**新**条目

```eselect news list new```

**阅读**所有未读新闻

```eselect news read```

阅读**指定**的新闻条目

```eselect news read 1 2 3```

将条目标记为**未读**

```eselect news unread 1 2```

**删除**已读的新闻条目

```eselect news purge```

**统计**新闻条目数量

```eselect news count new```

# SYNOPSIS

**eselect news** _action_ [_arguments_]

# DESCRIPTION

**eselect news** 是一个 eselect 模块，用于阅读 Gentoo 新闻条目。同步软件仓库后有新新闻可用时，Portage 会打印提示。

# PARAMETERS

**list [all|new]**
> 列出可用的新闻条目（默认为 all）

**read [NUMBERS...]**
> 阅读指定的新闻条目；未指定时阅读全部未读条目

**unread NUMBERS...**
> 将指定新闻条目标记为未读

**purge**
> 删除所有已读的新闻条目

**count [all|new]**
> 显示新闻条目的数量（默认为 new）

# CAVEATS

新闻条目是 Gentoo 开发者发布的仓库相关公告，涉及重要变更。阅读新闻条目会将其标记为已读，之后不会再收到提示。

# HISTORY

**eselect news** 是 Gentoo Linux 上 **eselect** 框架的一部分，该框架为配置管理提供了模块化的体系。

# SEE ALSO

[eselect](/man/eselect)(1), [emerge](/man/emerge)(1), [emaint](/man/emaint)(1)

# RESOURCES

```[Source code](https://gitweb.gentoo.org/proj/eselect.git/)```

```[Documentation](https://wiki.gentoo.org/wiki/Eselect)```

<!-- verified: 2026-07-14 -->
