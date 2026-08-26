# TAGLINE

Red Hat 软件包管理器

# TLDR

在现代发行版（RHEL 8+、Fedora 22+）上，**yum** 是指向 **dnf** 的符号链接。

**安装**软件包

```sudo yum install [package]```

**移除**软件包

```sudo yum remove [package]```

**更新**所有软件包

```sudo yum update```

**更新**指定软件包

```sudo yum update [package]```

按名称**搜索**软件包

```yum search [keyword]```

**列出已安装的**软件包

```yum list installed```

**显示**软件包信息

```yum info [package]```

**清理**缓存数据

```yum clean all```

# SYNOPSIS

**yum** [_options_] [_command_] [_package_...]

# PARAMETERS

**install** _package_
> 安装一个或多个软件包。

**remove** _package_
> 移除软件包。

**update** [_package_]
> 更新所有软件包，若给定包名则只更新该包。

**search** _keyword_
> 搜索软件包名称和描述。

**info** _package_
> 显示软件包的详细信息。

**list** [_installed_|_available_|_updates_]
> 列出软件包。**installed** 为已安装，**available** 为仓库中的软件包，**updates** 为可用更新。

**clean** [_all_|_packages_|_metadata_]
> 清理缓存数据。

**provides** _file_
> 查找提供某个文件的软件包。

**groupinstall** _group_
> 安装软件包组。

**repolist** [_all_|_enabled_|_disabled_]
> 列出已配置的软件仓库。

**history**
> 查看事务历史。

**-y**
> 对所有提示自动回答 yes。

**--enablerepo=**_repo_
> 临时启用特定软件仓库。

**--disablerepo=**_repo_
> 临时禁用特定软件仓库。

**--nogpgcheck**
> 跳过 GPG 签名检查。

# DESCRIPTION

**yum**（Yellowdog Updater Modified）是 Red Hat 系 Linux 发行版传统的软件包管理器。在现代系统上（RHEL 8+、Fedora 22+），**yum** 是指向 **dnf** 的符号链接，dnf 以更好的性能提供相同的功能。

在 CentOS 7 等较旧的系统上，yum 是原生软件包管理器，负责从已配置的软件仓库进行软件包的安装、更新和移除。

# CAVEATS

在现代系统上，yum 是 dnf 的别名。旧版 yum 与 dnf 的行为可能略有差异。较新的系统请直接使用 **dnf**。

# SEE ALSO

[dnf](/man/dnf)(8), [rpm](/man/rpm)(8), [apt-get](/man/apt-get)(8), [zypper](/man/zypper)(8)
