# TAGLINE

逐字节比较压缩文件

# TLDR

**比较两个压缩文件**

```lzcmp [file1.xz] [file2.xz]```

**以详细输出进行比较**

```lzcmp -l [file1.xz] [file2.xz]```

**静默比较**

```lzcmp -s [file1.gz] [file2.gz]```

**将压缩文件与其未压缩的原始文件比较**

```lzcmp [file.xz]```

# SYNOPSIS

**lzcmp** [_cmp_options_] _file1_ [_file2_]

# PARAMETERS

**-l**
> 打印字节编号及不同的字节值。

**-s**
> 静默模式，不输出任何内容，仅返回退出状态。

所有选项都会直接传递给 **cmp**(1)。

# DESCRIPTION

**lzcmp** 对压缩文件调用 cmp(1)。它支持 xz、lzma、gzip、bzip2、lzop、zstd 和 lz4 压缩的文件。如果只指定一个文件，则将其与去掉了压缩后缀的同名文件比较。如果指定两个文件，两者会按需解压后送入 cmp。cmp 的退出状态会被保留：相同为 0，不同为 1，出错为 2。

提供 lzcmp 这个名称是为了向后兼容 LZMA Utils。它已被弃用，建议改用 **xzcmp**，并将在未来版本的 XZ Utils 中移除。

# INSTALL

```dnf: sudo dnf install xz```

```pacman: sudo pacman -S xz```

```apk: sudo apk add xz```

```zypper: sudo zypper install xz```

```brew: brew install xz```

```nix: nix profile install nixpkgs#xz```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cmp](/man/cmp)(1), [lzdiff](/man/lzdiff)(1), [xzcmp](/man/xzcmp)(1), [xzdiff](/man/xzdiff)(1), [zcmp](/man/zcmp)(1), [xz](/man/xz)(1)
