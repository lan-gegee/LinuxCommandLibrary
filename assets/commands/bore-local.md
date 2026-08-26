# TAGLINE

通过远程隧道暴露本地端口

# TLDR

使用公共 bore.pub 服务器**暴露**本地端口

```bore local [local_port] --to bore.pub```

将本地端口**暴露**到你自己的远程 Bore 服务器

```bore local [local_port] --to [remote_server_address]```

暴露**指定的本地主机**而非 localhost

```bore local [local_port] --local-host [host] --to [remote_server_address]```

显式请求**指定的远程端口**

```bore local [local_port] --to [remote_server_address] --port [remote_port]```

使用**密钥进行认证**

```bore local [local_port] --to [remote_server_address] --secret [your_secret]```

# SYNOPSIS

**bore local** [_options_] _local_port_

# DESCRIPTION

**bore local** 创建从本地端口到远程 bore 服务器的隧道，使本地服务可以通过远程服务器的公共地址访问。这适用于暴露开发服务器、Webhook 或其他本地服务。

只要命令在运行，连接就会保持，流量会双向转发。

# PARAMETERS

**-t, --to** _address_
> 远程 bore 服务器地址（必填）。

**-l, --local-host** _host_
> 要转发的本地主机（默认：localhost）。

**-p, --port** _port_
> 向服务器请求的远程端口（默认：0，表示由服务器分配一个随机的可用端口）。

**-s, --secret** _secret_
> 服务器的认证密钥。

**-h, --help**
> 显示帮助信息。

# CAVEATS

当 **--port** 为 0（默认值）时，服务器会分配一个随机的可用端口，并在启动时打印生成的公共地址。连接稳定性取决于网络状况。如果服务器要求认证，密钥必须与服务器配置的密钥一致。转发的流量不会由 bore 加密。

# INSTALL

```pacman: sudo pacman -S bore```

```nix: nix profile install nixpkgs#bore```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bore](/man/bore)(1), [ssh](/man/ssh)(1)

# RESOURCES

```[Source code](https://github.com/ekzhang/bore)```

```[Homepage](https://bore.pub)```

<!-- verified: 2026-06-19 -->
