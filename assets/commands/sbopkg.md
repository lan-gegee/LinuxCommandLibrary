# TAGLINE

SlackBuilds.org 软件包管理工具

# TLDR

**与 SlackBuilds.org 仓库同步**

```sbopkg -r```

**启动 dialog 交互界面**

```sbopkg```

从命令行**安装软件包**

```sbopkg -i [package]```

按依赖顺序**安装多个软件包**

```sbopkg -i "[dep1] [dep2] [package]"```

**检查**已安装 SBo 软件包的**更新**

```sbopkg -c```

**搜索并查看**软件包

```sbopkg -s [package]```

**构建软件包但不安装**

```sbopkg -b [package]```

# SYNOPSIS

**sbopkg** [_-r_] [_-c_] [_-i package_] [_-b package_] [_-s package_] [_-g_]

# PARAMETERS

**-r**
> 与远程 SlackBuilds.org 仓库同步

**-c**
> 检查已安装 SBo 软件包的更新

**-i** _package_
> 安装指定软件包（多个软件包需加引号）

**-b** _package_
> 构建软件包但不安装

**-s** _package_
> 搜索并显示软件包信息（README、SlackBuild、.info）

**-g**
> 升级有可用更新的已安装软件包

**-V**
> 显示版本信息

**-h**
> 显示帮助及所有命令行选项

# DESCRIPTION

**sbopkg** 是一款面向 Slackware Linux 的工具，用于对接 SlackBuilds.org（SBo）仓库。它可以同步仓库的本地副本、浏览可用软件包，并自动化第三方软件的构建与安装。

该工具既提供基于 dialog 的交互界面，也提供命令行选项。它可以查看 README 文件、SlackBuild 脚本和 .info 文件，通过 MD5 校验下载源码，并构建 Slackware 软件包。队列文件（.sqf）支持批量处理多个软件包。

当主下载 URL 失败时，sbopkg 可以回退到 SBo Source Archive 获取源码。

# CAVEATS

sbopkg 不会自动处理依赖，因为这不是 Slackware 的原生特性。请按顺序手动安装依赖，或在引号内列出所有软件包：**-i "dep1 dep2 package"**。必须以 root 身份运行。

# HISTORY

sbopkg 的创建旨在简化对 SlackBuilds.org（一个面向 Slackware 软件包的社区构建脚本仓库）的访问。新版本随每个 Slackware 发行版一同发布，以保持与发行版和 SBo 仓库的兼容性。

# SEE ALSO

[slackpkg](/man/slackpkg)(8), [installpkg](/man/installpkg)(8), [upgradepkg](/man/upgradepkg)(8), [makepkg](/man/makepkg)(8)
