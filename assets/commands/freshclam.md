# TAGLINE

ClamAV 病毒数据库更新器

# TLDR

**更新病毒定义**

```freshclam```

仅**检查更新**

```freshclam --check```

以**守护进程**模式运行

```freshclam -d```

**详细输出**

```freshclam -v```

**使用指定配置**

```freshclam --config-file=[/path/freshclam.conf]```

# SYNOPSIS

**freshclam** [_options_]

# PARAMETERS

**-d**, **--daemon**
> 作为后台守护进程运行。

**-c** _N_, **--checks** _N_
> 以守护进程运行时每天的检查次数。

**-v**, **--verbose**
> 详细输出。

**--check**
> 只检查更新而不下载。

**--config-file** _FILE_
> 配置文件路径。

**-l** _FILE_, **--log** _FILE_
> 日志文件路径。

**-F**, **--foreground**
> 与 **-d** 组合使用时，保持在前台而不是脱离终端。

**-u** _USER_, **--user** _USER_
> 以 root 启动时，将权限降为指定用户。

**--datadir** _PATH_
> 覆盖数据库目录（默认 `/var/lib/clamav`）。

**--stdout**
> 将所有日志输出写到 stdout。

**--show-progress**
> 下载时显示进度条。

**--quiet**
> 仅输出错误信息。

**--no-warnings**
> 抑制警告信息。

**--update-db** _NAME_
> 只更新指定的数据库（`main`、`daily`、`bytecode`）。

**--on-update-execute** _CMD_
> 更新成功后运行 _CMD_。

**--on-error-execute** _CMD_
> 更新失败时运行 _CMD_。

**-V**, **--version**
> 输出版本信息并退出。

**--help**
> 显示帮助信息。

# CONFIGURATION

**/etc/clamav/freshclam.conf**
> 主配置文件，控制数据库镜像、更新频率、代理设置和通知选项。

# DESCRIPTION

**freshclam** 下载并更新 ClamAV 病毒特征数据库。它连接到 ClamAV 镜像，为 clamscan 和 clamd 扫描器获取最新的恶意软件定义。

该工具可以作为守护进程自动更新，也可以手动触发。多个镜像提供了冗余。下载的数据库在安装前会经过校验。

要让 ClamAV 对新威胁持续有效，freshclam 是必不可少的。

# CAVEATS

需要能访问镜像的网络。下载频率存在限制。首次运行时会下载较大的数据库。

# HISTORY

freshclam 是 **ClamAV**（开源防病毒引擎）的一部分。ClamAV 创建于 2001 年，后被 Sourcefire（即后来的 Cisco）收购，为 Unix 系统提供免费的病毒扫描。

# INSTALL

```apt: sudo apt install clamav-freshclam```

```dnf: sudo dnf install clamav-freshclam```

```apk: sudo apk add freshclam```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[clamscan](/man/clamscan)(1), [clamd](/man/clamd)(8), [clamdscan](/man/clamdscan)(1)
