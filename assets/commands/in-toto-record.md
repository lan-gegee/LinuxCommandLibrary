# TAGLINE

为构建步骤创建供应链证明

# TLDR

**开始记录**

```in-toto-record start -n [step_name] -k [key.pem]```

**结束记录**

```in-toto-record stop -n [step_name] -k [key.pem] -p [products]```

**带输入物记录**

```in-toto-record start -n [step] -k [key] -m [src/]```

**指定产物**

```in-toto-record stop -n [step] -k [key] -p [dist/]```

# SYNOPSIS

**in-toto-record** _command_ [_options_]

# PARAMETERS

**start**
> 开始记录步骤。

**stop**
> 结束记录步骤。

**-n** _NAME_
> 步骤名称（用于将链接与布局中的步骤关联）。

**-k** _KEY_, **--signing-key** _KEY_
> 签名密钥文件的路径。

**-g** _ID_, **--gpg** _ID_
> 用于对生成的链接元数据进行签名的 GPG keyid。

**--gpg-home** _PATH_
> GPG 主目录的路径。

**-m** _MATERIALS_
> 输入物的路径（与 start 搭配使用）。

**-p** _PRODUCTS_
> 产物的路径（与 stop 搭配使用）。

**-d** _DIR_
> 存储生成的链接元数据的目录（与 stop 搭配使用）。

**--exclude** _PATTERN_
> 记录时要排除的路径模式。

**--base-path** _PATH_
> 相对输入物/产物路径的基准路径。

**--lstrip-paths** _PREFIX_
> 在存入链接元数据前去除路径左侧的前缀。

**--use-dsse**
> 使用 DSSE 信封格式进行签名。

**-v**
> 详细输出。

**-q**
> 安静模式。

# DESCRIPTION

**in-toto-record** 为构建步骤创建供应链证明。它在一个步骤之前记录输入物、之后记录产物，并生成经过签名的链接元数据。

该工具支持拆分记录，即 start 和 stop 是两条独立命令。这样可以记录跨多条命令或多个会话执行的步骤。

# CAVEATS

需要签名密钥。属于 in-toto 框架。链接必须经过验证。

# HISTORY

in-toto-record 是 **in-toto** 的一部分，这是一个由 **纽约大学** 安全系统实验室开发的供应链完整性框架。

# SEE ALSO

[in-toto-run](/man/in-toto-run)(1), [in-toto-sign](/man/in-toto-sign)(1)
