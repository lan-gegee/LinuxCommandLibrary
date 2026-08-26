# TAGLINE

类 APT 的 Slackware 软件包管理器

# TLDR

**更新**可用软件包列表

```slapt-get --update```

**安装**软件包

```slapt-get --install [package]```

**移除**软件包

```slapt-get --remove [package]```

**升级**所有已安装的软件包

```slapt-get --upgrade```

**搜索**软件包

```slapt-get --search [query]```

**显示**软件包信息

```slapt-get --show [package]```

# SYNOPSIS

**slapt-get** [_options_] [_package_...]

# PARAMETERS

**--update**
> 从软件源更新软件包列表

**--install _package_**
> 安装或升级软件包

**--remove _package_**
> 移除已安装的软件包

**--upgrade**
> 升级所有已安装的软件包

**--search _query_**
> 按名称、磁盘集或版本搜索软件包

**--show _package_**
> 显示软件包信息

**--clean**
> 清理软件包缓存

**--autoclean**
> 仅从缓存中移除过时的软件包

**--dist-upgrade**
> 升级到更新的 Slackware 发行版本

**--available**
> 列出配置的软件源中可用的软件包

**--list**
> 列出所有软件包，包括已安装和可用的

**--installed**
> 列出当前所有已安装的软件包

**--filelist _package_**
> 显示某个软件包安装的文件

**--remove-obsolete**
> 移除配置的软件源中已不存在的软件包（与 --remove 或 --dist-upgrade 一起使用）

**--reinstall**
> 即使软件包已安装也重新安装

**--download-only**, **-d**
> 只下载软件包而不安装

**--simulate**, **-s**
> 模拟操作，不安装也不下载任何内容

**--no-dep**
> 跳过依赖解析

**--ignore-dep**
> 在安装或升级期间忽略依赖错误

**--no-prompt**, **-y**
> 不提示确认

**--print-uris**
> 将软件包的 URI 打印到 stdout，不下载

**--add-keys**
> 从软件源下载并导入 GPG 密钥

**--retry _N_**
> 下载失败时的重试次数

**--config**, **-c _file_**
> 使用替代的配置文件

# DESCRIPTION

**slapt-get** 是一个面向 Slackware Linux 的类 APT 软件包管理系统。它提供依赖解析功能，并复刻了大家熟悉的 apt-get 工作流来管理软件包。

软件源在 slapt-getrc 配置文件中设置。

# CONFIGURATION

**/etc/slapt-get/slapt-getrc**
> 主配置文件，定义软件源 URL、缓存目录和排除的软件包。

# CAVEATS

需要在 slapt-getrc 中配置好软件源。专为 Slackware Linux 发行版设计。

# SEE ALSO

[installpkg](/man/installpkg)(8), [removepkg](/man/removepkg)(8), [pkgtool](/man/pkgtool)(8), [slackpkg](/man/slackpkg)(1), [slapt-src](/man/slapt-src)(1)
