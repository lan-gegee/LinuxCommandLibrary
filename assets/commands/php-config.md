# TAGLINE

显示 PHP 编译期配置的相关信息

# TLDR

**显示 PHP 的安装前缀**

```php-config --prefix```

**显示扩展目录路径**

```php-config --extension-dir```

**显示头文件包含目录**

```php-config --include-dir```

**显示构建扩展所需的编译器 include 标志**

```php-config --includes```

**显示构建 PHP 时使用的 configure 选项**

```php-config --configure-options```

**显示 PHP 版本**

```php-config --version```

**显示 PHP 二进制文件路径**

```php-config --php-binary```

**显示所有可用的 SAPI 模块**

```php-config --php-sapis```

# SYNOPSIS

**php-config** [_options_]

# PARAMETERS

**--prefix**
> PHP 的安装前缀目录（如 /usr 或 /usr/local）。

**--includes**
> 所有包含目录的编译器 -I 标志，构建扩展时使用。

**--ldflags**
> 编译 PHP 时使用的链接器标志。

**--libs**
> 编译 PHP 时链接的额外库。

**--extension-dir**
> 扩展默认的安装与加载目录。

**--include-dir**
> 头文件的安装目录前缀。

**--php-binary**
> PHP CLI 或 CGI 二进制文件的完整路径。

**--php-sapis**
> 列出所有可用的 SAPI（Server API）模块（如 cli、fpm、apache2handler）。

**--configure-options**
> 构建 PHP 时使用的 ./configure 选项，可用于重现相同的构建。

**--version**
> PHP 版本字符串。

**--vernum**
> 以整数表示的 PHP 版本（如 8.2.0 对应 80200），便于在脚本中使用。

**--ini-path**
> PHP 读取主 INI 配置文件所在的目录。

**--ini-dir**
> PHP 扫描附加 INI 配置文件的目录。

# DESCRIPTION

**php-config** 是一个 shell 脚本，提供关于 PHP 编译期配置的信息。使用 **phpize** 构建 PHP 扩展以及编写需要链接 PHP 的 Makefile 时，它必不可少。

扩展开发中的典型用法是把 **--includes** 和 **--ldflags** 传给编译器，并通过 **./configure --with-php-config=/path/to/php-config** 指定 php-config 的完整路径。

# CAVEATS

输出因 PHP 安装和版本而异。安装了多个 PHP 版本时，每个版本都有自己的 php-config（如 php-config7.4、php-config8.2）。构建扩展时务必使用与目标 PHP 版本对应的路径。

# INSTALL

```apk: sudo apk add php85-dev```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[phpize](/man/phpize)(1), [php](/man/php)(1), [pecl](/man/pecl)(1)
