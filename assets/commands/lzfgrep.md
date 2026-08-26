# TAGLINE

在压缩文件中搜索固定字符串

# TLDR

在压缩文件中**搜索固定字符串**

```lzfgrep [string] [file.lz]```

**忽略大小写搜索**

```lzfgrep -i [string] [file.lz]```

显示匹配项所在的**行号**

```lzfgrep -n [string] [file.lz]```

**统计匹配的行数**

```lzfgrep -c [string] [file.lz]```

在**多个**压缩文件中**搜索**

```lzfgrep [string] [file1.lz] [file2.lz]```

**列出包含匹配项的文件**

```lzfgrep -l [string] [*.lz]```

# SYNOPSIS

**lzfgrep** [_grep_options_] [**-e**] _pattern_ [_file_...]

# PARAMETERS

所有选项都会直接传递给 **grep**(1)。常用选项包括：

**-i**
> 忽略大小写匹配。

**-n**
> 显示行号。

**-c**
> 只打印匹配行的数量。

**-l**
> 打印包含匹配项的文件名。

**-v**
> 反转匹配（显示不匹配的行）。

**-w**
> 仅匹配完整单词。

**-e** _pattern_
> 显式指定模式。

# DESCRIPTION

**lzfgrep** 在可能由 xz、lzma、gzip 或 bzip2 压缩的文件中搜索固定字符串。它等价于 **lzgrep -F**，对于字面字符串模式比基于正则表达式的搜索更快。文件会在搜索时即时解压。

lzfgrep 作为 xz-utils 的一部分提供，用于向后兼容 LZMA Utils。如果未指定文件，则会对标准输入按需解压后送入 grep。

# CAVEATS

从标准输入读取时不支持 gzip 和 bzip2 压缩文件。所有选项都会直接传递给 grep。

# INSTALL

```dnf: sudo dnf install xz```

```pacman: sudo pacman -S xz```

```apk: sudo apk add xz```

```zypper: sudo zypper install xz```

```brew: brew install xz```

```nix: nix profile install nixpkgs#xz```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lzgrep](/man/lzgrep)(1), [fgrep](/man/fgrep)(1), [lzegrep](/man/lzegrep)(1), [xzgrep](/man/xzgrep)(1), [zgrep](/man/zgrep)(1), [grep](/man/grep)(1)
