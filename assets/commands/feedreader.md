# TAGLINE

桌面端 RSS/Atom 新闻聚合器

# TLDR

打印**未读**文章数

```feedreader --unreadCount```

**添加**源 URL

```feedreader --addFeed=[feed_url]```

抓取特定文章

```feedreader --grabArticle=[article_url]```

下载文章中的**图片**

```feedreader --url=[feed_url] --grabImages=[article_path]```

播放 URL 中的**媒体**

```feedreader --playMedia=[article_url]```

以详细调试输出**运行**

```feedreader --verbose```

# SYNOPSIS

**feedreader** [_options_]

# DESCRIPTION

**feedreader** 是一款 GTK 桌面 RSS/Atom 订阅客户端。它聚合来自多个来源的新闻订阅，并为新文章提供桌面通知。该应用支持多种订阅服务，包括 Feedly、Inoreader 和本地订阅阅读，具备文章同步、标签和全文搜索等功能。

注意：FeedReader 已不再维护。建议用户迁移到 NewsFlash 等仍在积极开发的替代品。

# PARAMETERS

**--unreadCount**
> 显示数据库中当前未读文章的数量。

**--addFeed**=_URL_
> 将源添加到收藏。

**--grabArticle**=_URL_
> 使用 ContentGrabber 抓取给定的 URL。

**--grabImages**=_PATH_
> 下载 html 文档中的所有图片。

**--url**=_URL_
> grabImages 所需的文章 URL。

**--playMedia**=_URL_
> 用给定的 URL 启动媒体播放器。

**--ping**=_URL_
> 用给定的 URL 测试 ping 功能。

**--verbose**
> 输出所有调试信息。

**--about**
> 显示关于对话框。

**--version**
> 显示 FeedReader 版本号。

# CAVEATS

项目已停止维护。可考虑 NewsFlash 等替代品。支持 Feedly 和 Inoreader 等多种订阅服务。

# INSTALL

```aur: yay -S feedreader```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[newsboat](/man/newsboat)(1)
