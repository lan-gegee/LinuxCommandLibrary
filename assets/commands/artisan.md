# TAGLINE

Laravel 面向 PHP 开发任务的命令行界面。

# TLDR

**列出所有可用命令**

```php artisan list```

**启动开发服务器**

```php artisan serve```

**运行数据库迁移**

```php artisan migrate```

**创建新的控制器**

```php artisan make:controller [UserController]```

**创建新的模型**并附带迁移

```php artisan make:model [Post] --migration```

**生成应用密钥**

```php artisan key:generate```

**清除所有缓存**

```php artisan optimize:clear```

**打开交互式 Shell**（Tinker）

```php artisan tinker```

# SYNOPSIS

**php artisan** _command_ [_arguments_] [_options_]

# PARAMETERS

**list**
> 显示所有可用命令

**serve**
> 启动内置开发服务器

**migrate**
> 运行数据库迁移

**migrate:rollback**
> 回滚最近一次数据库迁移

**migrate:fresh**
> 删除所有表并重新执行全部迁移

**db:seed**
> 运行数据库填充器

**make:controller** _name_
> 创建新的控制器类

**make:model** _name_
> 创建新的 Eloquent 模型

**make:migration** _name_
> 创建新的迁移文件

**make:command** _name_
> 创建新的 Artisan 命令

**make:seeder** _name_
> 创建新的数据库填充器类

**make:factory** _name_
> 创建新的模型工厂

**cache:clear**
> 清除应用缓存

**config:cache**
> 缓存配置文件

**route:list**
> 列出所有已注册的路由

**queue:work**
> 处理队列中的任务

**schedule:run**
> 运行到期的计划任务

**vendor:publish**
> 发布软件包的资源和配置文件

**about**
> 显示应用环境与配置的摘要

**tinker**
> 打开交互式 REPL shell

**key:generate**
> 生成应用加密密钥

**optimize**
> 缓存配置、路由和视图

**optimize:clear**
> 清除所有缓存文件

**--help**, **-h**
> 显示某个命令的帮助信息

**-v**, **-vv**, **-vvv**
> 提高输出的详细程度

**--quiet**, **-q**
> 抑制全部输出

**--no-interaction**, **-n**
> 不提出任何交互式问题

**--version**, **-V**
> 显示应用版本

**--ansi**, **--no-ansi**
> 强制启用或禁用彩色输出

**--env=**_environment_
> 在指定的环境中运行命令

# DESCRIPTION

**Artisan** 是 Laravel 面向 PHP Web 应用开发的命令行界面。它为数据库迁移、代码生成、缓存管理和队列处理等常见任务提供命令。

该工具通过 **make:** 系列命令自动完成重复性的开发工作，为控制器、模型、迁移、测试等 Laravel 组件生成样板代码。数据库管理则通过迁移命令完成，迁移会对模式变更进行版本控制。

**Tinker** 提供交互式 REPL（读取-求值-打印循环），可用于探索应用、测试代码片段，以及直接与 Eloquent 模型交互。

自定义命令可通过 **make:command** 创建，并从 **app/Console/Commands** 目录自动注册。命令支持参数、选项、用户提示，以及包括表格和进度条在内的格式化输出。

# CAVEATS

必须在存在 **artisan** 文件的 Laravel 项目根目录下运行。需要安装 PHP 并将其加入系统 PATH。部分命令（如 **migrate**）需要先配置数据库。使用 Laravel Sail（Docker）时，请以 **sail** 而非 **php** 作为命令前缀。

# HISTORY

Artisan 由 Taylor Otwell 于 **2012** 年随 **Laravel 3** 推出，其灵感来自 Symfony Console。它随着每个 Laravel 版本不断成长，新增了各种生成器和实用工具。这个名字呼应了 Laravel "面向网页工匠的框架" 的定位。由 PsySH 驱动的 Laravel Tinker 后来被加入，用于提供交互式调试能力。

# INSTALL

```nix: nix profile install nixpkgs#artisan```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[composer](/man/composer)(1), [php](/man/php)(1), [symfony](/man/symfony)(1)

# RESOURCES

```[Source code](https://github.com/laravel/framework)```

```[Homepage](https://laravel.com)```

```[Documentation](https://laravel.com/docs/artisan)```

<!-- verified: 2026-06-16 -->
