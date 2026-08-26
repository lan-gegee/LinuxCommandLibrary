# TAGLINE

OpenWrt 固件升级工具

# TLDR

**检查**可用的固件升级

```owut check```

在保留所有软件包和配置的同时**升级**固件

```owut upgrade```

只**下载**固件镜像而不安装

```owut download```

**升级**到指定的 OpenWrt 版本

```owut upgrade -V [24.10.1]```

升级期间**添加软件包**

```owut upgrade -a [package1] -a [package2]```

升级期间**移除软件包**

```owut upgrade -r [package_name]```

**列出**所有用户安装的软件包

```owut list```

**显示可用**的 OpenWrt 版本

```owut versions```

# SYNOPSIS

**owut** [_options_] _command_

# DESCRIPTION

**owut**（OpenWrt Upgrade Tool）是一款命令行工具，通过 Attended Sysupgrade（ASU）服务器构建自定义镜像来升级 OpenWrt 路由器固件。它会构建保留所有已安装软件包和配置的个性化固件镜像，然后下载、验证并安装它们。

该工具与 ASU 服务器通信，请求构建与设备当前软件包集合相匹配的镜像，并可选择添加或移除软件包。它处理整个升级流程：收集设备信息、请求构建、监控进度、下载镜像、验证完整性以及执行 sysupgrade。

# COMMANDS

**check**
> 收集所有资源并报告升级统计信息，但不执行任何操作。

**upgrade**
> 构建、下载、验证并安装固件镜像。

**download**
> 构建并下载镜像并验证，但不安装。

**verify**
> 验证之前下载的固件镜像。

**install**
> 安装指定的本地固件镜像。

**list**
> 显示用户安装的所有软件包。

**versions**
> 显示可用的 OpenWrt 版本。

**blob**
> 显示 ASU 构建请求的 JSON 数据块。

**dump**
> 收集所有资源并导出内部数据结构。

# PARAMETERS

**-V** _version_, **--version-to** _version_
> 指定目标版本。默认为当前安装的版本。

**-R** _code_, **--rev-code** _code_
> 指定版本代号。允许字面值 **none**。默认为最新构建。

**-a** _package_, **--add** _package_
> 向构建列表添加新软件包。可重复使用。

**-r** _package_, **--remove** _package_
> 从构建列表中移除已安装的软件包。可重复使用。

**-i** _path_, **--image** _path_
> 用于 download、verify、install 和 upgrade 的镜像文件路径。默认为 **/tmp/firmware.bin**。

**-I** _path_, **--init-script** _path_
> 首次启动时运行的 uci-defaults 脚本路径。使用 **-** 表示从标准输入读取。

**-F** _type_, **--fstype** _type_
> 期望的根文件系统类型：**squashfs**、**ext4**、**ubifs** 或 **jffs2**。

**-S** _size_, **--rootfs-size** _size_
> 根文件系统大小（MB）。请谨慎使用。

**-p** _script_, **--pre-install** _script_
> 在启动最终 sysupgrade 之前执行的脚本。

**-f** _format_, **--format** _format_
> **list** 输出的格式：**fs-user**、**fs-all** 或 **config**。

**-k**, **--keep**
> 保存所有已下载的工作文件。

**--force**
> 即使存在降级或无更改也强制构建。

**--clean-slate**
> 从构建中移除除默认软件包以外的所有软件包。

**-v**, **--verbose**
> 输出各种诊断信息。重复使用可获得更多输出。

**-q**, **--quiet**
> 减少输出。重复使用可完全静默。

**-h**, **--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# CAVEATS

由于依赖 **ucode-mod-uclient** 软件包，owut 要求 OpenWrt **24.10 或更高版本**（包括 main 快照）。对于较旧的 OpenWrt 版本（23.05 及更早），请改用 **auc** 软件包。如果使用不当，**--rootfs-size** 选项可能导致设备无法启动。固件升级始终存在风险，应在稳定的电源和网络连接下进行。

# HISTORY

owut 由 **efahl** 创建并以开源项目形式发布在 GitHub 上，采用 **GPL-2.0** 许可证。它作为 **auc**（Attended Upgrade Client）工具的后继者开发，用 **ucode** 而非 C 重写，以便于维护和扩展。自 **24.10** 版本起成为 OpenWrt 的标准软件包，集成了自 **2017** 年以来一直是 OpenWrt 生态系统一部分的 Attended Sysupgrade 服务器基础设施。

# SEE ALSO

[opkg](/man/opkg)(1)
