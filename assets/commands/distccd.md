# TAGLINE

用于分布式编译的 distcc 服务器守护进程

# TLDR

**启动 distcc 守护进程**

```distccd --daemon```

**以允许的主机列表启动**

```distccd --daemon --allow [192.168.1.0/24]```

**在前台启动**

```distccd --no-detach --daemon --allow [0.0.0.0/0]```

**指定监听地址**

```distccd --daemon --listen [0.0.0.0]```

# SYNOPSIS

**distccd** [_options_]

# PARAMETERS

**--daemon**
> 以守护进程方式运行。

**--allow** _spec_
> 允许来自指定地址的连接。

**--listen** _addr_
> 监听指定地址。

**--no-detach**
> 不脱离终端。

**--port** _port_
> 监听指定端口（默认 3632）。

**--jobs** _n_
> 最大并发作业数。

**--log-file** _file_
> 记录到文件而非 syslog。

# DESCRIPTION

**distccd** 是 distcc 的服务器守护进程，接收并处理网络中 distcc 客户端发来的编译作业。它接受预处理后的源代码，用本地编译器编译，并将目标文件返回给请求的客户端。

守护进程默认监听 TCP 端口 3632，应配置访问控制以防止未授权的编译请求。安全性通过 --allow 选项指定的 IP 地址白名单实现，因为协议本身不提供认证。

distccd 可以限制并发编译作业数量，防止系统过载。它默认记录到 syslog，但也可以配置为写入指定的日志文件。出于安全考虑，守护进程通常以权限受限的专用用户运行。

# CONFIGURATION

**/etc/default/distccd**
> 基于 Debian 的系统上 distccd 守护进程的默认配置。

**/etc/sysconfig/distccd**
> 基于 Red Hat 的系统上 distccd 守护进程的默认配置。

# CAVEATS

确保防火墙允许端口 3632 上的连接。使用 --allow 将访问限制在可信网络内。

# INSTALL

```apt: sudo apt install distcc```

```dnf: sudo dnf install distcc```

```pacman: sudo pacman -S distcc```

```apk: sudo apk add distcc```

```zypper: sudo zypper install distcc```

```brew: brew install distcc```

```nix: nix profile install nixpkgs#distcc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[distcc](/man/distcc)(1), [ccache](/man/ccache)(1)

# RESOURCES

```[Source code](https://github.com/distcc/distcc)```

```[Homepage](https://www.distcc.org)```

<!-- verified: 2026-07-11 -->
