# TAGLINE

用于创建新 Laravel PHP 框架应用的安装器 CLI

# TLDR

**创建新的 Laravel 项目**

```laravel new [project-name]```

**使用指定的入门套件创建项目**

```laravel new [project-name] --jet```

**使用 Breeze 创建项目**

```laravel new [project-name] --breeze```

**创建时不初始化 Git**

```laravel new [project-name] --no-git```

# SYNOPSIS

**laravel** _command_ [_options_]

# PARAMETERS

**new** _name_
> 创建新的 Laravel 应用。

**--jet**
> 安装时附带 Laravel Jetstream。

**--breeze**
> 安装时附带 Laravel Breeze。

**--pest**
> 使用 Pest 进行测试。

**--no-git**
> 跳过 Git 初始化。

**--force**
> 覆盖已存在的目录。

# DESCRIPTION

**laravel** 是 Laravel 安装器 CLI，用于创建新的 Laravel PHP 框架应用。它为 Jetstream 和 Breeze 等入门套件提供脚手架选项，可作为 Composer create-project 的替代方案。

# INSTALL

```nix: nix profile install nixpkgs#laravel```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[composer](/man/composer)(1), [php-artisan](/man/php-artisan)(1)
