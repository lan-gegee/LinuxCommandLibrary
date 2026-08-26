# TAGLINE

基于终端的参考文献管理器

# TLDR

**启动** TUI

```cobib```

**初始化**一个带 git 跟踪的新数据库

```cobib init --git```

通过 DOI **添加**条目

```cobib add --doi [10.1234/example]```

通过 arXiv ID **添加**条目

```cobib add --arxiv [1701.08213]```

从 BibTeX 文件**导入**条目

```cobib import --bibtex [references.bib]```

按年份排序**列出**条目

```cobib list --sort year --reverse --limit 20```

使用过滤器**不区分大小写地搜索**

```cobib search --ignore-case "[quantum]" -- ++year [2024]```

**导出**为 BibTeX

```cobib export --bibtex [output.bib]```

# SYNOPSIS

**cobib** [**-c** _CONFIG_] [**-v**] [_COMMAND_] [_ARGS_...]

# PARAMETERS

**-c**, **--config** _CONFIG_
> 配置文件路径。

**-v**, **--verbose**
> 增加详细输出。

# SUBCOMMANDS

**init** [**--git**]
> 初始化数据库。使用 **--git** 启用 git 跟踪。

**add** [**--doi**|**--arxiv**|**--isbn**|**--bibtex**|**--url**|**--yaml** _SOURCE_] [**-l** _LABEL_] [**-f** _FILE_]
> 从各种来源添加新的文献条目。

**list** [**-s** _FIELD_] [**-r**] [**-l** _N_] [**-i**] [**-z** _N_] [_FILTER_...]
> 列出并过滤数据库条目。过滤器使用 **++FIELD** VALUE 表示包含，或 **--FIELD** VALUE 表示排除。

**search** [**-c** _N_] [**--skip-files**] _QUERY_ [**--** _FILTER_...]
> 使用正则表达式模式搜索条目。

**show** _LABEL_
> 以 BibTeX 格式显示单个条目。

**edit** _LABEL_
> 在编辑器中编辑条目。

**delete** [**-y**] _LABEL_...
> 删除条目。使用 **-y** 跳过确认。

**open** _LABEL_
> 打开条目关联的文件。

**export** **--bibtex**|**--zip** [**--** _FILTER_...]
> 将条目导出为 BibTeX 或 ZIP 归档。

**import** **--bibtex** _FILE_
> 从 BibTeX 文件批量导入条目。

**review** [_FILTER_...]
> 条目的交互式审阅工作流。

**note** _LABEL_
> 打开/编辑条目的笔记。

**undo** / **redo**
> 撤销/重做数据库更改（需要启用 git 集成）。

**git** [_ARGS_...]
> 透传给 git，作用于数据库仓库。

**lint**
> 校验并检查数据库条目。

# DESCRIPTION

**cobib**（Console Bibliography）是一款参考文献管理工具，将参考文献存储在纯文本 YAML 数据库中。它同时提供命令行界面和基于 Textual 框架构建的 TUI。该工具支持从 arXiv、DOI、ISBN、BibTeX、URL 和 YAML 来源导入参考文献，并可自动下载 PDF。数据库可以用 git 进行跟踪以实现版本控制，从而支持撤销/重做操作。搜索支持正则表达式、模糊匹配、LaTeX 和 Unicode 解码，以及通过 ripgrep-all 进行的 PDF 全文搜索。插件系统允许自定义命令、导入器、导出器和解析器。

# CONFIGURATION

配置保存在 **~/.config/cobib/config.py**（Python 文件）。可用 **-c** 标志或 **COBIB_CONFIG** 环境变量覆盖。使用 **cobib _example_config** 可生成示例配置。

# CAVEATS

需要 Python 3.10 或更高版本。Windows 支持尚属实验性；建议使用 WSL。模糊匹配需要可选的 **regex** 依赖。PDF 全文搜索需要 **ripgrep-all**（rga）。撤销/重做命令需要启用 git 集成。

# HISTORY

**cobib** 由 **Max Rossmannek** 于 **2019 年 6 月**创建，旨在成为 Mendeley、Zotero 等文献管理器的易用替代品。采用 Python 编写，MIT 许可证发布。4.0 版引入了基于 Textual 构建的 TUI。最新版本为 6.0.1（2025 年 10 月），拥有超过 1420 次提交和 66 个发布版本。

# INSTALL

```aur: yay -S cobib```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bibtex](/man/bibtex)(1), [papis](/man/papis)(1), [zotero](/man/zotero)(1)
