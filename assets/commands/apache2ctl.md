# TAGLINE

在 Debian 上管理 Apache HTTP 服务器

# TLDR

**启动** Apache 守护进程

```sudo apache2ctl start```

**停止** Apache 守护进程

```sudo apache2ctl stop```

**重启** Apache 守护进程

```sudo apache2ctl restart```

测试配置文件的**语法**

```sudo apache2ctl -t```

列出**已加载模块**

```sudo apache2ctl -M```

**优雅**重启且不断开连接

```sudo apache2ctl graceful```

# SYNOPSIS

**apache2ctl** _command_

**apache2ctl** [_httpd-argument_]

# DESCRIPTION

**apache2ctl** 是 Apache 超文本传输协议（HTTP）服务器的前端工具，旨在帮助管理员管理 Apache 守护进程。该命令随基于 Debian 的操作系统提供；基于 RHEL 的系统请参见 **httpd**。

# PARAMETERS

**start**
> 启动 Apache 守护进程；若已在运行则报错

**stop**
> 停止 Apache 守护进程

**restart**
> 通过 SIGHUP 重启 Apache；包含配置校验

**graceful**
> 重启但不终止活动连接

**graceful-stop**
> 停止 Apache 但不中断当前连接

**status**
> 显示简要的运行状态报告

**fullstatus**
> 通过 mod_status 显示完整状态（需要 lynx）

**configtest**
> 校验配置文件中的语法

**-t**
> 测试配置文件语法

**-M**
> 列出已加载模块（静态与共享）

**-S**
> 显示解析后的虚拟主机配置和监听端口

**-V**
> 显示版本、构建设置和编译时配置

**-l**
> 列出编译进服务器的模块

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

Debian 要求在 /etc/apache2/envvars 中设置环境变量 **APACHE_RUN_USER**、**APACHE_RUN_GROUP** 和 **APACHE_PID_FILE**。

# HISTORY

**Apache HTTP Server** 项目的一部分，是最古老、使用最广泛的 Web 服务器之一，由 Apache 软件基金会开发。

# INSTALL

```apt: sudo apt install apache2```

```zypper: sudo zypper install apache2```

```brew: brew install apache2```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[apachectl](/man/apachectl)(8), [a2enmod](/man/a2enmod)(8), [a2dismod](/man/a2dismod)(8), [a2ensite](/man/a2ensite)(8), [httpd](/man/httpd)(8)

# RESOURCES

```[Source code](https://github.com/apache/httpd)```

```[Homepage](https://httpd.apache.org/)```

```[Documentation](https://manpages.debian.org/bookworm/apache2/apache2ctl.8.en.html)```

<!-- verified: 2026-06-11 -->
