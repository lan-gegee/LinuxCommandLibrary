# TAGLINE

为仓库启动内置 HTTP 服务器

# TLDR

**启动 HTTP 服务器**

```hg serve```

**指定端口**

```hg serve -p [8080]```

**指定地址**

```hg serve -a [0.0.0.0]```

**允许推送**

```hg serve --config web.push_ssl=false --config web.allow_push=*```

**在后台运行**

```hg serve -d```

# SYNOPSIS

**hg serve** [_options_]

# PARAMETERS

**-p**, **--port** _PORT_
> 监听端口（默认 8000）。

**-a**, **--address** _ADDR_
> 监听地址。

**-d**, **--daemon**
> 在后台运行。

**--pid-file** _FILE_
> PID 文件位置。

**-n**, **--name** _NAME_
> 仓库名称。

**--web-conf** _FILE_
> Web 配置文件。

**-A**, **--accesslog** _FILE_
> 要写入的访问日志文件名。

**-E**, **--errorlog** _FILE_
> 要写入的错误日志文件名。

**--certificate** _FILE_
> SSL 证书文件，用于通过 HTTPS 提供服务。

**--print-url**
> 启动服务器并只打印其 URL。

**--help**
> 显示帮助信息。

# DESCRIPTION

**hg serve** 为仓库启动内置 HTTP 服务器。它通过 Web 浏览器提供读取访问，也为其他客户端提供 clone/pull 访问。

该服务器便于快速共享，但不适合生产环境。通过配置可以支持多个仓库。

# CAVEATS

不具备生产环境可用性。推送默认禁用。单线程运行。

# HISTORY

serve 是 **Mercurial** 自 1.0 版本以来内置的快速仓库共享功能。

# SEE ALSO

[hg](/man/hg)(1), [hg-clone](/man/hg-clone)(1), [hg-pull](/man/hg-pull)(1)
