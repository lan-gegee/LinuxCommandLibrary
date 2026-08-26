# TAGLINE

用于暴露本地端口的简单 TCP 隧道

# TLDR

使用公共 bore.pub 服务器**暴露**本地端口

```bore local [local_port] --to bore.pub```

将本地端口**暴露**到你自己的远程 Bore 服务器

```bore local [local_port] --to [remote_server_address]```

**启动** Bore 服务器

```bore server```

**启动**要求共享密钥的 Bore 服务器

```bore server --secret [your_secret]```

显示**帮助**

```bore -h```

# SYNOPSIS

**bore** _command_ [_options_]

# DESCRIPTION

**bore** 是一个现代、简单的 TCP 隧道工具，可将本地端口暴露到远程服务器供公开访问。它让本地服务无需复杂的端口转发或防火墙配置即可从互联网访问。

该工具由客户端组成：客户端将本地端口连接到远程 bore 服务器，由后者为传入连接提供公共端点。公共服务器位于 **bore.pub**，也可以用 `bore server` 运行自己的服务器。它是一个用 Rust 编写的单一自包含二进制文件。

# SUBCOMMANDS

**local**
> 将本地端口暴露到远程服务器。接受位置参数形式的本地端口以及用于服务器地址的 **-t, --to**（参见 [bore-local](/man/bore-local)(1)）。

**server**
> 运行接受客户端隧道的 bore 服务器。

# PARAMETERS

**-t, --to** _address_
> 远程 bore 服务器地址（用于 **local**）。

**-s, --secret** _secret_
> 用于认证的共享密钥（**local** 和 **server** 均适用）。

**--min-port** _port_
> 服务器：接受的最小 TCP 端口号（默认：1024）。

**--max-port** _port_
> 服务器：接受的最大 TCP 端口号（默认：65535）。

**--bind-addr** _address_
> 服务器：控制连接绑定的地址（默认：0.0.0.0）。

**-h, --help**
> 显示帮助信息。

# CAVEATS

需要有正在运行且可访问的 bore 服务器。流量经由远程服务器隧道传输，会增加延迟。共享密钥只认证隧道控制通道：转发的流量不由 bore 加密，因此敏感数据应使用 HTTPS 或其他加密层。不适合高带宽应用。

# INSTALL

```pacman: sudo pacman -S bore```

```nix: nix profile install nixpkgs#bore```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bore-local](/man/bore-local)(1), [ngrok](/man/ngrok)(1), [ssh](/man/ssh)(1)

# RESOURCES

```[Source code](https://github.com/ekzhang/bore)```

```[Homepage](https://bore.pub)```

<!-- verified: 2026-06-19 -->
