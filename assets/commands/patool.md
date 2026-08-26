# TAGLINE

可移植的归档文件管理器，为众多归档格式提供统一接口

# TLDR

**解压**归档

```patool extract [path/to/archive]```

**创建**归档

```patool create [path/to/archive] [files...]```

**列出**归档内容

```patool list [path/to/archive]```

**比较**两个归档

```patool diff [archive1] [archive2]```

在归档中**搜索**字符串

```patool search [pattern] [path/to/archive]```

**测试**归档完整性

```patool test [path/to/archive]```

# SYNOPSIS

**patool** [**extract**|**create**|**list**|**diff**|**search**|**test**|**repack**] [_options_] _archive_ [_files_...]

# COMMANDS

**extract**
> 从归档中解压文件

**create**
> 从文件创建新归档

**list**
> 列出归档内容

**diff**
> 比较两个归档的内容

**search**
> 在归档内容中搜索模式

**test**
> 测试归档完整性

**repack**
> 将归档转换为其他格式

# PARAMETERS

**-v, --verbose**
> 详细输出

**-n, --non-interactive**
> 非交互模式

**--outdir _dir_**
> 解压到指定目录

# DESCRIPTION

**patool** 是一个可移植的归档文件管理器，为众多归档格式提供统一接口。它会自动检测归档类型，并为每种格式选用合适的后端工具。

支持的格式包括 zip、tar、gzip、bzip2、xz、7z、rar、lzma 等。该工具屏蔽了各格式专属的命令，让所有归档类型的操作方式保持一致。

# CAVEATS

每种归档格式都需要相应的后端工具（unzip、tar、7z 等）。部分格式的支持程度取决于可用工具。创建某些格式可能需要特定的实用程序。

# HISTORY

**patool** 由 **Bastian Kleineidam** 创建，旨在简化归档处理。它使用 Python 编写，作为各种归档工具的封装，无论底层格式如何都能提供一致的接口。

# INSTALL

```dnf: sudo dnf install patool```

```zypper: sudo zypper install patool```

```nix: nix profile install nixpkgs#patool```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tar](/man/tar)(1), [unzip](/man/unzip)(1), [7z](/man/7z)(1), [unrar](/man/unrar)(1)
