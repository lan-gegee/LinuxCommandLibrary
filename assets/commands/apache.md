# TAGLINE

控制 Apache HTTP Web 服务器

# TLDR

**启动 Apache** 守护进程

```apachectl start```

**优雅停止 Apache**（完成当前请求）

```apachectl graceful-stop```

**优雅重启** Apache（先完成当前请求再重启）

```apachectl graceful```

**测试配置**是否有语法错误

```apachectl configtest```

**显示 Apache 版本**

```apachectl -v```

**显示编译内置的模块**

```apachectl -l```

**显示所有已加载模块**（静态与共享）

```apachectl -M```

**显示解析后的虚拟主机配置**

```apachectl -S```

# SYNOPSIS

**apachectl** _command_

**httpd** [**-d** _serverroot_] [**-f** _config_] [**-D** _parameter_]

# PARAMETERS

**start**
> 启动 Apache httpd 守护进程。

**stop**
> 立即停止守护进程。

**restart**
> 重启守护进程（中断当前连接）。

**graceful**
> 优雅重启（先完成当前请求再重启）。

**graceful-stop**
> 优雅停止（先完成当前请求再停止）。

**configtest**
> 检查配置文件语法。

**fullstatus**
> 显示完整的服务器状态（需要 **mod_status** 和基于文本的浏览器）。

**-v**
> 显示版本号。

**-V**
> 显示版本和构建参数。

**-l**
> 列出编译内置的模块。

**-M**
> 列出所有已加载模块（静态与共享）。

**-t**
> 测试配置语法（同 configtest）。

**-S**
> 显示解析后的虚拟主机配置。

**-f** _file_
> 指定替代的配置文件。

**-D** _name_
> 定义用于配置条件判断的参数。

# DESCRIPTION

**Apache HTTP Server**（httpd）是使用最广泛的 Web 服务器软件之一。它通过 HTTP/HTTPS 提供静态和动态内容，支持虚拟主机、URL 重写、身份验证以及丰富的模块化扩展能力。

**apachectl** 脚本为控制 Apache 守护进程提供了便捷接口。它既可以作为 **httpd** 命令的简单前端运行，也可以充当 SysV init 脚本，把 **start**、**restart**、**stop** 等单词参数转换为相应的信号。

配置主要通过 **httpd.conf** 及相关文件完成。模块化架构允许启用 SSL/TLS（mod_ssl）、URL 重写（mod_rewrite）、代理（mod_proxy）等功能，并可通过 CGI、PHP 或 mod_wsgi 提供动态内容。

Apache 支持多种多处理模块：面向兼容性的 **prefork**（基于进程）、**worker**（多线程），以及面向更高并发、改进了 keep-alive 处理的 **event**（多线程）。

# CAVEATS

配置更改需要重启或重载才能生效。配置文件中的语法错误会阻止启动；务必先运行 **configtest**。生产环境中首选 **graceful** 重启，以免断开活动连接。日志文件可能变得很大，需要进行轮转。**apachectl** 脚本成功时返回退出码 0，出错时返回大于 0 的值。

# HISTORY

Apache HTTP Server 源自伊利诺伊大学的 **NCSA HTTPd** 服务器。**1995 年**，一群开发者开始协作打补丁，"a patchy server"（打满补丁的服务器）之名由此演变为 Apache。**Apache 软件基金会**于 **1999 年**成立以支持其发展。Apache 曾主导 Web 服务器市场份额二十余年，不过自 **2010 年**起 nginx 已占据相当份额。

# INSTALL

```pacman: sudo pacman -S apache```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[nginx](/man/nginx)(8), [httpd](/man/httpd)(8), [htpasswd](/man/htpasswd)(1), [ab](/man/ab)(1)
