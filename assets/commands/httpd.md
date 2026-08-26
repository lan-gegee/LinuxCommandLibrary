# TAGLINE

Apache HTTP 服务器守护进程

# TLDR

**启动** Apache HTTP 服务器

```sudo httpd```

**测试**配置文件语法

```httpd -t```

以单进程调试模式（前台）**启动**

```httpd -X```

**列出所有已加载的**模块（静态与共享）

```httpd -M```

**显示版本**及编译参数

```httpd -V```

**使用指定的**配置文件

```httpd -f [/path/to/httpd.conf]```

**向运行中的实例发送信号**（start、stop、restart、graceful）

```httpd -k [graceful]```

**优雅地停止** Apache

```httpd -k graceful-stop```

# SYNOPSIS

**httpd** [_options_]

# DESCRIPTION

**httpd** 是 Apache HTTP 服务器的守护进程。它通过 HTTP/HTTPS 协议提供 Web 内容服务，处理静态文件、CGI 脚本以及反向代理。

Apache 可通过模块和配置指令高度定制，支持虚拟主机、访问控制以及众多认证方法。

# PARAMETERS

**-t**
> 测试配置语法。

**-T**
> 启动时跳过文档检查。

**-X**
> 以单进程调试模式运行。

**-f** _file_
> 指定配置文件。

**-M**
> 列出已加载的模块。

**-V**
> 显示版本和构建信息。

**-k** _signal_
> 向运行中的实例发送信号：start、stop、restart、graceful、graceful-stop。

**-D** _param_
> 定义一个运行时配置参数。

**-d** _dir_
> 设置 ServerRoot 目录。

**-e** _level_
> 设置启动日志级别（debug、info、notice、warn、error、crit、alert、emerg）。

**-n** _name_
> 设置服务名称（仅限 Windows）。

**-l**
> 列出编译进程序的模块（仅静态模块）。

# CAVEATS

指令和模块数量庞大，配置对初学者来说可能比较复杂。模块兼容性因主版本而异。高流量站点需要进行性能调优（MPM 选择、worker/线程上限）。在许多 Linux 发行版上，管理服务首选 **apachectl** 或 **systemctl**，而非直接调用 **httpd**。在 Debian/Ubuntu 上，二进制文件名为 **apache2** 而非 **httpd**。

# HISTORY

**Apache HTTP Server** 项目始于 **1995 年**，基于 NCSA HTTPd 发展而来，此后数十年一直是最流行的 Web 服务器。**Apache Software Foundation** 也是围绕它发展起来的。由于其起源于一系列补丁，名字来自 "a patchy server" 的谐音。

# INSTALL

```apt: sudo apt install merecat```

```dnf: sudo dnf install httpd```

```apk: sudo apk add apache2```

```zypper: sudo zypper install apache2```

```brew: brew install apache2```

```nix: nix profile install nixpkgs#merecat```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nginx](/man/nginx)(1), [apache2](/man/apache2)(1), [apachectl](/man/apachectl)(1), [a2enmod](/man/a2enmod)(1), [htpasswd](/man/htpasswd)(1), [caddy](/man/caddy)(1)
