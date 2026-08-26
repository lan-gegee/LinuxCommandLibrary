# TAGLINE

查看 gzip 压缩文件的内容

# TLDR

**查看** gzip 压缩文件的**内容**

```zcat [file.gz]```

**查看多个** gzip 压缩文件的**内容**

```zcat [file1.gz] [file2.gz]```

将输出**管道传给**其他命令

```zcat [file.gz] | grep "[pattern]"```

带行号显示

```zcat [file.gz] | nl```

**分页浏览** gzip 压缩文件

```zcat [file.gz] | less```

**合并解压**多个文件到一个输出

```zcat [file1.gz] [file2.gz] > [combined.txt]```

# SYNOPSIS

**zcat** [_options_] [_file ..._]

# PARAMETERS

**-f**, **--force**
> 即使文件有多个链接或后缀不匹配也强制解压。

**-q**, **--quiet**
> 抑制所有警告消息。

**-v**, **--verbose**
> 显示每个文件的文件名和压缩比。

**-h**, **--help**
> 显示帮助信息并退出。

**-V**, **--version**
> 显示版本信息并退出。

# DESCRIPTION

**zcat** 解压 gzip 压缩文件并将未压缩的数据写到标准输出，类似于对普通文件使用 **cat**。它等价于 **gunzip -c** 或 **gzip -dc**。

zcat 可解压由 gzip、zip、compress 或 pack 创建的文件。它通过魔数（magic number）识别压缩文件，而不仅靠 .gz 扩展名，因此也能解压名称非标准的文件。

从标准输入读取时，若数据不是可识别的压缩格式，zcat 会原样透传（行为类似 cat）。

# CAVEATS

zcat 只输出到标准输出，不能就地解压文件。要解压到文件，请使用 **gunzip** 或 **gzip -d**。在某些系统（如 macOS）上，zcat 可能安装为 **gzcat**，以免与 compress 工具的 zcat 冲突。与 gzip/gunzip 不同，zcat 不支持 -t（测试）、-l（列出）、-k（保留）、-r（递归）等选项，因为它只读取并解压到标准输出。

# HISTORY

zcat 是 **gzip** 软件包的一部分，gzip 由 **Jean-loup Gailly** 和 **Mark Adler** 编写。gzip 于 **1992 年**首次发布，是 Unix compress 工具的自由替代品——后者受 LZW 算法专利限制。gzip 成为 GNU 项目的一部分，如今已是类 Unix 系统上的标准工具。

# INSTALL

```apt: sudo apt install gzip```

```dnf: sudo dnf install gzip```

```pacman: sudo pacman -S gzip```

```apk: sudo apk add gzip```

```zypper: sudo zypper install gzip```

```brew: brew install gzip```

```nix: nix profile install nixpkgs#gzip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gzip](/man/gzip)(1), [gunzip](/man/gunzip)(1), [cat](/man/cat)(1), [zless](/man/zless)(1), [zgrep](/man/zgrep)(1), [bzcat](/man/bzcat)(1), [xzcat](/man/xzcat)(1)
