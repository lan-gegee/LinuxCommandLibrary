# TAGLINE

简化的 Debian 软件包管理封装工具

# TLDR

**更新**软件包列表

```wajig update```

**安装**软件包

```wajig install [package]```

**清除**软件包

```wajig purge [package]```

**每日升级**

```wajig daily-upgrade```

显示软件包**大小**

```wajig sizes```

列出**版本**

```wajig versions```

列出**可升级的软件包**

```wajig toupgrade```

显示**依赖者**

```wajig dependents [package]```

# SYNOPSIS

**wajig** _COMMAND_ [_ARGS_...]

# COMMANDS

**update**
> 更新软件包列表

**install**
> 安装或升级软件包

**purge**
> 删除软件包及其配置

**daily-upgrade**
> 更新并执行 dist-upgrade

**sizes**
> 显示已安装软件包的大小

**versions**
> 列出所有软件包的版本

**toupgrade**
> 列出可升级的软件包

**dependents**
> 显示依赖指定软件包的软件包

# DESCRIPTION

**wajig** 是一款面向 Debian 系系统的简化一站式系统支持工具。它将 apt、dpkg 等工具封装成一致的接口，提供易于记忆的命令。

该工具为常见的软件包管理任务提供了统一的界面。

# CAVEATS

仅适用于 Debian 系系统。大多数操作需要 root 权限。它只是对标准软件包工具的封装。

# SEE ALSO

[apt](/man/apt)(8), [dpkg](/man/dpkg)(1), [aptitude](/man/aptitude)(8)
