# TAGLINE

查询基于 Debian 系统上的 PHP 配置

# TLDR

列出可用的 **PHP 版本**

```sudo phpquery -V```

列出某版本的可用 **SAPI**

```sudo phpquery -v [7.4] -S```

列出某版本和 SAPI 下**已启用的扩展**

```sudo phpquery -v [7.4] -s [cli] -M```

**检查**扩展是否已启用

```sudo phpquery -v [7.4] -s [apache2] -m [json]```

# SYNOPSIS

**phpquery** [**-v** _version_] [**-s** _sapi_] [**-V**|**-S**|**-M**|**-m** _module_]

# PARAMETERS

**-v _version_**
> 要查询的 PHP 版本

**-s _sapi_**
> 要查询的 SAPI

**-V**
> 列出可用的 PHP 版本

**-S**
> 列出可用的 SAPI

**-M**
> 列出已启用的模块

**-m _module_**
> 检查特定模块是否已启用

**-q**
> 静默模式，仅返回退出状态

# DESCRIPTION

**phpquery** 在基于 Debian 的系统上查询 PHP 配置。它报告已安装的 PHP 版本、可用的 SAPI（Server API）以及已启用的扩展。这对于需要检测 PHP 配置的脚本和自动化任务很有用。

该工具从 /etc/php/ 目录结构读取配置，并报告控制模块启用的符号链接的状态。

# CAVEATS

这是 Debian/Ubuntu 特有的工具。某些查询可能需要 root 权限。只报告通过 phpenmod/phpdismod 机制管理的扩展。

# HISTORY

**phpquery** 是由 Debian PHP 团队维护的 **php-defaults** 软件包的一部分。它与 phpenmod 和 phpdismod 相辅相成，为 PHP 配置管理提供查询能力。

# SEE ALSO

[phpenmod](/man/phpenmod)(8), [phpdismod](/man/phpdismod)(8), [php](/man/php)(1)
