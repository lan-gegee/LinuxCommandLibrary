# TAGLINE

ModemManager 的命令行界面，ModemManager 是一个基于 DBus 的守护进程

# TLDR

**列出可用的调制解调器**

```mmcli --list-modems```

**打印**调制解调器的信息

```mmcli --modem=[modem_id]```

**启用**调制解调器

```mmcli --modem=[modem_id] --enable```

**禁用**调制解调器

```mmcli --modem=[modem_id] --disable```

**列出调制解调器上的短信**

```sudo mmcli --modem=[modem_id] --messaging-list-sms```

**删除短信**

```sudo mmcli --modem=[modem_id] --messaging-delete-sms=[sms_path]```

**监视调制解调器状态**变化

```mmcli --monitor-modems```

# SYNOPSIS

**mmcli** [**--list-modems**] [**--modem** _id_] [**--enable**|**--disable**] [**--messaging-list-sms**] [_options_]

# PARAMETERS

**-L, --list-modems**
> 列出所有可用的调制解调器

**-m, --modem _id_**
> 按索引或 DBus 路径指定调制解调器

**-M, --monitor-modems**
> 监视调制解调器状态变化

**-e, --enable**
> 启用指定的调制解调器

**-d, --disable**
> 禁用指定的调制解调器

**-r, --reset**
> 重置调制解调器

**--factory-reset _code_**
> 用解锁码将调制解调器恢复出厂状态

**--command _at_command_**
> 向调制解调器发送原始 AT 命令

**--messaging-list-sms**
> 列出调制解调器上的短信

**--messaging-create-sms _properties_**
> 创建新短信

**--messaging-delete-sms _sms_**
> 删除短信

**-S, --scan-modems**
> 扫描新的调制解调器

**--output-json**
> 以 JSON 格式输出

**--output-keyvalue**
> 以键值对形式输出

**-v, --verbose**
> 启用详细输出

# DESCRIPTION

**mmcli** 是 ModemManager 的命令行界面。ModemManager 是一个基于 DBus 的守护进程，在 Linux 上提供对移动宽带调制解调器的统一控制。它支持多种调制解调器类型，包括 USB 调制解调器、嵌入式蜂窝模块和手机网络共享。

该工具可以启用/禁用调制解调器、管理连接、收发短信、控制 GPS 功能、扫描网络以及执行 SIM 卡操作。它通过 DBus 与 ModemManager 通信。

# CAVEATS

某些操作需要 root 权限，尤其是短信和连接管理。调制解调器索引可能在重启或设备重新连接后发生变化；请使用 DBus 路径作为稳定标识。恢复出厂设置需要运营商特定的解锁码，并会清除所有调制解调器配置。

# HISTORY

**mmcli** 属于由 freedesktop.org 社区开发的 **ModemManager**。ModemManager 为移动宽带调制解调器提供统一的高级 API，屏蔽了不同厂商实现之间的差异。它通常与 NetworkManager 搭配使用以提供移动网络连接。

# INSTALL

```apt: sudo apt install modemmanager```

```pacman: sudo pacman -S modemmanager```

```apk: sudo apk add modemmanager```

```nix: nix profile install nixpkgs#modemmanager```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[NetworkManager](/man/NetworkManager)(8), [nmcli](/man/nmcli)(1)
