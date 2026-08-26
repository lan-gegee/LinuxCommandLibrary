# TAGLINE

将软件包锁定在特定版本

# TLDR

将软件包**锁定在其当前安装的版本**

```sudo yum versionlock add [package_name]```

**列出所有已锁定的软件包**

```yum versionlock list```

**移除**特定软件包的锁定

```sudo yum versionlock delete [package_name]```

**清除所有版本锁定**

```sudo yum versionlock clear```

将软件包**锁定到指定版本**

```sudo yum versionlock add [package_name]-[version]-[release]```

**排除匹配某模式的软件包**，使其不被更新

```sudo yum versionlock exclude [package_pattern*]```

显示 versionlock 插件的**状态**

```yum versionlock status```

# SYNOPSIS

**yum versionlock** [_add_] [_list_] [_delete_] [_clear_] [_exclude_] [_status_] [_package ..._]

# PARAMETERS

**add** _package_
> 将指定软件包锁定在其当前安装的版本，阻止 yum 更新这些包。

**list**
> 显示当前所有已锁定的软件包及其版本。

**delete** _package_
> 移除指定软件包的版本锁定，允许其再次被更新。

**clear**
> 移除系统上所有的版本锁定。

**exclude** _package_
> 排除匹配给定通配符的软件包的当前可用版本。

**status**
> 列出当前被 versionlock 阻止的所有可用更新。

# DESCRIPTION

**yum-versionlock** 是一个 yum 插件，允许管理员将特定软件包锁定在其当前安装的版本，防止它们在系统升级时被更新。当较新的软件包版本可能破坏兼容性，或出于合规要求必须使用特定版本时，这个功能有助于维持系统稳定性。

软件包被锁定后，即使在已配置的软件仓库中有更新的版本，yum 也会在 **yum update** 操作中跳过它。锁定会跨重启和更新会话保持有效，直到被显式移除。

被锁定的软件包保存在 **/etc/yum/pluginconf.d/versionlock.list**（或因发行版而异的类似路径）中。每个条目遵循 NEVRA 格式：name-epoch:version-release.arch。

该插件需要单独安装：**yum install yum-plugin-versionlock**（RHEL/CentOS 7）或 **dnf install python3-dnf-plugin-versionlock**（Fedora/RHEL 8+）。在使用 DNF 的较新系统上，命令语法为 **dnf versionlock**。

# CAVEATS

如果其他软件包依赖较新的版本，锁定可能造成依赖冲突。被锁定软件包的安全更新也会被阻止，可能导致漏洞得不到修补。锁定文件的格式在 yum 和 dnf 版本之间有所变化。版本锁定不能阻止手动安装特定版本。

# HISTORY

versionlock 插件是为 Red Hat 系 Linux 发行版开发的 yum-utils 软件包集合的一部分。它提供的功能类似于 Debian 系统上的 apt-mark hold。随着 Fedora 22（2015 年）和 RHEL 8（2019 年）从 yum 向 DNF 过渡，该插件被重写为 DNF 插件，同时保持了命令兼容性。

# SEE ALSO

[yum](/man/yum)(8), [dnf](/man/dnf)(8), [rpm](/man/rpm)(8), [yum-config-manager](/man/yum-config-manager)(1)
