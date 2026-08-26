# TAGLINE

提交和查询 Arch 软件包使用统计

# TLDR

匿名**提交**已安装软件包数据

```pkgstats submit```

以 **JSON 转储**显示将要提交的内容而不发送

```pkgstats submit --dump-json```

按名称**搜索**软件包

```pkgstats search [term]```

**比较**多个软件包的热门程度

```pkgstats show [firefox] [chromium]```

显示**帮助**

```pkgstats --help```

# SYNOPSIS

**pkgstats** _subcommand_ [_options_] [_packages_...]

# COMMANDS

**submit**
> 匿名收集并发送已安装软件包列表、架构和镜像站信息。

**search** _term_
> 搜索软件包并显示其热门程度指标。

**show** _packages_...
> 比较给定软件包的热度统计。

# PARAMETERS

**--dump-json**
> 配合 `submit` 使用时，打印将要发送的 JSON 数据而不实际提交。

**-h**, **--help**
> 显示帮助信息。

**-V**, **--version**
> 显示版本信息。

# CONFIGURATION

**/etc/pkgstats.yaml**
> 可选的配置文件，用 glob 模式将某些软件包或镜像站从提交内容中过滤掉。

# DESCRIPTION

**pkgstats** 收集并提交关于已安装软件包的匿名统计信息，帮助 Arch Linux 社区了解软件包的使用模式。这些数据有助于维护者确定开发工作的优先级。

用户也可以查询收集到的统计信息，查看软件包热度并比较不同软件包。提交是自愿的且保护隐私。

# CAVEATS

提交和查询都需要联网。数据是匿名的，但包含软件包列表和架构信息。仅限自愿参与。

# HISTORY

**pkgstats** 由 **Arch Linux DE** 社区维护，用于收集软件包使用统计。它帮助 Arch 社区就软件包维护和仓库组织做出明智决策。

# INSTALL

```pacman: sudo pacman -S pkgstats```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pacman](/man/pacman)(8), [pkgfile](/man/pkgfile)(1)
