# TAGLINE

让外部硬盘在空闲一段时间后停转的工具

# TLDR

**启动** hd-idle 服务并使用默认设置（10 分钟空闲时间）

```systemctl start hd-idle```

**立即停转**某块磁盘

```hd-idle -t [/dev/sdX]```

以秒为单位设置**各磁盘的空闲时间**

```hd-idle -i 0 -a /dev/sda -i [300] -a /dev/sdb -i [1200]```

全局禁用停转，仅为**特定磁盘**启用

```hd-idle -i 0 -a [/dev/sda] -i [600]```

# SYNOPSIS

**hd-idle** [_options_]

# PARAMETERS

**-a** _DEVICE_
> 将其后的空闲时间应用到指定设备

**-i** _SECONDS_
> 设置空闲时间（秒）（0 表示禁用停转）

**-t** _DEVICE_
> 立即停转指定磁盘

**-l** _LOGFILE_
> 将停转事件记录到指定文件

**-d**
> 以调试模式运行，不守护进程化

# DESCRIPTION

**hd-idle** 是一款在空闲一段时间后停转外部硬盘的工具。对于不支持 hdparm -S 自动停转命令的 USB 或 eSATA 硬盘，它尤其有用。

守护进程监视磁盘活动，并在磁盘空闲达到配置的时间后发出停转命令。可以为不同的磁盘设置不同的空闲时间，从而对电源管理进行细粒度控制。

# CAVEATS

对不支持原生 APM 的外置硬盘效果最好。有些硬盘可能不响应软件发出的停转命令。频繁的停转/启动循环可能会缩短硬盘寿命。

# HISTORY

hd-idle 是为缺乏妥善电源管理支持的外置硬盘而设计的解决方案。它填补了 hdparm 停转功能无法工作时的空白——这种情况常见于不透传 ATA 命令的 USB 硬盘盒。

# INSTALL

```apt: sudo apt install hd-idle```

```dnf: sudo dnf install hd-idle```

```apk: sudo apk add hd-idle```

```nix: nix profile install nixpkgs#hd-idle```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hdparm](/man/hdparm)(8), [smartctl](/man/smartctl)(8)
