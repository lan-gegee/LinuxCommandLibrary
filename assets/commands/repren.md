# TAGLINE

使用模式重命名文件并替换文本

# TLDR

按模式**重命名**

```repren --rename --from "[old]" --to "[new]" [files]```

**替换文件内容**

```repren --from "[search]" --to "[replace]" [files]```

**使用模式文件**

```repren --patterns [patterns.txt] [files]```

**预览更改**

```repren --dry-run --from "[old]" --to "[new]" [files]```

**保留大小写风格**

```repren --preserve-case --from "[foo]" --to "[bar]" [files]```

**字面字符串**

```repren --literal --from "[text]" --to "[replacement]" [files]```

# SYNOPSIS

**repren** [_--rename_] [_--from pattern_] [_--to pattern_] [_options_] _files_

# PARAMETERS

**--rename**
> 重命名文件/目录。

**--from** _PATTERN_
> 搜索模式。

**--to** _PATTERN_
> 替换模式。

**--patterns** _FILE_
> 从文件读取模式。

**--dry-run**
> 仅预览。

**--preserve-case**
> 匹配原有的大小写风格。

**--literal**
> 按字面字符串处理。

**-r**, **--recursive**
> 递归操作。

# DESCRIPTION

**repren** 是一个功能多样的批量工具，可使用正则表达式或字面模式对多个文件进行重命名和查找替换操作。它可以同时应用来自模式文件的多条替换规则，因此非常适合变量重命名、更新导入语句或重组文件结构等大规模重构任务。

其一大特性是保留大小写的替换，会自动保持原文的大小写风格。例如，把 "foo" 替换为 "bar" 时，"Foo" 会变成 "Bar"，"FOO" 会变成 "BAR"。**--dry-run** 标志可以显示所有计划的更改而不修改任何文件，便于在执行批量操作前安全地核对。

该工具通过 **--rename** 标志同时支持文件内容替换和文件/目录重命名。模式可以使用带捕获组的完整 Python 正则表达式，也可以用 **--literal** 进行直接的字符串替换。

# CAVEATS

需要 Python。复杂模式需谨慎。请备份重要文件。

# HISTORY

**repren** 作为一个多功能的重命名与替换工具而创建，支持借助模式文件完成复杂的批量操作。

# INSTALL

```brew: brew install repren```

```nix: nix profile install nixpkgs#repren```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rename](/man/rename)(1), [sed](/man/sed)(1), [perl](/man/perl)(1)
