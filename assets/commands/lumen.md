# TAGLINE

Laravel 出品的 PHP 微框架

# TLDR

**创建新项目**

```lumen new [project-name]```

**运行应用**

```php -S localhost:8000 -t public```

**生成密钥**

```php artisan key:generate```

**运行数据库迁移**

```php artisan migrate```

**列出路由**

```php artisan route:list```

**清除缓存**

```php artisan cache:clear```

# SYNOPSIS

**lumen** _command_ [_options_]

# PARAMETERS

_COMMAND_
> 要执行的 Lumen 命令。

**new** _NAME_
> 创建新项目。

**--help**
> 显示帮助信息。

# DESCRIPTION

**lumen** 是 Laravel 出品的 PHP 微框架。它专为快速开发微服务和 API 而设计。

该框架以极小的开销提供路由、缓存和 Eloquent ORM。

# CAVEATS

需要 PHP 和 Composer。是 Laravel 功能的一个子集。命令通过 artisan 使用。

# HISTORY

Lumen 由 **Taylor Otwell** 于 2015 年创建，作为 Laravel 面向微服务的轻量版本。

# INSTALL

```nix: nix profile install nixpkgs#lumen```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[php](/man/php)(1), [composer](/man/composer)(1), [artisan](/man/artisan)(1)
