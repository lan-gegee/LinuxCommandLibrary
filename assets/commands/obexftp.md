# TAGLINE

通过 OBEX 协议传输文件

# TLDR

**列出设备上的文件**

```obexftp -b [device_address] -l [/]```

**下载文件**

```obexftp -b [device_address] -g [remote_file]```

**上传文件**

```obexftp -b [device_address] -p [local_file]```

**列出已配对的设备**

```obexftp -s```

**使用 USB 连接**

```obexftp -u [device] -l [/]```

# SYNOPSIS

**obexftp** [_options_] [_command_]

# PARAMETERS

**-b** _ADDRESS_
> 蓝牙设备地址。

**-u** _DEVICE_
> USB 设备。

**-l** _PATH_
> 列出目录。

**-g** _FILE_
> 获取/下载文件。

**-p** _FILE_
> 放置/上传文件。

**-s**
> 搜索设备。

**--help**
> 显示帮助信息。

# DESCRIPTION

**obexftp** 通过 OBEX 协议传输文件，支持蓝牙和 USB。

该工具可与移动设备交换文件，是 OpenOBEX 的一部分。

# CAVEATS

需要蓝牙或 USB OBEX 支持。设备必须已配对。

# HISTORY

obexftp 为通过蓝牙使用 OBEX 协议进行**文件传输**而创建。

# INSTALL

```apt: sudo apt install obexftp```

```zypper: sudo zypper install obexftp```

```nix: nix profile install nixpkgs#obexftp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bluetooth](/man/bluetooth)(1), [hcitool](/man/hcitool)(1)
