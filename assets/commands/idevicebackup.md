# TAGLINE

创建和恢复 iOS 设备的备份

# TLDR

**创建备份**

```idevicebackup backup [backup-dir]```

**从备份恢复**

```idevicebackup restore [backup-dir]```

**备份指定设备**

```idevicebackup -u [device-udid] backup [backup-dir]```

# SYNOPSIS

**idevicebackup** [_options_] _command_ _directory_

# SUBCOMMANDS

**backup**
> 创建设备备份。

**restore**
> 从备份恢复。

# PARAMETERS

**-u** _udid_
> 指定目标设备。

**-n**
> 通过网络连接。

**-d**
> 启用调试输出。

# DESCRIPTION

**idevicebackup** 创建并恢复 iOS 设备的备份，属于 libimobiledevice 套件。适用于较旧的 iOS 版本。对于 iOS 4 及更高版本，请改用 **idevicebackup2**。

# CAVEATS

在较新的 iOS 版本上已弃用。iOS 4+ 请使用 idevicebackup2。

# INSTALL

```apt: sudo apt install libimobiledevice-utils```

```dnf: sudo dnf install libimobiledevice-utils```

```apk: sudo apk add libimobiledevice-progs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[idevicebackup2](/man/idevicebackup2)(1), [ideviceinfo](/man/ideviceinfo)(1)

