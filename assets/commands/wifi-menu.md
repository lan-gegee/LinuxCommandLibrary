# TAGLINE

交互式无线网络连接对话框

# TLDR

以**交互方式**连接

```wifi-menu```

连接时**遮蔽**密码

```wifi-menu -o```

显示**帮助**

```wifi-menu -h```

# SYNOPSIS

**wifi-menu** [_OPTIONS_] [_INTERFACE_]

# PARAMETERS

**-o, --obscure**
> 遮蔽无线密码短语

**-h, --help**
> 显示帮助信息

# DESCRIPTION

**wifi-menu** 提供交互式的文本界面用于连接无线网络。它会扫描可用网络，并允许通过对话框菜单进行选择和配置。

它是 Arch Linux netctl 软件包的一部分，为无线连接创建和管理 netctl 配置文件。

# CAVEATS

Arch Linux 专用（netctl）。需要 root 权限。会在 /etc/netctl/ 中创建配置文件。可能与 NetworkManager 冲突。

# SEE ALSO

[netctl](/man/netctl)(1), [nmcli](/man/nmcli)(1), [iwctl](/man/iwctl)(1)
