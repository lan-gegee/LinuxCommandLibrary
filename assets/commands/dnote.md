# TAGLINE

多设备 CLI 笔记本，用于记录命令、代码片段和笔记

# TLDR

向笔记本**添加**笔记（会打开配置的编辑器）

```dnote add [book_name]```

以**内联内容**添加笔记

```dnote add [book_name] -c "[note content]"```

**列出**所有笔记本，或某个笔记本中的笔记

```dnote view
dnote view [book_name]```

**搜索**笔记（全文检索）

```dnote find "[keywords]"```

按 ID **编辑**笔记

```dnote edit [note_id]```

**移除**一条笔记或整个笔记本

```dnote remove [note_id|book_name]```

与 Dnote 服务器**同步**笔记

```dnote sync```

# SYNOPSIS

**dnote** _command_ [_options_] [_args_]

# PARAMETERS

**add** _book_ [**-c** _content_]
> 向 _book_ 添加笔记（别名：**a**、**n**、**new**）。省略内容时打开编辑器；也接受 stdin 输入。

**view** [_book_ [_index_]]
> 列出笔记本、某笔记本中的笔记或特定笔记（别名：**v**）

**edit** _note-id_|_book_
> 编辑笔记或重命名笔记本（别名：**e**）。**--book** 移动笔记；**--name** 重命名笔记本

**remove** _note-id_|_book_
> 删除笔记或笔记本（别名：**rm**、**d**、**delete**）。**-y** 跳过确认

**find** _keywords_
> 全文检索；**-b** _book_ 限定范围（别名：**f**）

**sync**
> 与已配置的 Dnote 服务器同步（**--full** 表示完整同步）

**login** / **logout**
> 登录或退出 Dnote 服务器

**--dbPath** _path_
> 使用自定义 SQLite 数据库路径，而非 XDG data 下的默认位置

# DESCRIPTION

**dnote** 是一款命令行笔记本，用于将简短的笔记、命令和代码片段整理到不同的**笔记本（books）**中。笔记本地存储在 SQLite 中，也可以选择同步到自建或托管的 Dnote 服务器，实现多设备访问。

内容可以通过系统编辑器、**-c** 参数或 stdin 输入（便于把命令输出管道传入笔记本）。搜索支持跨笔记的全文检索。Linux 上默认数据库路径通常位于 **~/.local/share/dnote/** 下。

# CONFIGURATION

编辑器和 API 端点的设置保存在 CLI 所用的 Dnote 配置文件中。可用 **--dbPath** 覆盖数据库位置。在 **dnote sync** 之前，先用 **dnote login** 配合 **--apiEndpoint** 指定自建服务器。

# SEE ALSO

[nb](/man/nb)(1), [zk](/man/zk)(1)

# RESOURCES

```[Homepage](https://www.getdnote.com)```

```[Documentation](https://www.getdnote.com/docs/cli/commands/)```

```[Source code](https://github.com/dnote/dnote)```

<!-- verified: 2026-07-14 -->

# INSTALL

```brew: brew install dnote```

```nix: nix profile install nixpkgs#dnote```

<!-- packages: 2026-07-22 -->
