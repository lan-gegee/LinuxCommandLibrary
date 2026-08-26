# TAGLINE

扫描并列出所有卷组中的全部逻辑卷

# TLDR

**列出所有逻辑卷**

```sudo lvscan```

**包含内部 LV 组件**（镜像等）

```sudo lvscan --all```

**以 JSON 格式输出**

```sudo lvscan --reportformat json```

**以只读模式运行**，不获取锁

```sudo lvscan --readonly```

**输出更多细节的详细日志**

```sudo lvscan -v```

# SYNOPSIS

**lvscan** [_options_]

# DESCRIPTION

**lvscan** 扫描并列出所有卷组中的全部逻辑卷。输出为每个逻辑卷显示一行，指明其处于活动还是非活动状态、LV 路径及其大小。

# PARAMETERS

**-a**, **--all**
> 显示作为普通 LV 组成部分的内部 LV（例如镜像和日志）的信息。

**-b**, **--blockdevice**
> 已不再使用。请改用 lvs(8) 或 lvdisplay(8)。

**--readonly**
> 不获取锁直接读取磁盘上的元数据。可用于检查虚拟机或集群 VG 中的元数据。

**--reportformat** _FORMAT_
> 输出格式：basic 或 json。

**--ignorelockingfailure**
> 允许在锁定失败后以只读元数据方式继续执行命令。

**-d**, **--debug**
> 增加调试详细程度（可重复 1-6 次）。

**-q**, **--quiet**
> 抑制输出和日志消息。

**-t**, **--test**
> 以测试模式运行，不更新元数据。

**-v**, **--verbose**
> 增加详细程度（可重复 1-4 次）。

# INSTALL

```apt: sudo apt install lvm2```

```dnf: sudo dnf install lvm2```

```pacman: sudo pacman -S lvm2```

```apk: sudo apk add lvm2```

```zypper: sudo zypper install lvm2```

```nix: nix profile install nixpkgs#lvm2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lvs](/man/lvs)(8), [lvdisplay](/man/lvdisplay)(8), [vgscan](/man/vgscan)(8), [pvscan](/man/pvscan)(8), [lvm](/man/lvm)(8)
