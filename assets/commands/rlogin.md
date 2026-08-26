# TAGLINE

远程登录到另一台主机

# TLDR

**登录**到远程主机

```rlogin [remote_host]```

**以指定用户名登录**

```rlogin -l [username] [remote_host]```

**使用自定义转义字符**代替默认的波浪号

```rlogin -e [^] [remote_host]```

**强制 IPv4 连接**

```rlogin -4 [remote_host]```

**允许 8 位数据**（用于非 ASCII 区域设置）

```rlogin -8 [remote_host]```

# SYNOPSIS

**rlogin** [**-468DEd**] [**-e** _char_] [**-i** _localname_] [**-l** _username_] _host_

# PARAMETERS

**-4**
> 只使用 IPv4 地址。

**-6**
> 只使用 IPv6 地址。

**-8**
> 始终允许 8 位输入数据通路；否则奇偶校验位会被剥离。

**-D**
> 设置 TCP_NODELAY 套接字选项以改善交互响应。

**-d**
> 在通信使用的 TCP 套接字上开启套接字调试（SO_DEBUG）。

**-E**
> 禁止任何字符被识别为转义字符。

**-e** _char_
> 设置转义字符（默认：**~**）。可以是字面字符，或用 \\nnn 表示八进制。

**-i** _localname_
> 指定另一个用于认证的本地名称。

**-l** _username_
> 指定用于远程登录的其他用户名（默认：当前用户）。

# DESCRIPTION

**rlogin** 使用 Berkeley 的 rhosts 授权机制在远程主机上启动终端会话。它会读取 **~/.rhosts** 和 **/etc/hosts.equiv**，以决定是否允许来自受信任账户的无密码登录。

转义字符（默认 **~**）作为一行的第一个字符输入时可触发特殊操作：**~.** 断开连接，**~^Z** 挂起会话，**~~** 发送字面波浪号。远程终端类型和窗口大小会从本地环境传递过去。

# CAVEATS

**已弃用且不安全**：rlogin 以明文形式在网络上传输凭据、命令和会话数据，使得嗅探密码和劫持会话变得轻而易举。rhosts 信任机制也容易受到欺骗攻击。大多数现代发行版默认禁用它或完全不再提供。任何远程登录用途都**请改用 [ssh](/man/ssh)(1)**。

# HISTORY

起源于 **4.2BSD**（1983 年），是 Berkeley "r-commands" 套件（**rlogin**、**rsh**、**rcp**）的一部分。20 世纪 80 至 90 年代在 Unix 网络上广泛部署，后因缺乏加密而在 90 年代末被 **ssh** 取代。在 Linux 上它通常由 **GNU inetutils** 提供。

# SEE ALSO

[ssh](/man/ssh)(1), [rsh](/man/rsh)(1), [rcp](/man/rcp)(1), [rexec](/man/rexec)(1), [telnet](/man/telnet)(1)
