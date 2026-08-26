# TLDR

# TAGLINE

查询 Mageia 软件包信息

# TLDR

显示软件包**信息**

```urpmq -i [package]```

显示**依赖关系**

```urpmq --requires [package]```

显示**递归**依赖

```urpmq -d [package]```

列出该 **RPM** 缺失的依赖

```sudo urpmq -d -m --sources [path/to/file.rpm]```

列出带 URL 的**介质**

```urpmq --list-media --list-url```

带分组和版本的**模糊**搜索

```urpmq -g -r -y [keyword]```

**精确**名称搜索

```urpmq -g -r [package]```

# SYNOPSIS

**urpmq** [_OPTIONS_] [_PACKAGE_...]

# PARAMETERS

**-i**
> 显示软件包信息

**--requires**
> 显示直接依赖

**-d, --requires-recursive**
> 递归显示全部依赖

**-m**
> 显示依赖的来源

**--sources**
> 打印软件包来源

**--list-media**
> 列出已配置的介质

**--list-url**
> 显示介质 URL

**-g**
> 显示软件包所属分组

**-r**
> 显示发行版本信息

**-y, --fuzzy**
> 模糊匹配软件包名称

# DESCRIPTION

**urpmq** 用于查询 Mageia Linux 中软件包和介质的信息。它可以显示软件包详情、依赖关系以及已配置仓库的信息。

属于 Mageia 的 urpmi 软件包管理套件。

# CAVEATS

Mageia 专用。部分操作需要 root 权限。递归依赖查询可能会产生非常长的输出。

# SEE ALSO

[urpmi](/man/urpmi)(8), [urpmf](/man/urpmf)(8), [urpme](/man/urpme)(8)
