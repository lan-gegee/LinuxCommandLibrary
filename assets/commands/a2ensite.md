# TAGLINE

启用 Apache2 虚拟主机站点

# TLDR

**启用**一个虚拟主机

```sudo a2ensite [virtual_host]```

一次**启用多个**站点

```sudo a2ensite [site1] [site2]```

**启用 default** 站点

```sudo a2ensite 000-default```

不显示**提示信息**

```sudo a2ensite -q [virtual_host]```

启用后**重新加载** Apache 以应用更改

```sudo systemctl reload apache2```

# SYNOPSIS

**a2ensite** [_-q_|_--quiet_] [_-m_|_--maintmode_] [_site_]

# DESCRIPTION

**a2ensite** 是一个 Debian 特有的工具，它在 **/etc/apache2/sites-enabled** 中创建指向 **/etc/apache2/sites-available** 中站点文件的符号链接，从而启用 Apache2 虚拟主机配置。

第一个虚拟主机负责处理未匹配的请求，因此应将其命名为 **000-default**，以保证按字母序最先加载。该工具与负责禁用站点的 **a2dissite** 配合使用。

# PARAMETERS

**-q, --quiet**
> 不显示提示信息

**-m, --maintmode**
> 启用维护者模式；程序调用由维护者脚本自动执行。并非为最终用户准备。

# EXIT STATUS

**0** - 所有站点处理成功。

**1** - 发生错误。

**2** - 使用了无效选项。

# FILES

**/etc/apache2/sites-available/**
> 存放可用站点配置文件的目录。

**/etc/apache2/sites-enabled/**
> 指向已启用站点配置的符号链接目录（由 a2ensite/a2dissite 管理）。

# CAVEATS

此工具为 **Debian 特有**，在其他 Linux 发行版上不可用。站点更改需要重启或重新加载 Apache 才能生效。虚拟主机按字母顺序加载，因此命名很重要。

# HISTORY

作为 **Debian GNU/Linux** Apache2 软件包的一部分创建，属于管理 Apache 虚拟主机的 a2ensite/a2dissite 工具家族。

# INSTALL

```apt: sudo apt install apache2```

```zypper: sudo zypper install apache2```

```brew: brew install apache2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[a2dissite](/man/a2dissite)(8), [a2enmod](/man/a2enmod)(8), [a2dismod](/man/a2dismod)(8), [a2enconf](/man/a2enconf)(8), [a2disconf](/man/a2disconf)(8), [apache2ctl](/man/apache2ctl)(8)
