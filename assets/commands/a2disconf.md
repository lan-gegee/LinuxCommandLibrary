# TAGLINE

禁用 Apache2 配置文件

# TLDR

**禁用**一个配置文件

```sudo a2disconf [configuration_file]```

不显示**提示信息**

```sudo a2disconf -q [configuration_file]```

禁用一个配置并从内部状态数据库中**清除**其所有痕迹

```sudo a2disconf -p [configuration_file]```

# SYNOPSIS

**a2disconf** [_-q_|_--quiet_] [_-m_|_--maintmode_] [_-p_|_--purge_] [_configuration_]

# DESCRIPTION

**a2disconf** 是一个 Debian 特有的工具，它通过删除 **/etc/apache2/conf-enabled** 中的符号链接来禁用 Apache2 配置文件。它与负责启用配置的 **a2enconf** 配合使用。

如果指定的配置已被禁用，该工具会静默地成功返回，因此在脚本中使用是安全的。禁用配置后，必须重启或重新加载 Apache 才能使更改生效。

# PARAMETERS

**-q, --quiet**
> 不显示提示信息

**-m, --maintmode**
> 启用维护者模式；程序调用由维护者脚本自动执行

**-p, --purge**
> 禁用配置时，从内部状态数据库中清除其所有痕迹

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

[a2enconf](/man/a2enconf)(8), [a2enmod](/man/a2enmod)(8), [a2dismod](/man/a2dismod)(8), [a2ensite](/man/a2ensite)(8), [a2dissite](/man/a2dissite)(8), [apache2ctl](/man/apache2ctl)(8)

# RESOURCES

```[Homepage](https://httpd.apache.org/)```

```[Documentation](https://manpages.debian.org/a2disconf)```

<!-- verified: 2026-06-10 -->
