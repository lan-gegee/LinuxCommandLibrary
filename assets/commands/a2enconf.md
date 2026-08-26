# TAGLINE

启用 Apache2 配置文件

# TLDR

**启用**一个配置文件

```sudo a2enconf [configuration_file]```

不显示**提示信息**

```sudo a2enconf -q [configuration_file]```

# SYNOPSIS

**a2enconf** [_-q_|_--quiet_] [_-m_|_--maintmode_] [_configuration_]

# DESCRIPTION

**a2enconf** 是一个 Debian 特有的工具，它在 **/etc/apache2/conf-enabled** 中创建指向 **/etc/apache2/conf-available** 中文件的符号链接，从而启用 Apache2 配置文件。

该工具与负责禁用配置的 **a2disconf** 配合使用。启用配置后，必须重启或重新加载 Apache 才能使更改生效。

# PARAMETERS

**-q, --quiet**
> 不显示提示信息

**-m, --maintmode**
> 启用维护者模式；程序调用由维护者脚本自动执行

# CAVEATS

此工具为 **Debian 特有**，在其他 Linux 发行版上不可用。配置更改需要重启或重新加载 Apache 才能生效。

# HISTORY

作为 **Debian GNU/Linux** Apache2 软件包的一部分创建。手册页由 Arno Toell 编写，可追溯到 **2012 年 2 月**。

# INSTALL

```apt: sudo apt install apache2```

```zypper: sudo zypper install apache2```

```brew: brew install apache2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[a2disconf](/man/a2disconf)(8), [a2enmod](/man/a2enmod)(8), [a2dismod](/man/a2dismod)(8), [a2ensite](/man/a2ensite)(8), [a2dissite](/man/a2dissite)(8), [apache2ctl](/man/apache2ctl)(8)

# RESOURCES

```[Homepage](https://httpd.apache.org/)```

```[Documentation](https://manpages.debian.org/a2enconf)```

<!-- verified: 2026-06-10 -->
