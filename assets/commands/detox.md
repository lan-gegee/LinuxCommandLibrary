# TAGLINE

清理有问题的文件名

# TLDR

**清理当前目录中的文件名**

```detox *```

**递归清理文件名**

```detox -r [directory]```

**预览更改**而不实际重命名

```detox -n [files]```

**显示详细输出**

```detox -v [files]```

**使用指定的过滤序列**

```detox -s [iso8859_1] [files]```

**列出可用的序列**

```detox -L```

# SYNOPSIS

**detox** [_options_] _file-or-directory_...

# PARAMETERS

_FILE_
> 要处理的文件或目录。

**-r**, **--recurse**
> 递归处理目录。

**-n**, **--dry-run**
> 显示将要进行的重命名但不实际修改。

**-v**, **--verbose**
> 输出详细信息，显示重命名过程。

**-s** _SEQUENCE_
> 要使用的清理序列（默认运行 safe 和 wipeup 过滤器）。

**-L**
> 列出当前可用的序列。

**--special**
> 同时处理链接和特殊文件。

**-f** _FILE_
> 使用指定的配置文件而不是默认配置。

**--help**
> 显示帮助信息。

# DESCRIPTION

**detox** 通过将有问题的字符替换为安全字符来清理文件名。它能处理空格、特殊字符、Unicode 字符以及其他可能在 shell 脚本或跨平台文件共享中引发问题的元素。

该工具应用可配置的转换序列，包括把空格替换为下划线、移除或转写非 ASCII 字符、修复大小写问题等。多个内置序列应对不同的清理场景。

detox 对于批量处理来自 Windows 系统的文件、命名复杂的音乐库，或任何命名规范不一致的来源都很有价值。

# CONFIGURATION

**/etc/detoxrc** 或 **~/.detoxrc**
> 定义清理序列和文件名过滤器的配置文件。

# CAVEATS

可能产生重名文件，需要手动解决。没有备份时操作不可逆。Unicode 转写可能丢失信息。某些序列比较激进，可能把名字过度简化。

# HISTORY

detox 由 **Doug Harple** 编写，用于解决 Unix 环境中管理问题文件名的常见困扰。它为文件名净化提供了系统化的方法。

# INSTALL

```apt: sudo apt install detox```

```dnf: sudo dnf install detox```

```pacman: sudo pacman -S detox```

```brew: brew install detox```

```nix: nix profile install nixpkgs#detox```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rename](/man/rename)(1), [mv](/man/mv)(1), [convmv](/man/convmv)(1)

# RESOURCES

```[Source code](https://github.com/dharple/detox)```

<!-- verified: 2026-07-11 -->
