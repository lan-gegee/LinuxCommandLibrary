# TAGLINE

解压 RAR 归档文件

# TLDR

**解压归档文件**

```unrar x [archive.rar]```

**解压到指定目录**

```unrar x [archive.rar] [destination/]```

**不保留路径解压**

```unrar e [archive.rar]```

**列出内容**

```unrar l [archive.rar]```

**测试归档**

```unrar t [archive.rar]```

**用密码解压**

```unrar x -p[password] [archive.rar]```

**解压并覆盖**

```unrar x -o+ [archive.rar]```

# SYNOPSIS

**unrar** _command_ [_-switches_] _archive_ [_files_] [_destination_]

# COMMANDS

**x**
> 保留完整路径解压。

**e**
> 不保留路径解压。

**l**, **v**
> 列出内容。

**t**
> 测试归档。

**p**
> 打印到 stdout。

# PARAMETERS

**-p** [_PASSWORD_]
> 密码。

**-o+**
> 覆盖已存在的文件。

**-o-**
> 跳过已存在的文件。

**-or**
> 重命名已存在的文件。

**-y**
> 对所有询问回答是。

**-x** _PATTERN_
> 排除文件。

**-n** _PATTERN_
> 仅包含匹配的文件。

**-v**
> 详细列出内容。

**-c-**
> 禁用注释显示。

**-id**
> 禁用消息输出。

**-kb**
> 保留损坏的文件。

# DESCRIPTION

**unrar** 用于解压 RAR 归档。它支持所有 RAR 版本，包括压缩率更高的 RAR5。

保留路径解压（x）会重建目录结构。不保留路径解压（e）则把所有文件放到目标位置。

多卷归档会自动处理。只需提供第一个卷，后续分卷会被自动找到。

支持对文件内容和头部的密码保护。没有正确的密码时，连文件名都可能被隐藏。

测试操作在不解压的情况下验证归档完整性，可确认归档未损坏。

该工具还能处理恢复记录。如果存在恢复数据，轻微损坏的归档仍可解压。

# CAVEATS

只读——无法创建 RAR 归档（需要 rar）。免费软件但不开源。某些发行版提供自由的替代品。

# HISTORY

**unrar** 由 **RARLAB**（Eugene Roshal）开发，作为解压 RAR 归档的免费软件提供。创建归档则需要商业化的 rar 程序。

# INSTALL

```dnf: sudo dnf install unrar```

```pacman: sudo pacman -S unrar```

```nix: nix profile install nixpkgs#unrar```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rar](/man/rar)(1), [7z](/man/7z)(1), [unzip](/man/unzip)(1), [tar](/man/tar)(1)
