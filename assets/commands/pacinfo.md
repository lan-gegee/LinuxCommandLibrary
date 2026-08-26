# TAGLINE

从 pacman 数据库显示软件包的详细信息

# TLDR

显示**特定软件包**的信息

```pacinfo [package_name]```

禁用下载的**低速超时**

```pacinfo --no-timeout [package_name]```

以字节显示大小并以 **Unix 时间戳**显示日期

```pacinfo --raw [package_name]```

显示**额外的**软件包信息

```pacinfo --verbose [package_name]```

显示**帮助**

```pacinfo --help```

# SYNOPSIS

**pacinfo** [_options_] _package_...

# PARAMETERS

**--raw**
> 以字节显示大小并以 Unix 时间戳显示日期

**--verbose**
> 显示额外的软件包信息

**--no-timeout**
> 禁用低速下载超时

**--config** _file_
> 使用备用的 pacman 配置文件

**--dbpath** _path_
> 使用备用的数据库路径

**--root** _path_
> 使用备用的安装根目录

**--help**
> 显示帮助信息

**--version**
> 显示版本信息

# DESCRIPTION

**pacinfo** 从 pacman 数据库显示软件包的详细信息。它展示软件包元数据，包括名称、版本、描述、依赖、安装日期、大小以及存储在软件包数据库中的其他属性。

该工具可以查询本地已安装的软件包以及已配置仓库中可用的软件包。相比 pacman 内置的查询命令，它提供了更多详细的输出选项，并带有便于脚本处理的机器可读原始输出。

# CAVEATS

要求软件包存在于 pacman 数据库中（已安装或在仓库中可用）。若同步数据库不是最新的，查询仓库软件包需要联网。

# HISTORY

属于 **pacutils**，Andrew Gregory 编写的 pacman 辅助工具集。相比标准的 **pacman -Qi** 和 **pacman -Si** 命令，提供了增强的软件包信息显示能力。

# SEE ALSO

[pacman](/man/pacman)(8), [pacconf](/man/pacconf)(8), [pacsift](/man/pacsift)(8)
