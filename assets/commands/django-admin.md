# TAGLINE

Django 管理任务的命令行工具

# TLDR

**创建新项目**

```django-admin startproject [project_name]```

**创建新应用**

```django-admin startapp [app_name]```

**运行开发服务器**

```django-admin runserver```

**生成数据库迁移**

```django-admin makemigrations```

**应用数据库迁移**

```django-admin migrate```

**创建超级用户**

```django-admin createsuperuser```

**打开 Django shell**

```django-admin shell```

# SYNOPSIS

**django-admin** _command_ [_options_]

# PARAMETERS

_COMMAND_
> 要执行的 Django 管理命令。

**startproject** _NAME_
> 创建新的 Django 项目。

**startapp** _NAME_
> 创建新的 Django 应用。

**runserver** [_PORT_]
> 运行开发服务器。

**makemigrations** [_APP_]
> 创建迁移文件。

**migrate** [_APP_]
> 应用迁移。

**createsuperuser**
> 创建管理员用户。

**shell**
> 打开带 Django 上下文的交互式 Python shell。

**--settings** _MODULE_
> 要使用的设置模块。

**--help**
> 显示帮助信息。

# DESCRIPTION

**django-admin** 是 Django 用于管理任务的命令行工具。它提供项目初始化、数据库管理、测试以及开发服务器运行等命令。

该工具需要一个 Django 设置模块才能工作。在项目目录内时会自动发现设置；否则需通过 DJANGO_SETTINGS_MODULE 环境变量或 --settings 标志指定配置。

项目中通常会用 manage.py 别名或替代 django-admin，它会自动配置设置模块。两者功能完全相同。

# CONFIGURATION

**settings.py**
> Django 项目设置模块，控制数据库、已安装的应用、中间件及全部配置。

**manage.py**
> django-admin 的项目专用包装器，会自动设置设置模块。

# CAVEATS

需要安装 Django。部分命令要求配置好设置和数据库。开发服务器不适合生产环境。迁移命令需要数据库访问权限。

# HISTORY

django-admin 是 **Django** 的组成部分，Django 由 **Adrian Holovaty** 和 **Simon Willison** 在 Lawrence Journal-World 报社开发，于 **2005 年**开源发布，如今已成为最流行的 Python Web 框架之一。

# INSTALL

```apk: sudo apk add py3-django```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[python](/man/python)(1), [pip](/man/pip)(1)
