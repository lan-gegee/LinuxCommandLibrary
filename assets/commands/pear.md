# TAGLINE

PHP 扩展与应用仓库管理器

# TLDR

**安装软件包**

```pear install [package]```

**升级软件包**

```pear upgrade [package]```

**列出已安装的软件包**

```pear list```

**搜索软件包**

```pear search [keyword]```

**卸载软件包**

```pear uninstall [package]```

# SYNOPSIS

**pear** [_options_] _command_ [_command-options_] _args_

# PARAMETERS

**install**
> 安装软件包。

**upgrade**
> 升级软件包。

**uninstall**
> 移除软件包。

**list**
> 列出已安装的软件包。

**search**
> 搜索软件包。

**info**
> 软件包信息。

**channel-discover**
> 添加新通道。

# DESCRIPTION

**pear** 是 PHP 扩展与应用仓库（PEAR）管理器。它负责安装、升级和管理 PHP 软件包与扩展，早于 Composer 出现，曾是 PHP 的主要软件包管理器。
# 安装软件包
pear install Mail

# 从特定通道安装
pear channel-discover pear.phpunit.de
pear install phpunit/PHPUnit

# 列出过期的软件包
pear list-upgrades

# 获取软件包信息
pear info DB
```

# CHANNELS

```bash
# Add channel
pear channel-discover pear.example.com

# List channels
pear list-channels
```

# CAVEATS

在大多数使用场景下正被 Composer 取代。仍用于 PHP 扩展。全系统安装需要 root 权限。

# HISTORY

PEAR 由 **Stig Bakken** 于 1999 年作为 PHP 项目的一部分发起，目的是提供一套标准的软件包体系。

# SEE ALSO

[pecl](/man/pecl)(1), [composer](/man/composer)(1), [php](/man/php)(1)

# INSTALL

```apk: sudo apk add php85-pear```

<!-- packages: 2026-07-22 -->
