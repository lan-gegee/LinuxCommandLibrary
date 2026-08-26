# TAGLINE

PHP 备份工具

# TLDR

**执行备份**

```phpbu```

**使用特定配置**

```phpbu --configuration=[phpbu.xml]```

**模拟备份**

```phpbu --simulate```

**详细输出**

```phpbu -v```

# SYNOPSIS

**phpbu** [_options_]

# PARAMETERS

**--configuration=**_FILE_
> phpbu XML 配置文件的路径。

**--bootstrap=**_FILE_
> 在运行备份前引入的引导 PHP 文件。

**--simulate**
> 执行试运行，不做任何更改。

**--limit=**_SUBSET_
> 将备份执行限制到指定的子集。

**--restore**
> 打印已配置备份的恢复指南。

**--generate-configuration**
> 以交互方式创建新的配置骨架。

**--colors**
> 启用彩色输出。

**--debug**
> 在备份生成期间显示调试信息。

**-v**, **--verbose**
> 输出更详细的信息。

**-V**, **--version**
> 输出版本信息并退出。

**-h**, **--help**
> 显示用法信息。

# DESCRIPTION

**phpbu** 是 PHP Backup Utility。它自动化备份创建流程。

该工具可处理数据库、文件及同步任务。通过 XML 进行配置。

# CAVEATS

需要进行配置。支持 MySQL、文件等。

# HISTORY

PHPBU 为 **PHP 应用的自动化备份**工作流而创建。

# SEE ALSO

[mysqldump](/man/mysqldump)(1), [rsync](/man/rsync)(1)
