# TAGLINE

Android 设备端口转发器

# TLDR

将本地端口**转发**到设备端口

```adb forward tcp:[8080] tcp:[8080]```

转发到 **Unix 抽象域套接字**

```adb forward tcp:[8080] localabstract:[socket_name]```

**列出**所有转发的端口

```adb forward --list```

**移除**特定的转发规则

```adb forward --remove tcp:[8080]```

移除**所有**转发规则

```adb forward --remove-all```

按序列号对**特定设备**进行转发

```adb -s [serial] forward tcp:[8080] tcp:[8080]```

# SYNOPSIS

**adb forward** [_--no-rebind_] _local_ _remote_

**adb forward** --list | --remove _local_ | --remove-all

# DESCRIPTION

**adb forward** 建立从电脑本地端口到所连 Android 设备端口的端口转发。这使得你可以像访问本地服务一样访问设备上运行的服务。

常见用途包括：配合远程调试器调试应用、访问设备上运行的开发服务器，或连接应用专用的套接字。

# PARAMETERS

**tcp:**_port_
> TCP 端口号。远程端口可为 "tcp:0"，表示自动选择任一空闲端口。

**localabstract:**_name_
> 抽象命名空间中的 Unix 域套接字。

**localreserved:**_name_
> 保留命名空间中的 Unix 域套接字。

**localfilesystem:**_name_
> 文件系统命名空间中的 Unix 域套接字。

**jdwp:**_pid_
> 进程 ID 对应的 JDWP（Java Debug Wire Protocol）。

**vsock:**_CID:port_
> vsock 地址（CID 和端口）。

**--no-rebind**
> 若本地端口已被转发则失败

**--list**
> 列出所有活动的端口转发

**--remove** _local_
> 移除指定的转发规则

**--remove-all**
> 移除所有转发规则

# CAVEATS

端口转发会一直保留，直到被移除、设备断开或 adb 服务器重启。本地和远程端口都必须可用。防火墙可能阻止被转发的连接。

# HISTORY

自 **2008** 年 Android 首次发布以来，端口转发一直是 adb 的核心功能，是通过 JDWP 等协议远程调试 Android 应用不可或缺的手段。

# INSTALL

```apt: sudo apt install adb```

```dnf: sudo dnf install android-tools```

```pacman: sudo pacman -S android-tools```

```apk: sudo apk add android-tools-adb```

```zypper: sudo zypper install android-tools```

```nix: nix profile install nixpkgs#android-tools```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[adb](/man/adb)(1), [adb-reverse](/man/adb-reverse)(1)
