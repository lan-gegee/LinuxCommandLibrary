# TAGLINE

为运行 iOS 4 及更高版本的 iOS 设备创建和恢复备份

# TLDR

**创建完整备份**

```idevicebackup2 backup [backup-dir]```

**从备份恢复**

```idevicebackup2 restore [backup-dir]```

**列出备份中的文件**

```idevicebackup2 list [backup-dir]```

**备份指定设备**

```idevicebackup2 -u [device-udid] backup [backup-dir]```

**强制完整备份**

```idevicebackup2 backup --full [backup-dir]```

**启用备份加密**

```idevicebackup2 encryption on [password]```

# SYNOPSIS

**idevicebackup2** [_OPTIONS_] _CMD_ [_CMDOPTIONS_] _DIRECTORY_

# SUBCOMMANDS

**backup**
> 创建设备备份。使用 --full 强制进行完整备份。

**restore**
> 从备份恢复。支持 --system、--settings、--remove、--copy、--skip-apps、--no-reboot、--password。

**list**
> 以 CSV 格式列出最近一次已完成备份的文件。

**unback**
> 解包一个已完成的备份。

**encryption** on|off [_PWD_]
> 启用或禁用备份加密。

**changepw** [_OLD_] [_NEW_]
> 在目标设备上更改备份密码。

**cloud** on|off
> 启用或禁用云备份（需要 iCloud 账户）。

**info**
> 显示最近一次已完成备份的详细信息。

# PARAMETERS

**-u**, **--udid** _UDID_
> 按 UDID 指定目标设备。

**-s**, **--source** _UDID_
> 使用按 UDID 指定设备的备份数据。

**-i**, **--interactive**
> 在命令行上交互式请求密码。

**-n**, **--network**
> 连接到网络设备。

**-d**, **--debug**
> 启用通信调试。

# DESCRIPTION

**idevicebackup2** 为运行 iOS 4 及更高版本的 iOS 设备创建和恢复备份，属于 libimobiledevice 套件。支持加密备份、增量备份以及从其他设备恢复备份。

# INSTALL

```apt: sudo apt install libimobiledevice-utils```

```dnf: sudo dnf install libimobiledevice-utils```

```apk: sudo apk add libimobiledevice-progs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ideviceinfo](/man/ideviceinfo)(1), [idevicebackup](/man/idevicebackup)(1)

