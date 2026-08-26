# TAGLINE

基于快照的系统备份与恢复工具

# TLDR

**列出**所有快照

```sudo timeshift --list```

带说明文字**创建**快照

```sudo timeshift --create --comments "[description]"```

以特定**标签****创建**快照

```sudo timeshift --create --tags D```

**检查**计划任务，到点则创建快照

```sudo timeshift --check```

**恢复**指定快照

```sudo timeshift --restore --snapshot '[snapshot_name]'```

将快照**恢复**到指定的**目标设备**

```sudo timeshift --restore --snapshot '[snapshot_name]' --target-device [/dev/sda1]```

**删除**指定快照

```sudo timeshift --delete --snapshot '[snapshot_name]'```

**删除全部**快照

```sudo timeshift --delete-all```

# SYNOPSIS

**timeshift** [_OPTIONS_]

# PARAMETERS

**--list**
> 列出所有快照。

**--list-devices**
> 列出可用设备。

**--check**
> 如果到达计划的快照时间则创建快照。

**--create**
> 创建新快照（即使未到计划时间）。

**--restore**
> 恢复快照。

**--delete**
> 删除快照。

**--delete-all**
> 删除所有快照。

**--snapshot** _NAME_
> 指定要恢复或删除的快照。

**--comments** _TEXT_
> 设置快照描述。

**--tags** _{O,B,H,D,W,M}_
> 为快照添加标签：Ondemand、Boot、Hourly、Daily、Weekly、Monthly（默认：O）。

**--target-device** _DEVICE_
> 指定恢复的目标设备。

**--grub-device** _DEVICE_
> 指定安装 GRUB2 引导加载程序的设备。

**--skip-grub**
> 恢复时跳过重新安装 GRUB2。

**--snapshot-device** _DEVICE_
> 指定备份设备（默认：取自配置）。

**--btrfs**
> 切换到 BTRFS 模式。

**--rsync**
> 切换到 RSYNC 模式。

**--yes**
> 对所有确认提示回答 YES。

**--scripted**
> 以非交互模式运行。

# DESCRIPTION

**timeshift** 是一款 Linux 系统恢复工具，使用 rsync 或 btrfs 快照创建文件系统的增量快照。它可以在保留用户数据的同时回滚系统变更。

类似于 Windows 的系统还原或 macOS 面向系统文件的 Time Machine。

# CAVEATS

需要足够的存储空间。BTRFS 快照比 rsync 更节省空间。为安全起见，默认排除 /home 中的用户数据。恢复通常需要重启。所有操作均需 root 权限。

# HISTORY

**Timeshift** 由 **Tony George** 创建，是一款 Linux 系统备份的 GUI 和 CLI 工具，最初发布于 **2014 年**。

# INSTALL

```apt: sudo apt install timeshift```

```dnf: sudo dnf install timeshift```

```pacman: sudo pacman -S timeshift```

```zypper: sudo zypper install timeshift```

```nix: nix profile install nixpkgs#timeshift```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rsync](/man/rsync)(1), [btrfs](/man/btrfs)(8), [snapper](/man/snapper)(1), [btrbk](/man/btrbk)(1), [restic](/man/restic)(1)
