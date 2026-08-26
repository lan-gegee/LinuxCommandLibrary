# TAGLINE

功能丰富的终端分页器，less 的替代品

# TLDR

**查看文件**

```ov [path/to/file]```

**查看压缩文件**

```ov [file.gz]```

**查看多个文件**

```ov [file1] [file2]```

**跟踪日志文件**（类似 tail -f）

```ov --follow-mode [path/to/log]```

**带行号查看**

```ov -n [path/to/file]```

**以列模式并指定分隔符查看**

```ov -d "," [data.csv]```

**用作系统分页器**

```export PAGER=ov```

# SYNOPSIS

**ov** [_options_] [_files_...]

# DESCRIPTION

**ov** 是一款功能丰富的终端分页器，可作为 less 和 more 的替代品。它支持压缩文件（gzip、bzip2、zstd、lz4、xz）、多色高亮、快速打开大文件以及同时查看多个文件。

它可以用作系统级的 **PAGER** 替代品。

# PARAMETERS

**-n**
> 显示行号。

**-d** _delimiter_
> 使用指定分隔符的列模式。

**-H** _n_
> 固定在顶部的表头行数。

**--follow-mode**
> 跟踪文件更新（类似 tail -f）。

**--follow-all**
> 同时跟踪所有文件。

**-w**
> 换行显示长行。

**--tab-width** _n_
> 制表符宽度（默认 8）。

# CAVEATS

部分按键绑定与 less 不同。习惯 less 导航方式的用户可能需要适应。

# HISTORY

**ov** 由 **Noboru Saito**（noborus）创建，使用 **Go** 编写。

# INSTALL

```dnf: sudo dnf install ov```

```brew: brew install ov```

```nix: nix profile install nixpkgs#ov```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[less](/man/less)(1), [more](/man/more)(1), [bat](/man/bat)(1)
