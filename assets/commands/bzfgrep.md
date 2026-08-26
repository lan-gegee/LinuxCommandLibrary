# TAGLINE

在 bzip2 文件中搜索固定字符串模式

# TLDR

**在 bzip2 压缩文件中搜索固定字符串**

```bzfgrep "[string]" [path/to/file.bz2]```

**不区分大小写地搜索**

```bzfgrep -i "[string]" [path/to/file.bz2]```

**打印匹配行的行号**

```bzfgrep -n "[string]" [path/to/file.bz2]```

**搜索多个压缩文件**

```bzfgrep "[string]" [file1.bz2] [file2.bz2]```

**统计匹配行数**

```bzfgrep -c "[string]" [path/to/file.bz2]```

# SYNOPSIS

**bzfgrep** [_fgrep_options_] [**-e**] _pattern_ [_filename..._]

# DESCRIPTION

**bzfgrep** 在可能经 bzip2 压缩的文件中搜索匹配固定字符串模式的行。它会在搜索前透明地解压 **.bz2** 文件，并将所有选项直接传递给 **fgrep**。

与 **bzgrep** 或 **bzegrep** 不同，bzfgrep 将模式解释为字面字符串而不是正则表达式。这使得简单字符串搜索更快，也无需转义特殊字符。

如果未指定文件，bzfgrep 会从标准输入读取，必要时进行解压。

# PARAMETERS

支持所有 **fgrep** 选项，包括：

**-i**
> 不区分大小写的匹配

**-n**
> 打印行号

**-c**
> 只打印匹配行的数量

**-v**
> 反转匹配（显示不匹配的行）

**-l**
> 只打印包含匹配内容的文件名

**-e** _pattern_
> 指定模式（当模式以 - 开头时很有用）

# CAVEATS

可以设置 **GREP** 环境变量来指定替代的 grep 程序。模式被视为固定字符串而不是正则表达式。要进行正则表达式搜索，请使用 **bzgrep** 或 **bzegrep**。

# INSTALL

```apt: sudo apt install bzip2```

```dnf: sudo dnf install bzip2```

```pacman: sudo pacman -S bzip2```

```apk: sudo apk add bzip2```

```zypper: sudo zypper install bzip2```

```brew: brew install bzip2```

```nix: nix profile install nixpkgs#bzip2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bzgrep](/man/bzgrep)(1), [bzegrep](/man/bzegrep)(1), [fgrep](/man/fgrep)(1), [bzip2](/man/bzip2)(1)

# RESOURCES

```[Source code](https://gitlab.com/bzip2/bzip2)```

```[Homepage](https://sourceware.org/bzip2/)```

<!-- verified: 2026-06-22 -->
