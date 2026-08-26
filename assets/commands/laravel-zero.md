# TAGLINE

基于 Laravel 组件构建的控制台应用微框架

# TLDR

**创建新的 Laravel Zero 应用**

```laravel-zero new [app-name]```

**构建独立 PHAR**

```php [app-name] app:build```

**安装可选组件**

```php [app-name] app:install```

# SYNOPSIS

**laravel-zero** _command_ [_options_]

# PARAMETERS

**new** _name_
> 创建新的 Laravel Zero 应用。

**--force**
> 覆盖已存在的目录。

# DESCRIPTION

**laravel-zero** 是一个基于 Laravel 组件构建的控制台应用微框架。它可以创建能编译成单个 PHAR 文件的独立命令行应用，非常适合借助 Laravel 优雅的语法来构建 CLI 工具。

# INSTALL

```nix: nix profile install nixpkgs#laravel```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[laravel](/man/laravel)(1), [composer](/man/composer)(1)
