# TAGLINE

处理 roff 源文件中的 .so 包含

# TLDR

**处理文件中的 .so 请求**

```zsoelim [file.man]```

**从 stdin 处理**

```cat [file.man] | zsoelim```

**处理压缩的 man page**

```zcat [file.man.gz] | zsoelim```

# SYNOPSIS

**zsoelim** [**-CVh**] [_file_...]

# PARAMETERS

**-C**, **--compatible**
> 允许 .so 请求后面跟非空白字符

**-V**, **--version**
> 显示版本信息

**-h**, **--help**
> 显示帮助信息

# DESCRIPTION

**zsoelim** 用于处理 roff/man page 源文件中的 **.so** 请求。**.so** 指令会把另一个文件的内容包含进来，类似 C 语言的 #include。

当 man page 中出现 **.so man3/other.3** 这样的行时，zsoelim 会读取被引用文件的内容并加以替换。man page 系统用它来避免为命令别名重复编写文档。

"z" 前缀表示支持 gzip 压缩的输入文件，这在 man page 系统中很典型，因为源文件可能以压缩形式存储。

zsoelim 会在标准 man page 目录层级中搜索被包含的文件，并进行递归处理。

# CAVEATS

主要作为 man page 处理流水线的一环使用，很少被直接调用。

.so 指令中的文件路径是相对于 man 目录结构的，而非当前目录。

该工具要求输入为 roff/man page 格式。它不是通用的文件包含工具。

# SEE ALSO

[soelim](/man/soelim)(1), [man](/man/man)(1), [groff](/man/groff)(1), [zcat](/man/zcat)(1)
