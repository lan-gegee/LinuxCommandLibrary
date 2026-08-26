# TAGLINE

从 S3 删除对象

# TLDR

从 S3 **删除单个对象**

```aws s3 rm s3://[bucket-name]/[file.txt]```

**递归删除**某个前缀下的所有对象

```aws s3 rm s3://[bucket-name]/[prefix/] --recursive```

**删除存储桶中的所有对象**

```aws s3 rm s3://[bucket-name] --recursive```

**删除时排除**某些文件类型之外的所有对象

```aws s3 rm s3://[bucket-name]/ --recursive --exclude "*.jpg"```

**预览删除操作**而不实际执行

```aws s3 rm s3://[bucket-name]/ --recursive --dryrun```

# SYNOPSIS

**aws s3 rm** _S3Uri_ [_options_]

# DESCRIPTION

**aws s3 rm** 从 Amazon S3 删除对象。默认只删除单个对象。使用 **--recursive** 选项可删除指定前缀下的所有对象。

该命令支持通过 **--include** 和 **--exclude** 选项进行模式匹配，从而按条件选择性地删除对象。

# PARAMETERS

**S3Uri**
> 要删除的对象或前缀的 S3 URI（s3://bucket-name/key）

**--recursive**
> 删除指定前缀下的所有对象

**--dryrun**
> 显示将要执行的操作但不实际执行

**--quiet**
> 在删除过程中抑制输出

**--include** _pattern_
> 包含匹配模式的对象（与 --exclude 配合使用）

**--exclude** _pattern_
> 从删除中排除匹配模式的对象

**--only-show-errors**
> 仅显示错误和警告，抑制成功操作的输出

**--page-size** _value_
> 每次 API 调用获取的对象数（默认：1000）

# CAVEATS

此命令删除的是未版本化的对象。对于启用版本控制的存储桶，删除操作只会创建删除标记，并不会永久移除之前的版本。要永久删除已版本化的对象，请使用 **aws s3api delete-object** 配合 **--version-id**。对未版本化的存储桶而言，删除是永久性的，无法撤销。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws-s3](/man/aws-s3)(1), [aws-s3-rb](/man/aws-s3-rb)(1), [rm](/man/rm)(1)

# RESOURCES

```[Source code](https://github.com/aws/aws-cli)```

```[Homepage](https://aws.amazon.com/cli/)```

```[Documentation](https://docs.aws.amazon.com/cli/latest/reference/s3/rm.html)```

<!-- verified: 2026-06-18 -->
