# TAGLINE

管理 MaxCompute（ODPS）项目资源

# TLDR

**列出当前项目中的所有资源**

```odpscmd resource list```

**添加 JAR 资源**

```odpscmd resource add jar [file.jar]```

**添加 Python 资源**

```odpscmd resource add py [file.py]```

**添加带注释的文件资源**

```odpscmd resource add file [data.csv] -c "[description]"```

**添加归档资源**

```odpscmd resource add archive [file.tar.gz]```

**查看资源详情**

```odpscmd resource desc [resource_name]```

**删除资源**

```odpscmd resource drop [resource_name]```

# SYNOPSIS

**odpscmd** **resource** _command_ [_options_]

# PARAMETERS

**list**
> 列出当前项目中的所有资源。

**add** _TYPE_ _FILE_ [**-c** _COMMENT_]
> 上传资源。TYPE 可以是：jar、py、file、archive、table。

**drop** _NAME_
> 按名称删除资源。

**desc** _NAME_
> 显示资源的元数据和详情。

**-c** _COMMENT_
> 上传资源时添加注释或描述。

**-f**
> 若同名资源已存在则强制覆盖。

**--help**
> 显示帮助信息。

# DESCRIPTION

**odpscmd resource** 管理阿里云 MaxCompute（前身为 ODPS）项目中的资源。资源是上传到项目中的文件，可被 MapReduce 作业、UDF（用户自定义函数）和 Graph 作业引用。

支持的资源类型包括：用于 Java UDF 和 MapReduce 程序的 JAR 文件，用于 PyODPS UDF 的 Python 文件，用于数据的普通文件，以及用于打包依赖的归档（tar.gz、zip）。table 资源则引用已有的 MaxCompute 表。

资源必须先上传才能在函数定义或作业提交中使用。每个资源在项目内名称唯一，并且可以附带可选的注释以便说明用途。

# CAVEATS

单个资源文件有大小限制（通常为 500 MB，具体因配置而异）。资源名在同一项目内必须唯一。覆盖已有资源需要 **-f** 标志。属于 odpscmd CLI 的一部分，后者需要有效的 MaxCompute 项目配置。

# HISTORY

odpscmd resource 是 **MaxCompute 控制台**（odpscmd）的组成部分，后者是阿里云用于管理 MaxCompute 项目的命令行工具，最初名为 ODPS（Open Data Processing Service）。

# INSTALL

```aur: yay -S odpscmd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[odpscmd](/man/odpscmd)(1), [odpscmd-func](/man/odpscmd-func)(1), [odpscmd-auth](/man/odpscmd-auth)(1), [odpscmd-tunnel](/man/odpscmd-tunnel)(1)
