# TAGLINE

Cloudflare Workers 模拟器

# TLDR

**启动本地 worker**

```miniflare [worker.js]```

**指定端口**

```miniflare [worker.js] --port [8787]```

**使用 KV 命名空间**

```miniflare [worker.js] --kv [NAMESPACE]```

**使用 D1 数据库**

```miniflare [worker.js] --d1 [DB]```

**使用环境变量**

```miniflare [worker.js] --env [.env]```

**监视变更**

```miniflare [worker.js] --watch```

# SYNOPSIS

**miniflare** [_options_] [_script_]

# PARAMETERS

**--port** _port_
> HTTP 端口。

**--host** _host_
> 绑定地址。

**--kv** _namespace_
> KV 命名空间。

**--d1** _database_
> D1 数据库。

**--r2** _bucket_
> R2 存储桶。

**--env** _file_
> 环境变量文件。

**--watch**
> 监视变更。

**--wrangler-config** _file_
> Wrangler 配置文件。

# DESCRIPTION

**Miniflare** 是一个 Cloudflare Workers 模拟器。它在本地运行 Workers，完整支持 KV、Durable Objects、R2、D1 及其他 Cloudflare 服务。

Miniflare 无需部署到 Cloudflare 即可进行本地开发和测试。

# FEATURES

```
- KV storage
- Durable Objects
- R2 buckets
- D1 databases
- Cache API
- Scheduled events
```

# CAVEATS

行为可能与生产环境不同。存储是本地/临时的。某些功能需要额外配置。现已集成到 Wrangler 中。

# HISTORY

Miniflare 由 **Brendan Coll** 于 **2021 年**创建，用于支持 Cloudflare Workers 的本地开发。后来被 Cloudflare 正式采用。

# SEE ALSO

[wrangler](/man/wrangler)(1), [cloudflared](/man/cloudflared)(1)
