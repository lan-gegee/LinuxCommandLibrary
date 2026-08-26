# TAGLINE

合并 PDF 文件

# TLDR

**合并 PDF**

```pdfjoin [file1.pdf] [file2.pdf]```

**以指定输出名合并**

```pdfjoin -o [output.pdf] [file1.pdf] [file2.pdf]```

**合并指定页面**

```pdfjoin [file.pdf] [1-5] [file2.pdf] [2,4,6]```

**合并目录中的所有 PDF**

```pdfjoin [*.pdf]```

**不旋转超尺寸页面**

```pdfjoin --rotateoversize false [file1.pdf] [file2.pdf]```

# SYNOPSIS

**pdfjoin** [_-o output_] [_options_] _file1_ [_pages_] _file2_ [_pages_] ...

# PARAMETERS

**-o** _FILE_
> 输出文件名。

**--rotateoversize** _BOOL_
> 旋转超出纸张尺寸的页面。

**--paper** _SIZE_
> 纸张大小（a4、letter）。

**--landscape**
> 横向方向。

**--tidy**
> 删除临时文件。

**--**
> 选项结束。

# DESCRIPTION

**pdfjoin** 合并 PDF 文件。它将多个 PDF 组合为一个。

属于 pdfjam 工具集。使用 LaTeX 的 pdfpages 宏包。

支持页面选择。可指定范围或单个页面。

保留 PDF 质量。不做重新压缩。

# CAVEATS

需要安装 LaTeX。属于 pdfjam 软件包的一部分。大文件可能处理较慢。

# HISTORY

**pdfjoin** 是 **pdfjam** 的一部分，这是一组基于 LaTeX 进行 PDF 操作的 shell 脚本。

# SEE ALSO

[pdfjam](/man/pdfjam)(1), [pdfunite](/man/pdfunite)(1), [gs](/man/gs)(1)
