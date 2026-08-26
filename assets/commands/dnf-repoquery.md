# TAGLINE

查询软件仓库中的软件包信息

# TLDR

查询软件包**依赖关系**

```dnf repoquery --deplist [package]```

# SYNOPSIS

**dnf repoquery** [_options_] [_package_]

# DESCRIPTION

**dnf repoquery** 是一款强大的查询工具，可搜索本地已安装的软件包和远程仓库元数据，无需安装即可查询。它提供详细的软件包信息，包括依赖、文件列表、能力以及软件包之间的关系。

与简单的包列表命令不同，repoquery 支持复杂的查询：查找哪个软件包提供了特定文件或能力、显示某个软件包的全部依赖，或列出某个软件包内的所有文件。--whatprovides 选项特别适合找出缺失的库或命令属于哪个软件包。输出格式可通过 --queryformat 高度定制，非常适合脚本编写和自动化。该工具无需 root 权限，可以不下载就查询仓库中的软件包。

# PARAMETERS

**--deplist**
> 显示依赖关系

**--provides**
> 显示软件包提供的内容

**--requires**
> 显示依赖要求

**--whatprovides** _file_
> 查找提供某文件的软件包

**--installed**
> 仅查询已安装的软件包

**--available**
> 仅查询可用的软件包

**-l, --list**
> 列出软件包内的文件

# CAVEATS

既可查询已安装的软件包，也可查询仓库中的软件包。输出格式可通过 --queryformat 自定义。

# SEE ALSO

[dnf](/man/dnf)(8), [rpm](/man/rpm)(8)

# RESOURCES

```[Source code](https://github.com/rpm-software-management/dnf)```

```[Documentation](https://dnf.readthedocs.io/en/latest/command_ref.html)```

<!-- verified: 2026-07-11 -->
