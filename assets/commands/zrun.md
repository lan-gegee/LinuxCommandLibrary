# TAGLINE

自动解压参数，对压缩文件运行命令

# TLDR

**对压缩文件运行命令**

```zrun [command] [file.gz]```

**对两个压缩文件运行 diff**

```zrun diff [file1.gz] [file2.gz]```

**对 gzip 文件运行 less**

```zrun less [file.gz]```

# SYNOPSIS

**zrun** _command_ [_arguments_]

# DESCRIPTION

**zrun** 会先将压缩文件参数透明地解压到临时文件，再交给指定命令处理。它根据扩展名识别哪些参数是压缩文件，只把这些解压到临时文件（而不是管道），用解压后的路径运行命令，最后完成清理。

对于原生不支持压缩输入的命令，它可以省去手动解压的步骤。

支持以下压缩类型：**gz**、**bz2**、**Z**、**xz**、**lzma**、**lzo**。

如果把 **zrun** 符号链接为一个以 **z** 开头的名字（例如 **zprog**），那么执行该链接就等同于运行 **zrun prog**。

# CAVEATS

对解压出的临时文件所做的修改不会回写到输入文件，因此不能用这个办法让编辑器支持压缩文件。

较大的压缩文件解压时需要占用临时磁盘空间。

命令看到的是不同的（临时）文件名，而不是原始文件名，这对某些工具可能有影响。

# INSTALL

```apt: sudo apt install moreutils```

```dnf: sudo dnf install moreutils```

```pacman: sudo pacman -S moreutils```

```apk: sudo apk add moreutils```

```zypper: sudo zypper install moreutils```

```brew: brew install moreutils```

```nix: nix profile install nixpkgs#moreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[zcat](/man/zcat)(1), [zless](/man/zless)(1), [zgrep](/man/zgrep)(1), [gzip](/man/gzip)(1), [bzip2](/man/bzip2)(1), [xz](/man/xz)(1)
