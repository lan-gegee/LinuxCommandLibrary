# TAGLINE

Calibre 电子书数据库的命令行接口

# TLDR

**列出所有图书**

```calibredb list```

**向书库添加图书**

```calibredb add [book.epub]```

**按 ID 删除图书**

```calibredb remove [23]```

**搜索图书**

```calibredb search "[title:keyword]"```

**显示图书元数据**

```calibredb show_metadata [42]```

**设置图书元数据**

```calibredb set_metadata [42] -f [title:"New Title"]```

**导出图书**

```calibredb export [23,45] --to-dir [output/]```

**为已有图书添加格式**

```calibredb add_format [42] [book.mobi]```

# SYNOPSIS

**calibredb** _command_ [_options_] [_arguments_]

# DESCRIPTION

**calibredb** 是 Calibre 电子书数据库的命令行接口。它可管理电子书库、添加/删除图书、修改元数据，还能连接本地或远程的 Calibre 内容服务器。

# COMMANDS

**list**
> 列出数据库中的图书，支持自定义字段和过滤。

**add**
> 将图书文件导入书库。

**remove**
> 按 ID 删除图书。

**search**
> 使用 calibre 的搜索语法查询书库。

**show_metadata**
> 显示某本书已存储的元数据。

**set_metadata**
> 从 OPF 文件或单个字段更新图书元数据。

**export**
> 将图书及其关联文件导出到文件系统。

**add_format**
> 为已有图书附加一个电子书文件格式。

**remove_format**
> 从图书中移除指定格式。

**catalog**
> 生成格式化的书库目录。

**backup_metadata**
> 将元数据导出为单独的 OPF 文件。

**restore_database**
> 从 OPF 元数据文件重建数据库。

**check_library**
> 校验书库文件系统的完整性。

**clone**
> 创建一个具有相同自定义列和设置的空书库。

**embed_metadata**
> 根据数据库记录更新书籍文件的元数据。

**fts_index**
> 管理全文搜索索引。

**fts_search**
> 在书库内容中执行全文搜索。

# PARAMETERS

**--library-path** _path_
> Calibre 书库路径（包含 metadata.db 的目录）。

**--with-library** _url_
> 连接到 Calibre 内容服务器（如 http://localhost:8080）。

**--username** _user_
> 内容服务器验证用的用户名。

**--password** _pass_
> 内容服务器验证用的密码。

**--timeout** _seconds_
> 网络连接超时时间，单位秒（默认：120）。

**-f**, **--field** _name:value_
> 设置元数据字段（与 set_metadata 配合使用）。

**--as-opf**
> 以 OPF XML 格式输出元数据。

**--for-machine**
> 以 JSON 格式输出（便于机器读取）。

# CAVEATS

图书 ID 可通过 **list** 或 **search** 命令查找。含空格的参数必须加引号。macOS 上，命令行工具位于 calibre.app 包内的 `/Applications/calibre.app/Contents/MacOS/`。在本地书库上使用 calibredb 时不应同时运行 Calibre 图形界面，或者改用 **--with-library** 通过内容服务器连接。

# HISTORY

**calibredb** 是 **calibre** 的一部分。calibre 是由 **Kovid Goyal** 创建的电子书管理应用，首次发布于 **2006** 年。

# SEE ALSO

[calibre](/man/calibre)(1), [ebook-convert](/man/ebook-convert)(1), [ebook-meta](/man/ebook-meta)(1), [calibre-server](/man/calibre-server)(1)
