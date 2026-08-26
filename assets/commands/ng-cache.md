# TAGLINE

管理 Angular CLI 的持久化磁盘缓存

# TLDR

**启用缓存**

```ng cache enable```

**禁用缓存**

```ng cache disable```

**从磁盘删除所有已缓存的构建产物**

```ng cache clean```

**打印缓存配置和统计信息**

```ng cache info```

**在所有环境（包括 CI）中启用缓存**

```ng config cli.cache.environment all```

**更改缓存存储路径**

```ng config cli.cache.path ".cache/ng"```

# SYNOPSIS

**ng cache** _command_ [_options_]

# PARAMETERS

**enable**, **on**
> 为工作区中的所有项目启用持久化磁盘缓存。

**disable**, **off**
> 为工作区中的所有项目禁用持久化磁盘缓存。

**clean**
> 从磁盘删除持久化磁盘缓存。

**info**
> 打印持久化磁盘缓存的配置和统计信息。

# DESCRIPTION

**ng cache** 管理 Angular CLI 的持久化磁盘缓存。该缓存保存可缓存操作的结果，让后续构建可以复用这些结果，从而显著缩短构建时间。

本地开发机器上缓存**默认启用**。CI 环境中默认禁用（通过 **CI** 环境变量检测）。

缓存行为可在 **angular.json** 的 `cli.cache` 下进一步配置：

- **enabled** —— 缓存是否处于活动状态
- **environment** —— 缓存适用范围：`local`（默认）、`ci` 或 `all`
- **path** —— 存储缓存文件的目录（默认：`.angular/cache`）

# SEE ALSO

[ng](/man/ng)(1), [ng-build](/man/ng-build)(1), [ng-config](/man/ng-config)(1)
