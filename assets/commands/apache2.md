# TAGLINE

Apache HTTP 服务器守护进程

# TLDR

**启动** Apache 服务器

```sudo apache2```

以**前台**模式启动以便调试

```sudo apache2 -X```

测试**配置语法**

```apache2 -t```

显示**已加载模块**

```apache2 -M```

显示**版本**和构建选项

```apache2 -V```

显示**解析后的虚拟主机**配置

```apache2 -S```

使用**指定配置**启动

```sudo apache2 -f [/path/to/httpd.conf]```

# SYNOPSIS

**apache2** [_-d serverroot_] [_-f config_] [_-D parameter_] [_options_]

# DESCRIPTION

**apache2** 是 Apache HTTP 服务器守护进程，也是使用最广泛的 Web 服务器之一。它处理 HTTP 请求、提供静态内容、运行 CGI 脚本，并通过各种模块与应用服务器集成。

在 Debian/Ubuntu 系统上，apache2 通常通过 systemctl 或 apache2ctl 管理，而非直接调用。

# PARAMETERS

**-t**
> 测试配置文件语法

**-X**
> 以单进程调试模式运行

**-M**
> 列出已加载模块（编译内置与共享）

**-V**
> 显示版本和编译设置

**-f** _file_
> 指定配置文件

**-d** _directory_
> 服务器根目录

**-D** _name_
> 为 <IfDefine> 定义参数

**-e** _level_
> 启动错误日志级别。

**-k** _command_
> 信号命令：start、stop、restart、graceful、graceful-stop。

**-S**
> 显示解析后的虚拟主机配置。

**-l**
> 列出编译内置的模块。

**-L**
> 列出可用的配置指令。

**-C** _directive_
> 在读取配置文件之前处理该指令。

**-c** _directive_
> 在读取配置文件之后处理该指令。

**-h**
> 显示命令行选项的简要摘要。

# CONFIGURATION

**/etc/apache2/apache2.conf**
> Debian/Ubuntu 系统上的主配置文件。

**/etc/apache2/sites-available/**
> 虚拟主机配置文件，通过 a2ensite 启用。

**/etc/apache2/mods-available/**
> 模块配置文件，通过 a2enmod 启用。

**/etc/apache2/envvars**
> Apache 进程的环境变量（用户、组、pid 文件）。

**/etc/apache2/ports.conf**
> Listen 指令，指定 Apache 绑定哪些端口。

# CAVEATS

很少需要直接调用；请使用 apache2ctl 或 systemctl。重启前应先运行配置测试（-t）。绑定低于 1024 的端口需要 root 权限。

# HISTORY

Apache HTTP Server 源自 **1995 年**的 NCSA HTTPd 补丁，"Apache" 据称意为 "A Patchy Server"（打满补丁的服务器）。它已主导 Web 服务器市场数十年。

# INSTALL

```apt: sudo apt install apache2-bin```

```zypper: sudo zypper install apache2```

```brew: brew install apache2```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[apache2ctl](/man/apache2ctl)(8), [apachectl](/man/apachectl)(8), [nginx](/man/nginx)(8)
