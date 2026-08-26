# TAGLINE

在 gzip 压缩文件中搜索模式

# TLDR

**在 gzip 压缩文件中搜索模式**

```zgrep "[pattern]" [file.gz]```

**不区分大小写搜索**

```zgrep -i "[pattern]" [file.gz]```

**显示行号**

```zgrep -n "[pattern]" [file.gz]```

**在压缩文件中递归搜索**

```zgrep -r "[pattern]" [directory]```

**统计匹配的行数**

```zgrep -c "[pattern]" [file.gz]```

**只显示包含匹配项的文件名**

```zgrep -l "[pattern]" [*.gz]```

# SYNOPSIS

**zgrep** [_grep-options_] [**-e**] _pattern_ [_file_...]

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

**-r**, **-R**
> 递归搜索

**-E**
> 扩展正则表达式（类似 egrep）

**-F**
> 固定字符串匹配（类似 fgrep）

**-e** _pattern_
> 指定模式

# DESCRIPTION

**zgrep** 在 gzip 压缩文件中搜索模式，无需手动解压。它等价于 **gunzip -c file.gz | grep pattern**，但更方便。

该工具会自动检测文件是否被压缩并相应处理。因此可以放心用于同时包含压缩和未压缩文件的目录。

zgrep 支持与 grep 相同的选项，包括基本和扩展正则表达式。要显式指定正则模式，请使用 **zegrep**（扩展）或 **zfgrep**（固定字符串）。

可以搜索多个文件，当多个文件有匹配时默认显示文件名。

# CAVEATS

原生仅支持 gzip 压缩。其他格式：
- bzip2：使用 **bzgrep**
- xz：使用 **xzgrep**
- zstd：通过 **zstdcat** 管道处理

大型压缩文件必须完全解压才能搜索，会消耗 CPU 并可能占用大量内存。

在某些系统上，zgrep 是一个封装脚本，行为可能与原生 grep 略有不同。

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

[grep](/man/grep)(1), [zegrep](/man/zegrep)(1), [zfgrep](/man/zfgrep)(1), [zcat](/man/zcat)(1), [gzip](/man/gzip)(1), [bzgrep](/man/bzgrep)(1)
