# TAGLINE

用于在 Digital Ocean 上部署 Laravel 应用的服务器配置工具

# TLDR

以默认 PHP 版本**配置**服务器

```larasail setup```

以**指定的 PHP 版本**配置服务器

```larasail setup [php71]```

**添加**新的 Laravel 站点

```larasail host [domain] [path/to/site_directory]```

获取 Larasail **用户密码**

```larasail pass```

获取 **MySQL 密码**

```larasail mysqlpass```

# SYNOPSIS

**larasail** _command_ [_arguments_]

# PARAMETERS

**setup** [_php_version_]
> 配置服务器并安装 Laravel 依赖

**host** _domain_ _directory_
> 添加一个新的 Laravel 站点

**pass**
> 显示 Larasail 用户密码

**mysqlpass**
> 显示 MySQL 密码

# DESCRIPTION

**larasail** 是一款用于在 Digital Ocean 服务器上部署 Laravel 应用的服务器配置工具。它会自动安装 PHP、Nginx、MySQL、Composer 以及其他 Laravel 依赖。

该工具简化了搭建生产级 Laravel 环境的过程，负责处理 Web 服务器配置、SSL 证书和数据库设置。

# CAVEATS

专为运行 Ubuntu 的 Digital Ocean droplet 设计。需要在服务器上拥有 root 权限。SSL 证书配置可能需要额外的步骤。

# HISTORY

Larasail 由 DevDojo 创建，旨在简化 Laravel 部署，为更复杂的服务器管理工具提供了一个轻量替代方案。

# SEE ALSO

[composer](/man/composer)(1), [php](/man/php)(1), [nginx](/man/nginx)(8)
