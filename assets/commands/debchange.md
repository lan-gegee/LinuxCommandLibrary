# TAGLINE

Debian 变更日志维护工具

# TLDR

为**非维护者上传**添加新版本条目

```debchange -n```

向当前版本**追加**条目

```debchange -a```

添加用于**关闭某个 bug** 的条目

```debchange --closes [bug_id]```

# SYNOPSIS

**debchange** [_options_] [_text_]

# DESCRIPTION

**debchange**（也称 dch）维护 Debian 源码包的 debian/changelog 文件。它按照 Debian 政策处理版本编号、时间戳和变更日志条目的格式。

对 Debian 软件包维护者而言，它是跟踪软件包版本间变更的必备工具。

# PARAMETERS

**-n, --nmu**
> 为非维护者上传递增版本号

**-a, --append**
> 追加到当前变更日志条目

**--closes** _bug_
> 添加关闭指定 bug 的条目

**-i, --increment**
> 递增版本号并添加新条目

**-v** _version_
> 设置特定版本号

**-D** _distribution_
> 设置发行版（stable、unstable 等）

**-r, --release**
> 完成发布用的变更日志定稿

**--create**
> 创建新的 debian/changelog 文件

# CONFIGURATION

**~/.devscripts**
> debchange 行为的默认配置选项，包括维护者姓名和邮箱。

**/etc/devscripts.conf**
> 系统级 devscripts 配置文件。

# CAVEATS

必须在 Debian 源码包目录中运行。要求正确的 debian/changelog 格式。属于 devscripts 软件包。

# SEE ALSO

[dch](/man/dch)(1), [dpkg-buildpackage](/man/dpkg-buildpackage)(1), [debuild](/man/debuild)(1)

# RESOURCES

```[Source code](https://salsa.debian.org/debian/devscripts)```

```[Documentation](https://manpages.debian.org/devscripts/debchange.1)```

<!-- verified: 2026-07-11 -->
