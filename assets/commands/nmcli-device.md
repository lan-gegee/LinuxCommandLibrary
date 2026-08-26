# TAGLINE

使用 NetworkManager 管理网络接口

# TLDR

显示所有网络接口的**状态**

```nmcli device```

列出可用的 **Wi-Fi 网络**

```nmcli device wifi```

**连接**到 Wi-Fi 网络（会提示输入密码）

```nmcli device wifi connect [ssid] --ask```

连接到**隐藏**的 Wi-Fi 网络

```nmcli device wifi connect [ssid] password [password] hidden yes```

显示当前 Wi-Fi 的**密码**和二维码

```nmcli device wifi show-password```

显示某个设备的**详细信息**

```nmcli device show [wlan0]```

**断开**设备

```nmcli device disconnect [wlan0]```

**重新扫描**可用的 Wi-Fi 网络

```nmcli device wifi rescan```

# SYNOPSIS

**nmcli device** {_status_|_show_|_set_|_connect_|_reapply_|_modify_|_disconnect_|_delete_|_monitor_|_wifi_|_lldp_} [_ARGUMENTS_]

# DESCRIPTION

**nmcli device** 使用 NetworkManager 管理网络接口。它可以显示设备状态、连接到网络、管理 Wi-Fi 连接以及控制接口状态。

# COMMANDS

**status**
> 打印所有网络设备的状态

**show [ifname]**
> 显示某个设备的详细信息

**set ifname [property value]**
> 设置设备属性（autoconnect、managed）

**connect ifname**
> 连接一个设备

**reapply ifname**
> 将连接设置重新应用到设备

**disconnect ifname**
> 断开一个设备

**delete ifname**
> 删除一个软件设备

**monitor [ifname]**
> 监视设备活动

**wifi list**
> 列出可用的 Wi-Fi 接入点

**wifi connect ssid [password passwd] [hidden yes|no]**
> 连接到 Wi-Fi 网络，可选择指定密码和隐藏状态

**wifi rescan**
> 请求进行一次 Wi-Fi 扫描

**wifi hotspot [ifname wlan0] [ssid name] [password passwd]**
> 创建 Wi-Fi 热点

**wifi show-password**
> 显示当前 Wi-Fi 连接的密码

**lldp [list]**
> 显示 LLDP 邻居

# PARAMETERS

**-a, --ask**
> 连接时提示输入密码

**--rescan auto|no|yes**
> 控制在列出之前是否扫描 Wi-Fi

**-w, --wait seconds**
> 完成操作的超时时间

**ifname**
> 网络接口名称（eth0、wlan0 等）

# CAVEATS

Wi-Fi 操作要求 NetworkManager 守护进程正在运行且设备受其管理。在 wifi connect 时配合 **--ask** 可以交互式输入密码。

# HISTORY

是 **NetworkManager** 的 **nmcli** 命令行界面的一部分。提供设备级的网络管理。

# INSTALL

```apt: sudo apt install network-manager```

```apk: sudo apk add networkmanager-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nmcli](/man/nmcli)(1), [nmcli-connection](/man/nmcli-connection)(1), [nmcli-general](/man/nmcli-general)(1), [iw](/man/iw)(8), [iwctl](/man/iwctl)(1)
