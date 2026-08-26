# TAGLINE

禁用 Apache2 模块

# TLDR

**禁用**一个模块

```sudo a2dismod [module]```

不显示**提示信息**

```sudo a2dismod -q [module]```

**强制**禁用一个模块，即使它不存在或已被禁用

```sudo a2dismod -f [module]```

禁用一个模块并从内部状态数据库中**清除**其所有痕迹

```sudo a2dismod -p [module]```

# SYNOPSIS

**a2dismod** [_-q_|_--quiet_] [_-f_|_--force_] [_-m_|_--maintmode_] [_-p_|_--purge_] [_module_]

# DESCRIPTION

**a2dismod** 是一个 Debian 特有的工具，它通过删除 **/etc/apache2/mods-enabled** 中的符号链接来禁用 Apache2 模块。它会同时管理每个模块的 **.load** 文件和关联的 **.conf** 文件。

该工具与负责启用模块的 **a2enmod** 配合使用。禁用模块后，必须重启或重新加载 Apache 才能使更改生效。

# PARAMETERS

**-q, --quiet**
> 不显示提示信息

**-f, --force**
> 如果指定的模块不存在或已被禁用，也不报错

**-m, --maintmode**
> 启用维护者模式；程序调用由维护者脚本自动执行

**-p, --purge**
> 禁用模块时，从内部状态数据库中清除其所有痕迹

# CAVEATS

此工具为 **Debian 特有**，在其他 Linux 发行版上不可用（Ubuntu 及其衍生版同样可用）。禁用模块后，必须重启或重新加载 Apache 才能使更改生效。

# HISTORY

作为 **Debian GNU/Linux** Apache2 软件包的一部分创建。手册页由 Daniel Stone 编写，可追溯到 **2006 年 10 月**。

# INSTALL

```apt: sudo apt install apache2```

```zypper: sudo zypper install apache2```

```brew: brew install apache2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[a2enmod](/man/a2enmod)(8), [a2enconf](/man/a2enconf)(8), [a2disconf](/man/a2disconf)(8), [a2ensite](/man/a2ensite)(8), [a2dissite](/man/a2dissite)(8), [apache2ctl](/man/apache2ctl)(8)
