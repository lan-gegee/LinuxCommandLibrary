# TAGLINE

在运行时将路径 bind 挂载到 unit 的挂载命名空间

# TLDR

将路径 **bind 挂载**到 unit

```systemctl bind [unit] [/path/to/host]```

挂载到 unit 内的**不同**位置

```systemctl bind [unit] [/host/path] [/unit/path]```

以**只读**方式挂载

```systemctl bind [unit] [/path] --read-only```

绑定前**创建**目标目录

```systemctl bind [unit] [/host/path] [/unit/path] --mkdir```

# SYNOPSIS

**systemctl bind** _UNIT_ _PATH_ [_PATH_]

# PARAMETERS

**--read-only**
> 在 unit 内以只读方式挂载该路径

**--mkdir**
> 如果目标目录不存在则创建它

# DESCRIPTION

**systemctl bind** 将主机上的文件或目录临时 bind 挂载到运行中 unit 的挂载命名空间。这允许向沙箱化的服务注入文件，而无需修改其 unit 配置。

如果只指定一个路径，挂载会出现在 unit 内的相同位置。如果给出两个路径，源路径会挂载到 unit 内的目标路径。

# CAVEATS

要求 unit 拥有独立的挂载命名空间（PrivateMounts=yes 或类似设置）。bind 是临时的，不会在 unit 重启后保留。unit 必须正在运行。

# HISTORY

**bind** 子命令加入 **systemctl**，用于在运行时向隔离的服务注入文件。它与 systemd 的 PrivateMounts、ProtectSystem 等沙箱特性互为补充。

# SEE ALSO

[systemctl](/man/systemctl)(1), [mount](/man/mount)(8), [systemd-run](/man/systemd-run)(1)
