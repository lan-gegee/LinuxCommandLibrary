# TAGLINE

Drupal 的命令行 Shell

# TLDR

**清空所有缓存**

```drush cache:rebuild```

**启用并安装**模块

```drush pm:install [module_name]```

**更新数据库**

```drush updatedb```

**运行 cron**

```drush cron```

**显示站点状态**

```drush status```

**导出配置**

```drush config:export```

**导入配置**

```drush config:import```

**生成一次性**登录链接

```drush user:login```

**将数据库转储**到 SQL 文件

```drush sql:dump --result-file=[dump.sql]```

**打开交互式 SQL** shell

```drush sql:cli```

# SYNOPSIS

**drush** _command_ [_options_] [_arguments_]

# PARAMETERS

_COMMAND_
> 要执行的 Drush 命令。

**cache:rebuild**, **cr**
> 清空所有缓存。

**pm:install** _NAME_, **en**
> 启用并安装模块。

**pm:uninstall** _NAME_, **pmu**
> 卸载模块。

**updatedb**, **updb**
> 应用数据库更新。

**config:export**, **cex**
> 导出配置。

**config:import**, **cim**
> 导入配置。

**user:login**, **uli**
> 生成登录链接。

**sql:dump**
> 将数据库导出为 SQL 文件。

**sql:cli**, **sqlc**
> 使用 Drupal 凭据打开交互式 SQL shell。

**status**, **st**
> 显示站点信息。

**--yes**, **-y**
> 自动接受确认提示。

**--uri** _URI_
> 多站点设置中使用的 Drupal URI。

**--help**
> 显示帮助信息。

# CONFIGURATION

**~/.drush/drush.yml**
> Drush 用户级配置，用于默认选项和别名。

**drush/drush.yml** 或 **drush/sites/**.yml
> 位于 Drupal 根目录的项目专属 Drush 配置文件。

**/drush/sites/*.site.yml**
> 站点别名定义，用于管理多个 Drupal 站点。

# DESCRIPTION

**Drush**（Drupal Shell）是 Drupal 的命令行界面，提供站点管理、开发和部署工具。它是 Drupal 开发者和管理员的必备工具。

该工具负责缓存清理、模块管理、数据库更新、配置同步和用户管理。短别名（cr、cex、cim）可快速调用常用命令。

Drush 支持通过站点别名管理多个 Drupal 站点，并与配置管理的部署工作流集成。

# CAVEATS

需要 Drupal 环境。必须在站点根目录运行或使用别名。版本必须与 Drupal 版本匹配。部分命令需要数据库访问。

# HISTORY

Drush 由 **Moshe Weitzman** 等人于 **2007 年**为 Drupal 5 创建。它随 Drupal 一同演进，已成为 Drupal 管理与开发的标准 CLI 工具。

# INSTALL

```zypper: sudo zypper install drush```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[drupal](/man/drupal)(1), [composer](/man/composer)(1), [php](/man/php)(1)
