# TAGLINE

通过 odpscmd 管理 MaxCompute 用户自定义函数

# TLDR

**列出当前项目中的函数**

```list functions;```

**查看函数详情**

```desc function [name];```

**基于已上传的资源创建函数**

```create function [name] as '[package.ClassName]' using '[resource.jar]';```

**删除函数**

```drop function [name];```

**显示内置函数**

```show builtin functions;```

# SYNOPSIS

在 **odpscmd** 客户端中以类 SQL 语句执行：

**list** **functions** [**-p** _project_]**;**
**desc** **function** _name_**;**
**create** **function** _name_ **as** '_class_' **using** '_resources_'**;**
**drop** **function** _name_**;**

# PARAMETERS

**list functions**
> 列出用户自定义函数（别名：**show functions**）。

**desc function** _name_
> 显示函数的所有者、创建时间、类名和资源。

**create function** _name_ **as** '_class_' **using** '_resources_'
> 注册新的 UDF。_class_ 是全限定 Java 类或 Python 模块；_resources_ 是已上传资源的逗号分隔列表。

**drop function** _name_
> 删除 UDF（需要删除权限）。

**show builtin functions** [_name_]
> 列出或描述 MaxCompute 内置函数（客户端 v0.43.0+）。

**-p** _project_
> 在特定项目上操作（仅限 list functions）。

# DESCRIPTION

MaxCompute UDF 通过 **odpscmd** 命令行客户端发出的类 SQL 语句进行管理。必须先使用 `add jar` / `add py` / `add archive` 上传资源（jar、py 文件、归档），然后函数才能引用它。

函数名在同一项目内唯一。用户需要对项目拥有写权限才能创建函数，拥有删除权限才能删除函数。

# CAVEATS

需要已完成配置且能访问项目的 odpscmd 客户端。通过 odpscmd 或 MaxCompute Studio 注册的 UDF 不会自动出现在 DataWorks 中。对于 Python UDF，请确保项目支持相应的 Python 运行时。

# HISTORY

属于**阿里云 MaxCompute**（ODPS）CLI 工具链的一部分。UDF 支持自 MaxCompute 首次公开发布以来一直是其核心特性。

# SEE ALSO

[odps](/man/odps)(1), [odps-resource](/man/odps-resource)(1)
