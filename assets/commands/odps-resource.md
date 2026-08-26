# TAGLINE

管理 MaxCompute（ODPS）资源

# TLDR

**列出当前项目中的所有资源**

```odps resource list```

**上传 JAR 资源**

```odps resource add [file.jar] -t jar```

**上传 Python 文件资源**

```odps resource add [script.py] -t py```

**上传通用文件资源并添加注释**

```odps resource add [data.csv] -t file -c "[description]"```

**按名称删除资源**

```odps resource drop [resource_name]```

**下载资源到本地文件**

```odps resource get [resource_name] -o [output_file]```

# SYNOPSIS

**odps** **resource** [_command_] [_options_]

# PARAMETERS

**list**
> 列出当前项目中的所有资源。

**add** _FILE_
> 将本地文件作为资源上传。

**drop** _NAME_
> 按名称删除资源。

**get** _NAME_
> 将资源下载到本地存储。

**-t** _TYPE_
> 资源类型：jar、py、file、archive 或 table。

**-c** _COMMENT_
> 为资源添加注释或描述。

**-o** _OUTPUT_
> get 命令的输出文件路径。

**-f**
> 若资源已存在则强制覆盖。

**--help**
> 显示帮助信息。

# DESCRIPTION

**odps resource** 管理阿里云 MaxCompute（前身为 ODPS）中的资源。资源包括供 UDF 使用的 JAR 文件、Python 脚本、普通文件以及可被 MaxCompute 作业引用的归档。

上传的资源保存在当前项目中，可用于 SQL 语句、MapReduce 作业和用户自定义函数。属于 ODPS CLI（odpscmd）工具集的一部分。

# CAVEATS

存在资源大小限制（文件默认为 512 MB）。需要包含项目和凭证的有效 ODPS 配置。资源名在同一项目内必须唯一；使用 -f 可覆盖已有资源。

# HISTORY

odps resource 为阿里云 MaxCompute 提供**资源管理**功能。

# SEE ALSO

[odps](/man/odps)(1), [odps-func](/man/odps-func)(1), [odps-tunnel](/man/odps-tunnel)(1)
