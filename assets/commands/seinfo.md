# TAGLINE

查询和检查 SELinux 策略组件

# TLDR

**显示**当前系统策略的**策略统计信息**

```seinfo```

**列出策略中的所有类型**

```seinfo -t```

以展开信息**显示特定类型的详情**

```seinfo -t [httpd_t] -x```

**列出**类型属性所包含的所有属性

```seinfo -a [exec_type] -x```

**列出策略中的所有角色**

```seinfo -r```

**列出策略中的所有布尔值**

```seinfo -b```

**显示**对象类的约束

```seinfo --constrain [file]```

**查询指定的策略文件**而非系统默认策略

```seinfo [options] [path/to/policy]```

# SYNOPSIS

**seinfo** [_options_] [_expression_] [_policy_]

# PARAMETERS

**-a** [_ATTR_]
> 显示类型属性或某个具名属性的详细信息。

**-b** [_BOOL_]
> 显示布尔值或特定的布尔配置。

**-c** [_CLASS_]
> 列出对象类或特定类的权限。

**-r** [_ROLE_]
> 查询角色或角色相关信息。

**-t** [_TYPE_]
> 检查类型或其被赋予的属性。

**-u** [_USER_]
> 显示用户或用户声明。

**--category** [_CAT_]
> 显示类别或关联的敏感级别。

**--common** [_COMMON_]
> 列出公共权限集合。

**--constrain** [_CLASS_]
> 显示某个对象类的约束和 mlsconstraints。

**--all**
> 查询所有策略组件。

**-x**, **--expand**
> 为每个匹配表达式的组件打印更多细节。

**--flat**
> 不输出格式化标题和缩进。

**-v**, **--verbose**
> 显示额外的信息内容。

**--debug**
> 启用调试输出。

**-h**, **--help**
> 显示帮助文档。

**--version**
> 显示版本信息。

# DESCRIPTION

**seinfo** 是一款 SELinux 策略查询工具，允许用户检查 SELinux 策略的各个组件。它可以分析二进制和源码格式的策略，提供关于类型、属性、角色、用户、布尔值、对象类和约束的详细信息。

未提供策略文件时，seinfo 会搜索系统默认策略：先查找源码格式策略，然后查找与运行中内核首选版本匹配的二进制策略，最后查找可用的最高版本。该工具支持加载源码格式（policy.conf）、二进制格式（如 policy.20）以及带可加载策略模块的模块化格式策略。

seinfo 是 SETools 套件的一部分，常用于启用 SELinux 的系统上的策略分析、调试和安全审计。

# CAVEATS

策略文件必须对运行 seinfo 的用户可读。分析模块化策略时，列出的第一个模块必须是 base 模块。某些查询选项在复杂策略上可能产生大量输出；使用 **--flat** 或通过管道传给分页器可获得更好的可读性。

# HISTORY

**seinfo** 属于 SETools 项目，这是一套最初由 Tresys Technology 开发的 SELinux 策略分析工具。SETools 的创建旨在帮助管理员和安全专业人员理解和管理 SELinux 策略。该项目随 SELinux 的发展持续维护和更新，版本不断演进以支持新的策略特性和格式。

# INSTALL

```apt: sudo apt install setools```

```dnf: sudo dnf install setools```

```nix: nix profile install nixpkgs#setools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sesearch](/man/sesearch)(1), [semanage](/man/semanage)(8), [getenforce](/man/getenforce)(1)
