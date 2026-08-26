# TAGLINE

创建和管理 RAR 压缩归档

# TLDR

**创建归档**

```rar a [archive.rar] [files]```

**解压归档**

```rar x [archive.rar]```

**解压到指定目录**

```rar x [archive.rar] [destination/]```

**列出内容**

```rar l [archive.rar]```

**带密码添加文件**

```rar a -p[password] [archive.rar] [files]```

**指定压缩级别添加文件**

```rar a -m[5] [archive.rar] [files]```

**测试归档**

```rar t [archive.rar]```

**添加恢复记录**

```rar a -rr[5%] [archive.rar] [files]```

# SYNOPSIS

**rar** _command_ [_-switches_] _archive_ [_files_]

# PARAMETERS

**a**
> 将文件添加到归档。

**x**
> 以完整路径解压。

**e**
> 不带路径解压。

**l**, **v**
> 列出归档内容。

**t**
> 测试归档。

**d**
> 从归档中删除。

**u**
> 更新文件。

**-m** _N_
> 压缩级别（0-5）。

**-p** [_PASSWORD_]
> 设置密码。

**-r**
> 递归处理子目录。

**-rr** [_N_]
> 添加恢复记录（百分比）。

**-v** _SIZE_
> 创建分卷。

**-y**
> 对所有询问回答"是"。

**-o+**, **-o-**
> 覆盖模式。

**-hp** [_PASSWORD_]
> 同时加密文件头。

# DESCRIPTION

**rar** 用于创建和管理 RAR 归档。它提供高压缩比以及恢复记录、固实压缩等特性。

压缩级别从 0（仅存储）到 5（最高）。级别越高耗时越长，但生成的文件更小。

恢复记录可防止数据损坏。它添加冗余信息，能够修复不超过指定百分比的损伤。

文件头加密（-hp）在加密内容之外还会隐藏文件名。标准密码保护（-p）只加密数据，文件名仍然可见。

分卷功能可将归档拆分为多个部分。大小可以按字节、千字节或兆字节指定。

固实归档将多个文件一起压缩，对相似文件的压缩比更好。但提取单个文件时需要先处理之前的文件。

# CAVEATS

专有格式——需要 rar 或 unrar。免费版本仅提供命令行界面。Linux 版可用但并非开源。

# HISTORY

**RAR** 由 **Eugene Roshal** 于 **1993 年**创建（Roshal ARchive，即 Roshal 归档）。它在宽带普及之前因分发大文件而流行。该格式持续发展，不断改进压缩和加密能力。

# INSTALL

```nix: nix profile install nixpkgs#rar```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[unrar](/man/unrar)(1), [7z](/man/7z)(1), [zip](/man/zip)(1), [tar](/man/tar)(1)
