# TAGLINE

用于终端显示的 nroff 输出过滤器

# TLDR

**过滤 nroff 输出**以便在终端上显示

```colcrt [file]```

**抑制下划线**

```colcrt -2 [file]```

**半行处理**

```colcrt - [file]```

通过管道**处理 nroff 输出**

```nroff -man [man.1] | colcrt```

# SYNOPSIS

**colcrt** [_options_] [_file_...]

# DESCRIPTION

**colcrt** 用于过滤 nroff 输出，以便在 CRT（终端）上预览。它处理反向换行，并将下划线和半行移动转换为适合终端显示的形式。

该工具主要用于在无法处理叠印的终端上预览格式化后的 man 手册页及其他 nroff 输出。它将下划线转换为单独一行上的破折号。

# PARAMETERS

**-**
> 将半行按整行打印，适用于不支持半行的终端。

**-2**
> 完全抑制下划线，只打印文本。

# CAVEATS

为老式终端的处理而设计。现代终端通常能直接处理 nroff 输出。输出可能无法保留全部格式。主要是具有历史意义的工具。

# HISTORY

**colcrt** 是一款传统 Unix 工具，可追溯到 **1970 年代**的 **BSD** 系统。它诞生于各终端能力参差不齐、并非都能处理 nroff 输出中转义序列的年代。如今虽已很少需要，但仍保留在许多 Unix 发行版中。

# INSTALL

```apt: sudo apt install bsdextrautils```

```apk: sudo apk add util-linux-misc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nroff](/man/nroff)(1), [col](/man/col)(1), [ul](/man/ul)(1), [man](/man/man)(1)

# RESOURCES

```[Source code](https://github.com/util-linux/util-linux)```

```[Documentation](https://man7.org/linux/man-pages/man1/colcrt.1.html)```

<!-- verified: 2026-06-22 -->
