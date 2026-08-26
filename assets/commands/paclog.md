# TAGLINE

过滤并显示 pacman 日志文件中的条目

# TLDR

显示**完整的 pacman 日志**

```paclog```

显示日志中 pacman 风格的**命令行条目**

```paclog --commandline```

显示**特定软件包**的日志事件

```paclog --package [package_name]```

显示**特定类型**的软件包操作

```paclog --action [install|reinstall|upgrade|downgrade|remove|all]```

仅显示**错误、警告和提示**

```paclog --warnings```

根据日志显示**已安装软件包**列表

```paclog --pkglist```

# SYNOPSIS

**paclog** [_options_]

# PARAMETERS

**--commandline**
> 显示日志中的命令行条目

**--package _name_**
> 过滤特定软件包的条目

**--action _type_**
> 按操作过滤：install、reinstall、upgrade、downgrade、remove、all

**--warnings**
> 仅显示警告、错误和提示

**--pkglist**
> 根据日志列出当前已安装的软件包

**--after _date_**
> 显示指定日期之后的条目

**--before _date_**
> 显示指定日期之前的条目

**--logfile _file_**
> 使用备用的日志文件

**--help**
> 显示帮助信息

**--version**
> 显示版本信息

# DESCRIPTION

**paclog** 过滤并显示 pacman 日志文件（/var/log/pacman.log）中的条目。它以结构化的方式访问软件包管理历史，便于查看软件包何时被安装、升级或移除。

作为 **pacutils** 工具集的一部分，paclog 可以按软件包名称、操作类型、日期范围或严重级别进行过滤。这对于通过回顾最近的软件包变更来排查系统问题，或追踪特定软件包的历史非常有用。

**--pkglist** 选项通过重放日志重建当前的已安装软件包列表，适用于验证或恢复场景。

# CAVEATS

依赖完整无缺的 pacman.log 文件。日志轮转或清空会导致历史数据丢失。属于 pacutils 软件包（Arch 上默认不安装）。日期解析要求特定的格式。

# SEE ALSO

[pacman](/man/pacman)(8), [pactree](/man/pactree)(8), [pacsift](/man/pacsift)(1), [pacinfo](/man/pacinfo)(1)
