# TAGLINE

PHP 扩展社区库管理器

# TLDR

**安装扩展**

```pecl install [extension]```

**搜索扩展**

```pecl search [query]```

**列出已安装扩展**

```pecl list```

**卸载扩展**

```pecl uninstall [extension]```

**升级扩展**

```pecl upgrade [extension]```

**显示扩展信息**

```pecl info [extension]```

# SYNOPSIS

**pecl** [_command_] [_options_] [_package_]

# PARAMETERS

**install** _PACKAGE_
> 安装扩展。

**uninstall** _PACKAGE_
> 移除扩展。

**search** _QUERY_
> 搜索软件包。

**list**
> 列出已安装的扩展。

**upgrade** _PACKAGE_
> 升级扩展。

**info** _PACKAGE_
> 显示软件包信息。

# DESCRIPTION

**pecl** 是 PHP 扩展社区库（PECL）管理器，用于安装 PHP 扩展。

该工具管理已编译的扩展。属于 PEAR 的一部分。

# CAVEATS

需要 PHP 开发工具。可能需要 root 权限。需要编译器。

# HISTORY

PECL 的创立是为了让 **PHP 扩展**能够独立于核心进行分发。

# INSTALL

```apk: sudo apk add php85-pear```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pear](/man/pear)(1), [php](/man/php)(1), [phpize](/man/phpize)(1)
