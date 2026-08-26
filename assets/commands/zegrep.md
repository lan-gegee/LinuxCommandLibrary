# TAGLINE

使用扩展正则表达式搜索 gzip 压缩文件

# TLDR

**在 gzip 压缩文件中搜索模式**

```zegrep "[pattern]" [file.gz]```

**不区分大小写搜索**

```zegrep -i "[pattern]" [file.gz]```

**显示行号**

```zegrep -n "[pattern]" [file.gz]```

**搜索多个文件**

```zegrep "[pattern]" [file1.gz] [file2.gz]```

**扩展正则表达式搜索（选择、量词）**

```zegrep "(foo|bar)+" [file.gz]```

# SYNOPSIS

**zegrep** [_grep-options_] [**-e**] _pattern_ [_file_...]

# PARAMETERS

**-i**
> 不区分大小写匹配

**-n**
> 显示行号

**-l**
> 只列出包含匹配项的文件名

**-c**
> 统计匹配的行数

**-v**
> 反向匹配（显示不匹配的行）

**-h**
> 输出中不显示文件名

**-e** _pattern_
> 指定模式（对以 - 开头的模式很有用）

# DESCRIPTION

**zegrep** 在 gzip 压缩文件中搜索模式，无需手动解压。它等价于 **zcat file.gz | egrep pattern**，但更方便。

其中的 "e" 表示支持扩展正则表达式，与 **grep -E** 相同。这允许模式中使用 **+**、**?**、**|** 和 **()** 而无需转义。

zegrep 会自动检测输入文件是否被压缩。未压缩的文件按常规方式搜索，因此可以放心用于混合文件集合。

可以使用 **-e** 指定多个模式，或在模式中用 **|** 分隔。

# CAVEATS

zegrep 需要先解压文件才能搜索，这会消耗 CPU。对于较大的压缩文件，速度可能较慢。

仅支持 gzip 压缩。其他格式请使用 **bzgrep**（bzip2）或 **xzgrep**（xz）。

内存占用随解压后的文件大小增长，因为文件必须经过解压器处理。

在某些系统上，zegrep 是围绕 zcat 和 egrep 的脚本封装。

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

[zgrep](/man/zgrep)(1), [zfgrep](/man/zfgrep)(1), [zcat](/man/zcat)(1), [grep](/man/grep)(1), [egrep](/man/egrep)(1), [gzip](/man/gzip)(1), [bzgrep](/man/bzgrep)(1), [xzgrep](/man/xzgrep)(1)
