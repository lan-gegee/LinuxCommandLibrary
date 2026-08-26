# TAGLINE

Laravel 框架的命令行界面

# TLDR

**列出命令**

```php artisan list```

**启动开发服务器**

```php artisan serve```

**执行数据库迁移**

```php artisan migrate```

**生成控制器**

```php artisan make:controller [UserController]```

**生成模型及迁移**

```php artisan make:model [User] -m```

**清除缓存**

```php artisan cache:clear```

**生成迁移**

```php artisan make:migration [create_users_table]```

**回滚上一次迁移**

```php artisan migrate:rollback```

**列出所有路由**

```php artisan route:list```

**启动交互式 shell（tinker）**

```php artisan tinker```

**缓存配置**

```php artisan config:cache```

# SYNOPSIS

**php artisan** _command_ [_options_] [_arguments_]

# PARAMETERS

**serve**
> 启动开发服务器。

**migrate**
> 执行数据库迁移。

**make:controller** _name_
> 生成控制器。

**make:model** _name_
> 生成模型。

**make:migration** _name_
> 生成迁移。

**cache:clear**
> 清除应用缓存。

**config:cache**
> 缓存配置。

**route:list**
> 列出所有路由。

**tinker**
> 启动交互式 shell。

**queue:work**
> 开始处理队列中的任务。

**schedule:run**
> 运行计划任务命令。

**migrate:rollback**
> 回滚最近一次数据库迁移。

**migrate:fresh**
> 删除所有数据表并重新执行全部迁移。

**make:middleware** _name_
> 生成中间件类。

**make:seeder** _name_
> 生成数据库填充类。

**-v**, **-vv**, **-vvv**
> 提高输出的详细程度。

**--env** _ENV_
> 命令运行所处的环境。

# DESCRIPTION

**php artisan** 是 Laravel 框架的命令行界面。它提供代码生成、数据库迁移、缓存和服务器管理等常见开发任务的命令。

# INSTALL

```dnf: sudo dnf install php```

```pacman: sudo pacman -S php```

```apk: sudo apk add php85```

```brew: brew install php```

```nix: nix profile install nixpkgs#php85```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[php](/man/php)(1), [composer](/man/composer)(1), [laravel](/man/laravel)(1)
