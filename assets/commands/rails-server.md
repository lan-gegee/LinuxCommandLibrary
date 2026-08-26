# TAGLINE

启动 Rails 开发 Web 服务器

# TLDR

**启动 Rails 开发服务器**

```rails server```

**在指定端口启动服务器**

```rails server -p [port]```

**绑定到所有网络接口启动服务器**

```rails server -b 0.0.0.0```

**在生产环境中启动服务器**

```rails server -e production```

**使用指定的服务器启动**（Puma、Thin 等）

```rails server -u [puma|thin|webrick]```

**以守护进程模式启动**（后台）

```rails server -d```

# SYNOPSIS

**rails server** [**-p** _port_] [**-b** _address_] [**-e** _environment_] [**-d**] [**-u** _server_]

# PARAMETERS

**-p**, **--port** _PORT_
> 在指定端口运行服务器（默认：3000）

**-b**, **--binding** _IP_
> 绑定到指定 IP 地址（默认：localhost）

**-e**, **--environment** _ENV_
> 在指定环境中运行（development、test、production）

**-d**, **--daemon**
> 以守护进程（后台进程）方式运行服务器

**-u**, **--using** _SERVER_
> 使用指定的 Rack 服务器（puma、thin、webrick 等）

**-P**, **--pid** _FILE_
> 指定 PID 文件路径

**-C**, **--dev-caching**
> 切换开发模式缓存

**--early-hints**
> 启用 HTTP/2 early hints

**-h**, **--help**
> 显示帮助信息

# DESCRIPTION

**rails server** 为 Rails 应用启动一个 Web 服务器。默认情况下，它使用 Puma，并在开发环境下监听 http://localhost:3000。

在开发模式下，服务器会自动重载代码变更，无需重启即可快速迭代。它会在终端显示请求日志，包括 HTTP 方法、路径、响应码和耗时信息。

绑定到 0.0.0.0 可以让网络中的其他机器访问该服务器，适合在移动设备或其他电脑上进行测试。

# CAVEATS

默认绑定到 localhost（127.0.0.1），只接受来自本机的连接。使用 **-b 0.0.0.0** 可接受外部连接，但要注意安全影响。

开发模式不适合生产环境。它缺少性能优化，且可能暴露调试信息。已部署的应用务必配合正确的生产配置使用 **-e production**。

守护进程模式（**-d**）需要手动管理进程。生产部署请使用 systemd 或 Passenger 等进程管理器。

# SEE ALSO

[rails](/man/rails)(1), [puma](/man/puma)(1), [rails-routes](/man/rails-routes)(1), [bundle](/man/bundle)(1)
