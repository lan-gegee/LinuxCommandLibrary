# TAGLINE

使用 less 分页器查看 bzip2 压缩文件

# TLDR

**查看**压缩文件

```bzless [file.txt.bz2]```

# SYNOPSIS

**bzless** [_file_...]

# DESCRIPTION

**bzless** 是一个用于查看 bzip2 压缩文件的过滤器，基于 less 分页器。它会即时解压文件，并提供 less 的全部功能，可用于导航、搜索和查看。

该工具将 bzcat 与 less 结合，方便地查看压缩文件。

# FEATURES

- 完整的 less 导航功能
- 在压缩文件内搜索
- 无需解压到磁盘
- 支持多个文件
- 保留原始文件

# LESS KEYBINDINGS

- **Space/f** - 向下翻页
- **b** - 向上翻页
- **/pattern** - 向前搜索
- **?pattern** - 向后搜索
- **n** - 下一个匹配
- **q** - 退出

# WORKFLOW

```bash
# View compressed log
bzless logfile.bz2

# View multiple files
bzless file1.bz2 file2.bz2

# Search within
bzless logfile.bz2
# Then: /error
```

# CAVEATS

为便于浏览会解压整个文件。无法编辑文件。比查看未压缩文件慢。较大的压缩文件加载可能较慢。

# HISTORY

**bzless** 自 **1996** 年起就是 bzip2 工具集的一部分，仿照针对 gzip 文件的 zless 设计。

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

[less](/man/less)(1), [bzcat](/man/bzcat)(1), [bzmore](/man/bzmore)(1), [zless](/man/zless)(1)

# RESOURCES

```[Source code](https://gitlab.com/bzip2/bzip2)```

```[Homepage](https://sourceware.org/bzip2/)```

<!-- verified: 2026-06-22 -->
