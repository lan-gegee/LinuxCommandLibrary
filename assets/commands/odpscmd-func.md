# TAGLINE

管理用户自定义函数

# TLDR

**列出函数**

```odpscmd func list```

**创建函数**

```odpscmd func create [name] --class [classname] --resource [res]```

**删除函数**

```odpscmd func drop [name]```

**查看函数详情**

```odpscmd func desc [name]```

# SYNOPSIS

**odpscmd** **func** [_command_] [_options_]

# PARAMETERS

**list**
> 列出所有函数。

**create** _NAME_
> 创建函数。

**drop** _NAME_
> 删除函数。

**desc** _NAME_
> 显示函数详情。

**--class** _NAME_
> Java 类名。

**--resource** _RES_
> 资源依赖。

**--help**
> 显示帮助信息。

# DESCRIPTION

**odpscmd func** 管理用户自定义函数，负责创建和维护 UDF。

该工具处理 MaxCompute 函数，属于 odpscmd 套件的一部分。

# CAVEATS

属于旧版工具。需要相应的权限。

# HISTORY

odpscmd func 为 MaxCompute 控制台提供 **UDF 管理**功能。

# SEE ALSO

[odpscmd](/man/odpscmd)(1), [odpscmd-resource](/man/odpscmd-resource)(1)
