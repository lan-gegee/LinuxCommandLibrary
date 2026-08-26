# TAGLINE

为 systemd 容器和系统扩展管理磁盘镜像

# TLDR

从 URL **下载** tar 归档镜像

```sudo importctl pull-tar [URL] [name]```

**拉取** raw 或 qcow2 磁盘镜像

```sudo importctl pull-raw [https://example.com/source.ext] [name] --class=[machine|portable|sysext|confext]```

**导入** raw 磁盘镜像

```importctl import-raw [path/to/file.ext] [name] --class=[machine|portable|sysext|confext]```

**列出**当前正在进行的传输

```importctl list-transfers```

**取消**正在运行的传输

```importctl cancel-transfer [transfer-id]```

将容器镜像**导出**为 tar 归档

```importctl export-tar --class=[machine|portable|sysext|confext] [name] [path/to/file.ext]```

# SYNOPSIS

**importctl** _command_ [_options_]

# PARAMETERS

**pull-tar** _URL_ _NAME_
> 从 URL 下载并导入 tar 归档

**pull-raw** _URL_ _NAME_
> 下载并导入 raw/qcow2 磁盘镜像

**import-tar** _FILE_ _NAME_
> 将本地 tar 归档导入镜像目录

**import-raw** _FILE_ _NAME_
> 导入本地 raw 磁盘镜像

**export-tar** _NAME_ _FILE_
> 将容器导出为 tar 归档

**export-raw** _NAME_ _FILE_
> 将容器导出为 raw 磁盘镜像

**list-transfers**
> 显示当前正在运行的传输

**cancel-transfer** _ID_
> 取消正在运行的导入、导出或下载

**--class** _TYPE_
> 镜像类别：machine、portable、sysext、confext

**--verify** _MODE_
> 下载的校验模式：no、checksum、signature（默认：signature）

**--format** _FORMAT_
> raw 操作使用的镜像格式：raw、qcow2（默认：raw）

# DESCRIPTION

**importctl** 为 systemd 容器和系统扩展管理磁盘镜像。它可以下载、导入和导出多种镜像格式，包括 tar 归档、raw 磁盘镜像和 qcow2 虚拟机镜像。

该工具与 systemd-machined 和 systemd-importd 服务集成，处理容器、可移植服务以及系统/配置扩展的镜像管理。

# CAVEATS

需要安装 systemd 且相关服务正在运行。某些操作需要 root 权限。网络操作依赖 systemd-importd 服务。

# HISTORY

importctl 是 systemd 的一部分，旨在为容器和扩展镜像的管理提供统一接口。它取代了 systemd 生态中旧的、较为零散的镜像管理方式。

# INSTALL

```apt: sudo apt install systemd-container```

```dnf: sudo dnf install systemd-container```

```zypper: sudo zypper install systemd-container```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[machinectl](/man/machinectl)(1), [systemd-nspawn](/man/systemd-nspawn)(1), [systemctl](/man/systemctl)(1)
