# TAGLINE

现代化的模块化 TUI 十六进制编辑器

# TLDR

在十六进制编辑器中**打开文件**

```hexabyte [path/to/file]```

**打开单个文件**并以分屏视图显示

```hexabyte -s [path/to/file]```

**并排打开两个文件**进行比较

```hexabyte [path/to/file1] [path/to/file2]```

**使用自定义配置文件**

```hexabyte -c [path/to/config.toml] [path/to/file]```

# SYNOPSIS

**hexabyte** [_options_] _file_ [_file2_]

# PARAMETERS

**-s**, **--split**
> 在两个分屏编辑器中显示单个文件。

**-c**, **--config** _FILE_
> 使用自定义配置文件（默认：`~/.config/hexabyte/config.toml`）。

**-h**, **--help**
> 显示帮助信息并退出。

# DESCRIPTION

**hexabyte** 是一个现代化、模块化且健壮的 TUI 十六进制编辑器，用于在字节级别修改文件内容。它支持以十六进制、UTF-8 文本和二进制方式查看与编辑，并提供多种显示模式：**单文件**编辑、针对同一文件的**分屏**视图，以及同时打开两个文件时的**比较（diff）**模式。

该编辑器采用可扩展的插件架构，提供标准的十六进制编辑操作，包括插入、删除和替换字节，以及选择和复制/粘贴字节区间。

# CAVEATS

需要 Python 3.10 及以上版本。非常大的文件可能影响性能。比较模式会高亮字节级差异，对于结构差异较大的文件可能产生大量噪声输出。

# HISTORY

**hexabyte** 由 **thetacom** 创建，使用 **Python** 编写。其设计目标是成为传统终端十六进制编辑器的现代、可扩展替代品。

# INSTALL

```aur: yay -S hexabyte```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hexyl](/man/hexyl)(1), [xxd](/man/xxd)(1), [heh](/man/heh)(1)
