# TAGLINE

在基于 Debian 的系统上通过创建符号链接启用 PHP 扩展

# TLDR

对所有 PHP 版本和 SAPI **启用**扩展

```sudo phpenmod [extension]```

对**特定版本**和 SAPI 启用扩展

```sudo phpenmod -v [7.4] -s [cli] [extension]```

# SYNOPSIS

**phpenmod** [**-v** _version_] [**-s** _sapi_] _module_

# PARAMETERS

**-v _version_**
> PHP 版本（如 7.4、8.0、8.1）

**-s _sapi_**
> SAPI 类型（cli、fpm、apache2、cgi）

**module**
> 要启用的扩展名

# DESCRIPTION

**phpenmod** 在基于 Debian 的系统上通过在 conf.d 目录中创建指向模块配置文件的符号链接来启用 PHP 扩展。未指定版本或 SAPI 时，会对所有已安装的 PHP 版本和所有 SAPI 启用该扩展。

该命令会在 /etc/php/VERSION/SAPI/conf.d/ 中创建符号链接，指向 mods-available 中的模块配置文件。

# CAVEATS

这是 Debian/Ubuntu 专属工具。需要 root 权限。更改需重启 PHP-FPM 或 Apache 后生效。扩展必须已安装才能被启用。

# HISTORY

**phpenmod** 是由 Debian PHP 团队维护的 **php-defaults** 软件包的一部分。它提供了管理 PHP 扩展的标准方式，类似于 a2enmod/a2dismod 管理 Apache 模块的方式。

# SEE ALSO

[phpdismod](/man/phpdismod)(8), [phpquery](/man/phpquery)(8), [php](/man/php)(1)
