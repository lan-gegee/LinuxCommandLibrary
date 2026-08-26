# TAGLINE

创建并使用 PAR2 文件进行数据恢复

# TLDR

**创建恢复文件**

```par2 create [backup.par2] [files]```

**校验文件**

```par2 verify [backup.par2]```

**修复受损文件**

```par2 repair [backup.par2]```

**以指定冗余级别创建**

```par2 create -r[10] [backup.par2] [files]```

**以指定块数创建**

```par2 create -c[100] [backup.par2] [files]```

**校验指定文件**

```par2 verify [backup.par2] [file1] [file2]```

**静默运行**

```par2 create -q [backup.par2] [files]```

# SYNOPSIS

**par2** [_create_] [_verify_] [_repair_] [_-r percent_] [_-c count_] [_options_] _par2file_ [_files_]

# PARAMETERS

**create**
> 创建 PAR2 恢复文件。

**verify**, **v**
> 使用 PAR2 校验文件。

**repair**, **r**
> 修复受损文件。

**-r** _PERCENT_
> 冗余百分比。

**-c** _COUNT_
> 块数量。

**-b** _SIZE_
> 以字节为单位的块大小。

**-n** _COUNT_
> 恢复文件的数量。

**-u**
> 使恢复文件的大小保持一致。

**-q**
> 安静模式。

**-v**
> 详细输出。

**--**
> 选项结束标记。

# DESCRIPTION

**par2** 创建并使用 PAR2（Parity Archive 2）文件进行数据恢复。这些文件可以用来修复损坏或缺失的数据。

恢复文件包含根据源文件计算出的奇偶校验信息。如果源文件损坏或部分丢失，PAR2 文件能够重建原始数据。

冗余级别（-r）决定可修复的损坏程度。10% 的冗余意味着即使丢失 10% 的数据也仍然可以恢复。冗余越高，占用的空间越大。

基于块的恢复会把文件拆分成块。文件某一部分的损坏只消耗受影响块对应的恢复容量，而不涉及整个文件。

校验会将文件与保存的校验和进行比对，识别损坏但不做修复。修复模式则利用现有的恢复数据来解决问题。

该格式常用于 Usenet 下载、归档分发和备份校验。

# CAVEATS

恢复所需的 PAR2 数据量取决于损坏程度。如果损坏超过冗余量则无法修复。处理大文件需要大量时间和内存。

# HISTORY

**PAR2** 在 **2003 年**前后开发，是对原始 PAR 格式的改进。它采用 Reed-Solomon 纠错实现块级恢复。该格式已成为文件共享与存档领域数据恢复的标准。

# INSTALL

```apt: sudo apt install par2```

```dnf: sudo dnf install par2cmdline```

```pacman: sudo pacman -S par2cmdline```

```apk: sudo apk add par2cmdline```

```zypper: sudo zypper install par2cmdline```

```brew: brew install par2```

```nix: nix profile install nixpkgs#par2cmdline```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rzip](/man/rzip)(1), [gzip](/man/gzip)(1), [rar](/man/rar)(1)
