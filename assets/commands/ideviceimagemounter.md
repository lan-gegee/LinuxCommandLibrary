# TAGLINE

在 iOS 设备上挂载磁盘镜像

# TLDR

**挂载开发者磁盘镜像**

```ideviceimagemounter [DeveloperDiskImage.dmg]```

**带签名文件挂载**

```ideviceimagemounter [DeveloperDiskImage.dmg] [DeveloperDiskImage.dmg.signature]```

**列出已挂载的镜像**

```ideviceimagemounter -l```

**指定目标设备**

```ideviceimagemounter -u [device-udid] [image.dmg]```

# SYNOPSIS

**ideviceimagemounter** [_options_] _image_ [_signature_]

# PARAMETERS

**-u** _udid_
> 指定目标设备。

**-l**
> 列出已挂载的镜像。

**-n**
> 通过网络连接。

**-t** _type_
> 镜像类型（默认：Developer）。

# DESCRIPTION

**ideviceimagemounter** 在 iOS 设备上挂载磁盘镜像，属于 libimobiledevice 套件。主要用于挂载开发者磁盘镜像，以便使用调试和开发工具（如 Xcode instruments）。需要提供对应的签名文件。

# INSTALL

```apt: sudo apt install libimobiledevice-utils```

```dnf: sudo dnf install libimobiledevice-utils```

```apk: sudo apk add libimobiledevice-progs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ideviceinfo](/man/ideviceinfo)(1)

