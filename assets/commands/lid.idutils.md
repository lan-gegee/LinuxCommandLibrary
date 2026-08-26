# TAGLINE

查询 ID 数据库以查找与指定模式匹配的标记

# TLDR

列出 ID 数据库中的所有**标记及其所在文件位置**

```lid```

查找**包含特定标记的文件**

```lid [token]```

查找与模式匹配且**忽略大小写**的标记

```lid -i [token]```

查找与**扩展正则表达式**匹配的标记

```lid -r "[pattern]"```

以 **grep 风格格式**输出匹配行

```lid -R grep [token]```

查找**只出现一次**的标记（用于找出未使用的定义）

```lid -F 1```

# SYNOPSIS

**lid** [_options_] [_pattern_]

# PARAMETERS

**-f _filename_**
> 指定要读取的 ID 数据库文件

**-i, --ignore-case**
> 执行不区分大小写的模式匹配

**-l, --literal**
> 将模式视为字面字符串（不使用正则表达式）

**-r, --regexp**
> 强制进行正则表达式模式匹配

**-w, --word**
> 仅匹配完整单词（非子串搜索）

**-s, --substring**
> 执行子串搜索

**-k _style_**
> 控制输出格式：token、pattern 或 none

**-R, --result _style_**
> 控制结果类型：filenames、grep（显示行）、edit（在编辑器中打开）或 none

**-F, --frequency _range_**
> 按出现频率匹配标记（例如 1 表示只出现一次的标记）

# DESCRIPTION

**lid** 查询 ID 数据库以查找与指定模式匹配的标记。它是 GNU **idutils** 的一部分，通过搜索预先构建的标记数据库，快速定位源文件中的标识符。

必须先用 **mkid** 命令构建 ID 数据库。该数据库为源文件中发现的所有标记（标识符、关键字、字符串）建立索引，从而无需重新扫描整个代码库即可快速查找。

模式的解释方式很灵活：如果模式包含正则表达式元字符，lid 会执行正则子串搜索；否则进行字面单词搜索。若未给出模式，则列出数据库中的所有条目。

# CAVEATS

需要先用 **mkid** 创建预构建的 ID 数据库。源文件变更后必须重新生成数据库才能反映当前内容。默认情况下，lid 会在当前目录及其父目录中查找名为 **ID** 的文件。

# HISTORY

lid 命令是 **GNU idutils** 的一部分，最初由 Greg McGary 编写。idutils 软件包自 20 世纪 90 年代初以来一直作为 GNU 项目的一部分维护，提供高效的源代码索引和搜索功能。

# SEE ALSO

[mkid](/man/mkid)(1), [grep](/man/grep)(1)
