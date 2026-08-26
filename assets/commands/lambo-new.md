# TAGLINE

以自动化方式创建新的 Laravel 项目

# TLDR

**创建 Laravel 项目**

```lambo new [project-name]```

**指定编辑器创建**

```lambo new [project-name] --editor=[code]```

**同时创建数据库**

```lambo new [project-name] --create-db```

**附带认证脚手架**

```lambo new [project-name] --auth```

**完整设置**

```lambo new [project-name] --create-db --auth --editor=[code]```

# SYNOPSIS

**lambo new** [_options_] _name_

# PARAMETERS

_NAME_
> 项目目录名称。

**-e**, **--editor** _EDITOR_
> 安装完成后用于打开项目的编辑器命令。

**-m**, **--message** _MSG_
> 初始 git 提交信息。

**-p**, **--path** _PATH_
> 项目将被创建到的路径。

**-b**, **--browser** _URL_
> 安装完成后在给定 URL 打开浏览器。

**-l**, **--link**
> 为项目创建一个 Valet link。

**-s**, **--secure**
> 为项目配置 Valet 的 HTTPS。

**--create-db**
> 创建对应的 MySQL 数据库。

**--dbuser** _USER_
> 数据库用户（默认：root）。

**--dbpassword** _PASS_
> 数据库密码。

**--auth**
> 运行 php artisan make:auth 脚手架（旧版 Laravel）。

**--dev**
> 使用 Laravel 开发版本。

**--node**
> 创建后运行 npm install。

**--mix**
> 创建后运行 npm run dev（Laravel Mix）。

**--quiet**
> 最少输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**lambo new** 以自动化方式创建新的 Laravel 项目。它把多个设置步骤合并为一条命令。

该命令会处理 git 初始化、依赖安装和各项配置，并在你的编辑器中打开项目。

# CAVEATS

是 lambo 的子命令。需要 Laravel 安装器。需要 PHP/Composer。

# HISTORY

lambo new 是 **lambo** 的主命令，由 Matt Stauffer 创建，用于快速搭建 Laravel 项目。

# SEE ALSO

[lambo](/man/lambo)(1), [laravel](/man/laravel)(1), [composer](/man/composer)(1)
