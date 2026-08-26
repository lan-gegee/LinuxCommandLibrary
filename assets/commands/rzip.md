# TAGLINE

面向大文件的长距离压缩工具

# TLDR

**压缩文件**（删除原文件）

```rzip [file]```

**压缩时保留原文件**

```rzip -k [file]```

**解压文件**

```rzip -d [file.rz]```

**设置最高压缩级别**

```rzip -9 [file]```

**压缩并显示进度**

```rzip -P [file]```

**压缩到指定的输出文件**

```rzip -o [output.rz] [file]```

**强制覆盖已存在的文件**

```rzip -f [file]```

# SYNOPSIS

**rzip** [_options_] _files_...

# PARAMETERS

**-d**
> 解压。当程序以 `runzip` 名称调用时自动启用。

**-k**
> 压缩或解压后保留输入文件。

**-f**
> 强制覆盖已存在的输出文件。

**-o** _filename_
> 指定输出文件名。不能与多个输入文件同时使用。

**-S** _suffix_
> 设置压缩后缀。默认为 `.rz`。

**-P**
> 压缩时显示百分比进度。

**-0** 到 **-9**
> 压缩级别，从最快（0）到最佳（9）。默认为 6。

**-V**
> 显示版本号。

**-h**
> 输出帮助摘要。

# DESCRIPTION

**rzip** 是一款专为大文件设计的压缩程序。它分两个阶段工作：第一阶段使用类似 rsync 的滚动校验和算法，查找并对可能在相距极远位置（最长接近 1 GB）的大块重复数据进行编码；第二阶段使用 bzip2 压缩第一阶段的输出。

得益于长距离匹配，rzip 对重复内容相距很远、普通压缩器无法利用的文件尤为有效。

# CAVEATS

内存占用与文件大小成正比。由于算法特性，无法从标准输入/标准输出进行压缩或解压。最适合 10 MB 以上的文件。默认在成功压缩或解压后删除源文件（用 -k 可保留）。

# HISTORY

rzip 由 **Andrew Tridgell**（rsync 和 Samba 的作者）编写，用于高效压缩具有远距离冗余数据的大型文件。

# INSTALL

```apt: sudo apt install rzip```

```dnf: sudo dnf install rzip```

```zypper: sudo zypper install rzip```

```brew: brew install rzip```

```nix: nix profile install nixpkgs#rzip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lrzip](/man/lrzip)(1), [bzip2](/man/bzip2)(1), [gzip](/man/gzip)(1), [xz](/man/xz)(1), [rsync](/man/rsync)(1)
