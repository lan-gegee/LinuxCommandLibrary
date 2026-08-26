# TAGLINE

Varnish HTTP 反向代理缓存守护进程

# TLDR

**以默认后端启动**

```varnishd -a :80 -b localhost:8080```

**以 VCL 配置启动**

```varnishd -a :80 -f /etc/varnish/default.vcl```

**以前台方式运行**

```varnishd -F -a :80 -b localhost:8080```

**设置缓存存储大小**

```varnishd -a :80 -b localhost:8080 -s malloc,[256m]```

**启用管理接口**

```varnishd -a :80 -b localhost:8080 -T localhost:6082```

**设置默认 TTL**

```varnishd -a :80 -b localhost:8080 -t [120]```

**设置运行时参数**

```varnishd -a :80 -b localhost:8080 -p thread_pools=[2]```

# SYNOPSIS

**varnishd** [_options_]

# PARAMETERS

**-a** _address[:port]_
> 监听客户端请求（默认端口：80）。

**-b** _host[:port]_
> 后端服务器（默认端口：80）。

**-f** _config_
> VCL 配置文件。

**-F**
> 以前台方式运行（不 fork）。

**-s** _[name=]type[,options]_
> 存储后端：malloc、file、persistent。

**-t** _ttl_
> 缓存对象的默认 TTL（秒）。

**-T** _address[:port]_
> 管理接口地址。

**-S** _secret-file_
> 管理接口的认证密钥文件。

**-n** _name_
> 实例名和工作目录。

**-p** _param=value_
> 设置运行时参数。

**-r** _param[,param...]_
> 将参数设为只读。

**-i** _identity_
> 服务器身份字符串。

**-I** _clifile_
> 启动时从文件执行 CLI 命令。

**-d**
> 启用调试模式（不启动工作进程，在标准输入上接受 CLI 命令）。

**-j** _jail[,jailoptions]_
> 为工作进程指定沙箱隔离技术。

# DESCRIPTION

**varnishd** 是 Varnish HTTP 加速器守护进程。它充当反向代理缓存，接收 HTTP 请求，转发给后端服务器，并缓存响应以便更快地服务后续请求。

该守护进程使用 VCL（Varnish Configuration Language，Varnish 配置语言）定义缓存策略、请求路由和响应处理。VCL 会被编译为 C 并动态加载。

存储后端包括 malloc（内存）和 file（基于磁盘并使用内存映射）。可以配置多个存储后端和监听地址。

管理接口支持运行时配置更改、VCL 加载，以及通过 varnishadm 访问统计信息。

# CAVEATS

必须提供 -b 或 -f 选项之一。修改 VCL 后需通过管理接口重新加载。内存存储的内容在重启后会丢失。在 80 端口上运行需要 root 权限或相应 capabilities。

# HISTORY

**Varnish** 由 Poul-Henning Kamp 创建并于 2006 年发布。它专为现代硬件和操作系统从零开始设计，采用了内存映射文件和内核级优化等技术。如今它已成为部署最广泛的 HTTP 加速器之一。

# INSTALL

```apt: sudo apt install varnish```

```dnf: sudo dnf install varnish```

```apk: sudo apk add varnish```

```brew: brew install varnish```

```nix: nix profile install nixpkgs#varnish```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[varnishlog](/man/varnishlog)(1), [varnishstat](/man/varnishstat)(1), [nginx](/man/nginx)(8)
