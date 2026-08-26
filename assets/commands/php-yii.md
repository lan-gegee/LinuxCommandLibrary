# TAGLINE

Yii 框架控制台命令运行器

# TLDR

**列出可用命令**

```php yii help```

**执行数据库迁移**

```php yii migrate```

**创建新迁移**

```php yii migrate/create [create_users_table]```

**回滚上一次迁移**

```php yii migrate/down```

**从数据表生成模型**

```php yii gii/model --tableName=[table] --modelClass=[ModelName]```

**生成 CRUD**

```php yii gii/crud --modelClass=[app\\models\\Post]```

**清除所有缓存**

```php yii cache/flush-all```

**查看特定命令的帮助**

```php yii help [migrate]```

# SYNOPSIS

**php** **yii** [_command_] [_--option=value_...]

# SUBCOMMANDS

**help** [_command_]
> 显示可用命令或特定命令的帮助。

**migrate**
> 执行待处理的数据库迁移。

**migrate/create** _name_
> 创建新的迁移文件。

**migrate/down** [_count_]
> 回滚迁移。默认：1。

**migrate/redo** [_count_]
> 重做迁移（先 down 再 up）。

**gii/model**
> 从数据库表生成模型类。

**gii/crud**
> 生成 CRUD 控制器和视图。

**gii/controller**
> 生成控制器类。

**cache/flush-all**
> 清除所有应用缓存。

**cache/flush** _component_
> 刷新指定的缓存组件。

**asset/compress** _configFile_ _bundleFile_
> 合并并压缩 JavaScript 和 CSS 文件。

**serve**
> 运行 PHP 内置 Web 服务器。

# PARAMETERS

**--tableName** _name_
> 数据库表名（gii/model）。

**--modelClass** _class_
> 模型类名（gii/model、gii/crud）。

**--interactive** _0|1_
> 以非交互模式运行。默认：1。

**--color** _0|1_
> 启用/禁用 ANSI 彩色输出。

# DESCRIPTION

**yii** 是 Yii 2.0 PHP 框架应用的控制台入口。它提供对内置命令的访问，涵盖数据库迁移、代码生成、缓存、资源管理与应用服务器等功能。

控制台命令使用 **controller/action** 路由格式（如 migrate/create）。选项以 **--option=value** 形式传递。继承 yii\console\Controller 即可创建自定义控制台命令。

**gii** 命令为模型、控制器、CRUD 界面、表单、模块和扩展提供代码生成能力。**migrate** 命令通过带版本的迁移文件管理数据库结构变更。

# CAVEATS

必须在存在 yii 引导文件的项目根目录下运行。需要正确配置的 Yii 2.0 应用。某些命令（如 gii）需要 yii2-gii 扩展。数据库命令需要已配置的数据库连接。

# HISTORY

Yii 控制台随 **Yii 2.0** 引入，由 **Qiang Xue** 于 **2014 年**发布。控制台运行器取代了 Yii 1.x 的 yiic 工具，采用了更灵活的命令架构。

# INSTALL

```dnf: sudo dnf install php```

```pacman: sudo pacman -S php```

```apk: sudo apk add php85```

```brew: brew install php```

```nix: nix profile install nixpkgs#php85```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[php](/man/php)(1), [composer](/man/composer)(1), [artisan](/man/artisan)(1), [symfony](/man/symfony)(1)
