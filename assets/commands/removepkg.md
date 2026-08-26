# TAGLINE

移除 Slackware 软件包

# TLDR

**移除**软件包

```sudo removepkg package_name```

生成**模拟卸载报告**

```removepkg -warn package_name```

**保留**软件包文件后再移除

```sudo removepkg -preserve package_name```

**复制**软件包而不移除

```removepkg -copy package_name```

**保留**临时文件以便调试

```sudo removepkg -keep package_name```

# SYNOPSIS

**removepkg** [_options_] _package_name_

# PARAMETERS

**-warn**
> 生成模拟卸载报告，但不实际移除

**-preserve**
> 在移除前于 /tmp/preserved_packages 中重建软件包目录树

**-copy**
> 将软件包复制到 /tmp/preserved_packages，不移除

**-keep**
> 保留临时文件以便调试

# DESCRIPTION

**removepkg** 从系统中移除指定的 Slackware 软件包。它可以模拟移除、在删除前保留软件包文件，或复制软件包而不实际移除。

该工具是 Slackware 原生软件包管理系统的一部分。

# CAVEATS

不会自动处理依赖。移除被其他软件包依赖的软件包可能导致系统损坏。

# HISTORY

属于 **Slackware** 软件包管理工具集的一部分。为 Slackware Linux 发行版提供基础的软件包移除功能。

# SEE ALSO

[installpkg](/man/installpkg)(8), [upgradepkg](/man/upgradepkg)(8), [pkgtool](/man/pkgtool)(8)
