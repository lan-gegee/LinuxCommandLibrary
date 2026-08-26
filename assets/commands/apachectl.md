# TAGLINE

控制 Apache HTTP 服务器

# TLDR

**启动**服务器

```sudo apachectl start```

**重启**服务器

```sudo apachectl restart```

**停止**服务器

```sudo apachectl stop```

测试**配置文件**是否有效

```apachectl configtest```

检查服务器**状态**（需要 lynx 浏览器）

```apachectl status```

不断开连接地**重载**配置

```sudo apachectl graceful```

打印完整的 **Apache 配置**

```apachectl -S```

# SYNOPSIS

**apachectl** _command_

**apachectl** [_httpd-argument_]

# DESCRIPTION

**apachectl** 是 Apache 超文本传输协议（HTTP）服务器的前端工具，旨在帮助管理员管理 Apache 守护进程。它既能以 SysV init 模式执行简单命令，也能把参数直接传给 httpd。

# PARAMETERS

**start**
> 启动 Apache 守护进程

**stop**
> 停止 Apache 守护进程

**restart**
> 重启 Apache；未运行时则启动

**graceful**
> 优雅重启，不终止活动连接

**graceful-stop**
> 优雅停止，不中断当前连接

**configtest**
> 校验配置文件中的语法

**status**
> 显示简要运行状态（需要 lynx 和 mod_status）

**fullstatus**
> 显示完整的状态报告

**-S**
> 打印完整的 Apache 配置（解析后的虚拟主机）

**-t**
> 测试配置语法

**-M**
> 列出已加载模块（传给 httpd）

**-V**
> 显示 httpd 编译时设置和版本

**-l**
> 列出静态编译的模块

**-h**
> 显示帮助

# CONFIGURATION

**/etc/httpd/conf/httpd.conf**
> RHEL/CentOS/Fedora 系统上的主配置文件。

**/etc/apache2/apache2.conf**
> Debian/Ubuntu 系统上的主配置文件。

**/etc/httpd/conf.d/**
> 基于 RHEL 的系统中存放附加配置文件的目录。

**/etc/apache2/sites-available/**
> 基于 Debian 系统中的虚拟主机配置文件。

# CAVEATS

**status** 和 **fullstatus** 命令需要 lynx 文本浏览器并启用 mod_status。

# HISTORY

**Apache HTTP Server** 项目的一部分，由 Apache 软件基金会自 **1995 年**起开发。

# INSTALL

```apt: sudo apt install apache2```

```apk: sudo apk add apache2-ctl```

```zypper: sudo zypper install apache2```

```brew: brew install apache2```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[apache2ctl](/man/apache2ctl)(8), [httpd](/man/httpd)(8)
