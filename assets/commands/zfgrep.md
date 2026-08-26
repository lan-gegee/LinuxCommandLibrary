# TAGLINE

在 gzip 压缩文件中搜索固定字符串

# TLDR

**在 gzip 压缩文件中搜索字面字符串**

```zfgrep "[string]" [file.gz]```

**不区分大小写搜索**

```zfgrep -i "[string]" [file.gz]```

**显示行号**

```zfgrep -n "[string]" [file.gz]```

**统计匹配的行数**

```zfgrep -c "[string]" [file.gz]```

**列出包含匹配项的文件**

```zfgrep -l "[string]" [*.gz]```

# SYNOPSIS

**zfgrep** [_grep-options_] [**-e**] _pattern_ [_file_...]

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
> 指定模式

**-x**
> 只匹配整行

# DESCRIPTION

**zfgrep** 在 gzip 压缩文件中搜索固定字符串，无需手动解压。它等价于 **zcat file.gz | fgrep pattern**，但更方便。

其中的 "f" 表示固定字符串匹配（如同 **grep -F**）。模式按字面解释，不作为正则表达式。这比正则匹配更快，适合搜索包含特殊字符的字符串。

zfgrep 自动处理压缩和未压缩的文件，因此可以放心用于混合文件集合。

可以使用 **-e** 指定多个模式，每行一个，或用换行符分隔。

# CAVEATS

仅支持 gzip 压缩。bzip2 文件请使用 **bzfgrep**，其他格式请通过相应的解压器管道处理。

固定字符串匹配意味着 **.**、**\***、**[** 等特殊字符按字面处理。需要正则表达式时请使用 **zgrep** 或 **zegrep**。

处理大型压缩文件需要消耗 CPU 进行解压。

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

[zgrep](/man/zgrep)(1), [zegrep](/man/zegrep)(1), [fgrep](/man/fgrep)(1), [zcat](/man/zcat)(1), [gzip](/man/gzip)(1)
