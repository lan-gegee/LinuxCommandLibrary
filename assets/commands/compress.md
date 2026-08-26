# TAGLINE

使用 LZW 压缩减小文件体积

# TLDR

**压缩**文件

```compress path/to/file1 path/to/file2```

以**强制**模式压缩（覆盖已有文件）

```compress -f path/to/file```

设置最大**压缩位数**

```compress -b 12 path/to/file```

输出到**stdout**，不修改文件

```compress -c path/to/file```

**解压**文件

```compress -d path/to/file.Z```

显示**压缩百分比**

```compress -v path/to/file```

**保留**原始文件

```compress -k path/to/file```

# SYNOPSIS

**compress** [**-fkvcV**] [**-b** _bits_] [_file_...]

# DESCRIPTION

**compress** 是经典的 Unix 压缩工具，实现了 LZW（Lempel-Ziv-Welch）算法，生成的文件带有标志性的 .Z 扩展名。在 20 世纪 90 年代初被 gzip 大规模取代之前，它一直是 Unix 系统上的标准压缩工具。该算法采用自适应字典压缩，从 9 位编码开始，并按需扩展至最多 16 位。

压缩文件时，compress 会保留重要的文件元数据，包括所有者、权限（mode）和时间戳。它默认安全运行：除非使用 -f 强制选项，否则拒绝压缩符号链接以及拥有多个硬链接的文件。除非指定了 -c stdout 选项或 -k 保留选项，否则压缩后的文件会替换原文件。

压缩比因文件类型而异，文本文件通常可缩减 50-60% 的体积。二进制文件的压缩效果可能较差。虽然如今 compress 在大多数场景下已被视为过时，但它仍可用于兼容遗留的 .Z 归档以及仍在使用该格式的系统。gzip 和 bzip2 等现代替代品能提供更好的压缩比，且得到更广泛的支持。

# PARAMETERS

**-f**
> 强制压缩，覆盖已有文件，并压缩拥有硬链接的文件

**-k**
> 保留（不删除）输入文件

**-v**
> 详细输出模式；显示每个文件的压缩百分比

**-c**
> 将结果写入 stdout，不修改任何文件

**-V**
> 打印版本和补丁级别信息

**-r**
> 递归地处理目录

**-b BITS**
> 设置每编码的最大位数（9-16，默认 16）

**--**
> 停止解析选项；将剩余参数视为文件名

# CAVEATS

该程序使用改进的 Lempel-Ziv 算法，从 9 位编码开始。文本文件的典型压缩效果为缩减 50-60%。退出状态码：0 表示成功，2 表示输出会比输入更大，1 表示出错。为兼容较旧的系统请使用 -b12。

# HISTORY

**compress** 实现了经典的 Unix LZW 压缩算法。虽然在很大程度上已被 gzip 及其他现代压缩工具取代，但它仍可用于兼容性需求和处理 .Z 文件。

# INSTALL

```apt: sudo apt install ncompress```

```dnf: sudo dnf install ncompress```

```pacman: sudo pacman -S ncompress```

```zypper: sudo zypper install ncompress```

```brew: brew install ncompress```

```nix: nix profile install nixpkgs#ncompress```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[uncompress](/man/uncompress)(1), [gzip](/man/gzip)(1), [bzip2](/man/bzip2)(1), [zcat](/man/zcat)(1)

# RESOURCES

```[Source code](https://github.com/vapier/ncompress)```

```[Homepage](https://vapier.github.io/ncompress/)```

<!-- verified: 2026-06-22 -->
