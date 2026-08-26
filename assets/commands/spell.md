# TAGLINE

经典的 Unix 拼写检查工具

# TLDR

**检查文件拼写**

```spell [file.txt]```

**从 stdin 检查拼写**

```echo "[text to check]" | spell```

**按英式拼写规则检查**

```spell -b [file.txt]```

**使用自定义词表**作为附加词典

```spell +[custom_words.txt] [file.txt]```

**显示所有不在词典中的词**，包括看似合理的派生词

```spell -v [file.txt]```

**使用指定的词典**文件

```spell -d [path/to/dictionary] [file.txt]```

**检查多个文件**

```spell [file1.txt] [file2.txt]```

# SYNOPSIS

**spell** [_options_] [**+**_local_file_] [_file_...]

# PARAMETERS

**-b**, **--british**
> 使用英式拼写规则（colour, centre, -ise 结尾）

**-v**, **--verbose**
> 打印所有字面上不在词典中的词，包括看似合理的派生词

**-d**, **--dictionary**=_FILE_
> 使用 FILE 作为查词词典

**-i**, **--ispell**=_PROGRAM_
> 将 PROGRAM 作为 Ispell 调用（默认：ispell）

**-n**, **--number**
> 在每行前打印行号

**-o**, **--print-file-name**
> 在每行前打印文件名

**-l**, **--all-chains**
> 跟踪被包含文件的链（仅为兼容性保留）

**+**_local_file_
> 使用附加词表；在此文件中找到的词不会被报告为拼写错误

**-h**, **--help**
> 打印选项摘要

**-V**, **--version**
> 打印版本号

# DESCRIPTION

**spell** 是一款经典的 Unix 拼写检查工具，用于报告拼写错误的单词。它从文件（未指定时从 stdin）读取文本，在词典中查找每个单词，并输出未找到或无法由已知单词派生出的词。

与 **aspell** 或 **ispell** 等现代拼写检查器不同，spell 不提供纠正建议，也没有交互式界面。它只是将无法识别的单词列出并输出到标准输出，因此适合脚本编写和批处理。

**-v** 选项显示那些可以派生出来但字面上不在词典中的词。可以用 **+filename** 指定自定义词表，为系统词典补充领域专用或技术术语。

在大多数现代 Linux 发行版上，**spell** 命令由 GNU spell 提供，它是 **ispell** 的一个包装器。传统的 Unix spell 还有一些额外选项（如用于打印词干的 **-x**），GNU 版本为保持兼容而忽略它们。

# CAVEATS

spell 不提供拼写建议，也没有交互式纠错功能。专有名词、技术术语和缩写可能被误报为拼写错误。词典覆盖范围因发行版而异。如需更完善的拼写检查，可考虑 **aspell** 或 **ispell**。

# HISTORY

**spell** 由贝尔实验室的 **Stephen C. Johnson** 开发，于 **1975 年**随 **Version 6 Unix** 首次亮相。它是最早的文本处理工具之一，帮助确立了 Unix 作为文档准备系统的地位。该命令基本保持原样，延续了其简单的基于过滤器的设计哲学。

# INSTALL

```apt: sudo apt install spell```

```apk: sudo apk add aspell-compat```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aspell](/man/aspell)(1), [ispell](/man/ispell)(1), [hunspell](/man/hunspell)(1), [look](/man/look)(1)
