# TAGLINE

逐行比较 gzip 压缩文件

# TLDR

**比较两个压缩文件**

```zdiff [file1.gz] [file2.gz]```

**以统一格式比较**

```zdiff -u [file1.gz] [file2.gz]```

**以上下文格式比较**

```zdiff -c [file1.gz] [file2.gz]```

**并排比较**

```zdiff -y [file1.gz] [file2.gz]```

将**压缩文件与其未压缩版本进行比较**

```zdiff [file.gz]```

# SYNOPSIS

**zdiff** [_diff_options_] _file1_ [_file2_]

# PARAMETERS

所有选项都直接传给 **diff**(1)。常用选项包括：

**-u**
> 统一输出格式。

**-c**
> 上下文输出格式。

**-y**
> 并排输出。

**-q**
> 只报告文件是否不同。

**-i**
> 忽略大小写差异。

**-w**
> 忽略所有空白字符。

# DESCRIPTION

**zdiff** 无需手动解压即可逐行比较 gzip 压缩文件。它的工作方式类似 **diff**，但透明地处理 .gz 文件，在比较前即时解压。

若只指定一个文件，则将其与对应的 .gz 文件的解压内容进行比较。若指定两个文件，则它们的内容（必要时先解压）会送入 diff。

支持所有标准的 diff 输出格式。diff 接受的任何选项都可以传给 zdiff。diff 的退出状态会被保留。

该命令是 gzip 软件包的一部分。要逐字节比较，请改用 **zcmp**。

# CAVEATS

只处理 gzip 压缩文件。比较前两个文件会完整解压到内存中。xz/lzma 文件请使用 xzdiff；bzip2 文件请使用 bzdiff。

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

[diff](/man/diff)(1), [zcmp](/man/zcmp)(1), [zcat](/man/zcat)(1), [gzip](/man/gzip)(1), [zmore](/man/zmore)(1)
