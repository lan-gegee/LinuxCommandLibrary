# TAGLINE

Composer 使用的 PHP 软件包主仓库

# TLDR

**搜索软件包**

```composer search [query]```

**显示软件包信息**

```composer show [vendor/package]```

**引入软件包**

```composer require [vendor/package]```

**在网页上浏览**

```xdg-open https://packagist.org/packages/[vendor/package]```

# SYNOPSIS

**Packagist** - PHP 软件包仓库

# DESCRIPTION

**Packagist** 是 Composer 使用的 PHP 软件包主仓库。它汇集来自 GitHub、GitLab 及其他来源的 PHP 软件包，使其可以通过 Composer 安装。

Packagist 不是命令，而是一项通过 Composer 和网页界面访问的服务。

# COMPOSER COMMANDS

```bash
# Search packages
composer search monolog

# Get package info
composer info monolog/monolog

# Install package
composer require monolog/monolog

# Update packages
composer update
```

# PUBLISHING

```bash
# Submit to Packagist
# 1. Create composer.json
# 2. Push to GitHub
# 3. Submit URL at packagist.org
```

# PACKAGE NAMING

```
vendor/package
monolog/monolog
symfony/console
laravel/framework
```

# CAVEATS

需要安装 Composer。软件包需要 composer.json。会自动从 VCS 仓库更新。

# HISTORY

Packagist 由 **Jordi Boggiano** 和 **Nils Adermann** 于 **2011** 年创建，作为 PHP 依赖管理器 Composer 的默认仓库。

# SEE ALSO

[composer](/man/composer)(1), [php](/man/php)(1), [phpunit](/man/phpunit)(1)
