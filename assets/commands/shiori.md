# TAGLINE

带 Web 界面的自托管书签管理器

# TLDR

**启动服务器**

```shiori serve```

**添加书签**

```shiori add [https://example.com]```

**带标题添加**

```shiori add -t "[Title]" [https://example.com]```

**搜索书签**

```shiori search [query]```

**列出书签**

```shiori print```

**删除书签**

```shiori delete [id]```

**导出书签**

```shiori export > [bookmarks.html]```

**导入书签**

```shiori import [bookmarks.html]```

# SYNOPSIS

**shiori** _command_ [_options_] [_args_]

# PARAMETERS

**serve**
> 启动 Web 服务器。

**add** _URL_
> 添加书签。

**search** _QUERY_
> 搜索书签。

**print**
> 列出书签。

**delete** _ID_
> 删除书签。

**export**
> 导出书签。

**import** _FILE_
> 导入书签。

**-t**, **--title** _TITLE_
> 设置标题。

**-e**, **--excerpt** _TEXT_
> 设置摘要。

**--tags** _TAGS_
> 添加标签。

# DESCRIPTION

**shiori** 是一款自托管书签管理器，可将网页保存下来供离线阅读。添加 URL 时，shiori 会下载页面，用可读性算法提取正文内容，并将原始 HTML 和干净的文本版本一并存储到数据库中。

书签支持跨标题、URL 和已保存内容的全文搜索，便于找回先前保存的页面。标签提供了额外的组织方式，内置的 Web 界面则以可视化方式浏览、编辑和管理收藏。

数据可以从标准的书签 HTML 文件导入和导出，实现与浏览器及其他书签管理器的互操作。CLI 提供与 Web 界面相同的功能，方便脚本化和自动化。

# CONFIGURATION

**SHIORI_DIR**
> 设置数据库和存档页面数据目录的环境变量（默认：~/.local/share/shiori）。

# CAVEATS

需要数据库（默认 SQLite）。大量存档会占用存储空间。部分页面解析效果不佳。

# HISTORY

**Shiori** 由 **RadhiFadlillah** 创建，最初是一款简单的书签管理器。其名称取自日语的"书签"，专注于离线阅读。

# INSTALL

```nix: nix profile install nixpkgs#shiori```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[buku](/man/buku)(1), [pocket](/man/pocket)(1)
