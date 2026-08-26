# TAGLINE

用于比较表格和 CSV 文件的数据差异工具

# TLDR

**比较两个 CSV 文件并显示差异**

```daff [file1.csv] [file2.csv]```

**带彩色输出进行比较**

```daff --color [file1.csv] [file2.csv]```

**将差异输出保存到文件**

```daff --output [changes.csv] [file1.csv] [file2.csv]```

**应用补丁以更新文件**

```daff patch [file.csv] [changes.csv]```

**原地应用补丁**

```daff patch --inplace [file.csv] [changes.csv]```

**基于共同父版本进行三方合并**

```daff merge [parent.csv] [local.csv] [remote.csv]```

**将差异渲染为 HTML**

```daff render --output [diff.html] [diff.csv]```

**在格式之间复制/转换**

```daff copy [input.csv] [output.tsv]```

# SYNOPSIS

**daff** [_command_] [_options_] [_files_]

# DESCRIPTION

**daff** 是一个数据差异工具，专为比较表格数据而设计，例如 CSV 文件、数据库表和电子表格。它提供类似 git 的 diff 和 patch 操作，并针对结构化数据格式做了专门优化。

该工具可以检测新增、删除和修改的行与列，以多种格式呈现差异（包括 HTML 和彩色终端输出），并可应用补丁来更新数据文件。它特别适合跟踪数据导出、数据库转储以及协作式数据编辑流程中的变更。

# COMMANDS

_a.csv b.csv_ (default)
> 比较两个表并输出差异。

**patch** [**--inplace**] _a.csv patch.csv_
> 将补丁文件应用到表。

**merge** [**--inplace**] _parent.csv a.csv b.csv_
> 对表执行三方合并。

**render** _diff.csv_
> 将差异渲染为 HTML。

**trim** _source.csv_
> 去除表中多余的空白。

**copy** _in.csv out.tsv_
> 在表格格式之间复制并转换。

**git**
> 作为表格文件的 git diff 驱动使用。

**version**
> 显示 daff 版本。

# OPTIONS

**--color**
> 强制彩色输出（默认：自动检测）

**--no-color**
> 禁用彩色输出

**--output** _FILE_
> 将输出写入文件而非 stdout。

**--input-format** _FORMAT_
> 输入格式（例如 sqlite，用于比较数据库）。

**--www**
> 在网页浏览器中打开差异。

**--inplace**
> 直接修改输入文件（用于 patch 和 merge）。

**--unordered**
> 比较时将行视为无序。

**-h**, **--help**
> 显示帮助并退出。

# CAVEATS

数据类型根据内容推断；不支持显式的类型声明。非常大的文件可能需要大量内存。无序数据的比较需要更多计算资源。二进制数据和特殊字符在某些输出格式下可能无法正确处理。

# HISTORY

**daff** 最初由 Paul Fitzpatrick 创建，是一款面向数据版本管理与协作的工具。名字来源于 "data diff"。它有多种语言的实现，包括 JavaScript、Python 和 Java。该工具旨在把版本控制的理念引入数据文件，使跟踪数据集随时间的变化更加容易。

# SEE ALSO

[diff](/man/diff)(1), [patch](/man/patch)(1), [git](/man/git)(1), [csvlens](/man/csvlens)(1)
