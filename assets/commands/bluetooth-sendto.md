# TAGLINE

通过图形对话框经蓝牙发送文件

# TLDR

**打开文件传输对话框以选择设备和文件**

```bluetooth-sendto```

**向特定蓝牙设备发送文件**

```bluetooth-sendto --device=[XX:XX:XX:XX:XX:XX] [path/to/file]```

**向具有指定名称的设备发送文件**

```bluetooth-sendto --device=[XX:XX:XX:XX:XX:XX] --name="[Device Name]" [path/to/file]```

**向一个设备发送多个文件**

```bluetooth-sendto --device=[XX:XX:XX:XX:XX:XX] [file1] [file2] [file3]```

# SYNOPSIS

**bluetooth-sendto** [**--device=**_XX:XX:XX:XX:XX:XX_] [**--name=**_NAME_] [_file..._]

# DESCRIPTION

**bluetooth-sendto** 是一款通过蓝牙传输文件的 GTK 应用程序。它是 **gnome-bluetooth** 软件包的一部分，提供用于选择设备和待传文件的图形对话框。

不带参数运行时会显示文件选择器和设备选择对话框。指定设备地址时则直接连接该设备。单次操作可发送多个文件。

# PARAMETERS

**--device=**_XX:XX:XX:XX:XX:XX_
> 指定目标设备的蓝牙 MAC 地址。省略时将显示设备选择对话框

**--name=**_NAME_
> 指定设备名称。省略时名称会根据设备地址自动检测

**file...**
> 要发送的一个或多个文件。省略时将显示文件选择对话框

# CAVEATS

需要启用蓝牙，且目标设备已配对并在通信范围内。接收设备必须接受传入的文件传输请求。属于 GNOME Bluetooth 栈的一部分，因此需要 GTK 环境。

# INSTALL

```apt: sudo apt install gnome-bluetooth-sendto```

```dnf: sudo dnf install gnome-bluetooth```

```apk: sudo apk add gnome-bluetooth```

```zypper: sudo zypper install gnome-bluetooth```

```nix: nix profile install nixpkgs#gnome-bluetooth```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bluetoothctl](/man/bluetoothctl)(1)

# RESOURCES

```[Source code](https://gitlab.gnome.org/GNOME/gnome-bluetooth)```

```[Documentation](https://manpages.debian.org/testing/gnome-bluetooth/bluetooth-sendto.1.en.html)```

<!-- verified: 2026-06-19 -->
