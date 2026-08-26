# TAGLINE

NetworkManager 的命令行客户端

# TLDR

列出所有 **NetworkManager 连接**

```nmcli connection```

显示**设备状态**

```nmcli device```

**连接**到 Wi-Fi 网络

```nmcli device wifi connect ssid --ask```

显示可用的 **Wi-Fi 网络**

```nmcli device wifi```

显示当前 Wi-Fi 的**密码**

```nmcli device wifi show-password```

**激活**一个连接

```nmcli connection up connection_name```

**停用**一个连接

```nmcli connection down connection_name```

# SYNOPSIS

**nmcli** [_OPTIONS_] {_general_|_networking_|_radio_|_connection_|_device_|_agent_|_monitor_} [_COMMAND_] [_ARGUMENTS_]

# DESCRIPTION

**nmcli** 是 NetworkManager 的命令行客户端。它可以控制 NetworkManager 并报告网络状态，创建、编辑、激活和停用网络连接，以及管理网络设备。

# OBJECTS

**general**
> 管理 NetworkManager 状态、主机名、权限和日志

**networking**
> 控制整体网络状态和连通性

**radio**
> 管理 Wi-Fi 和 WWAN 无线电开关

**connection**
> 管理网络连接配置文件

**device**
> 管理网络接口

**agent**
> 作为 NetworkManager 密钥代理或 polkit 代理运行

**monitor**
> 实时观察 NetworkManager 活动

# PARAMETERS

**-t, --terse**
> 生成适合脚本的简洁输出

**-p, --pretty**
> 生成人类可读的格式化输出

**-m, --mode tabular|multiline**
> 在输出模式之间切换

**-c, --colors auto|yes|no**
> 控制彩色输出

**-f, --fields**
> 指定要输出的字段/列

**-e, --escape yes|no**
> 转义值中的列分隔符

**-a, --ask**
> 对缺失的参数进行询问

**-s, --show-secrets**
> 显示密码和密钥

**-w, --wait seconds**
> 为操作设置超时时间

**--offline**
> 在不使用 NetworkManager 守护进程的情况下工作

# COMMON CONNECTION COMMANDS

**nmcli connection show**: 列出所有连接
**nmcli connection up**: 激活一个连接
**nmcli connection down**: 停用一个连接
**nmcli connection add**: 创建一个新连接
**nmcli connection modify**: 更改连接设置
**nmcli connection delete**: 移除一个连接
**nmcli connection import**: 导入 VPN 连接

# CAVEATS

**--ask** 标志会交互式地提示输入密码。**--show-secrets** 会显示敏感信息，请谨慎使用。**-t** 配合 **-f** 非常适合脚本编写。

# HISTORY

**nmcli** 是 **NetworkManager** 的命令行界面，大约于 2004 年首次发布。它为没有图形界面的系统提供网络连接管理方式，也可用于自动化。

# INSTALL

```apt: sudo apt install network-manager```

```apk: sudo apk add networkmanager-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nmtui](/man/nmtui)(1), [NetworkManager](/man/NetworkManager)(8), [nm-settings](/man/nm-settings)(5)
