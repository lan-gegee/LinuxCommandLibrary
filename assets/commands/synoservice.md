# TAGLINE

Synology NAS 服务管理

# TLDR

**列出所有服务**

```synoservicecfg --list```

**检查服务状态**

```synoservice --status [servicename]```

**启动服务**

```synoservicecfg --start [servicename]```

**停止服务**

```synoservicecfg --stop [servicename]```

**强制停止服务**

```synoservicecfg --hard-stop [servicename]```

**重启服务**

```synoservice --restart [servicename]```

**重启软件包服务**

```synoservicectl --restart [pkgctl-WebStation]```

# SYNOPSIS

**synoservice** {--status|--restart} [_service_]

**synoservicecfg** {--start|--stop|--hard-start|--hard-stop|--list} [_service_]

**synoservicectl** {--start|--stop|--restart|--status} [_service_]

# PARAMETERS

**--status**
> 显示指定服务的状态。

**--start**
> 启动指定的服务。

**--stop**
> 停止指定的服务。

**--restart**
> 重启指定的服务。

**--hard-start**
> 强制启动服务。

**--hard-stop**
> 强制停止服务。

**--list**
> 列出所有可用服务。

# DESCRIPTION

**synoservice** 及相关命令（**synoservicecfg**、**synoservicectl**）是 Synology NAS 的实用工具，可通过 SSH 在命令行管理系统服务和软件包服务。

这些命令控制 DSM（DiskStation Manager）的服务，包括 Web 服务器、Samba 文件共享、SSH、FTP、Docker 以及第三方套件。它们位于 /usr/syno/sbin/ 下，需要 root 权限。

常见服务包括 DSM、nginx、samba、ssh-shell、nfsd、ftpd、crond，以及以 pkgctl- 为前缀的软件包服务，例如 pkgctl-Docker 和 pkgctl-WebStation。

在 DSM 7 及更新版本中，也可以使用标准的 **systemctl** 命令管理服务。

# CAVEATS

需要 SSH 访问和 root 权限（使用 sudo -i）。不同 DSM 版本之间命令可能略有差异。软件包服务使用 pkgctl- 前缀。某些关键服务不应被远程停止。在 DSM 7 及以上版本，可考虑改用 systemctl。

# HISTORY

**synoservice** 系列工具是 Synology 专有工具，为其 DiskStation Manager 操作系统开发。它们在不同 DSM 版本和硬件平台上提供一致的服务管理接口。DSM 7 在保留这些传统工具的同时引入了更好的 systemd 集成。

# SEE ALSO

[systemctl](/man/systemctl)(1), [service](/man/service)(8)
