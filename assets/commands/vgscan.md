# TAGLINE

扫描 LVM 卷组

# TLDR

**扫描所有卷组**

```sudo vgscan```

**扫描并重建缺失的设备节点**

```sudo vgscan --mknodes```

**以详细输出进行扫描**

```sudo vgscan -v```

**以测试模式扫描，不更新元数据**

```sudo vgscan -t```

# SYNOPSIS

**vgscan** [_options_]

# DESCRIPTION

**vgscan** 扫描系统中所有受支持的 LVM 块设备以查找卷组。它会构建 LVM 缓存文件，其中保存系统上卷组的当前信息。

在现代 LVM2 系统中，发生变更时会自动执行卷组扫描。手动运行 vgscan 主要用于硬件变更之后或需要重建缓存时。

# PARAMETERS

**--mknodes**
> 检查并重建 /dev 中的 LVM 特殊设备文件。创建缺失的节点并移除未使用的节点。

**-v**, **--verbose**
> 详细模式。最多可重复 4 次以增加细节。

**--notifydbus**
> 扫描完成后向 D-Bus 发送通知。

**--reportformat** _basic|json_
> 覆盖报告的输出格式。

**--ignorelockingfailure**
> 锁定失败后仍继续执行只读元数据操作。

**-t**, **--test**
> 以测试模式运行，不更新元数据。

**-d**, **--debug**
> 设置调试级别。最多可重复 6 次以增加细节。

**-q**, **--quiet**
> 抑制输出和日志消息。

# CAVEATS

vgscan 通常在系统启动期间自动运行。现代系统上很少需要手动运行 vgscan，因为 LVM 会自动检测变更。扫描后使用 **vgchange -a y** 激活卷组。需要 root 权限。

# HISTORY

**vgscan** 是 **LVM2**（逻辑卷管理器）的一部分，LVM2 由最初的 LVM 实现演化而来。LVM2 由 **Red Hat** 开发，使用 device-mapper 内核框架在 Linux 上实现动态磁盘管理。

# INSTALL

```apt: sudo apt install lvm2```

```dnf: sudo dnf install lvm2```

```pacman: sudo pacman -S lvm2```

```apk: sudo apk add lvm2```

```zypper: sudo zypper install lvm2```

```nix: nix profile install nixpkgs#lvm2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vgdisplay](/man/vgdisplay)(8), [vgchange](/man/vgchange)(8), [vgcreate](/man/vgcreate)(8), [pvscan](/man/pvscan)(8), [lvscan](/man/lvscan)(8), [lvm](/man/lvm)(8)
