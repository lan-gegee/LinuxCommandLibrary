# TAGLINE

报告设备和分区的 CPU 与 I/O 统计信息

# TLDR

显示 **CPU 和磁盘**统计信息

```iostat```

以**兆字节**为单位显示

```iostat -m```

仅显示 **CPU 统计信息**

```iostat -c```

带名称显示**磁盘统计信息**

```iostat -N```

显示**扩展的**磁盘统计信息

```iostat -x```

显示**特定设备**的扩展统计信息

```iostat -xN [sda]```

每隔 **2 秒**显示一次报告

```iostat 2```

以 2 秒为间隔显示 **5 份报告**

```iostat 2 5```

以 **JSON 格式**显示

```iostat -o JSON```

省略**首次启动报告**并只显示活跃设备

```iostat -yz 2```

# SYNOPSIS

**iostat** [_options_] [_device_...] [_interval_ [_count_]]

# DESCRIPTION

**iostat** 通过观察设备活跃时间与其平均传输速率的关系来监视系统输入/输出设备的负载。它生成的 CPU 和设备利用率报告有助于优化 I/O 性能。

# PARAMETERS

**-c**
> 仅显示 CPU 利用率

**-d**
> 仅显示设备利用率

**-x**
> 显示扩展统计信息

**-k**
> 以每秒千字节为单位显示统计信息

**-m**
> 以每秒兆字节为单位显示统计信息

**-N**
> 显示已注册的 device mapper 名称（LVM）

**-p** [_device_|ALL]
> 显示块设备及所有分区的统计信息。

**-h**
> 使 NFS 和设备报告更易于人类阅读。

**-t**
> 为每份报告打印时间戳

**-y**
> 省略第一份报告（启动以来的统计）

**-z**
> 从报告中排除不活跃的设备

**-g GROUP**
> 分组显示统计信息

**-H**
> 配合 -g 只显示分组总计

**-j {ID|LABEL|PATH|UUID}**
> 显示持久化设备名

**-o JSON**
> 以 JSON 格式输出

**--human**
> 以人类可读格式打印大小

**--pretty**
> 美化打印设备名。

**-s**
> 显示适合 80 列屏幕的简短（窄幅）报告。

**-V**
> 打印版本号并退出。

# CAVEATS

第一份报告显示自启动以来的统计信息。要查看当前活动，请使用 **-y** 选项或忽略第一份报告。扩展统计（**-x**）提供更详细的 I/O 指标。

# HISTORY

**iostat** 是 **sysstat** 软件包的一部分，为 Linux 提供系统性能监控工具。

# INSTALL

```apt: sudo apt install sysstat```

```dnf: sudo dnf install sysstat```

```pacman: sudo pacman -S sysstat```

```apk: sudo apk add sysstat```

```zypper: sudo zypper install sysstat```

```brew: brew install sysstat```

```nix: nix profile install nixpkgs#sysstat```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sar](/man/sar)(1), [vmstat](/man/vmstat)(8), [mpstat](/man/mpstat)(1), [pidstat](/man/pidstat)(1)
