# TAGLINE

启用和禁用无线设备

# TLDR

**列出**设备

```rfkill```

筛选**列**

```rfkill -o ID,TYPE,DEVICE```

**封锁**设备类型

```rfkill block wifi```

**解除封锁**设备类型

```rfkill unblock bluetooth```

输出 **JSON**

```rfkill -J```

# SYNOPSIS

**rfkill** [_OPTIONS_] [_command_] [_identifier_]

# DESCRIPTION

**rfkill** 通过内核的 rfkill 子系统启用和禁用无线通信设备（WiFi、蓝牙、GPS、NFC 等）。它可以在软件层面软封锁设备，同时遵循硬件无线开关的状态。

# PARAMETERS

**list**
> 列出所有设备（默认操作）

**block** _type|id_
> 禁用指定的设备类型或 ID

**unblock** _type|id_
> 启用指定的设备类型或 ID

**toggle** _type|id_
> 切换设备状态

**-o, --output** _columns_
> 指定输出列

**-J, --json**
> 以 JSON 格式输出

**-n, --noheadings**
> 不打印列标题

# CAVEATS

软件无法覆盖硬件无线开关。如果多个设备共享同一个 rfkill 开关，封锁可能影响多个设备。某些设备可能需要重启才能完全重置。

# HISTORY

**rfkill** 是 **util-linux** 的一部分，提供对内核 rfkill 子系统中无线设备的控制。

# INSTALL

```apt: sudo apt install rfkill```

```apk: sudo apk add util-linux-misc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[iw](/man/iw)(8), [bluetoothctl](/man/bluetoothctl)(1)
