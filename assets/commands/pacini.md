# TAGLINE

解析并查询 pacman 所用格式的 INI 风格配置文件

# TLDR

显示**完整解析后**的配置文件

```pacini [path/to/file]```

列出**已配置的节**

```pacini [path/to/file] --section-list```

即使是单项指令也始终显示**指令名称**

```pacini [path/to/file] --verbose```

显示**特定节**中的指令

```pacini [path/to/file] --section [section_name]```

显示**帮助**

```pacini --help```

# SYNOPSIS

**pacini** [_options_] [_file_] [_directive_...]

# PARAMETERS

**--section-list**
> 列出配置文件中的所有节

**--section** _name_
> 仅查询指定节中的指令

**--verbose**
> 输出中始终显示指令名称

**--null**
> 输出使用 null 分隔符

**--help**
> 显示帮助信息

**--version**
> 显示版本信息

# DESCRIPTION

**pacini** 解析并查询 pacman 所用格式的 INI 风格配置文件。它可以显示完整解析后的配置、列出各个节，或从指定节中提取特定指令的值。

该工具能处理 pacman 配置格式中的 Include 指令，非常适合需要从 pacman.conf 或类似配置文件中提取值的脚本使用。未指定文件时从标准输入读取。

# CAVEATS

仅适用于 pacman 风格的 INI 格式；可能无法正确解析所有 INI 变体。默认不跟随 Include 指令。节的名称区分大小写。

# HISTORY

属于 **pacutils**，Andrew Gregory 编写的 pacman 工具集。提供了一个专门解析 pacman 配置文件的工具，与专门处理 pacman.conf 的 pacconf 相互补充。

# SEE ALSO

[pacconf](/man/pacconf)(8), [pacman.conf](/man/pacman.conf)(5)
