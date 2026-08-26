# TAGLINE

将磁盘镜像挂载到单元的命名空间

# TLDR

将镜像**挂载**到单元中

```systemctl mount-image [unit] [/path/to/image] [/path/in/unit]```

带**选项**挂载

```systemctl mount-image [unit] [/path/to/image] [/path/in/unit] root:ro,nosuid```

挂载前**创建**目录

```systemctl mount-image --mkdir [unit] [/path/to/image] [/path/in/unit]```

以**只读**方式挂载

```systemctl mount-image --read-only [unit] [/path/to/image] [/path/in/unit]```

# SYNOPSIS

**systemctl mount-image** _UNIT_ _IMAGE_ [_PATH_ [_PARTITION:OPTIONS_]]

# PARAMETERS

**--mkdir**
> 如果目标目录不存在则创建它

**--read-only**
> 以只读方式挂载镜像

**--no-block**
> 不等待操作完成

# DESCRIPTION

**systemctl mount-image** 将一个磁盘镜像文件挂载到正在运行的单元的挂载命名空间中。仅支持拥有独立挂载命名空间的单元（使用 RootImage=、PrivateMounts= 等）。该功能在 systemd 248 中加入。

镜像通过 systemd 的可发现磁盘镜像（DDI）支持进行解析，自动找到并挂载合适的分区。可以在路径后使用 `PARTITION:OPTIONS` 语法指定分区名称和挂载选项。

# CAVEATS

要求单元拥有独立的挂载命名空间。只对正在运行的单元有效。挂载是临时性的，不会在单元重启后保留。支持 GPT 分区镜像和原始文件系统。

# HISTORY

**mount-image** 子命令可以在运行时将磁盘镜像注入隔离的服务中，无需完整的容器运行时即可实现类似容器的高级隔离。

# SEE ALSO

[systemctl-bind](/man/systemctl-bind)(1), [systemd-dissect](/man/systemd-dissect)(1), [systemctl](/man/systemctl)(1)
