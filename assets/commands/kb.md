# TAGLINE

极简的命令行知识库管理器

# TLDR

向知识库**添加新笔记**

```kb add "[title]" -c "[category]"```

**列出所有笔记**

```kb list```

**按类别过滤列出笔记**

```kb list -c "[category]"```

按标题或内容**搜索笔记**

```kb grep "[pattern]"```

**查看指定笔记**

```kb view "[title]"```

**编辑笔记**

```kb edit "[title]"```

**删除笔记**

```kb delete "[title]"```

**导出知识库**

```kb export```

# SYNOPSIS

**kb** _command_ [_options_] [_arguments_]

# SUBCOMMANDS

**add**
> 添加新笔记（用 `-t` 从文件添加，或打开 `$EDITOR`）。

**list**
> 列出笔记；可用 `-c`（类别）、`-t`（标签）或 `-v`（详细模式）过滤。

**view**
> 显示笔记内容。

**edit**
> 在 `$EDITOR` 中打开笔记。

**grep**
> 跨笔记进行全文搜索。

**delete**
> 删除笔记（使用 `--id` 可按数字 ID 定位）。

**update**
> 修改已有笔记的元数据（标题、类别、标签）。

**import** / **export**
> 以 `.kb.tar.gz` 归档的形式将笔记移入或移出知识库。

**erase**
> 确认后清空整个知识库。

# COMMON OPTIONS

**-c** _CATEGORY_
> 笔记所属类别。

**-t** _TAGS_
> 分号分隔的标签列表（如 `linux;networking`）。

**-g** _PATTERN_
> Glob 匹配模式（配合 list 使用）。

**--no-color**
> 在输出中禁用 ANSI 颜色。

# DESCRIPTION

**kb** 是一个面向文本的极简命令行知识库管理器，专为软件开发者、渗透测试人员、学生以及任何需要高效收集和整理笔记的人设计。它支持笔记的分类、打标签和全文搜索。

虽然主要面向文本笔记的收集，kb 也支持图片、PDF 和视频等非文本文件。笔记可以按标题、类别、标签和其他元数据过滤。

# CAVEATS

需要 Python 3.6 或更高版本。知识库数据存储在本地。没有内置的跨设备同步功能。

# HISTORY

**kb** 由 **gnebbia** 创建，用 **Python** 编写。它被设计为一个快速的笔记收集和检索工具，注重简洁和高效。

# INSTALL

```nix: nix profile install nixpkgs#kb```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tldr](/man/tldr)(1), [cheat](/man/cheat)(1), [nb](/man/nb)(1)
