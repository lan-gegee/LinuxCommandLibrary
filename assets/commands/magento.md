# TAGLINE

Magento/Adobe Commerce 电子商务平台的命令行界面

# TLDR

**列出可用命令**

```magento list```

**启用维护模式**

```magento maintenance:enable```

**禁用维护模式**

```magento maintenance:disable```

**清理缓存**

```magento cache:clean```

**清空缓存**

```magento cache:flush```

**重建全部索引**

```magento indexer:reindex```

**编译依赖注入**

```magento setup:di:compile```

**部署静态内容**

```magento setup:static-content:deploy```

# SYNOPSIS

**magento** [_command_] [_--help_] [_options_] [_arguments_]

# PARAMETERS

**cache:clean**
> 清理指定类型的缓存。

**cache:flush**
> 清空缓存存储。

**cache:status**
> 显示缓存状态。

**cache:enable** _TYPE_
> 启用缓存类型。

**cache:disable** _TYPE_
> 禁用缓存类型。

**indexer:reindex**
> 重建所有索引器。

**indexer:status**
> 显示索引器状态。

**maintenance:enable**
> 启用维护模式。

**maintenance:disable**
> 禁用维护模式。

**setup:upgrade**
> 升级数据库架构。

**setup:di:compile**
> 编译依赖注入。

**setup:static-content:deploy**
> 部署静态视图文件。

**module:enable** _MODULE_
> 启用模块。

**module:disable** _MODULE_
> 禁用模块。

**deploy:mode:set** _MODE_
> 设置应用模式（developer、production）。

# DESCRIPTION

**magento** 是 Magento/Adobe Commerce 电子商务平台的命令行界面。它负责管理店铺运营、部署和维护任务。

缓存管理对性能至关重要。clean 会清除特定的缓存数据，而 flush 则清空全部存储。不同的缓存类型（config、layout、block_html、collections 等）可以单独处理。

部署过程包括依赖注入编译、静态内容部署和数据库升级。代码更改或安装模块后都需要执行这些步骤。

索引器使派生数据与源数据保持同步。目录变更、价格更新或库存修改后都需要重建索引。

维护模式下顾客会看到服务不可用页面，同时管理员仍可正常工作。可以配置 IP 白名单例外。

# CAVEATS

命令必须在 Magento 根目录下运行。文件权限至关重要——请以 web 服务器用户身份运行。对大型商品目录而言，静态内容部署比较耗时。大型商店可能需要调大内存限制。

# HISTORY

**Magento** 由 **Varien** 于 **2008 年**创立，**2011 年**被 **eBay** 收购，后又被分拆为独立公司。**Adobe** 于 **2018 年**收购了 Magento。该 CLI 随 **2015 年**发布的 Magento 2 推出，取代了此前基于管理后台的配置方式。

# SEE ALSO

[composer](/man/composer)(1), [php](/man/php)(1), [mysql](/man/mysql)(1), [nginx](/man/nginx)(8)
