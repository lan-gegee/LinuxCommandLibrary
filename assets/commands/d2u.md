# TAGLINE

DOS 到 Unix 行尾转换器

# TLDR

**将文件**的行尾从 DOS 转换为 Unix 格式

```d2u [file.txt]```

**转换多个文件**

```d2u [file1.txt] [file2.txt] [file3.txt]```

**转换并保留原文件的备份**

```d2u -b [file.txt]```

**使用自定义备份后缀**进行转换

```d2u -b -e [.bak] [file.txt]```

**转换为新文件**而非原地修改

```d2u -n [input.txt] [output.txt]```

**静默地原地转换文件**

```d2u -q [file.txt]```

# SYNOPSIS

**d2u** [_options_] [_file_...]

# PARAMETERS

_FILE_
> 要转换的文件。默认原地转换。

**-b**, **--backup**
> 保留原文件的备份。

**-e** _SUFFIX_, **--extension** _SUFFIX_
> 备份文件的扩展名（默认：.bak）。

**-n**, **--newfile** _infile_ _outfile_
> 转换 infile 并写入 outfile（新文件模式）。

**-q**, **--quiet**
> 安静模式，不输出信息。

**-k**, **--keepdate**
> 保留原文件的时间戳。

**-f**, **--force**
> 即使是二进制文件也强制转换。

**-l**, **--newline**
> 在每个转换后的换行符后再追加一个换行符。

**-o**, **--oldfile**
> 原地转换模式（默认）。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**d2u** 将文本文件的行尾从 DOS/Windows 格式（CRLF，回车 + 换行）转换为 Unix 格式（仅 LF）。它是 **dos2unix** 工具的别名或替代名称。

该工具默认原地修改文件，便于批量转换。它会自动检测二进制文件并跳过，除非强制指定。单条命令即可处理多个文件。

在将文本文件从 Windows 传输到 Unix/Linux 系统，或处理因版本控制系统而混用行尾的文件时，通常需要进行这种转换。

# CAVEATS

二进制文件被转换后可能损坏；工具会尝试检测并跳过它们。不带备份的原地转换可能丢失原始数据。某些文件中的 CRLF 序列是有意为之，不应被转换。

# HISTORY

d2u 通常是 **dos2unix** 的别名，后者作为标准 Unix 工具已存在数十年。行尾转换的需求源于 20 世纪 70 年代末和 80 年代 CP/M、DOS 与 Unix 采用的不同约定。

# SEE ALSO

[dos2unix](/man/dos2unix)(1), [unix2dos](/man/unix2dos)(1), [u2d](/man/u2d)(1), [tr](/man/tr)(1)
