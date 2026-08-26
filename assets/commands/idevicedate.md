# TAGLINE

显示或设置 iOS 设备上的日期和时间

# TLDR

**显示设备的日期和时间**

```idevicedate```

**设置日期和时间**

```idevicedate -s "[2024-01-15 10:30:00]"```

**以 UTC 显示**

```idevicedate -u```

**指定目标设备**

```idevicedate -u [device-udid]```

# SYNOPSIS

**idevicedate** [_options_]

# PARAMETERS

**-s** _datetime_
> 设置设备日期/时间。

**-u**
> 以 UTC 显示时间。

**-c**
> 使用当前主机时间。

**-n**
> 通过网络连接。

# DESCRIPTION

**idevicedate** 显示或设置 iOS 设备上的日期和时间，属于 libimobiledevice 套件。可将设备时间与主机系统同步。

# INSTALL

```apt: sudo apt install libimobiledevice-utils```

```dnf: sudo dnf install libimobiledevice-utils```

```apk: sudo apk add libimobiledevice-progs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ideviceinfo](/man/ideviceinfo)(1), [date](/man/date)(1)

