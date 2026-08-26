# TAGLINE

自动化 Laravel 项目创建流程

# TLDR

**创建新的 Laravel 项目**

```lambo new [project-name]```

**携带选项创建**

```lambo new [project-name] --editor=[code]```

**连同数据库一起创建**

```lambo new [project-name] --create-db```

**连同认证一起创建**

```lambo new [project-name] --auth```

**跳过常见交互提示**

```lambo new [project-name] --quiet```

# SYNOPSIS

**lambo new** [_options_] _name_

# PARAMETERS

_NAME_
> 项目名称。

**--editor** _EDITOR_
> 在编辑器中打开。

**--create-db**
> 创建数据库。

**--auth**
> 安装认证功能。

**--quiet**
> 跳过交互提示。

**--browser** _BROWSER_
> 在浏览器中打开。

**--help**
> 显示帮助信息。

# DESCRIPTION

**lambo** 用于自动化 Laravel 项目的创建过程。只需一条命令即可执行多个设置步骤。

该工具会处理 git init、composer install 和常见配置，让新项目的搭建流程更加顺畅。

# CAVEATS

需要 Laravel 安装器。需要 PHP 和 Composer。主要面向 macOS。

# HISTORY

lambo 由 Tighten 的 **Matt Stauffer** 创建，用于加速 Laravel 项目的初始化。

# SEE ALSO

[laravel](/man/laravel)(1), [composer](/man/composer)(1), [php](/man/php)(1)
