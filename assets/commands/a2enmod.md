# TAGLINE

启用 Apache2 模块

# TLDR

**启用**一个模块

```sudo a2enmod [module]```

**启用**模块并**重新加载** Apache

```sudo a2enmod [module] && sudo systemctl reload apache2```

**启用 rewrite** 模块

```sudo a2enmod rewrite```

**启用 SSL** 模块

```sudo a2enmod ssl```

不显示**提示信息**

```sudo a2enmod -q [module]```

# SYNOPSIS

**a2enmod** [_-q_|_--quiet_] [_-m_|_--maintmode_] [_module_]

# DESCRIPTION

**a2enmod** 是一个 Debian 特有的工具，它在 **/etc/apache2/mods-enabled** 中创建指向 **/etc/apache2/mods-available** 中模块文件的符号链接，从而启用 Apache2 模块。该工具会同时处理每个模块的 **.load** 文件和关联的 **.conf** 文件。

该工具与负责禁用模块的 **a2dismod** 配合使用。启用模块后，必须重启或重新加载 Apache 才能使更改生效。

# PARAMETERS

**-q, --quiet**
> 不显示提示信息

**-m, --maintmode**
> 启用维护者模式；程序调用由维护者脚本自动执行

# CAVEATS

此工具为 **Debian 特有**，在其他 Linux 发行版上不可用。启用某个模块可能需要先启用其依赖的模块。模块更改需要重启或重新加载 Apache 才能生效。

# HISTORY

作为 **Debian GNU/Linux** Apache2 软件包的一部分创建。手册页由 Daniel Stone 编写，可追溯到 **2006 年 10 月**。

# INSTALL

```apt: sudo apt install apache2```

```zypper: sudo zypper install apache2```

```brew: brew install apache2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[a2dismod](/man/a2dismod)(8), [a2enconf](/man/a2enconf)(8), [a2disconf](/man/a2disconf)(8), [a2ensite](/man/a2ensite)(8), [a2dissite](/man/a2dissite)(8), [apache2ctl](/man/apache2ctl)(8)
