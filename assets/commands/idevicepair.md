# TAGLINE

管理与 iOS 设备的配对

# TLDR

**与设备配对**

```idevicepair pair```

**检查配对状态**

```idevicepair validate```

**取消设备配对**

```idevicepair unpair```

**列出已配对的设备**

```idevicepair list```

**指定目标设备**

```idevicepair -u [udid] pair```

# SYNOPSIS

**idevicepair** [_options_] _command_

# PARAMETERS

_COMMAND_
> 操作（pair、validate、unpair、list）。

**pair**
> 与设备配对。

**validate**
> 检查配对状态。

**unpair**
> 移除配对。

**list**
> 列出已配对的设备。

**-u** _UDID_
> 目标设备。

**--help**
> 显示帮助信息。

# DESCRIPTION

**idevicepair** 管理与 iOS 设备的配对。配对可在计算机与设备之间建立信任关系。

该工具处理信任对话框的流程。大多数设备操作都需要先完成配对。

# CAVEATS

需要在设备上确认信任。属于 libimobiledevice。需要 USB 连接。

# HISTORY

idevicepair 是 **libimobiledevice** 的组成部分，用于与 iOS 设备建立受信任连接。

# INSTALL

```apt: sudo apt install libimobiledevice-utils```

```dnf: sudo dnf install libimobiledevice-utils```

```apk: sudo apk add libimobiledevice-progs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[idevice_id](/man/idevice_id)(1), [ideviceinfo](/man/ideviceinfo)(1), [idevicename](/man/idevicename)(1)
