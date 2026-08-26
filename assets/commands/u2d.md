# TAGLINE

将 Unix 换行符转换为 DOS 格式

# TLDR

**将文件**从 Unix 换行符转换为 DOS 换行符

```u2d [path/to/file]```

**转换多个文件**

```u2d [file1] [file2] [file3]```

**转换并保留修改日期**

```u2d -k [path/to/file]```

**仅在文件看起来是文本时转换**（跳过二进制文件）

```u2d -s [path/to/file]```

**转换并写入新文件**

```u2d -n [input_file] [output_file]```

# SYNOPSIS

**u2d** [**-k**] [**-s**] [**-n** _infile_ _outfile_] [_file_...]

# PARAMETERS

**-k**, **--keepdate**
> 转换后保留文件的原修改日期。

**-o**, **--oldfile**
> 就地转换，覆盖原文件。这是默认行为。

**-n**, **--newfile** _infile_ _outfile_
> 将转换结果写入新文件，而不是修改原文件。

**-s**, **--safe**
> 跳过二进制文件的转换，以防损坏。

**-q**, **--quiet**
> 安静模式。不输出提示信息。

**-V**, **--version**
> 显示版本信息。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**u2d**（Unix to DOS）将文本文件的换行符从 Unix 风格转换为 DOS/Windows 风格。Unix 文件使用单个换行符（LF，\n）表示换行，而 DOS/Windows 文件使用回车加换行（CRLF，\r\n）。

该命令通常是指向 **unix2dos** 的符号链接或别名。默认情况下它就地处理文件，用转换后的版本替换原文件。可以在命令行中指定多个文件进行批量转换。

在 Unix/Linux 和 Windows 系统之间传输文本文件时需要进行这种转换，因为许多 Windows 应用程序期望 CRLF 换行符，如果文件只包含 LF 结尾符，它们可能无法正确显示或处理。

# CAVEATS

转换二进制文件会使其损坏。使用 **-s** 选项自动跳过二进制文件，或确保只转换文本文件。默认就地修改文件；要保留原文件请使用 **-n**。某些发行版可能不带 u2d；可改用 unix2dos 或安装 dos2unix 软件包。

# HISTORY

自 **20 世纪 80 年代** Unix 与 DOS 系统之间开始传输文件起，就出现了各种换行符转换工具。提供 u2d 和 d2u 的 **dos2unix/unix2dos** 软件包最初是为 SunOS/Solaris 编写的，后来被移植到多种类 Unix 系统。存在多个不同名称的实现，包括 todos/fromdos、flip 和 endlines。

# SEE ALSO

[d2u](/man/d2u)(1), [dos2unix](/man/dos2unix)(1), [unix2dos](/man/unix2dos)(1), [tr](/man/tr)(1), [sed](/man/sed)(1)
