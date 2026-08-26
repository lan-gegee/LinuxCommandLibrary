# TAGLINE

在命令行中对 YouTube 频道字幕进行全文搜索

# TLDR

将频道的字幕**下载**到数据库

```yt-fts download "[https://www.youtube.com/@channel]"```

**搜索**短语

```yt-fts search "[keyword]"```

**语义搜索**（嵌入向量；需要 API 密钥）

```yt-fts vsearch "[query]"```

# SYNOPSIS

**yt-fts** *command* [*options*]

# DESCRIPTION

**yt-fts** 用 **yt-dlp** 抓取字幕，存储在 SQLite 中，支持关键词搜索和可选的语义搜索，并返回带时间戳的 YouTube URL。安装方式为 **pip install yt-fts**。

**注意：** 上游已表示该项目停止维护；它可能仍可使用，但只能获得有限的支持。

# PARAMETERS

**download** *channel_url*

> 获取字幕（**--jobs** 控制并行度）。

**search** *query*

> 全文搜索。

**vsearch** *query*

> 配置后可进行向量/语义搜索。

**update** / **list** / **export** 相关命令

> 维护本地库——详见 **yt-fts --help**。

# CAVEATS

存在上游停更的风险。YouTube 可能限流或要求提供 Cookie。语义功能需要 OpenAI（或兼容）API 密钥且产生费用。请遵守 YouTube 服务条款。

# SEE ALSO

[yt-dlp](/man/yt-dlp)(1), [sqlite3](/man/sqlite3)(1)

# RESOURCES

```[Source code](https://github.com/NotJoeMartinez/yt-fts)```

<!-- verified: 2026-07-19 -->
