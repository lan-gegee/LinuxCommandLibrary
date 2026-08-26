# TAGLINE

用于自动文本压缩的开放文本摘要器（Open Text Summarizer）

# TLDR

将文本文件**摘要**为默认的 20%

```ots [path/to/file.txt]```

将文件**摘要**为指定的**百分比**

```ots -r [10] [path/to/file.txt]```

**摘要**并保存到**输出文件**

```ots -r [15] -o [summary.txt] [path/to/file.txt]```

**生成**带高亮句子的 **HTML** 摘要

```ots --html --out=[summary.html] [path/to/file.txt]```

**提取**关键词和主题信息

```ots --about [path/to/file.txt]```

使用特定的**语言**词典进行**摘要**

```ots --dic=[de] [path/to/file.txt]```

从 **stdin** 进行**摘要**

```cat [path/to/file.txt] | ots -r [10]```

# SYNOPSIS

**ots** [_OPTIONS..._] [_file.txt_ | _stdin_]

# PARAMETERS

**-r** _INT_, **--ratio=**_INT_
> 摘要百分比；以输入长度的百分比设定输出长度。默认：**20**。

**-o** _FILE_, **--out=**_FILE_
> 输出文件路径。默认：stdout。

**-h**, **--html**
> 以 HTML 输出并高亮重要句子

**-a**, **--about**
> 仅输出关键词和主题提取（适合生成 meta 标签内容）

**-d** _STRING_, **--dic=**_STRING_
> 指定自定义词典/语言文件，用于停用词过滤

**-v**, **--version**
> 显示版本信息

**-?**, **--help**
> 显示帮助/用法信息

# DESCRIPTION

**ots**（Open Text Summarizer）是一款自动文本摘要工具，它读取文档、判断哪些句子最重要，然后生成精简版本。它执行的是**抽取式摘要**——选取并保留原句，而不是生成新的文字。

该工具分三个阶段工作：首先使用基于 XML 的语言词典**过滤**常见停用词，然后进行**词频分析**，按重要词的密度为句子打分，最后应用基于 Porter 词干算法的**语言学精炼**来归组词形变体。它通过 XML 词典文件支持 **37 种以上语言**。

输出可以是纯文本，也可以是高亮了重要句子的 HTML。

# CAVEATS

OTS 只做抽取式摘要，不会生成新的文字。它最适合结构良好的非虚构散文，如新闻文章和技术文档；对小说、短文本、列表和要点条目效果较差。Porter 词干器准确率约为 90%，可能遗漏词形变体，尤其是在非英语语言中。最后一个正式版本（0.5.0）发布于 **2007 年**，此后代码库再无活跃的功能开发。

# HISTORY

OTS 由 **Nadav Rotem** 自 **2003 年 4 月**起开发，0.1.0 版于 2003 年 5 月发布。到 2003 年 7 月语言支持扩展至 **24 种**，最终超过 37 种。它获得了学术界的认可，在至少四篇论文中被引用。该库作为插件集成进了 **AbiWord** 和 **gedit**。最新版本是 2007 年 4 月的 **0.5.0**。它至今仍被打包收录在 Debian、Ubuntu、Fedora 等发行版中。

# INSTALL

```apt: sudo apt install ots```

```dnf: sudo dnf install ots```

```brew: brew install ots```

```nix: nix profile install nixpkgs#ots```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wc](/man/wc)(1), [less](/man/less)(1), [fmt](/man/fmt)(1)
