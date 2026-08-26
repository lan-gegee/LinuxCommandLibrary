# TAGLINE

为源代码文件构建标识符数据库，支持快速搜索

# TLDR

为当前目录构建 **ID 数据库**

```mkid```

为**指定目录**构建 ID 数据库

```mkid [path/to/directory1] [path/to/directory2]```

构建 ID 数据库并**保存到指定文件**

```mkid -o [path/to/database.id]```

只包含**特定语言**

```mkid -i "C C++"```

在索引时**排除指定文件或目录**

```mkid -p [.git]```

构建数据库后显示**统计信息**

```mkid -s```

# SYNOPSIS

**mkid** [**-o** _outfile_] [**-i** _langs_] [**-x** _langs_] [**-p** _names_] [**-s**] [**-v**] [_file_...]

# PARAMETERS

**-o, --output _outfile_**
> 指定输出的数据库文件；默认为当前目录下的 ID

**-f, --file _outfile_**
> --output 的别名

**-i, --include _langs_**
> 只包含指定的语言；默认为 C、C++、asm

**-x, --exclude _langs_**
> 在索引中排除指定的语言

**-m, --lang-map _mapfile_**
> 使用自定义的文件名到语言映射

**-d, --default-lang _lang_**
> 为无法识别的文件设置默认语言

**-p, --prune _names_**
> 扫描时跳过指定的文件和目录

**--files0-from _file_**
> 从指定文件读取文件列表（以 NUL 结尾）

**-v, --verbose**
> 显示每个文件的处理统计信息

**-s, --statistics**
> 完成后显示汇总统计信息

# DESCRIPTION

**mkid** 为源代码文件构建标识符数据库，配合 **lid**、**gid** 及其他 GNU idutils 工具实现快速搜索。它扫描源文件，提取标识符（函数名、变量、宏），并将其存入一个紧凑的数据库。

该工具递归处理目录，识别多种编程语言，包括 C、C++、汇编、Perl 和纯文本。其数据库格式针对后续搜索的查找速度做了优化。

# CAVEATS

--include 与 --exclude 选项互斥。大型代码库初次建库可能需要大量时间和内存。源文件变更后必须重建数据库才能反映当前的标识符。

# HISTORY

**mkid** 属于 **GNU idutils**，最初由 Greg McGary 编写。该软件包提供构建和查询标识符数据库的工具，面向大规模软件开发。自 20 世纪 90 年代初起它就是 GNU 项目的一部分。

# SEE ALSO

[lid](/man/lid)(1), [grep](/man/grep)(1), [ctags](/man/ctags)(1)
