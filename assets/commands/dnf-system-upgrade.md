# TAGLINE

用于 Fedora 大版本离线升级的 DNF 插件

# TLDR

为目标发行版**下载**全部软件包

```sudo dnf system-upgrade download --releasever=[40]```

**重启**并执行已暂存的升级

```sudo dnf system-upgrade reboot```

**允许删除**阻碍依赖解析的软件包（如过时的第三方仓库）

```sudo dnf system-upgrade download --releasever=[40] --allowerasing```

**取消**已暂存的升级并清理缓存数据

```sudo dnf system-upgrade clean```

**检查状态**：查看待执行的升级

```dnf system-upgrade status```

**查看日志**：查看之前升级尝试的记录

```sudo dnf system-upgrade log --number=[-1]```

# SYNOPSIS

**dnf system-upgrade** _subcommand_ [_options_]

# PARAMETERS

**download**
> 下载升级所需的全部软件包，并为下次启动做好暂存。

**reboot**
> 触发重启进入离线升级环境以执行事务。

**clean**
> 移除缓存的软件包和保存的事务状态。

**status**
> 打印当前待处理升级的状态（无升级、下载完成等）。

**log**
> 列出之前的升级尝试；配合 **--number** _N_ 可显示对应那次启动的日志输出（通常用 **-1** 表示最近一次）。

**--releasever=**_VER_
> 设置要升级到的 Fedora 发行版版本（如 **40**、**41**）。

**--allowerasing**
> 允许 DNF 删除在新发行版上无法满足依赖的软件包。

**--best**
> 尽量使用最优的可用软件包版本，做不到则失败。

**--nogpgcheck**
> 跳过 GPG 签名验证（不建议）。

# DESCRIPTION

**dnf system-upgrade** 是一款 DNF 插件，用于以离线方式对 Fedora 及其他 RPM 系发行版进行大版本升级。它不在系统运行时直接升级，而是先下载所有必需的软件包，然后重启进入专用的 systemd target，在没有用户进程运行的情况下完成事务。

工作流分为三个阶段：**download** 暂存软件包并验证依赖；**reboot** 重启机器进入离线升级环境；完成后系统再次重启进入新版本。如果中途放弃升级，**clean** 会丢弃暂存的事务。

该插件还提供 **offline-upgrade** 和 **offline-distrosync** 子命令，将同样的离线机制应用于普通更新和 distro-sync，而非版本变更。

# CAVEATS

重启阶段会重写正在使用的根文件系统；机器必须接稳定电源且不能中断，否则系统可能无法启动。第三方仓库常常滞后一个发行版版本，因此经常需要 **--allowerasing**。该插件只支持向前升级；跨版本降级并不安全。官方不支持跳版本升级（如从 39 直接到 41），即使看起来能成功也不受支持。

# HISTORY

该插件起源于 **2012 年**面向 Fedora 18 的 **fedup**，提供了首个受支持的就地升级途径。**2015 年**为 Fedora 23 重写为 **dnf-plugin-system-upgrade** 以集成到 DNF，并被并入 **dnf-plugins-extras**。**2024 年**，该插件成为随 Fedora 41 发布的 **dnf5** 的一等组件。

# SEE ALSO

[dnf](/man/dnf)(8), [dnf5](/man/dnf5)(8), [systemctl](/man/systemctl)(1), [rpm](/man/rpm)(8)
