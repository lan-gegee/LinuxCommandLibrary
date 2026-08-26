# TAGLINE

解压 bzip2 压缩文件

# TLDR

**解压**文件（删除 .bz2 原文件）

```bunzip2 [file.txt.bz2]```

**解压**时保留压缩文件

```bunzip2 -k [file.txt.bz2]```

**解压**到 stdout（便于管道使用）

```bunzip2 -c [file.txt.bz2] > [file.txt]```

**测试**文件完整性而不解压

```bunzip2 -t [file.txt.bz2]```

**强制**覆盖已有的输出文件

```bunzip2 -f [file.txt.bz2]```

# SYNOPSIS

**bunzip2** [_options_] [_file_...]

# DESCRIPTION

**bunzip2** 解压用 bzip2 压缩的文件。它等同于 `bzip2 -d`，并在成功解压后删除 .bz2 文件。

该工具是 bzip2 的配套程序，用于提取压缩文件。

# PARAMETERS

**-k**, **--keep**
> 保留压缩文件

**-f**, **--force**
> 覆盖已有文件

**-c**, **--stdout**
> 写入标准输出

**-t**, **--test**
> 测试文件完整性

**-v**, **--verbose**
> 详细模式

**-q**, **--quiet**
> 抑制警告

**-s**, **--small**
> 降低内存占用但牺牲速度（每个文件约使用 2.5 MB 内存）

# CAVEATS

除非使用 -k，否则会删除原始 .bz2 文件。所需内存与压缩块大小成正比。无法解压损坏的文件。

# HISTORY

自 Julian Seward 于 **1996 年**创建 bzip2 起，**bunzip2** 就作为其组成部分一同发布。

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

[bzip2](/man/bzip2)(1), [bzcat](/man/bzcat)(1), [gunzip](/man/gunzip)(1), [xz](/man/xz)(1)
