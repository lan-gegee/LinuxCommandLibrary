# TAGLINE

从 ZIP 归档中提取文件

# TLDR

将文件**解压**到当前目录

```unzip [archive.zip]```

**解压到指定目录**

```unzip [archive.zip] -d [/path/to/directory]```

仅**列出内容**而不解压

```unzip -l [archive.zip]```

**解压特定文件**

```unzip [archive.zip] [file1.txt] [file2.txt]```

**按模式解压**

```unzip [archive.zip] "*.txt"```

**安静地解压**（最少输出）

```unzip -q [archive.zip]```

**解压并覆盖**已有文件

```unzip -o [archive.zip]```

**测试归档完整性**

```unzip -t [archive.zip]```

**保留目录结构解压**

```unzip [archive.zip]```

# SYNOPSIS

**unzip** [_options_] _file_[.zip] [_file(s)_] [**-x** _xfile(s)_] [**-d** _exdir_]

# DESCRIPTION

**unzip** 从 ZIP 归档中提取文件。它可以处理由 zip、WinZip、PKZIP 及其他兼容 ZIP 的程序创建的归档。该工具支持多种压缩方法，还能处理加密归档。

默认情况下，unzip 会把所有文件解压到当前目录，并保留归档中存储的目录结构。也可以指定单个文件或模式来进行选择性解压。

unzip 是 InfoZip 项目的一部分，是类 Unix 系统上标准的 ZIP 解压工具。

# PARAMETERS

**-l**
> 列出归档内容。

**-v**
> 详细列出并附带压缩信息。

**-t**
> 测试归档完整性。

**-d** _dir_
> 解压到指定目录。

**-o**
> 覆盖已有文件，不做提示。

**-n**
> 绝不覆盖已有文件。

**-q**
> 安静模式。

**-qq**
> 极安静模式。

**-j**
> 去掉路径（不创建目录）。

**-p**
> 解压到 stdout（管道）。

**-P** _password_
> 为加密文件提供密码。

**-x** _files_
> 排除指定文件。

**-C**
> 匹配时不区分大小写。

**-a**
> 转换文本文件的行尾符。

# CAVEATS

在命令行中传递密码并不安全（会暴露在进程列表中）。包含大量文件的大型归档解压可能较慢。部分 ZIP 特性（ZIP64、某些压缩方法）需要较新版本才能支持。归档中的符号链接可能带来安全风险。

# HISTORY

**unzip** 属于 **Info-ZIP** 项目，该项目始于 **1989 年**，旨在提供免费的 ZIP 工具。这些工具由 **Mark Adler**、**Jean-loup Gailly**、**Greg Roelofs** 等人开发，用以提供 PKWARE 公司 PKZIP 的开源替代方案。Info-ZIP 工具已成为 Unix 系统上的标准 ZIP 工具。

# INSTALL

```apt: sudo apt install unzip```

```dnf: sudo dnf install unzip```

```pacman: sudo pacman -S unzip```

```apk: sudo apk add unzip```

```zypper: sudo zypper install unzip```

```brew: brew install unzip```

```nix: nix profile install nixpkgs#unzip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[zip](/man/zip)(1), [tar](/man/tar)(1), [gzip](/man/gzip)(1), [7z](/man/7z)(1)
