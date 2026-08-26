# TAGLINE

查询 Apache2 配置状态

# TLDR

列出已启用的 Apache **模块**

```sudo a2query -m```

检查某个**特定模块**是否已启用

```sudo a2query -m [module_name]```

列出已启用的**虚拟主机**

```sudo a2query -s```

显示当前启用的**多处理模块（MPM）**

```sudo a2query -M```

显示 **Apache 版本**

```sudo a2query -v```

列出已启用的**配置文件**

```sudo a2query -c```

# SYNOPSIS

**a2query** [_-m_ [_MODULE_]] [_-s_ [_SITE_]] [_-c_ [_CONF_]] [_-a_] [_-v_] [_-M_] [_-d_] [_-h_]

# DESCRIPTION

**a2query** 是一个 Debian 特有的工具，用于从本地安装的 Apache2 Web 服务器中获取配置值。它提供了一个稳健的接口，主要面向维护者脚本，但对系统管理员同样有用。

**-c**、**-m** 和 **-s** 选项的参数采用灵活比较方式，会忽略开头的 **mod_** 前缀以及 **.conf** 或 **.load** 后缀。

# PARAMETERS

**-m [MODULE]**
> 检查某个模块是否已启用；未提供参数时返回所有已启用的模块

**-s [SITE]**
> 检查某个站点是否已启用；未提供参数时返回所有已启用的站点

**-c [CONF]**
> 检查某个配置是否已启用；未提供参数时返回所有已启用的配置

**-M**
> 返回当前使用的 Apache2 MPM（多处理模块）

**-v**
> 返回已安装的 Apache2 版本

**-a**
> 显示 Apache2 Module Magic Version（API 版本）号

**-q**
> 抑制输出；只关心返回码时有用

**-h**
> 显示用法帮助并退出

# CAVEATS

此工具为 **Debian 特有**，在其他 Linux 发行版上不可用。退出码 **32** 表示所查询的模块、站点或配置不存在。

# HISTORY

作为 **Debian GNU/Linux** Apache2 软件包的一部分创建。由 Arno Toell 编写。

# INSTALL

```apt: sudo apt install apache2```

```zypper: sudo zypper install apache2```

```brew: brew install apache2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[a2enmod](/man/a2enmod)(8), [a2dismod](/man/a2dismod)(8), [a2enconf](/man/a2enconf)(8), [a2disconf](/man/a2disconf)(8), [a2ensite](/man/a2ensite)(8), [a2dissite](/man/a2dissite)(8), [apache2ctl](/man/apache2ctl)(8)

# RESOURCES

```[Homepage](https://httpd.apache.org/)```

```[Documentation](https://manpages.debian.org/a2query)```

<!-- verified: 2026-06-10 -->
