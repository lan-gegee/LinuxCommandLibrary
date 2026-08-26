# TAGLINE

Synology NAS 软件包管理工具

# TLDR

**列出**已安装的软件包

```synopkg list --name```

列出**依赖于**其他软件包的软件包

```synopkg list --depend-on [package]```

**启动、停止或重启**软件包

```sudo synopkg [start|stop|restart] [package]```

显示软件包**状态**

```synopkg status [package]```

**卸载**软件包

```sudo synopkg uninstall [package]```

检查**更新**

```synopkg checkupdate [package]```

将所有软件包**升级**

```sudo synopkg upgradeall```

从 SPK 文件**安装**

```sudo synopkg install [path/to/package.spk]```

# SYNOPSIS

**synopkg** _command_ [_OPTIONS_]

# COMMANDS

**list** [**--name**] [**--depend-on** _pkg_]
> 列出已安装的软件包

**install** _file.spk_
> 从 SPK 文件安装软件包

**uninstall** _package_
> 移除已安装的软件包

**start** _package_
> 启动一个软件包服务

**stop** _package_
> 停止一个软件包服务

**restart** _package_
> 重启一个软件包服务

**status** _package_
> 显示软件包运行状态

**is_onoff** _package_
> 检查软件包是否已启用

**checkupdate** _package_
> 检查软件包更新

**upgradeall**
> 将所有软件包升级到最新版本

**log** _package_
> 查看软件包日志

# PARAMETERS

**--name**
> 只显示软件包名称

**--depend-on** _package_
> 列出依赖于指定软件包的软件包

# DESCRIPTION

**synopkg** 是 Synology DiskStation Manager（DSM）——Synology NAS 设备操作系统——的软件包管理工具。它提供对软件包安装、更新和服务管理的命令行控制。

该工具包装了位于 `/var/packages/<package>/scripts/start-stop-status` 的每个软件包的启动/停止脚本。安装软件包时它会自动处理依赖解析，并与 DSM 的套件中心集成。

# CAVEATS

安装/卸载/启动/停止操作需要 root 权限。Synology NAS 上必须启用 SSH 访问。只接受 SPK 软件包格式。安装约束与 Web 界面套件中心相同。

# HISTORY

**synopkg** 由 **Synology Inc.** 开发，是其 DiskStation Manager 操作系统的一部分。DSM 为 Synology NAS 设备提供基于 Linux 的平台，最早于 **2000 年代中期**推出。命令行工具是对基于 Web 的管理界面的补充。

# SEE ALSO

[synoupgrade](/man/synoupgrade)(8), [synoservice](/man/synoservice)(8)
