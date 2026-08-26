# TAGLINE

统计 PO 文件中的翻译统计数据

# TLDR

**统计翻译数据**

```pocount [file.po]```

**统计多个文件**

```pocount [*.po]```

**短格式输出**

```pocount --short [file.po]```

**CSV 输出**

```pocount --csv [file.po]```

# SYNOPSIS

**pocount** [_options_] [_files_]

# PARAMETERS

_FILES_
> PO 翻译文件。

**--short**
> 简短摘要格式。

**--csv**
> CSV 输出格式。

**--incomplete**
> 仅显示未完成的文件。

**--full**
> 完整详细输出。

# DESCRIPTION

**pocount** 统计 PO（Portable Object）文件中的翻译数据，报告已翻译、模糊（fuzzy）和未翻译的字符串及单词数量。它为本地化项目提供翻译进度的快速概览。

输出可格式化为简短摘要（**--short**）、CSV（**--csv**）或完整详情（**--full**）。**--incomplete** 标志只显示仍需翻译工作的文件。它是 **translate-toolkit** 套件的一部分。

# CAVEATS

需要 PO 格式的文件。是 translate-toolkit 的一部分。

# HISTORY

pocount 作为 **translate-toolkit** 的一部分创建，用于翻译统计。

# SEE ALSO

[msgfmt](/man/msgfmt)(1), [pofilter](/man/pofilter)(1), [gettext](/man/gettext)(1)
