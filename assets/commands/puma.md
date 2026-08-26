# TAGLINE

并发 Ruby Web 服务器

# TLDR

**启动 Puma 服务器**

```puma```

**使用配置文件启动**

```puma -C [config/puma.rb]```

**在指定端口启动**

```puma -p [3000]```

**带 worker 启动**

```puma -w [4]```

**以守护进程模式启动**

```puma -d```

# SYNOPSIS

**puma** [_options_] [_rackup file_]

# PARAMETERS

**-p**, **--port** _port_
> 监听端口。

**-b**, **--bind** _uri_
> 绑定的 URI。

**-C**, **--config** _file_
> 配置文件。

**-w**, **--workers** _n_
> worker 数量。

**-t**, **--threads** _min:max_
> 线程池大小。

**-d**, **--daemon**
> 将进程转为守护进程。

**-e**, **--environment** _env_
> 环境（development、production）。

# DESCRIPTION

**Puma** 是一个快速并发的 Ruby/Rack Web 服务器。它使用线程和可选的 worker 实现并行处理，非常适合生产环境的 Rails 部署。

# EXAMPLES

```bash
# Start on port 3000
puma -p 3000

# With workers and threads
puma -w 4 -t 8:32

# Bind to Unix socket
puma -b unix:///tmp/puma.sock

# Production mode
puma -e production -w 4

# With config file
puma -C config/puma.rb
```

# 配置 (puma.rb)

```ruby
workers 4
threads 4, 16
port 3000
environment 'production'
preload_app!

on_worker_boot do
  ActiveRecord::Base.establish_connection
end
```

# CAVEATS

需要 Ruby/Rack。worker 需要 copy-on-write 支持。生产环境中建议配合反向代理使用。

# HISTORY

Puma 由 **Evan Phoenix** 于 2011 年创建，作为 Mongrel 的替代品，专注于并发请求处理。

# INSTALL

```apt: sudo apt install puma```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rails](/man/rails)(1)
