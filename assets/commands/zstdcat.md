# TAGLINE

将 zstd 文件解压到 stdout

# TLDR

**解压到 stdout**

```zstdcat [file.zst]```

**解压多个文件**

```zstdcat [file1.zst] [file2.zst]```

**解压并通过管道传给其他命令**

```zstdcat [file.zst] | grep [pattern]```

**以详细输出解压**

```zstdcat -v [file.zst]```

# SYNOPSIS

**zstdcat** [_options_] [_files_...]

# PARAMETERS

**-v**, **--verbose**
> 详细模式。显示更多信息。

**-q**, **--quiet**
> 抑制警告和通知。

**--no-progress**
> 不显示进度条。

**-f**, **--force**
> 强制覆盖并对符号链接执行（解）压缩。

# DESCRIPTION

**zstdcat** 将 Zstandard（.zst）压缩文件解压并写到标准输出，等效于运行 **zstd -dcf**。因此非常适合把压缩数据通过管道传给其他命令，而不必在磁盘上生成中间解压文件。

给定多个输入文件时，zstdcat 会按顺序逐一解压，并将输出串联后写到 stdout。它是 zstd 压缩工具套件的一部分。

# INSTALL

```apt: sudo apt install zstd```

```dnf: sudo dnf install zstd```

```pacman: sudo pacman -S zstd```

```apk: sudo apk add zstd```

```zypper: sudo zypper install zstd```

```brew: brew install zstd```

```nix: nix profile install nixpkgs#zstd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[zstd](/man/zstd)(1), [unzstd](/man/unzstd)(1), [zstdless](/man/zstdless)(1)
