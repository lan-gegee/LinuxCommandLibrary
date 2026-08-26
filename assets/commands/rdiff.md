# TAGLINE

计算并应用 rsync 风格的文件差异

# TLDR

**创建签名文件**

```rdiff signature [original] [signature.sig]```

**根据签名创建差异**

```rdiff delta [signature.sig] [new_file] [delta.delta]```

**应用差异以重建文件**

```rdiff patch [original] [delta.delta] [output]```

# SYNOPSIS

**rdiff** _command_ [_options_] _files_

# COMMANDS

**signature** _basis_ [_sig_]
> 为基准文件创建签名。

**delta** _sig_ _new_ [_delta_]
> 根据签名和新文件创建差异。

**patch** _basis_ _delta_ [_output_]
> 将差异应用到基准文件。

# PARAMETERS

**-b** _blocksize_
> 签名的块大小（字节）。越小 = 差异越精确，但签名越大。

**-s**, **--statistics**
> 打印签名/差异的耗时和大小统计。

**-S** _sum_
> 签名中强校验和的长度（字节）（默认 8）。

**-H** _hash_
> 哈希算法：`md4`（遗留）或 `blake2`（librsync ≥ 2 的默认值）。

**-R**, **--rollsum**, **-I**, **--rabinkarp**
> 选择滚动校验和变体（rabinkarp 是默认值）。

**-f**, **--force**
> 若输出文件已存在则覆盖。

**-z**, **--compress** _FORMAT_
> 写入时用 `gzip` 或 `bzip2` 压缩差异。

**-v**, **--verbose**
> 提高详细程度。重复使用可获得更多信息。

**-V**, **--version**
> 打印 librsync 版本并退出。

# DESCRIPTION

**rdiff** 使用 rsync 算法计算并应用二进制差异。它只传输文件之间的不同之处，从而实现高效的文件同步。

# EXAMPLES

```bash
# Create signature
rdiff signature original.tar sig.sig

# Create delta (only differences)
rdiff delta sig.sig modified.tar changes.delta

# Apply delta to recreate file
rdiff patch original.tar changes.delta reconstructed.tar

# With statistics
rdiff -s signature largefile sig
```

# WORKFLOW

```
1. Create signature of original (small)
2. Send signature to remote
3. Remote creates delta against new file
4. Send delta back (efficient)
5. Apply delta to reconstruct
```

# CAVEATS

属于 librsync 的一部分。patch 需要基准文件。签名必须与原始文件版本匹配。

# HISTORY

rdiff 采用 **Andrew Tridgell** 提出的 **rsync** 算法，由 **Martin Pool** 在 **librsync** 中实现。

# INSTALL

```apt: sudo apt install rdiff```

```dnf: sudo dnf install librsync```

```pacman: sudo pacman -S librsync```

```apk: sudo apk add librsync```

```zypper: sudo zypper install rdiff```

```brew: brew install librsync```

```nix: nix profile install nixpkgs#librsync```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rsync](/man/rsync)(1), [diff](/man/diff)(1), [patch](/man/patch)(1), [xdelta](/man/xdelta)(1)
