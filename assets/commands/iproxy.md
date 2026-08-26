# TAGLINE

创建 TCP 代理，把本地端口的连接转发到 iOS 设备上的端口

# TLDR

**将本地端口 2222 转发到 USB 连接的 iOS 设备的端口 22**

```iproxy 2222 22```

按 UDID **将端口转发到特定设备**

```iproxy 2222 22 -u [device_udid]```

**转发到通过网络连接的设备**

```iproxy 2222 22 -n```

**创建 SSH 隧道**以访问 iOS 设备

```iproxy 2222 22 & ssh -p 2222 root@localhost```

**转发端口用于调试**（如 lldb debugserver）

```iproxy 1234 1234```

# SYNOPSIS

**iproxy** [_-u UDID_] [_-n_] [_-d_] [_-h_] _LOCAL_PORT_ _DEVICE_PORT_

# PARAMETERS

**-u** _UDID_
> 按设备的唯一标识符指定目标设备

**-n**
> 连接网络设备而非 USB 设备

**-d**
> 启用调试日志

**-h**
> 显示帮助信息

**-s** _SOURCE_
> 要绑定的源地址

# DESCRIPTION

**iproxy** 创建一个 TCP 代理，把来自本地端口的连接转发到通过 USB 或网络连接的 iOS 设备上的端口。它使用 usbmuxd 协议与 iOS 设备通信，无需进行网络配置。

对于越狱 iOS 设备的 SSH 访问、远程调试以及任何需要 TCP 连接到 iOS 的开发工作流，该工具都不可或缺。最常见的用法是转发端口 22 以进行 SSH 访问。

# CAVEATS

USB 连接要求 **usbmuxd** 正在运行。SSH 访问要求设备已越狱并安装 OpenSSH。设备必须与电脑完成配对/信任。网络模式要求设备处于同一网络中。

# HISTORY

**iproxy** 是 **libusbmuxd** 项目的一部分，后者又属于 **libimobiledevice** 套件。libimobiledevice 创建于约 **2009 年**，是一个与 iOS 设备通信的跨平台库，为 Apple 的专有协议提供了开源替代方案。

# INSTALL

```apt: sudo apt install libusbmuxd-tools```

```apk: sudo apk add libusbmuxd-progs```

```zypper: sudo zypper install libusbmuxd-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[idevice_id](/man/idevice_id)(1), [ideviceinfo](/man/ideviceinfo)(1), [ssh](/man/ssh)(1)
