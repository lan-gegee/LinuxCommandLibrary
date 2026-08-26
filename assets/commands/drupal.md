# TAGLINE

Drupal 代码生成与站点管理 CLI

# TLDR

**列出所有可用命令**

```drupal list```

**生成模块脚手架**（交互式）

```drupal generate:module```

**生成控制器类**

```drupal generate:controller```

**清空并重建所有缓存**

```drupal cache:rebuild```

**安装并启用模块**

```drupal module:install [module_name]```

**运行待执行的数据库更新**

```drupal update:execute```

**查看站点状态与配置**

```drupal site:status```

# SYNOPSIS

**drupal** _command_ [_options_] [_arguments_]

# PARAMETERS

_COMMAND_
> 要执行的 Drupal Console 命令。

**generate:module**
> 生成模块脚手架。

**generate:controller**
> 生成控制器类。

**cache:rebuild**
> 清空所有缓存。

**module:install** _NAME_
> 安装并启用模块。

**site:status**
> 显示站点信息。

**update:execute**
> 运行数据库更新。

**--help**
> 显示帮助信息。

# CONFIGURATION

**~/.console/config.yml**
> Drupal Console 的用户级配置，包括默认选项和偏好设置。

**drupal.yml**
> 位于 Drupal 根目录的项目专属配置文件，定义模块路径和自定义设置。

# DESCRIPTION

**Drupal Console** 是一款 CLI 工具，用于生成样板代码以及与 Drupal 8+ 应用交互和调试。它基于 Symfony Console 组件构建，通过代码生成加速开发，并为常见管理任务提供实用工具。

generate 系列命令按照最佳实践为模块、插件、控制器、表单和其他 Drupal 组件创建脚手架。交互式提示会引导你完成各项配置选项。

Drupal Console 还提供调试工具、缓存管理、配置导入/导出以及命令行数据库操作。

# CAVEATS

需要 Drupal 8+ 环境。必须在 Drupal 根目录下运行。部分命令需要数据库访问。该项目已不再活跃维护；**Drush** 吸收了它的许多功能，是现代 Drupal 开发推荐的 CLI 工具。

# HISTORY

Drupal Console 作为面向 **Drupal 8** 的代码生成与开发者工具而创建，发布于 **2015 年**前后。它受 Symfony Console 启发，将现代 CLI 开发实践带入 Drupal。

# INSTALL

```pacman: sudo pacman -S drupal```

```nix: nix profile install nixpkgs#drupal```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[drush](/man/drush)(1), [composer](/man/composer)(1), [php](/man/php)(1)
