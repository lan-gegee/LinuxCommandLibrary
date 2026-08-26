# TAGLINE

批量下载 Reddit 的帖子和媒体内容

# TLDR

**从 subreddit 下载帖子**

```bdfr download [./output] --subreddit [Python] -L [10]```

**下载用户发布的帖子**

```bdfr download [./output] --user [username] --submitted -L [100]```

**下载你收藏的帖子**（需要身份验证）

```bdfr download [./output] --user me --saved --authenticate -L [25]```

**归档帖子数据**及评论

```bdfr archive [./output] --user [username] --submitted --all-comments```

**克隆帖子和数据**（下载 + 归档）

```bdfr clone [./output] --subreddit [Python] -L [10]```

**从多个 subreddit 下载**

```bdfr download [./output] --subreddit "[Python, programming, linux]" -L [10]```

**搜索并下载**匹配的帖子

```bdfr download [./output] --subreddit [Python] --search "[machine learning]" -L [20]```

# SYNOPSIS

**bdfr** _mode_ _output_path_ [_options_]

# DESCRIPTION

**bdfr**（Bulk Downloader for Reddit）是一款从 Reddit 下载帖子、媒体和数据的工具。它可以归档帖子供研究使用、备份收藏内容，或从 subreddit 下载媒体文件。

该工具有三种模式：**download**（下载图片和视频等链接的媒体）、**archive**（以 JSON/YAML/XML 格式保存帖子元数据、正文和评论），以及 **clone**（高效地同时执行两种操作）。

# SUBCOMMANDS

**download**
> 下载 Reddit 帖子中链接的媒体

**archive**
> 归档帖子数据、元数据和评论

**clone**
> 同时执行下载和归档操作

# PARAMETERS

**-s, --subreddit** _name_
> 目标 subreddit；可重复指定，也可用逗号分隔多个

**-u, --user** _name_
> 目标 Reddit 用户名；"me" 表示已认证的用户（可重复）

**-m, --multireddit** _name_
> 目标为某用户的多版块聚合（multireddit）（需配合 --user；可重复）

**-l, --link** _url_
> 按 URL 或 ID 下载单个帖子（可重复）

**-L, --limit** _n_
> 每个来源的最大帖子数（默认约 1000，即 Reddit API 上限）

**--submitted**
> 下载用户发布的帖子

**--saved**
> 下载用户收藏的帖子（需要 --authenticate）

**--upvoted**
> 下载用户点赞过的帖子（需要 --authenticate）

**--authenticate**
> 使用 OAuth2 身份验证以访问私有内容

**--search** _query_
> 用于过滤帖子的搜索查询

**-S, --sort** _type_
> 排序方式：hot、top、new、controversial、rising、relevance

**-t, --time** _period_
> 时间过滤：all、hour、day、week、month、year

**--all-comments**
> 归档某用户的全部评论（archive 模式，配合 --user）

**-f, --format** _type_
> 归档输出格式：json（默认）、xml、yaml

**--file-scheme** _format_
> 自定义文件名模板（占位符：{POSTID}、{TITLE}、{REDDITOR}、{SUBREDDIT}、{DATE}、{FLAIR}、{UPVOTES}）

**--folder-scheme** _format_
> 使用相同占位符的自定义文件夹模板

**--skip** _ext_
> 跳过具有指定扩展名的文件（download 模式；可重复）

**--no-dupes**
> 跳过已下载的文件，通过 MD5 哈希检测（download 模式）

**-v, --verbose**
> 提高输出详细程度（可重复）

# CONFIGURATION

**~/.config/bdfr/default_config.cfg**
> 主配置文件（Linux），保存 client_id、client_secret、scopes 和默认选项。macOS 上位于 ~/Library/Application Support/bdfr。

# CAVEATS

需要 Python 3.9 或更高版本。访问收藏帖子、点赞过的帖子和私有 multireddit 需要身份验证。受 Reddit API 速率限制约束。某些媒体托管方可能阻止自动下载。

# HISTORY

BDFR 作为早期 Reddit 下载工具的现代化分支而创建，由 **Serene-Arc** 自 **2020** 年前后开始开发。它取代了最初的 Bulk Downloader for Reddit，架构得到改进，并持续适配不断变化的 Reddit API。

# SEE ALSO

[gallery-dl](/man/gallery-dl)(1), [yt-dlp](/man/yt-dlp)(1), [youtube-dl](/man/youtube-dl)(1), [wget](/man/wget)(1)

# RESOURCES

```[Source code](https://github.com/Serene-Arc/bulk-downloader-for-reddit)```

```[Documentation](https://github.com/Serene-Arc/bulk-downloader-for-reddit/blob/master/README.md)```

<!-- verified: 2026-06-19 -->
