# TAGLINE

报告并转换文本文件中的行尾字符

# TLDR

**报告文件的换行符风格**

```eol [file.txt]```

**转换为 Unix 风格**（LF）

```eol -c LF [file.txt]```

**转换为 Windows 风格**（CRLF）

```eol -c CRLF [file.txt]```

**转换为本平台原生**风格

```eol -c native [file.txt]```

**递归查找**带 DOS 换行符的文件

```eol -r -f dos [path]```

扫描时**跳过某个目录**

```eol -r -x .git [path]```

# SYNOPSIS

**eol** [_options_] _path_...

# PARAMETERS

**-c**, **--convert** _NAME_
> 将文件转换为指定的换行符风格。_NAME_ 为 LF、CRLF、CR、NATIVE 之一（别名：unix、dos/windows、mac、native——不区分大小写）。

**-f**, **--find** _NAME_
> 列出具有指定换行符风格的文件。接受与 `-c` 相同的名称，外加 NONE 和 MIXED。

**-r**, **--recursive**
> 递归遍历目录（默认关闭）。

**-x**, **--skip** _PATTERN_
> 跳过匹配 _PATTERN_ 的文件或目录（如 `.git`、`*.pyc`）。

**-v**, **--verbose**
> 显示调试级别的输出。

**-q**, **--quiet**
> 只显示警告和错误。

**--test**
> 运行工具的自检测试后退出。

**-h**, **--help**
> 显示帮助。

# DESCRIPTION

**eol** 是一个命令行脚本（也是 Python 模块），用于检查和转换文本文件中的行尾字符。不带动作标志时，它会报告每个文件检测到的换行符风格（Unix/LF、Windows/CRLF、经典 Mac/CR、混合或无）。

使用 `-c` 将文件改写为选定风格，或用 `-f` 定位已经采用某种风格的文件。除非给出 `-r`，否则不会递归遍历目录。二进制文件默认会被检测出来并跳过。

# CAVEATS

转换会就地重写文件；请保留备份或使用版本控制。对换行符混杂的文件执行 `-c` 时会统一为目标风格。这是 **trentm/eol** Python 工具；其他发行版中同名 _eol_ 的程序与本工具无关。

# HISTORY

**eol** 由 **Trent Mick** 编写，以 `eol` 包的形式发布在 PyPI 上。该项目自 2000 年代后期起一直在 GitHub 上维护。

# SEE ALSO

[dos2unix](/man/dos2unix)(1), [unix2dos](/man/unix2dos)(1), [file](/man/file)(1), [tr](/man/tr)(1)
