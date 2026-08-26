# TAGLINE

使用扩展正则表达式搜索 bzip2 文件

# TLDR

**在 bzip2 压缩文件中搜索扩展正则表达式模式**

```bzegrep "[pattern]" [path/to/file.bz2]```

**不区分大小写地搜索**

```bzegrep -i "[pattern]" [path/to/file.bz2]```

**打印匹配行的行号**

```bzegrep -n "[pattern]" [path/to/file.bz2]```

**搜索多个压缩文件**

```bzegrep "[pattern]" [file1.bz2] [file2.bz2]```

**统计匹配行数**

```bzegrep -c "[pattern]" [path/to/file.bz2]```

**从 stdin 搜索**

```bzcat [path/to/file.bz2] | bzegrep "[pattern]"```

# SYNOPSIS

**bzegrep** [_egrep_options_] [**-e**] _pattern_ [_filename..._]

# DESCRIPTION

**bzegrep** 在可能经 bzip2 压缩的文件中搜索匹配扩展正则表达式模式的行。它会在搜索前透明地解压 **.bz2** 文件，并将所有选项直接传递给 **egrep**。

如果未指定文件，bzegrep 会从标准输入读取，必要时进行解压。这使它可以与其他 bzip2 工具一起用于管道。

该命令等同于运行 **bzgrep**，但使用 **egrep**（扩展 grep）进行模式匹配，支持包括 **+**、**?**、**|** 和用于分组的圆括号在内的扩展正则表达式语法。

# PARAMETERS

支持所有 **egrep** 选项，包括：

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

**-h**
> 抑制输出中的文件名前缀（搜索多个文件时）

**-e** _pattern_
> 指定模式（当模式以 - 开头时很有用）

# CAVEATS

可以设置 **GREP** 环境变量来指定替代的 grep 程序。文件必须是 bzip2 压缩的才能透明解压；未压缩的文件会被直接搜索。

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

[bzgrep](/man/bzgrep)(1), [bzfgrep](/man/bzfgrep)(1), [egrep](/man/egrep)(1), [grep](/man/grep)(1), [bzip2](/man/bzip2)(1), [bzcat](/man/bzcat)(1), [zegrep](/man/zegrep)(1)
