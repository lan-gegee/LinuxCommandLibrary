# TAGLINE

Symfony PHP 框架开发 CLI

# TLDR

**创建新项目**

```symfony new [project_name]```

**创建 Web 应用**

```symfony new [project_name] --webapp```

**启动开发服务器**

```symfony server:start```

**停止服务器**

```symfony server:stop```

**显示服务器状态**

```symfony server:status```

**在浏览器中打开**

```symfony open:local```

**运行 console 命令**

```symfony console [command]```

**检查安全性**

```symfony check:security```

# SYNOPSIS

**symfony** _command_ [_options_] [_args_]

# PARAMETERS

**new** _NAME_
> 创建项目。

**server:start**
> 启动本地服务器。

**server:stop**
> 停止服务器。

**server:status**
> 显示本地服务器的状态。

**server:log**
> 显示本地 Web 服务器和 PHP-FPM 的日志。

**console** _CMD_
> 运行 Symfony console（包装 bin/console）。

**open:local**
> 在浏览器中打开本地项目 URL。

**check:security**
> 检查 composer.lock 依赖中的已知漏洞。

**local:php:list**
> 列出已安装的 PHP 版本。

**--webapp**
> 生成完整的 Web 应用模板（Twig、Doctrine、安全组件等）。

**--version** _VER_
> 安装指定的 Symfony 版本（例如 lts、6.4、7.1）。

**-d**, **--daemon**
> 在后台运行本地服务器。

**--allow-http**
> 禁用本地服务器的 HTTPS。

# DESCRIPTION

**symfony** 是管理 Symfony PHP 框架项目的官方命令行工具。它提供项目脚手架、内置的带 PHP 支持的本地开发服务器，以及常用 Symfony console 命令的封装。

项目创建提供的模板涵盖从极简微服务骨架到预配置 bundle 的完整 Web 应用。本地开发服务器包含通过本地可信证书实现的自动 HTTPS、PHP 版本管理，以及面向数据库等依赖服务的 Docker 集成。

console 封装会执行 Symfony console 命令（清缓存、数据库迁移、路由列表），并自动检测环境。安全检查将项目依赖与已知漏洞数据库比对扫描，并推荐更新。

# CAVEATS

需要 PHP。完整功能需要 Docker。云功能需要 Symfony 账号。

# HISTORY

**Symfony CLI** 由 **SensioLabs** 为 Symfony 框架开发而创建，整合了项目管理与本地开发功能。

# SEE ALSO

[php](/man/php)(1), [composer](/man/composer)(1)
