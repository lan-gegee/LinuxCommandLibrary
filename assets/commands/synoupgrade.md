# TAGLINE

Synology 固件升级工具

# TLDR

**检查**可用升级

```sudo synoupgrade --check```

只检查**补丁**

```sudo synoupgrade --check-smallupdate```

**下载**最新升级

```sudo synoupgrade --download```

**开始**升级过程

```sudo synoupgrade --start```

**自动**升级到最新版本

```sudo synoupgrade --auto```

**自动**只应用补丁

```sudo synoupgrade --auto-smallupdate```

从**补丁文件**升级

```sudo synoupgrade --patch [/path/to/file.pat]```

显示**帮助**

```synoupgrade```

# SYNOPSIS

**synoupgrade** [**-h**]

**synoupgrade** [**-p** _file.pat_] [**--no-reboot**]

**synoupgrade** [**--online** | **--online_download** | **--online_install**]

# PARAMETERS

**-h**
> 显示帮助信息

**-p, --patch** _file.pat_
> 从本地补丁文件升级（需要绝对路径）

**--no-reboot**
> 阻止升级后自动重启

**--check**
> 在线检查可用升级

**--check-smallupdate**
> 检查不含主版本升级的补丁

**--download**
> 下载最新升级

**--download-smallupdate**
> 只下载补丁

**--start**
> 开始升级过程

**--auto**
> 自动升级到最新版本

**--auto-smallupdate**
> 自动应用补丁

**--online**
> 在线检查服务器上的更新

**--online_download**
> 下载可用的更新

**--online_install**
> 安装已下载的更新

# DESCRIPTION

**synoupgrade** 是 Synology DiskStation Manager（DSM）的固件升级工具。它提供对 NAS 操作系统更新过程的命令行控制，既支持从本地补丁文件手动升级，也支持自动在线更新。

该工具处理 DSM 专有的 .pat 固件包，并管理包括下载、校验、安装和系统重启在内的完整升级流程。

# CAVEATS

需要 root 权限。NAS 上必须启用 SSH 访问。只接受 Synology 的 .pat 固件文件。升级过程中断可能导致系统损坏或数据丢失。升级前务必备份重要数据。除非指定 --no-reboot，系统通常会在升级后重启。

# HISTORY

**synoupgrade** 由 **Synology Inc.** 开发，是 DiskStation Manager 的一部分。Synology NAS 设备自 **2004 年**起上市，DSM 逐步演进为其主要操作系统。命令行升级工具是对 Web 控制面板升级界面的补充。

# SEE ALSO

[synopkg](/man/synopkg)(8), [synoservice](/man/synoservice)(8)
