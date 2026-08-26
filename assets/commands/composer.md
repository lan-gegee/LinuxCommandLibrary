# TAGLINE

PHP 项目的依赖管理器

# TLDR

**安装**依赖

```composer install```

**添加**软件包

```composer require [vendor/package]```

**更新**软件包

```composer update```

**创建**项目

```composer create-project [laravel/laravel] [myapp]```

**查看**已安装的软件包

```composer show```

**移除**软件包

```composer remove [vendor/package]```

# SYNOPSIS

**composer** _command_ [_options_]

# DESCRIPTION

**composer** 是 PHP 的依赖管理器。它管理项目依赖和自动加载，并通过 Packagist 及其他软件仓库提供软件包安装与版本管理工具。

该工具是现代 PHP 开发的基石，几乎所有 PHP 框架都在使用。

# PARAMETERS

**install**
> 根据 composer.json 安装依赖

**require** _package_
> 将软件包添加到依赖中

**update** [_packages_]
> 更新依赖

**remove** _package_
> 移除软件包

**create-project** _package_ _dir_
> 创建新项目

**show** [_package_]
> 显示软件包

**search** _query_
> 搜索软件包

**dump-autoload**
> 重新生成自动加载器

**self-update**
> 更新 Composer 自身

# CONFIGURATION

**composer.json**
> 项目依赖与元数据。

**composer.lock**
> 锁定的依赖版本，保证安装可复现。

**~/.composer/config.json**
> 全局 composer 配置。

**~/.composer/auth.json**
> 私有仓库的身份验证凭据。

# COMPOSER.JSON

```json
{
    "name": "vendor/project",
    "require": {
        "php": "^8.1",
        "monolog/monolog": "^3.0"
    },
    "require-dev": {
        "phpunit/phpunit": "^10.0"
    },
    "autoload": {
        "psr-4": {
            "App\\": "src/"
        }
    }
}
```

# WORKFLOW

```bash
# Initialize new project
composer init

# Add dependency
composer require guzzlehttp/guzzle

# Add dev dependency
composer require --dev phpunit/phpunit

# Install all dependencies
composer install

# Update specific package
composer update monolog/monolog

# Update all
composer update

# Show why package is installed
composer why vendor/package

# Check for security issues
composer audit
```

# VERSION CONSTRAINTS

- **^1.2.3** - >=1.2.3 <2.0.0（推荐）
- **~1.2.3** - >=1.2.3 <1.3.0
- **1.2.*** - >=1.2.0 <1.3.0
- **>=1.2.3** - 1.2.3 或更高
- **dev-master** - master 分支最新版本

# FEATURES

- 依赖解析
- 自动加载（PSR-4、PSR-0、classmap）
- 脚本与钩子
- 平台环境要求
- 私有仓库支持
- 安全审计
- 锁定文件（composer.lock）

# CAVEATS

首次安装可能较慢。大型项目内存消耗大。更新需要联网。composer.lock 应提交到版本库（针对应用程序）。版本冲突可能令人头疼。部分软件包已被弃养或维护不善。

# HISTORY

**Composer** 由 Nils Adermann 和 Jordi Boggiano 于 **2011 年**创建，灵感来自 npm 和 bundler，到 **2013 年**已成为 PHP 的标准依赖管理器。

# INSTALL

```dnf: sudo dnf install composer```

```pacman: sudo pacman -S composer```

```apk: sudo apk add composer```

```brew: brew install composer```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [pip](/man/pip)(1), [bundle](/man/bundle)(1)

# RESOURCES

```[Source code](https://github.com/composer/composer)```

```[Homepage](https://getcomposer.org)```

```[Documentation](https://getcomposer.org/doc/)```

<!-- verified: 2026-06-22 -->
