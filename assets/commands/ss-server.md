# TLDR

**以内联配置启动服务器**

```ss-server -s [0.0.0.0] -p [8388] -k "[password]" -m [aes-256-gcm]```

**使用配置文件启动服务器**

```ss-server -c [/etc/shadowsocks/config.json]```

**以详细模式启动**

```ss-server -c [config.json] -v```

**以指定用户身份启动**

```ss-server -c [config.json] -a [nobody]```

**以守护进程运行**

```ss-server -c [config.json] -f [/var/run/ss-server.pid]```

# SYNOPSIS

**ss-server** [**-c** _config_] [**-s** _server_] [**-p** _port_] [**-k** _password_] [**-m** _method_] [_options_]

# PARAMETERS

**-c**, **--config** _file_
> JSON 配置文件的路径。

**-s**, **--server** _address_
> 要绑定的服务器地址。

**-p**, **--server-port** _port_
> 服务器端口号。

**-k**, **--password** _password_
> 用于加密的密码。

**-m**, **--encrypt-method** _method_
> 加密方法（aes-256-gcm、chacha20-ietf-poly1305 等）。

**-t**, **--timeout** _seconds_
> 套接字超时时间，以秒为单位。

**-a**, **--user** _user_
> 以指定用户身份运行。

**-f**, **--pid-file** _file_
> 守护进程模式的 PID 文件路径。

**-d**, **--dns** _server_
> DNS 服务器地址。

**--fast-open**
> 启用 TCP fast open。

**--reuse-port**
> 启用端口复用以支持多个实例。

**-u**, **--udp**
> 启用 UDP 中继。

**-v**, **--verbose**
> 启用详细日志输出。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**ss-server** 是 Shadowsocks 的服务端组件。Shadowsocks 是一种旨在保护网络流量的安全代理协议。它监听来自 Shadowsocks 客户端的连接，并将流量转发到目标服务器。

服务器使用现代密码学算法加密客户端与服务器之间的所有流量。推荐的加密算法包括 **aes-256-gcm** 和 **chacha20-ietf-poly1305**（AEAD 加密）。旧的流式加密因存在安全漏洞已被弃用。

配置可以通过命令行参数或 JSON 文件提供。JSON 格式还支持多个服务器端口和插件配置等附加选项。

# CONFIGURATION

**/etc/shadowsocks-libev/config.json**
> 系统级 JSON 配置文件，指定服务器地址、端口、密码、加密方法、超时时间以及可选的插件设置。

# CAVEATS

避免使用已弃用的流式加密（rc4-md5、aes-cfb 等），它们缺少认证机制。为了安全请使用 AEAD 加密。不建议以 root 运行；请用 **-a** 降权。TCP fast open 需要内核支持，且可能被某些网络封锁。使用代理软件前请了解当地法律。

# HISTORY

**Shadowsocks** 由 clowwindy 于 **2012 年**创建，是一种安全代理协议。最初的 Python 实现之后出现了多种语言的移植版本。基于 libev 的实现（shadowsocks-libev）以高性能的 C 实现提供 **ss-server**。尽管原始仓库已被移除，该项目仍得到广泛采用，并在社区贡献下继续开发。

# INSTALL

```apt: sudo apt install shadowsocks-libev```

```zypper: sudo zypper install shadowsocks-libev```

```brew: brew install shadowsocks-libev```

```nix: nix profile install nixpkgs#shadowsocks-libev```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ss-local](/man/ss-local)(1)
