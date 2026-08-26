# TAGLINE

Shadowsocks 本地 SOCKS5 代理客户端

# TLDR

**启动客户端**

```ss-local -s [server] -p [8388] -l [1080] -k [password] -m [aes-256-gcm]```

**使用配置文件**

```ss-local -c [/etc/shadowsocks/config.json]```

**以前台方式运行**

```ss-local -c [config.json] -v```

**指定本地地址**

```ss-local -c [config.json] -b [127.0.0.1]```

**UDP 中继**

```ss-local -c [config.json] -u```

**使用 SIP003 插件**（例如 v2ray-plugin）

```ss-local -c [config.json] --plugin [v2ray-plugin] --plugin-opts "[tls;host=example.com]"```

**以守护进程运行**

```ss-local -c [config.json] -f [/var/run/ss-local.pid]```

# SYNOPSIS

**ss-local** [_-s server_] [_-p port_] [_-l local_port_] [_-k password_] [_-m method_] [_options_]

# PARAMETERS

**-s** _SERVER_
> 远程服务器主机名或 IP。

**-p** _PORT_
> 远程服务器端口。

**-l** _PORT_
> 本地 SOCKS5 监听端口。

**-k** _PASSWORD_
> 共享密码（必须与服务器一致）。

**-m** _METHOD_
> 加密方法（例如 aes-256-gcm、chacha20-ietf-poly1305）。

**-c** _FILE_
> JSON 配置文件。

**-b** _ADDR_
> 本地绑定地址。

**-i** _INTERFACE_
> 出站网络接口。

**-t** _SECONDS_
> 套接字超时时间（默认：60）。

**-a** _USER_
> 启动后降权到该用户运行。

**-f** _PIDFILE_
> 转入后台并写入 PID 文件。

**-n** _NUMBER_
> 最大打开文件数。

**-u**
> 在 TCP 之外同时启用 UDP 中继。

**-U**
> 仅 UDP 中继（禁用 TCP）。

**-6**
> 主机名解析优先使用 IPv6。

**-v**
> 详细日志输出。

**--fast-open**
> 启用 TCP Fast Open。

**--reuse-port**
> 启用 SO_REUSEPORT。

**--mptcp**
> 启用 Multipath TCP。

**--no-delay**
> 启用 TCP_NODELAY。

**--mtu** _MTU_
> 用于分片的接口 MTU。

**--acl** _FILE_
> 访问控制列表文件。

**--plugin** _NAME_
> SIP003 传输插件（例如 v2ray-plugin、obfs-local）。

**--plugin-opts** _OPTS_
> 传递给 SIP003 插件的选项。

**--key** _BASE64_
> 以 Base64 表示的预共享密钥（替代 -k）。

**-h**, **--help**
> 显示帮助。

# DESCRIPTION

**ss-local** 是 Shadowsocks（一种加密代理协议）的本地客户端组件。它在本机的一个端口上作为 SOCKS5 代理服务器监听，将所有流量加密后经远程 Shadowsocks 服务器转发，以绕过网络过滤。

配置为使用该本地 SOCKS5 代理的应用程序，其流量会在离开本机前使用 AES-256-GCM 或 ChaCha20-Poly1305 等方法加密。加密方法和密码必须与远程服务器的配置一致。UDP 中继模式（**-u**）可为 DNS 解析和游戏等应用代理 UDP 流量。

连接参数可以在命令行上指定，也可以为方便起见存放在 JSON 配置文件中。

# CONFIGURATION

**/etc/shadowsocks-libev/config.json**
> 系统级配置文件，指定服务器地址、端口、密码、加密方法和本地监听设置。

**~/.shadowsocks/config.json**
> 每用户配置文件，JSON 格式与系统级配置相同。

# CAVEATS

加密方法和密码必须与远程 ss-server 完全一致。默认只代理 TCP；需要 UDP 时请加上 **-u**。某些网络的深度包检测会识别并封锁 Shadowsocks；可借助 v2ray-plugin 或 obfs 等 SIP003 插件缓解。它不是完整的 VPN；只有配置为使用该 SOCKS5 端点的应用才会被代理。

# HISTORY

**Shadowsocks** 由 **clowwindy** 于 **2012 年**创建，用于规避互联网审查。它使用加密代理连接绕过过滤。

# INSTALL

```apt: sudo apt install shadowsocks-libev```

```zypper: sudo zypper install shadowsocks-libev```

```brew: brew install shadowsocks-libev```

```nix: nix profile install nixpkgs#shadowsocks-libev```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ss-server](/man/ss-server)(1), [proxychains](/man/proxychains)(1)
