# TAGLINE

处理 RPM 配置文件冲突

# TLDR

列出遗留文件并**交互式选择**处理动作

```sudo rpmconf -a```

**删除孤立的** .rpmnew 和 .rpmsave 文件

```sudo rpmconf -a -c```

# SYNOPSIS

**rpmconf** [_options_]

# PARAMETERS

**-a**, **--all**
> 处理所有配置文件

**-c**, **--clean**
> 删除孤立的配置备份文件

# DESCRIPTION

**rpmconf** 处理 RPM 软件包升级后遗留的 .rpmnew、.rpmsave 和 .rpmorig 文件。当软件包更新携带的配置变更可能与本地修改冲突时，就会产生这些文件。

该工具提供一个交互界面，用于合并、替换或保留配置文件。

# CAVEATS

应用更改前请仔细审阅。选择不当可能覆盖重要的自定义配置，或者留下过时的配置。

# HISTORY

属于 Fedora/RHEL 系统的 **rpmconf** 软件包。简化升级后的配置管理。

# INSTALL

```dnf: sudo dnf install rpmconf```

```zypper: sudo zypper install rpmconf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rpm](/man/rpm)(8), [dnf](/man/dnf)(8), [yum](/man/yum)(8)
