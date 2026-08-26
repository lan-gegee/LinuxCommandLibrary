# TAGLINE

使用 less 分页器查看压缩文件

# TLDR

**查看 gzip 压缩文件**

```zless [file.gz]```

**顺序查看多个压缩文件**

```zless [file1.gz] [file2.gz]```

**在压缩文件内搜索模式**

```zless [file.gz]```

然后输入 **/**_pattern_ 并按 **Enter**

**跳到压缩文件的最后一行**

```zless [file.gz]```

然后按 **G**

# SYNOPSIS

**zless** [_file ..._]

# PARAMETERS

**less** 中所有可用的参数和命令在 zless 中同样可用，包括：

**Space**
> 向前滚动一屏。

**b**
> 向后滚动一屏。

**/**_pattern_
> 向前搜索模式。

**?**_pattern_
> 向后搜索模式。

**n**
> 重复上一次搜索。

**N**
> 反方向重复上一次搜索。

**g**
> 跳到第一行。

**G**
> 跳到最后一行。

**q**
> 退出。

**h**
> 显示帮助。

# DESCRIPTION

**zless** 是 **gzip** 软件包的一部分。它的原理是将 `LESSOPEN` 设置为先让文件经过 `gzip -cdfq` 管道处理，再交给 **less** 查看。这样既能处理 gzip（.gz）压缩文件，也能处理未压缩的文件（gzip 会原样透传）。

该命令提供与 less 相同的交互式查看体验，包括前后翻页、搜索和跳转行。文件即时解压，不会创建临时文件。

如需支持更多格式（bzip2、xz、zstd 等），请改用配置了 **lesspipe** 作为 `LESSOPEN` 预处理器的 **less**。

# CAVEATS

zless 是 gzip 专用工具，原生不支持 bzip2、xz、lzma 等其他格式。对这些格式，请使用搭配 **lesspipe** 的 **less**，或通过相应的解压器做管道传输（例如 `xz -dc file.xz | less`）。对于 tar.gz 归档，zless 只会解开 gzip 层并显示原始 tar 数据；应改用 **tar -tzf** 列出内容。zless 无法从标准输入读取压缩数据；必须以参数形式给出文件。

# HISTORY

zless 是 **gzip** 软件包的一部分，是作为 zcat 和 zmore 工具的配套工具而创建的。它将 gzip 的解压能力与 **less** 的高级分页特性相结合；由于支持向后滚动和搜索，less 已取代 **more** 成为首选分页器。该命令作为标准 gzip 发行版的一部分，包含在大多数类 Unix 系统中。

# INSTALL

```apt: sudo apt install gzip```

```dnf: sudo dnf install gzip```

```pacman: sudo pacman -S gzip```

```apk: sudo apk add gzip```

```zypper: sudo zypper install gzip```

```brew: brew install gzip```

```nix: nix profile install nixpkgs#gzip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[less](/man/less)(1), [zcat](/man/zcat)(1), [zmore](/man/zmore)(1), [zgrep](/man/zgrep)(1), [gzip](/man/gzip)(1)
