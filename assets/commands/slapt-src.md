# TAGLINE

构建并安装 SlackBuild 软件包

# TLDR

**更新**可用的 slackbuilds 列表

```slapt-src -u```

**列出**所有可用的 slackbuilds

```slapt-src -l```

**安装**一个 slackbuild（抓取、构建、安装）

```slapt-src -i [slackbuild_name]```

按名称或描述**搜索** slackbuilds

```slapt-src -s [search_term]```

**显示**某个 slackbuild 的信息

```slapt-src -w [slackbuild_name]```

# SYNOPSIS

**slapt-src** [_OPTIONS_] [_slackbuild_name_...]

# PARAMETERS

**-u, --update**
> 从配置的软件源更新可用 slackbuilds 的列表

**-l, --list**
> 列出所有可用的 slackbuilds

**-i, --install** _name_
> 抓取、构建并安装指定的 slackbuild(s)

**-s, --search** _term_
> 按名称或描述搜索 slackbuilds

**-w, --show** _name_
> 显示某个 slackbuild 的详细信息

**-b, --build** _name_
> 只构建 slackbuild，不安装

**-f, --fetch** _name_
> 仅下载 slackbuild 源码

**--yes**
> 对所有提示默认回答是

**--no**
> 对所有提示默认回答否

**-c, --config** _file_
> 使用替代的配置文件

**-h, --help**
> 显示帮助信息

# DESCRIPTION

**slapt-src** 自动化从 SlackBuilds 构建软件包的过程，提供与 **slapt-get** 二进制软件包管理类似的工作流。它负责从配置的仓库中查询、获取、构建和安装 SlackBuild 软件包。

SlackBuild 软件源在 **slapt-srcrc** 配置文件中设置，该文件指定了仓库位置（SOURCE）、构建目录（BUILDDIR）、软件包扩展名（PKGEXT）和软件包标签（PKGTAG）。

# CONFIGURATION

**/etc/slapt-get/slapt-srcrc**
> 配置文件，定义 SlackBuild 仓库 URL（SOURCE）、构建目录（BUILDDIR）、软件包扩展名（PKGEXT）和软件包标签（PKGTAG）。

# CAVEATS

依赖 **slapt-get** 和 **curl**。SlackBuilds 是在你的系统上编译的源码包，大型软件包可能耗时较长。编译前必须满足构建依赖。配置必须指向有效的 SlackBuild 仓库。

# HISTORY

**slapt-src** 由 **Jason Woodward**（jaos）创建，作为 Slackware Linux 上 **slapt-get** 的配套工具。项目始于 **2010 年**前后，旨在为 SlackBuild 管理提供类 apt 的体验。它以 GPL-2.0 许可证发布，目前仍在积极维护。

# SEE ALSO

[slapt-get](/man/slapt-get)(8), [sbopkg](/man/sbopkg)(8), [slackpkg](/man/slackpkg)(8)
