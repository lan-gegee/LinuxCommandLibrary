# TAGLINE

从设备上擦除文件系统、RAID 或分区表签名

# TLDR

**显示**签名

```sudo wipefs /dev/sda```

**擦除**所有签名

```sudo wipefs -a /dev/sda```

擦除设备及**分区**

```sudo wipefs -a /dev/sda*```

**试运行**，只显示将要执行的操作

```sudo wipefs -a -n /dev/sda```

**擦除**签名并创建备份

```sudo wipefs -a -b /dev/sda```

**强制**擦除已挂载的设备

```sudo wipefs -a -f /dev/sda```

以 JSON 格式**输出**签名

```sudo wipefs -J /dev/sda```

# SYNOPSIS

**wipefs** [_OPTIONS_] _device_...

# DESCRIPTION

**wipefs** 从设备上擦除文件系统、RAID 或分区表签名。它移除标识设备类型的魔数字符串而不破坏实际数据，使设备可以被重新利用。

# PARAMETERS

**-a, --all**
> 擦除所有可用签名

**-n, --no-act**
> 试运行——只显示将要执行的操作

**-f, --force**
> 即使设备正在使用也强制擦除

**-o, --offset** _offset_
> 在特定偏移处擦除签名

**-b, --backup**
> 为被擦除的签名创建备份文件

**-t, --types** _list_
> 只擦除指定类型的签名

**-q, --quiet**
> 成功擦除签名后抑制输出消息

**-p, --parsable**
> 以可解析格式而非可读格式打印

**-J, --json**
> 使用 JSON 输出格式

**-O, --output** _list_
> 指定要打印哪些输出列

# CAVEATS

该命令移除的是文件系统识别签名，并不会擦除设备上的文件系统本身或其他任何数据。要彻底销毁数据，请使用 **blkdiscard** 或用 **dd** 覆写。擦除已挂载的文件系统可能导致数据丢失。要在非整盘设备上擦除嵌套的分区表，必须使用 **--force** 标志。

# HISTORY

**wipefs** 是 **util-linux** 软件包的一部分，为块设备提供签名管理功能。

# INSTALL

```apt: sudo apt install util-linux```

```dnf: sudo dnf install util-linux```

```pacman: sudo pacman -S util-linux```

```apk: sudo apk add wipefs```

```zypper: sudo zypper install util-linux```

```brew: brew install util-linux```

```nix: nix profile install nixpkgs#util-linux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[blkid](/man/blkid)(8), [lsblk](/man/lsblk)(8), [blkdiscard](/man/blkdiscard)(8), [dd](/man/dd)(1), [fdisk](/man/fdisk)(8)
