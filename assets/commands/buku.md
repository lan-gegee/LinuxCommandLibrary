# TAGLINE

支持标签和搜索的命令行书签管理器

# TLDR

**添加**书签

```buku -a [https://example.com] [tag1,tag2]```

**搜索**书签

```buku [keyword]```

**列出**所有书签

```buku -p```

**打开**书签

```buku -o [index]```

**删除**书签

```buku -d [index]```

**导出**为 HTML

```buku -e [bookmarks.html]```

# SYNOPSIS

**buku** [_options_] [_keywords_]

# DESCRIPTION

**buku** 是一个功能强大的命令行书签管理器。它将书签存储在 SQLite 数据库中，支持打标签、搜索、自动抓取标题以及浏览器集成。

书签可以用逗号分隔的标签来组织，并通过关键字、正则表达式或标签过滤器进行搜索。该工具在添加 URL 时会自动抓取页面标题和描述。它支持 HTML、Markdown 和 JSON 格式的导入导出，便于从浏览器和其他书签管理器迁移数据。还可选配 Web 界面（**bukuserver**），以图形方式访问同一个数据库。

# PARAMETERS

**-a**, **--add** _url_ [_tags_]
> 添加书签

**-u**, **--update** _index_
> 更新书签

**-d**, **--delete** _index_
> 删除书签

**-p**, **--print** [_index_]
> 列出书签

**-o**, **--open** _index_
> 在浏览器中打开

**-s**, **--sany** _keywords_
> 搜索（任意关键字）

**-S**, **--sall** _keywords_
> 搜索（全部关键字）

**-e**, **--export** _file_
> 导出为 HTML

**-i**, **--import** _file_
> 从 HTML/Markdown 导入

**-t**, **--tags**
> 列出所有标签

# FEATURES

- 自动抓取标题
- 全文搜索
- 基于标签的组织方式
- 浏览器集成
- 导入/导出（HTML、Markdown、JSON）
- 支持加密
- 正则表达式搜索
- 数据库可移植

# WORKFLOW

```bash
# Add bookmark
buku -a https://github.com programming,git

# Search
buku python

# Browse all
buku -p

# Open in browser
buku -o 5

# Update tags
buku -u 5 --tag +docker,-kubernetes

# Export
buku -e bookmarks.html
```

# BROWSER INTEGRATION

可以从以下浏览器导入：
- Chrome/Chromium
- Firefox
- Safari

# CAVEATS

抓取标题需要联网。浏览器集成需要额外配置。数据库保存在本地（不自动同步）。命令行界面不一定适合所有用户。图形界面可另行安装（bukuserver）。

# HISTORY

**buku** 由 Arun Prakash Jana 于 **2015 年**前后创建，旨在为终端提供一款快速、注重隐私的书签管理器。

# INSTALL

```dnf: sudo dnf install buku```

```apk: sudo apk add buku```

```brew: brew install buku```

```nix: nix profile install nixpkgs#buku```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[urlview](/man/urlview)(1), [qutebrowser](/man/qutebrowser)(1)

# RESOURCES

```[Source code](https://github.com/jarun/buku)```

```[Documentation](https://github.com/jarun/buku/wiki)```

<!-- verified: 2026-06-22 -->
