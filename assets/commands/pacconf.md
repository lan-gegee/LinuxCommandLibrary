# TAGLINE

按 pacman 自身的解析方式查询并显示其配置

# TLDR

显示**完整解析后**的 pacman 配置

```pacconf```

列出**已配置的仓库**

```pacconf --repo-list```

即使是单项指令也始终显示**指令名称**

```pacconf --verbose [directive]```

仅显示多值选项的**第一个值**

```pacconf --single```

显示**帮助**

```pacconf --help```

# SYNOPSIS

**pacconf** [_options_] [_directive_...]

# PARAMETERS

**--config** _file_
> 使用备用的配置文件

**--root** _path_
> 使用备用的安装根目录

**--repo-list**
> 列出已配置的仓库

**--repo** _name_
> 查询特定仓库的选项

**--verbose**
> 输出中始终显示指令名称

**--single**
> 仅显示多值指令的第一个值

**--null**
> 输出使用 null 分隔符

**--raw**
> 显示未处理的指令值

**--help**
> 显示帮助信息

**--version**
> 显示版本信息

# DESCRIPTION

**pacconf** 按 pacman 自身的解析方式查询并显示其配置。它可以显示完整的配置或特定指令的值，非常适合需要读取 pacman 设置的脚本使用。

该工具会处理配置中的 include 指令，并以与 pacman 相同的方式处理值，从而准确呈现实际生效的配置。它可以查询全局选项或特定仓库的设置。

# CAVEATS

输出反映的是解析后的配置，由于 include 和默认值的存在，可能与原始配置文件有所不同。查询特定仓库需要 **--repo** 选项。

# HISTORY

属于 **pacutils**，Andrew Gregory 编写的 pacman 辅助工具集。提供对 pacman 配置的程序化访问，适用于与 pacman 交互的系统管理脚本和工具。

# SEE ALSO

[pacman](/man/pacman)(8), [pacman.conf](/man/pacman.conf)(5), [paccheck](/man/paccheck)(8)
