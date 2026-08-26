# TAGLINE

带 CLI 和 TUI 的快速本地书签管理器

# TLDR

**启动**交互式 TUI

```bmm```

**添加**新书签

```bmm add "[url]" --title "[title]" --tags "[tag1,tag2]"```

按关键词**搜索**书签

```bmm search "[query]"```

**列出**所有书签

```bmm list```

按 ID **删除**书签

```bmm delete [id]```

从文件**导入**书签

```bmm import [path/to/file]```

# SYNOPSIS

**bmm** [_command_] [_options_]

# PARAMETERS

**add** _URL_
> 添加新书签，可选设置标题和标签。

**search** _QUERY_
> 按标题、URL 或标签搜索书签。

**list**
> 列出所有已保存的书签。

**delete** _ID_
> 按 ID 删除书签。

**import** _FILE_
> 从文件导入书签。

**export** _FILE_
> 将书签导出到文件。

**--title** _TEXT_
> 设置书签标题。

**--tags** _TAGS_
> 书签的标签，以逗号分隔。

# DESCRIPTION

**bmm** 是一款快速的本地优先书签管理器，同时提供命令行界面和交互式终端用户界面。书签存储在本地，无需依赖云服务或浏览器即可快速搜索、打标签和组织。

TUI 模式提供交互式的模糊搜索界面，用于浏览和管理书签。书签可以添加标签以便分类，也可以导出用于备份或分享。

# CAVEATS

书签存储在本地，默认不在多台设备间同步。导入格式可能仅限特定文件类型。

# INSTALL

```nix: nix profile install nixpkgs#bmm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[buku](/man/buku)(1), [nb](/man/nb)(1)
