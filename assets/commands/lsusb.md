# TAGLINE

显示 USB 总线和已连接设备的信息

# TLDR

列出所有 **USB 设备**

```lsusb```

以**树形**列出 USB 层次结构

```lsusb -t```

列出**详细**信息

```sudo lsusb -v```

显示**指定设备**的详情

```sudo lsusb -v -s 001:002```

按 **vendor:product** ID 过滤

```lsusb -d 1234:5678```

# SYNOPSIS

**lsusb** [_options_]

# DESCRIPTION

**lsusb** 显示系统中 USB 总线及连接设备的信息。它使用 udev 的硬件数据库提供人类可读的厂商名和产品名。

# PARAMETERS

**-v, --verbose**
> 显示详细的设备信息，包括配置和类描述符

**-s [[bus]:][devnum]**
> 只显示指定总线和/或设备号上的设备（十进制）

**-d [vendor]:[product]**
> 只显示具有指定 vendor/product ID 的设备（十六进制）

**-D** _device_
> 显示指定设备文件的信息（例如 /dev/bus/usb/001/002）

**-t, --tree**
> 以树形结构显示 USB 设备层次

**-V, --version**
> 显示版本信息

# CAVEATS

详细输出（**-v**）和部分设备细节需要 root 权限。设备号采用十进制格式，而 vendor/product ID 采用十六进制。

# HISTORY

**lsusb** 是 **usbutils** 软件包的一部分，自 Linux 早期支持 USB 以来就提供命令行的 USB 设备信息。

# INSTALL

```apt: sudo apt install usbutils```

```dnf: sudo dnf install usbutils```

```pacman: sudo pacman -S usbutils```

```apk: sudo apk add usbutils```

```zypper: sudo zypper install usbutils```

```brew: brew install usbutils```

```nix: nix profile install nixpkgs#usbutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lspci](/man/lspci)(8), [udevadm](/man/udevadm)(8)
