# TAGLINE

从终端浏览 Arch Linux Wiki

# TLDR

按标题**搜索** Arch Wiki

```archwiki-rs search "[query]"```

在页面正文中**搜索**

```archwiki-rs search "[query]" -t```

在终端中**阅读**页面

```archwiki-rs read-page "[Neovim]"```

以 Markdown 格式**阅读**页面

```archwiki-rs read-page "[Neovim]" --format markdown```

**下载**页面和分类名称以供离线搜索

```archwiki-rs sync-wiki```

**列出**所有可用页面

```archwiki-rs list-pages```

# SYNOPSIS

**archwiki-rs** _command_ [_options_] [_query_]

# DESCRIPTION

**archwiki-rs** 是一个命令行工具，用于在终端浏览 Arch Linux Wiki。它可以按标题或正文搜索页面，将页面内容渲染为纯文本或 Markdown，并缓存页面供离线阅读。

该工具提供可离线访问的 Arch Wiki 文档，对系统管理和故障排查很有用。

# PARAMETERS

**read-page** _page_
> 获取并显示 wiki 页面。使用 **--format** 选择输出格式（如 markdown）。

**search** _query_
> 按标题搜索页面；加上 **-t** 则改为搜索页面正文内容。

**list-pages**
> 列出所有可用的 wiki 页面（默认树形显示，**-f** 为平铺列表，**-c** 按分类过滤）。

**list-categories**
> 列出所有可用的 wiki 分类。

**list-languages**
> 列出支持的页面语言。

**sync-wiki**
> 下载搜索与列表命令所使用的页面和分类名称。

**local-wiki**
> 下载一份完整的 Arch Wiki 本地副本（会发起大量请求）。

**info**
> 显示应用元数据和配置，例如缓存目录。

**completions** _shell_
> 生成 Shell 补全文件。

**--json**, **--json-raw**
> 输出机器可读的 JSON。

# CAVEATS

离线使用时内容可能过时。格式可能与网页版不同。部分 wiki 功能在终端中不可用。

# HISTORY

**archwiki-rs** 是为偏好终端文档访问方式的 Arch Linux 用户开发的 Rust 工具。

# SEE ALSO

[man](/man/man)(1), [tldr](/man/tldr)(1), [curl](/man/curl)(1)

# RESOURCES

```[Source code](https://github.com/lucifayr/archwiki-rs)```

<!-- verified: 2026-06-11 -->
