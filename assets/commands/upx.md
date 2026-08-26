# TAGLINE

可执行文件终极打包工具

# TLDR

**压缩可执行文件**

```upx [program]```

**以最佳压缩比压缩**

```upx --best [program]```

**以最快速度压缩**

```upx -1 [program]```

**解压可执行文件**

```upx -d [program]```

**测试压缩后的文件**

```upx -t [program]```

**列出压缩信息**

```upx -l [program]```

**保留备份**

```upx -k [program]```

**安静地压缩**

```upx -q [program]```

**压缩到另一个输出文件**

```upx -o [packed_program] [program]```

# SYNOPSIS

**upx** [_-d_] [_-t_] [_-l_] [_--best_] [_-1..-9_] [_options_] _files_

# PARAMETERS

**-1** 至 **-9**
> 压缩级别（1=最快，9=最佳）。

**--best**
> -9 的别名，即最佳压缩比。

**--brute**
> 尝试所有压缩方法和过滤器（非常慢）。

**--ultra-brute**
> 更彻底的穷举搜索（极其缓慢）。

**-d**
> 解压。

**-t**
> 测试完整性。

**-l**
> 列出压缩信息。

**-k**
> 保留备份文件。

**-o** _FILE_
> 输出到指定文件。

**-f**
> 强制压缩。

**-q**
> 安静模式。

**-v**
> 详细输出模式。

**--no-backup**
> 不创建备份。

**--lzma**
> 使用 LZMA 压缩（压缩比更高，但解压更慢）。

**--no-lzma**
> 禁用 LZMA 压缩（覆盖 --brute 和 --all-methods）。

**--overlay=**_ACTION_
> 处理附加数据的方式：copy（默认）、strip。

# DESCRIPTION

**upx**（Ultimate Packer for eXecutables）用于压缩可执行文件。被压缩的程序在运行时会在内存中自行解压。

压缩可以显著缩小文件体积，对二进制文件通常能减少 50-70%。这既节省磁盘空间，也节省下载带宽。

压缩后的可执行文件是自解压式的。它在加载时把内容解压到内存，无需用户干预。

支持多种可执行文件格式：Linux ELF、Windows PE、macOS Mach-O 等。

解压速度很快，运行时开销极小。可执行文件的原始行为会被原样保留。

测试功能用于验证压缩后的文件是否有效，可以在部署之前发现损坏问题。

# CAVEATS

一些安全工具会将 UPX 压缩过的文件标记为可疑。代码签名可能会因此失效。启动时会因解压产生轻微的开销。部分格式不受支持。

# HISTORY

**UPX** 由 **Markus Oberhumer**、**László Molnár** 和 **John Reiser** 于 **1996 年**创建。它后来成为可执行文件压缩领域的标准工具，被广泛用于软件分发。

# INSTALL

```dnf: sudo dnf install upx```

```pacman: sudo pacman -S upx```

```apk: sudo apk add upx```

```zypper: sudo zypper install upx```

```brew: brew install upx```

```nix: nix profile install nixpkgs#upx```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[strip](/man/strip)(1), [gzip](/man/gzip)(1), [objcopy](/man/objcopy)(1)
