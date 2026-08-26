# TAGLINE

开源文献管理软件

# TLDR

**启动 Zotero**

```zotero```

**打开指定配置文件**

```zotero -P [profile_name]```

**通过配置文件管理器打开**

```zotero -ProfileManager```

**从文件导入**

```zotero -import [file.bib]```

**在 Zotero 中打开 URL**

```zotero zotero://select/library/items/[ITEM_KEY]```

# SYNOPSIS

**zotero** [_options_] [_URL_]

# PARAMETERS

**-P** _profile_
> 以指定的配置文件启动

**-ProfileManager**
> 启动时打开配置文件管理器

**-import** _file_
> 从指定文件导入

**-url** _url_
> 打开指定的 URL

**-jsconsole**
> 打开 JavaScript 控制台

**-purgecaches**
> 启动时清除所有缓存

**-ZoteroDebugText**
> 启用向终端输出的调试信息

**--help**
> 显示帮助信息

# DESCRIPTION

**Zotero** 是一款自由开源的文献管理软件。它帮助你收集、整理、引用和分享研究资料，包括论文、书籍、报告、网页等。

主要特性：
- 从数据库、图书馆目录和网页导入参考文献
- 用分类、标签和保存的搜索组织条目
- 以多种格式生成引文和参考文献列表
- 通过 Zotero 账户在多设备间同步文库
- 通过共享群组文库协作

Zotero 与文字处理软件（Word、LibreOffice、Google Docs）集成，可在文档中插入引文并自动生成参考文献列表。

数据默认存储在本地，云同步为可选功能。浏览器连接器可以直接从网页抓取参考文献。

# CAVEATS

存储同步（针对 PDF）的免费配额有限。可通过 WebDAV 自行托管。

某些出版商网站需要特定的浏览器连接器配置才能正确抓取元数据。

附件众多的大型文库可能占用大量磁盘空间。

离线访问需要先将文库数据同步到本地。

# INSTALL

```apk: sudo apk add zotero```

```nix: nix profile install nixpkgs#zotero```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jabref](/man/jabref)(1), [mendeley](/man/mendeley)(1), [papis](/man/papis)(1)
