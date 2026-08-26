# TAGLINE

Salix Package Installer：包装 slapt-get 和 slapt-src 的元软件包管理器

# TLDR

**搜索**二进制仓库和 SlackBuild 仓库（默认操作）

```spi [search_terms]```

**更新**软件包与 SlackBuild 本地缓存

```sudo spi -u```

**安装**软件包或 SlackBuild

```sudo spi -i [package_name]```

**模拟**安装过程，显示将要执行的操作

```spi -s -i [package_name]```

**升级**所有已安装的软件包

```sudo spi -U```

**显示信息**：查看某个软件包或 SlackBuild 的详情

```spi --show [package_name]```

**清理**本地软件包与 SlackBuild 缓存

```sudo spi --clean```

# SYNOPSIS

**spi** [_OPTIONS_] [_STRING(S)_]

# DESCRIPTION

**spi**（Salix Package Installer）是 **Salix Linux** 的命令行元软件包管理器，对 **slapt-get** 和 **slapt-src** 进行了封装。它通过单一界面提供对二进制软件包和 SlackBuilds 的统一访问。

搜索时，**spi** 会同时查询 **slapt-get** 二进制包缓存和 **slapt-src** SlackBuild 缓存。安装时，它优先使用二进制包：如果没有可用的二进制包，则回退到通过 **slapt-src** 从源码构建；当某个 SlackBuild 的依赖已有对应的二进制包时，它会通过 **slapt-get** 拉取这些依赖，而不是重新构建。

spi 只暴露基础功能；高级功能请直接使用底层的 **slapt-get** 和 **slapt-src** 工具。

# PARAMETERS

**--search** _STRING(S)_
> 同时搜索软件包和 SlackBuild 数据库。当调用 **spi** 时只给出一个或多个字符串而无其他选项，此为默认操作。支持正则表达式。

**--show** _PACKAGE(S)_
> 显示指定软件包或 SlackBuild 的详情（运行 **slapt-get --show** 和 **slapt-src --show**）。

**--clean**
> 清除缓存的软件包和 SlackBuild 构建目录。需要 root 权限。

**-u**, **--update**
> 更新软件包和 SlackBuild 本地缓存。需要 root 权限。

**-U**, **--upgrade**
> 使用 **slapt-get --upgrade** 升级所有已安装的软件包。需要 root 权限。

**-i**, **--install** _PACKAGE(S)_
> 安装指定的软件包或 SlackBuild。优先使用二进制包；否则构建并安装 SlackBuild。需要 root 权限。

**-s**, **--simulate**
> 与 **--install** 配合使用：模拟该操作，列出将要安装的软件包和 SlackBuild（包括依赖项）。

**-n**, **--no-colour**
> 搜索时禁用彩色输出。

**-h**
> 打印简要用法消息并退出。

# CAVEATS

需要已安装并配置好 **slapt-get** 和 **slapt-src**。SlackBuild 安装需从源码编译，可能比二进制安装慢得多。该工具仅适用于 **Salix** 及其他提供 slapt 工具链的 Slackware 衍生发行版。在搜索或安装新发布的软件包之前，必须先更新缓存（**spi -u**）。

# HISTORY

**spi** 由 **George Vlahavas**（gapan）为 **Salix** Linux 发行版创建。Salix 是一个注重简洁易用的 Slackware 衍生版，创立于 **2009 年**。此后 **spi** 一直是连接 Slackware 二进制软件包体系与 SlackBuild 源码构建体系的友好桥梁。

# SEE ALSO

[slapt-get](/man/slapt-get)(8), [slapt-src](/man/slapt-src)(8), [slackpkg](/man/slackpkg)(8)
