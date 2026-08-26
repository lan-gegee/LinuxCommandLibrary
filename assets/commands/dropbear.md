# TAGLINE

轻量级 SSH 服务器

# TLDR

**启动 SSH 服务器**

```dropbear```

**在指定端口启动**

```dropbear -p [2222]```

**在前台启动**

```dropbear -F```

**使用指定的主机密钥启动**

```dropbear -r [/etc/dropbear/dropbear_ed25519_host_key]```

完全**禁用密码登录**（仅限密钥）

```dropbear -s```

彻底**禁止 root 登录**

```dropbear -w```

如缺失则自动**生成主机密钥**

```dropbear -R```

**在前台运行并将日志输出到 stderr**（用于调试）

```dropbear -F -E```

# SYNOPSIS

**dropbear** [_options_]

# DESCRIPTION

**dropbear** 是一款小型 SSH 服务器，面向那些装不下 OpenSSH 的系统：路由器、嵌入式 Linux、initramfs 镜像和救援环境。它支持 SSH 2 协议，提供公钥和密码认证、TCP 端口转发，并可通过配套的 `scp` 二进制进行文件传输。

它的核心卖点就是体积。裁剪后的 Dropbear 二进制大约只有几百 KB，比 OpenSSH 的 sshd 小一个数量级——这正是它成为 OpenWrt 以及大多数提供 SSH 的消费级路由器之选的原因。

它通常在启动时作为守护进程运行，但也可以用 **-i** 从 **inetd** 运行，这适合只期待偶发连接、不想常驻进程的系统。

# PARAMETERS

**-p** [_address_:]_port_
> 在此地址和端口上监听。可多次给出。默认端口为 22。

**-F**
> 前台运行而不是守护进程化。

**-E**
> 日志输出到标准错误而非 syslog。

**-r** _keyfile_
> 使用此主机密钥文件。可为多种密钥类型重复使用。

**-R**
> 按需自动生成主机密钥。

**-s**
> 禁用密码登录，只保留公钥认证。

**-g**
> **仅对 root**禁用密码登录。其他用户仍可使用密码。

**-w**
> 完全禁止 root 登录。

**-B**
> 允许空密码。

**-T** _attempts_
> 每个连接的最大认证尝试次数。默认 10 次。

**-a**
> 允许远程主机连接到转发的端口。

**-j** / **-k**
> 分别禁用本地端口转发（包括 unix 流转发）或远程端口转发。

**-b** _banner_
> 在用户登录前显示此文件的内容。

**-m**
> 不显示当日消息（message of the day）。

**-c** _command_
> 运行此命令，忽略用户请求的命令。

**-I** _seconds_
> 会话空闲这么多秒后断开连接。

**-K** _seconds_
> 按此间隔发送 keepalive 流量。

**-P** _pidfile_
> 以守护进程运行时写入 PID 的位置。

**-i**
> 从 inetd 运行，而不是作为独立守护进程。

# CAVEATS

**-g** 和 **-w** 容易混淆：**-g** 只是阻止 root 使用*密码*（root 仍可用密钥登录），而 **-w** 则彻底封锁 root。如果目的是把 root 挡在门外，应使用 **-w**。

Dropbear 以**自己的格式**存储主机密钥和用户密钥，而非 OpenSSH 格式。两者之间的迁移必须用 `dropbearconvert` 转换；`~/.ssh/authorized_keys` 是唯一原样使用 OpenSSH 公钥格式的地方。

它**没有内置 SFTP 服务器**。如果系统中存在并配置了外部的 `sftp-server` 二进制文件，Dropbear 会调用它；但精简系统上通常没有，于是 `sftp` 失败而 `scp` 可用。一些构建版本为了节省空间还会省略 `scp`。

体积小意味着取舍：密码套件和密钥交换列表比 OpenSSH 短，老旧的厂商固件往往还带着一个古董版 Dropbear，其算法已被现代客户端弃用——这就是为什么连接路由器时可能需要在客户端显式重新启用旧式密钥交换。

# HISTORY

**dropbear** 由 **Matt Johnston** 编写，首次发布于 **2003 年**。当时小型设备上的选择要么完全没有 SSH，要么是被削得面目全非的 OpenSSH。它迅速成为嵌入式 Linux 的标配，OpenWrt 的采用更使其按装机数量计成为现存部署最广的 SSH 服务器之一，运行在数百万台其主人从未听说过它的路由器上。

# INSTALL

```apt: sudo apt install dropbear-bin```

```dnf: sudo dnf install dropbear```

```pacman: sudo pacman -S dropbear```

```apk: sudo apk add dropbear```

```brew: brew install dropbear```

```nix: nix profile install nixpkgs#dropbear```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dbclient](/man/dbclient)(1), [dropbearkey](/man/dropbearkey)(1), [dropbearconvert](/man/dropbearconvert)(1), [sshd](/man/sshd)(8), [ssh](/man/ssh)(1), [scp](/man/scp)(1)

# RESOURCES

```[Source code](https://github.com/mkj/dropbear)```

```[Homepage](https://matt.ucc.asn.au/dropbear/dropbear.html)```

<!-- verified: 2026-07-14 -->
