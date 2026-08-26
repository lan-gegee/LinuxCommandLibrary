# TAGLINE

底层蓝牙适配器管理工具

# TLDR

**启动交互模式**

```btmgmt```

**列出蓝牙适配器**

```btmgmt info```

**使用指定适配器**

```btmgmt -i [hci0] info```

**开启适配器电源**

```btmgmt power on```

**关闭适配器电源**

```btmgmt power off```

**开始发现设备**

```btmgmt find```

**启用监听输出模式**

```btmgmt -m```

**以超时方式运行命令**

```btmgmt -t [10] find```

# SYNOPSIS

**btmgmt** [_options_] [_command_]

# DESCRIPTION

**btmgmt** 是一个交互式蓝牙管理工具，通过蓝牙管理（Management）套接字向内核发送命令。它提供对蓝牙适配器设置、设备发现和配对功能的底层控制。

该工具是 BlueZ 蓝牙协议栈的一部分，使用 Linux 内核 3.4 起提供的管理接口。

# PARAMETERS

**-i, --index** _adapter_
> 指定适配器索引（例如 hci0）

**-m, --monitor**
> 启用监听输出

**-t, --timeout** _seconds_
> 非交互模式的超时时间

**-v, --version**
> 显示版本

**--init-script** _file_
> 从初始化脚本运行命令

**-h, --help**
> 显示帮助

# COMMANDS

**info**
> 显示适配器信息

**power** _on|off_
> 控制适配器电源状态

**find**
> 开始设备发现

**pair** _address_
> 与设备配对

**unpair** _address_
> 移除配对

**disconnect** _address_
> 断开设备连接

**con**
> 列出连接

# CAVEATS

某些命令需要 net-admin 能力或 root 权限。这是一个为 bluetoothd 设计的底层接口；应用程序应改用 D-Bus API。直接使用可能导致与蓝牙守护进程交互时出现意外行为。

# INSTALL

```apt: sudo apt install bluez```

```dnf: sudo dnf install bluez```

```pacman: sudo pacman -S bluez```

```apk: sudo apk add bluez-btmgmt```

```zypper: sudo zypper install bluez```

```brew: brew install bluez```

```nix: nix profile install nixpkgs#bluez```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bluetoothctl](/man/bluetoothctl)(1), [hciconfig](/man/hciconfig)(1), [hcitool](/man/hcitool)(1), [bluetoothd](/man/bluetoothd)(8)

# RESOURCES

```[Source code](https://github.com/bluez/bluez)```

<!-- verified: 2026-06-22 -->
