# TAGLINE

对 tar 归档中文件的内容应用模式匹配

# TLDR

**搜索模式并提取匹配的文件**

```ptargrep "[pattern]" [archive.tar.gz]```

**列出匹配文件的路径而不提取**

```ptargrep --list-only "[pattern]" [archive.tar]```

**不区分大小写搜索**

```ptargrep -i "[pattern]" [archive.tar.gz]```

**仅按基础名提取匹配文件（忽略目录路径）**

```ptargrep --basename "[pattern]" [archive.tar]```

**搜索多个归档并输出详细信息**

```ptargrep -v "[pattern]" [archive1.tar.gz] [archive2.tar.bz2]```

# SYNOPSIS

**ptargrep** [_options_] _pattern_ _tar-file_ ...

# PARAMETERS

**-b**, **--basename**
> 提取匹配文件时忽略归档中的目录路径，仅用基础名写入当前目录。同名文件会相互覆盖。

**-i**, **--ignore-case**
> 模式匹配不区分大小写。

**-l**, **--list-only**
> 将每个匹配文件的路径打印到 stdout，而不进行提取。

**-v**, **--verbose**
> 将调试信息记录到 stderr。

**-?**, **--help**
> 显示帮助文档。

# DESCRIPTION

**ptargrep** 允许对 tar 归档中文件的内容应用模式匹配。模式将作为 Perl 正则表达式使用。

默认行为是从归档中提取每个匹配的文件。若只需打印匹配文件的路径而不提取，请使用 **--list-only**。

压缩归档（gzip、bzip2、xz）会根据文件扩展名自动处理。

可以指定多个 tar 归档文件名，它们会被依次处理。

# CAVEATS

Perl 发行版的一部分（Archive::Tar 模块）。大型归档处理可能较慢。由于文件内容会读入内存，大文件可能占用较多内存。

# HISTORY

**ptargrep** 随 Perl 的 **Archive::Tar** 模块一同分发。它为归档内容提供类似 grep 的功能。

# INSTALL

```apt: sudo apt install perl```

```dnf: sudo dnf install perl```

```pacman: sudo pacman -S perl```

```apk: sudo apk add perl-utils```

```zypper: sudo zypper install perl```

```brew: brew install perl```

```nix: nix profile install nixpkgs#perl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[zgrep](/man/zgrep)(1), [tar](/man/tar)(1), [grep](/man/grep)(1), [perl](/man/perl)(1), [zipgrep](/man/zipgrep)(1)
