# TAGLINE

管理 PHP 归档（PHAR）文件，将 PHP 应用打包为单个可分发文件

# TLDR

向 PHAR 归档**添加**文件

```phar add -f [path/to/archive.phar] [files...]```

**列出**归档内容

```phar list -f [path/to/archive.phar]```

从归档中**删除**文件

```phar delete -f [path/to/archive.phar] -e [file]```

**压缩**归档内容

```phar compress -f [path/to/archive.phar] -c [gzip|bzip2]```

**获取**归档信息

```phar info -f [path/to/archive.phar]```

用哈希算法**签名**

```phar sign -f [path/to/archive.phar] -h [sha256|sha512]```

显示**帮助**

```phar help```

# SYNOPSIS

**phar** _command_ [**-f** _archive_] [_options_] [_files_...]

# COMMANDS

**add**
> 向归档添加文件或目录

**list**
> 列出归档内容

**delete**
> 从归档移除文件

**compress**
> 压缩归档内容

**info**
> 显示归档信息

**sign**
> 用哈希或密钥对归档签名

**extract**
> 解压归档内容

# PARAMETERS

**-f _archive_**
> 要操作的 PHAR 归档文件

**-c _algorithm_**
> 压缩算法（gzip、bzip2）

**-h _algorithm_**
> 用于签名的哈希算法

**-y _keyfile_**
> 用于 OpenSSL 签名的私钥文件

**-e _entry_**
> 归档中的特定条目

# DESCRIPTION

**phar** 管理 PHP Archive（PHAR）文件，这类文件将 PHP 应用打包为单个可分发的文件。PHAR 文件可以包含 PHP 代码、资源和元数据，并且能被 PHP 直接执行。

该工具支持创建、修改、解压和签名 PHAR 归档。签名通过哈希算法或 OpenSSL 密钥保证归档的完整性与真实性。

# CAVEATS

执行写操作需要在 php.ini 中设置 phar.readonly=0。OpenSSL 签名需要 OpenSSL 扩展。处理大型归档时可能消耗大量内存。

# HISTORY

**PHAR**（PHP Archive）在 PHP 5.3 中引入，作为分发 PHP 应用的原生方式。phar 命令行工具让开发者无需编写 PHP 脚本即可管理归档。

# INSTALL

```apk: sudo apk add php85-phar```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[php](/man/php)(1), [composer](/man/composer)(1)
