# TAGLINE

从 iOS 设备截取屏幕截图

# TLDR

**截取屏幕截图并保存到文件**

```idevicescreenshot [screenshot.tiff]```

**截取屏幕截图，自动生成文件名**

```idevicescreenshot```

**按 UDID 从指定设备截取屏幕截图**

```idevicescreenshot -u [udid] [output.tiff]```

**通过网络连接截取屏幕截图**

```idevicescreenshot -n [output.tiff]```

**启用调试输出**

```idevicescreenshot -d [output.tiff]```

# SYNOPSIS

**idevicescreenshot** [_options_] [_output_]

# PARAMETERS

_OUTPUT_
> 输出文件名。若省略，则生成带时间戳的文件名（如 screenshot-2024-01-15-12-30-00.tiff）。

**-u**, **--udid** _UDID_
> 按设备唯一标识符（UDID）指定目标设备。

**-n**, **--network**
> 连接网络设备而非 USB 设备。

**-d**, **--debug**
> 启用通信调试。

**-v**, **--version**
> 显示版本信息。

**-h**, **--help**
> 显示用法信息。

# DESCRIPTION

**idevicescreenshot** 从已连接的 iOS 设备截取屏幕截图。它将当前屏幕保存为 TIFF 图片。该工具通过 usbmuxd 协议与设备的 screenshotr 服务通信。

设备上必须已挂载开发者磁盘镜像，否则 screenshotr 服务不可用。截屏之前设备必须已完成配对并被信任。使用 **idevicepair** 管理设备配对。

# CAVEATS

属于 **libimobiledevice** 套件。设备必须已完成配对并被信任。需要挂载开发者磁盘镜像。受 DRM 保护的内容在截图中可能显示为黑屏。

# INSTALL

```apt: sudo apt install libimobiledevice-utils```

```dnf: sudo dnf install libimobiledevice-utils```

```apk: sudo apk add libimobiledevice-progs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[idevice_id](/man/idevice_id)(1), [idevicepair](/man/idevicepair)(1), [ideviceinfo](/man/ideviceinfo)(1), [scrcpy](/man/scrcpy)(1)
