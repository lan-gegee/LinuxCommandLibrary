# TAGLINE

PHP 的 API 文档生成器

# TLDR

**生成文档**

```doctum update [doctum.php]```

**解析并渲染**文档

```doctum render [doctum.php]```

一步完成**更新与渲染**

```doctum update [doctum.php] --force```

**显示详细输出**

```doctum update -v [doctum.php]```

# SYNOPSIS

**doctum** _command_ [_options_] _config-file_

# PARAMETERS

_COMMAND_
> 操作：update、render、parse。

_CONFIG-FILE_
> PHP 配置文件。

**update**
> 解析源码并渲染文档。

**render**
> 基于缓存的解析数据进行渲染。

**parse**
> 仅解析源码，不渲染。

**--force**
> 强制完整重新生成。

**--only-version** _VERSION_
> 将构建限制在指定版本。

**--no-progress**
> 禁用进度条。

**--ignore-parse-errors**
> 忽略解析错误并以退出码 0 结束。

**-v**, **--verbose**
> 详细输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**Doctum** 是一个面向 PHP 项目的 API 文档生成器。它解析 PHP 源码并生成可浏览的 HTML 文档，包含类层次结构、方法签名和 docblock 注释。

该工具是 Sami 的分支版本，提供了持续的维护和改进。它支持现代 PHP 特性，包括 trait、命名空间和类型声明。配置通过 PHP 文件完成，可实现灵活的自定义。

Doctum 生成的文档可搜索，并在类与方法之间建立交叉引用，非常适合用于编写库和框架的文档。

# CONFIGURATION

**doctum.php**
> 配置文件，用于定义源码目录、构建路径、主题和解析选项。

# CAVEATS

需要 PHP 8.1 及以上版本。大型代码库的首次解析可能较慢。编写配置需要具备 PHP 知识。某些 PHP 边缘情况可能无法正确解析。

# HISTORY

Doctum 是 **Sami** 的分支版本，Sami 由 **Fabien Potencier**（Symfony 的创造者）最初开发。当 Sami 被弃用时，Doctum 作为社区维护的延续版本出现，继续为 PHP 项目提供 API 文档生成能力。

# SEE ALSO

[phpdoc](/man/phpdoc)(1), [doxygen](/man/doxygen)(1), [php](/man/php)(1)
