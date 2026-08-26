# TAGLINE

通过 Gemini 协议提供内容服务

# TLDR

**启动** Gemini 服务器

```agate --content [/var/gemini] --hostname [example.com]```

使用**自定义证书**

```agate --content [/var/gemini] --hostname [example.com] --certs [/etc/agate/certs]```

在**自定义端口**上运行

```agate --content [/var/gemini] --hostname [example.com] --addr [0.0.0.0:1965]```

启用**日志记录**

```agate --content [/var/gemini] --hostname [example.com] --log-ip```

# SYNOPSIS

**agate** --content _dir_ --hostname _host_ [_options_]

# DESCRIPTION

**agate** 是一款简单而安全的 Gemini 协议服务器。Gemini 是一种轻量的 HTTP 替代协议，强调隐私与简洁。agate 只需极少配置即可通过 TLS 提供静态内容服务。

如果未提供 TLS 证书，服务器会自动生成；它支持多个虚拟主机，并根据文件扩展名来提供 Gemini 文本文件（.gmi）和其他内容类型。

# PARAMETERS

**--content** _dir_
> 内容的根目录

**--hostname** _host_
> 服务器的主机名（做虚拟主机时可重复使用）

**--addr** _address_
> 要绑定的地址（默认：0.0.0.0:1965）

**--certs** _dir_
> 存放 TLS 证书/密钥对的目录（默认：.certificates）。若证书缺失，会按主机名自动生成。

**--lang** _code_
> text/gemini 响应的默认语言代码。

**--log-ip**
> 记录客户端 IP 地址。

**-C**, **--central-conf**
> 改为从内容根目录读取单个 .meta 配置文件，而不是各目录各自的文件。

**--serve-secret**
> 提供名称以点号开头的文件和目录（默认视为隐藏而不提供服务）。

**-3**, **--only-tls13**
> 禁用 TLSv1.2，仅接受 TLSv1.3 连接。

**--skip-port-check**
> 不要求请求 URL 中的端口与监听端口一致（在反向代理后面很有用）。

**-s**, **--silent**
> 关闭日志输出。

# CAVEATS

Gemini 要求使用 TLS；不支持未加密的连接。默认的 Gemini 端口 1965 在某些系统上可能需要 root 权限。与 HTTP 浏览器相比，客户端支持较为有限。

# HISTORY

Gemini 协议由 Solderpunk 于 **2019** 年设计。随着 Gemini 生态不断发展，**agate** 作为其中一员诞生了。它是一个用 Rust 编写的简洁服务器实现，秉持该协议的极简哲学。

# INSTALL

```aur: yay -S agate```

```nix: nix profile install nixpkgs#agate```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[nginx](/man/nginx)(8)

# RESOURCES

```[Source code](https://github.com/mbrubeck/agate)```

<!-- verified: 2026-06-11 -->
