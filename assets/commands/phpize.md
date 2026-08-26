# TAGLINE

为编译准备 PHP 扩展

# TLDR

**为构建准备扩展**

```phpize```

**清理生成的文件**

```phpize --clean```

**显示版本**

```phpize --version```

**使用特定 PHP 版本**

```/usr/bin/phpize[7.4]```

# SYNOPSIS

**phpize** [_--clean_] [_--version_]

# PARAMETERS

**--clean**
> 删除生成的文件。

**--version**
> 显示 phpize 版本。

**--help**
> 显示帮助。

# DESCRIPTION

**phpize** 为编译 PHP 扩展做准备。它会生成 configure 脚本和构建文件。

在扩展源代码目录中运行 phpize。它会创建必要的 autoconf 文件。

configure 脚本由 config.m4 生成。这使得标准的 ./configure && make 安装流程成为可能。

多个 PHP 版本可能各自拥有独立的 phpize 二进制文件。请使用与目标 PHP 安装相匹配的版本。

运行 phpize 之后，使用 PHP 配置路径运行 configure。然后执行 make 和 make install 完成构建。

# BUILD STEPS

1. **phpize** - 生成 configure 脚本
2. **./configure** - 配置构建选项
3. **make** - 编译扩展
4. **make install** - 安装扩展
5. 将扩展添加到 php.ini

# CAVEATS

需要 PHP 开发头文件。扩展必须与 PHP 版本兼容。还需要 autoconf 和构建工具。

# HISTORY

**phpize** 是 PHP 构建系统的一部分，起源于 PHP 4。它使 PECL 扩展和自定义模块能够独立于主 PHP 安装进行构建。

# INSTALL

```apk: sudo apk add php85-dev```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[php](/man/php)(1), [php-config](/man/php-config)(1), [pecl](/man/pecl)(1), [make](/man/make)(1)
