# TAGLINE

wpa_supplicant 的交互式前端

# TLDR

**扫描**可用网络

```sudo wpa_cli scan```

显示**扫描结果**

```sudo wpa_cli scan_results```

**添加**新网络

```sudo wpa_cli add_network```

设置网络 **SSID**

```sudo wpa_cli set_network 0 ssid '"[MyNetwork]"'```

设置网络**密码**

```sudo wpa_cli set_network 0 psk '"[password]"'```

**启用**一个网络

```sudo wpa_cli enable_network 0```

**保存**配置

```sudo wpa_cli save_config```

显示连接**状态**

```sudo wpa_cli status```

# SYNOPSIS

**wpa_cli** [**-p** _path_] [**-g** _socket_] [**-i** _ifname_] [**-hvB**] [**-a** _file_] [_command_]

# DESCRIPTION

**wpa_cli** 是与 wpa_supplicant 交互的文本前端。它可以查询网络状态、修改配置以及处理身份验证请求。它既可以带提示符以交互模式运行，也可以通过参数以命令行模式运行。

# PARAMETERS

**-p PATH**
> 指定控制套接字的路径

**-g PATH**
> 连接到指定路径的全局控制套接字

**-i IFNAME**
> 选择网络接口

**-a FILE**
> 以守护进程模式运行，并通过动作文件处理事件

**-B**
> 作为后台守护进程运行

**-P FILE**
> 设置 PID 文件的位置

**-G INTERVAL**
> 设置 ping 间隔（秒）

**status**
> 显示当前连接状态

**scan**
> 发起网络扫描

**scan_results**
> 显示扫描结果

**list_networks**
> 列出已配置的网络

**add_network**
> 添加新网络（返回网络 ID）

**set_network ID PARAM VALUE**
> 设置网络参数

**enable_network ID**
> 启用一个网络

**disable_network ID**
> 禁用一个网络

**select_network ID**
> 选择并启用某个网络，同时禁用其他网络

**save_config**
> 将当前配置保存到文件

**reconfigure**
> 重新加载配置文件

**disconnect**
> 断开当前网络连接

**reassociate**
> 强制重新关联

**terminate**
> 停止 wpa_supplicant

# CAVEATS

需要 root 权限，或者控制接口所属的正确用户组。可以通过 wpa_supplicant.conf 中的 ctrl_interface GROUP 参数将控制接口配置为允许非 root 用户访问。

# HISTORY

**wpa_cli** 是 **wpa_supplicant** 的一部分。wpa_supplicant 是面向 Linux、BSD 和 Windows 的 WPA 与 WPA2 认证客户端，常用于无线网络身份验证。

# INSTALL

```apt: sudo apt install wpasupplicant```

```dnf: sudo dnf install wpa_supplicant```

```pacman: sudo pacman -S wpa_supplicant```

```apk: sudo apk add wpa_supplicant```

```zypper: sudo zypper install wpa_supplicant```

```nix: nix profile install nixpkgs#wpa_supplicant```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wpa_supplicant](/man/wpa_supplicant)(8), [iwconfig](/man/iwconfig)(8), [nmcli](/man/nmcli)(1), [iw](/man/iw)(8)
