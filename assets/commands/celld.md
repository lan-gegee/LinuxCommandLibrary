# TAGLINE

自托管的分布式 Durable Objects 运行时

# TLDR

**安装**二进制文件（发布版附带 GitHub attestations）

```curl -fsSL https://celld.dev/install.sh | sh```

将 Wrangler Worker 项目**部署**到 fleet bucket

```celld deploy . --bucket s3://[my-cells-bucket]```

针对同一 bucket **启动**一个节点

```celld --bucket s3://[my-cells-bucket] --listen 0.0.0.0:8080 --advertise [10.0.0.12:8080]```

使用 S3 兼容端点（如 Cloudflare R2）**运行**

```celld --bucket s3://[bucket] --endpoint https://[account].r2.cloudflarestorage.com --region auto --listen 0.0.0.0:8080 --advertise [node-a.internal:8080]```

**诊断** fleet 对等节点与节点健康状况

```celld diagnose --bucket s3://[my-cells-bucket]```

**显示**完整 CLI 帮助

```celld --help```

# SYNOPSIS

**celld** [**--bucket** _s3://bucket_] [**--endpoint** _url_] [**--region** _name_] [**--listen** _addr_] [**--advertise** _addr_] [_options_]

**celld** **deploy** _path_ [**--bucket** _s3://bucket_] [_options_]

**celld** **diagnose** [**--bucket** _s3://bucket_] [**--peer** _NODE_ID_]...

# DESCRIPTION

**celld** 是一个开源守护进程，可在你自己的机器上运行 Cloudflare Workers 和 Durable Objects。每个 Durable Object 都是一个 **cell**：一个拥有独立私有 SQLite 数据库的命名服务器。Cell 之间仅通过你拥有的 S3 兼容 bucket 进行协调和复制——没有单独的控制平面或共识服务。

每个节点内嵌 V8，执行 Wrangler 打包产物，并在 bucket 中共享部署、cell 状态和所有权记录。对象存储的 compare-and-swap 保证任一时刻只有一个节点拥有某个 cell。空闲的 cell 会休眠；不活跃的 cell 仅以 bucket 中对象的形式存在，几乎零成本。已确认的写入会先复制到 bucket（RPO=0）。

让多个节点指向同一个 bucket 即可组成一个 fleet。对等节点通过 bucket 中的租约相互发现。节点间 HTTP 使用 HMAC 认证且不终止 TLS——advertise 地址应保留在私有网络或加密覆盖网络（WireGuard、Tailscale）中。Worker 项目执行 `celld deploy` 时需要在 `PATH` 中有 **esbuild**；纯静态资源项目则不需要。

# PARAMETERS

**--bucket** _s3://bucket_
> 存放部署、SQLite 副本、所有权记录和节点认证的 fleet bucket。等同于 **CELLD_BUCKET**。

**--endpoint** _url_
> S3 兼容 API 端点（如 R2）。等同于 **S3_ENDPOINT**。

**--region** _name_
> 对象存储区域（R2 用 **auto**）。未设置时使用标准 AWS 区域变量。

**--listen** _addr_
> 本地 HTTP 监听地址（默认值适合本地开发）。等同于 **CELLD_ADDR**。

**--advertise** _addr_
> 其他节点和入口可访问的地址。多节点 fleet 必需。等同于 **CELLD_ADVERTISE**。

**--unsafe-public-advertise**
> 允许将字面公网 IP 用作 **--advertise**（默认拒绝）。

**deploy** _path_
> 打包 Wrangler 项目（Workers、Durable Object 绑定、静态资源）并写入 bucket。

**diagnose**
> 枚举节点租约并探测存活的对等节点，但不获取所有权。可选 **--peer** _NODE_ID_（可重复）。

**-h**, **--help**
> 显示完整选项列表和高级调参开关。

**--version**
> 输出二进制版本号。

# CONFIGURATION

**CELLD_BUCKET**
> 默认的 fleet bucket URI。

**AWS_ACCESS_KEY_ID**, **AWS_SECRET_ACCESS_KEY**, **AWS_SESSION_TOKEN**
> 显式凭证；同时也会使用标准 AWS 凭证链。

**S3_ENDPOINT**, **AWS_REGION**
> 非 AWS 或 R2 存储的端点和区域。

**CELLD_WATCH**
> 用于 SQLite 和复制状态的本地工作目录。

**CELLD_MAX_RESIDENT_CELLS**, **CELLD_RESIDENT_LOW_WATER**
> 常驻 cell 的可选压力卸载水位线。

**CELLD_MAX_RSS_MB**, **CELLD_MAX_CPU_PERCENT**
> Linux 上触发卸载空闲 cell 的内存/CPU 压力阈值。

**CELLD_ESBUILD**
> Worker 部署所用 **esbuild** 的路径。

**RUST_LOG**
> 运行时日志过滤器。

# CAVEATS

运行时及其与 Cloudflare 的兼容面仍在演进中。Bucket 凭证相当于 fleet 管理员权限——务必妥善保护。不要把节点端口暴露在公共互联网上；节点间流量不终止 TLS。公网 advertise IP 需要显式的 unsafe 标志。与完整 Workers/Durable Objects 参考行为的一致性仍在持续扩展。

# HISTORY

**celld** 是来自 **Deno Land**（Ryan Dahl 及合作者）的 Apache-2.0 项目，作为自托管 Durable Objects 运行时发布，用对象存储取代托管控制平面作为唯一协调者。

# SEE ALSO

[wrangler](/man/wrangler)(1), [esbuild](/man/esbuild)(1), [deno](/man/deno)(1)

# RESOURCES

```[Source code](https://github.com/denoland/celld)```

```[Homepage](https://celld.dev)```

```[Documentation](https://celld.dev/docs)```

<!-- verified: 2026-08-06 -->
