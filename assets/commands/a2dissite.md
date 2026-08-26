# TAGLINE

禁用 Apache2 虚拟主机

# TLDR

**禁用**一个虚拟主机

```sudo a2dissite [virtual_host]```

不显示**提示信息**

```sudo a2dissite -q [virtual_host]```

禁用一个虚拟主机并从内部状态数据库中**清除**其所有痕迹

```sudo a2dissite -p [virtual_host]```

# SYNOPSIS

**a2dissite** [_-q_|_--quiet_] [_-m_|_--maintmode_] [_-p_|_--purge_] [_site_]

# DESCRIPTION

**a2dissite** 是一个 Debian 特有的工具，它通过删除 **/etc/apache2/sites-enabled** 中的符号链接来禁用 Apache2 虚拟主机配置。站点配置文件仍保留在 **/etc/apache2/sites-available** 中，之后可以重新启用。

如果指定的站点已被禁用，该工具会静默地成功返回。禁用站点后，必须重启或重新加载 Apache 才能使更改生效。

# PARAMETERS

**-q, --quiet**
> 不显示提示信息

**-m, --maintmode**
> 启用维护者模式；程序调用由维护者脚本自动执行

**-p, --purge**
> 禁用站点时，从内部状态数据库中清除其所有痕迹

# CAVEATS

此工具为 **Debian 特有**，在其他 Linux 发行版上不可用。站点更改需要重启或重新加载 Apache 才能生效。

# HISTORY

作为 **Debian GNU/Linux** Apache2 软件包的一部分创建，属于管理 Apache 虚拟主机的 a2ensite/a2dissite 工具家族。

# INSTALL

```apt: sudo apt install apache2```

```zypper: sudo zypper install apache2```

```brew: brew install apache2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[a2ensite](/man/a2ensite)(8), [a2enmod](/man/a2enmod)(8), [a2dismod](/man/a2dismod)(8), [a2enconf](/man/a2enconf)(8), [a2disconf](/man/a2disconf)(8), [apache2ctl](/man/apache2ctl)(8)

# RESOURCES

```[Homepage](https://httpd.apache.org/)```

```[Documentation](https://manpages.debian.org/a2dissite)```

<!-- verified: 2026-06-10 -->
