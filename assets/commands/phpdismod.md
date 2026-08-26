# TAGLINE

在基于 Debian 的系统上通过移除符号链接来禁用 PHP 扩展

# TLDR

对所有 PHP 版本和 SAPI **禁用**扩展

```sudo phpdismod [extension]```

对**特定版本**和 SAPI 禁用扩展

```sudo phpdismod -v [7.4] -s [cli] [extension]```

# SYNOPSIS

**phpdismod** [**-v** _version_] [**-s** _sapi_] _module_

# PARAMETERS

**-v** _version_
> PHP 版本（如 7.4、8.0、8.1）。用 ALL 表示所有版本。

**-s** _sapi_
> SAPI 类型（cli、fpm、apache2、cgi）。用 ALL 表示所有 SAPI。

**-q**, **--quiet**
> 抑制输出消息。

_module_
> 要禁用的一个或多个扩展名。

# DESCRIPTION

**phpdismod** 在基于 Debian 的系统上通过从 conf.d 目录移除符号链接来禁用 PHP 扩展。未指定版本或 SAPI 时，会对所有已安装的 PHP 版本和所有 SAPI 禁用该扩展。

该命令的工作方式是操作 /etc/php/VERSION/SAPI/conf.d/ 中指向 mods-available 内模块配置文件的符号链接。

# CAVEATS

这是 Debian/Ubuntu 专属工具。需要 root 权限。更改需重启 PHP-FPM 或 Apache 后生效。某些扩展开启了依赖关系，禁用时可能引发问题。

# HISTORY

**phpdismod** 是由 Debian PHP 团队维护的 **php-defaults** 软件包的一部分。它提供了管理 PHP 扩展的标准方式，类似于 a2enmod/a2dismod 管理 Apache 模块的方式。

# SEE ALSO

[phpenmod](/man/phpenmod)(8), [phpquery](/man/phpquery)(8), [php](/man/php)(1)
