# TAGLINE

解压/解包工具的 shell 前端

# TLDR

**解压归档文件**

```unp [archive.tar.gz]```

**解压多个**归档文件

```unp [file1.zip] [file2.tar.bz2]```

**解压到**以归档命名的子目录中

```unp -u [archive.zip]```

**模拟解压**而不写入文件

```unp -n [archive.tar.gz]```

即使检查失败或目录冲突也**强制解压**

```unp -f [archive.zip]```

**显示支持的**格式

```unp -s```

**向后端工具传递选项**

```unp [archive.tar.gz] -- [-C] [/tmp]```

# SYNOPSIS

**unp** [_OPTION_]... [_FILE_]... [**--** _TOOL-OPTION_...]

# PARAMETERS

**-f**
> 即使程序可用性检查失败或发生目录冲突也继续执行。

**-u**
> 解压到以归档命名的子目录中。对于 Debian 软件包，会分别提取 data.tar.gz 和 control.tar.gz。

**-U**
> 智能模式：若归档包含多个元素则表现得与 -u 一样，但单个文件/目录元素则放在当前目录。

**-s**
> 显示支持的格式列表。

**-n**, **--dry-run**
> 显示计算出的命令但不执行。

**-v**
> 提高输出详细程度。

**--**
> 将后续参数传给后端工具（例如 tar 选项）。

# DESCRIPTION

**unp** 是各种解压/解包工具的 shell 前端。它会自动检测归档的格式并调用相应的解压程序。用户无需记住针对 tar、gzip、bzip2、zip、rar、7z 以及其他数十种格式的不同命令，只需对任何归档文件运行 unp 即可。

默认情况下，unp 解压到当前目录。它也可以选择为解压内容创建一个子目录，避免弄乱工作目录。**--** 之后的参数会传递给底层的解压工具。

# SUPPORTED FORMATS

tar、gz、bz2、xz、zip、rar、7z、arj、lha、deb、rpm、cpio

# CAVEATS

需要为每种格式安装对应的底层解压工具。应仔细检查 **-n** dry-run 的输出，因为归档中的恶意文件名如果被粘贴到 shell 中可能造成危险。

# HISTORY

**unp** 是作为通用解包脚本创建的，可自动检测并解压各种归档格式。

# INSTALL

```pacman: sudo pacman -S unp```

```brew: brew install unp```

```nix: nix profile install nixpkgs#unp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[unar](/man/unar)(1), [atool](/man/atool)(1), [tar](/man/tar)(1), [unzip](/man/unzip)(1)
