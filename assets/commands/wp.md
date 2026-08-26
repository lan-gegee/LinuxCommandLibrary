# TAGLINE

WordPress 命令行管理工具

# TLDR

**显示 WordPress 信息**

```wp --info```

**更新 WordPress 核心**

```wp core update```

**安装插件**

```wp plugin install [plugin-name]```

**激活插件**

```wp plugin activate [plugin-name]```

**安装主题**

```wp theme install [theme-name]```

**创建用户**

```wp user create [username] [email@example.com] --role=[editor]```

**在数据库中搜索替换**

```wp search-replace [old-url] [new-url]```

**导出数据库**

```wp db export [backup.sql]```

# SYNOPSIS

**wp** _command_ [_subcommand_] [_options_]

# PARAMETERS

**core**
> WordPress 核心的安装与更新。

**plugin**
> 插件管理（install、activate、deactivate、update、delete）。

**theme**
> 主题管理（install、activate、update、delete）。

**user**
> 用户管理（create、list、update、delete）。

**db**
> 数据库操作（export、import、query、optimize、repair）。

**search-replace** _old_ _new_
> 在数据库中搜索并替换字符串。

**cache**
> 对象缓存命令（flush、type）。

**config**
> 配置文件管理（create、get、set）。

**post**
> 文章管理（create、list、update、delete）。

**media**
> 媒体附件管理（import、regenerate）。

**--path=**_DIR_
> WordPress 安装路径。

**--url=**_URL_
> 目标站点 URL（用于多站点）。

**--skip-plugins**
> 跳过加载所有插件。

**--skip-themes**
> 跳过加载所有主题。

**--user=**_USER_
> 以特定用户身份运行命令。

**--allow-root**
> 允许以 root 身份运行（不建议）。

# DESCRIPTION

**wp**（WP-CLI）是 WordPress 官方的命令行管理界面。它让你可以在终端中完全控制 WordPress 站点，包括核心更新、插件和主题管理、用户管理以及数据库操作。

常见工作流包括安装并激活插件、创建具有特定角色的用户、导出导入数据库，以及在数据库中执行搜索替换（例如域名迁移）。该工具还能管理文章、页面、评论乃至 WordPress 站点的几乎所有方面，全程无需浏览器。

# CAVEATS

需要已存在的 WordPress 安装和 PHP CLI。某些操作需要直接访问数据库。除非指定 **--allow-root**，否则不建议以 root 身份运行。多站点环境下，请使用 **--url** 指定目标站点。

# HISTORY

**WP-CLI** 由 **Andreas Creten** 于 **2011 年**发起，后来由 **Daniel Bachhuber** 维护。它成为 WordPress 项目认可的官方命令行工具。该项目由开源社区积极维护。

# SEE ALSO

[php](/man/php)(1), [mysql](/man/mysql)(1)
