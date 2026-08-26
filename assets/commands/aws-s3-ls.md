# TAGLINE

列出 S3 存储桶和对象

# TLDR

**列出账户中的所有 S3 存储桶**

```aws s3 ls```

**列出**存储桶中的**对象**

```aws s3 ls s3://[bucket-name]/```

**列出**特定前缀下的**对象**

```aws s3 ls s3://[bucket-name]/[prefix/]```

**递归列出**存储桶中的所有对象

```aws s3 ls s3://[bucket-name] --recursive```

以**人类可读的大小**列出并显示汇总信息

```aws s3 ls s3://[bucket-name] --recursive --human-readable --summarize```

**列出**以特定前缀开头的**存储桶**

```aws s3 ls --bucket-name-prefix [my-prefix]```

# SYNOPSIS

**aws s3 ls** [_S3Uri_] [_options_]

# DESCRIPTION

**aws s3 ls** 列出指定前缀下的 S3 对象和公共前缀（common prefix），未提供 URI 时则列出所有 S3 存储桶。输出会显示每一项的最后修改日期、大小和对象键。

列出的存储桶内容中，对象会带时间戳和大小显示，而公共前缀（类似于目录）则以 **PRE** 标识显示。该命令支持递归列出，可显示某个前缀下的所有对象。

# PARAMETERS

**--recursive**
> 列出指定前缀下的所有对象，包括嵌套对象

**--human-readable**
> 以人类可读的格式（KB、MB、GB）显示文件大小

**--summarize**
> 显示汇总信息，包括对象总数和总大小

**--page-size** _value_
> 每个响应返回的结果数（默认：1000）

**--request-payer** _value_
> 确认请求方将承担请求和数据传输费用

**--bucket-name-prefix** _value_
> 将存储桶列表过滤为以指定前缀开头的名称

**--bucket-region** _value_
> 将存储桶列表过滤为位于指定 AWS 区域的存储桶

# CAVEATS

全局参数 **--output** 和 **--no-paginate** 在此命令中会被忽略。输出格式是固定的，无法更改为 JSON 或其他格式。若要以灵活的输出对 S3 列表进行编程式访问，请改用 **aws s3api list-objects-v2**。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws-s3](/man/aws-s3)(1), [aws-s3-cp](/man/aws-s3-cp)(1), [aws-s3api](/man/aws-s3api)(1), [ls](/man/ls)(1)

# RESOURCES

```[Source code](https://github.com/aws/aws-cli)```

```[Homepage](https://aws.amazon.com/cli/)```

```[Documentation](https://docs.aws.amazon.com/cli/latest/reference/s3/ls.html)```

<!-- verified: 2026-06-18 -->
