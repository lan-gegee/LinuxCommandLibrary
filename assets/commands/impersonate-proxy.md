# TAGLINE

可配置 TLS 和 HTTP 指纹的本地中间人代理

# TLDR

从克隆的仓库中**构建**二进制文件

```make build```

**启动**代理（重新构建、释放 8080 端口、读取 `config.yaml`）

```make run```

用默认配置**运行**已构建的二进制文件

```impersonate-proxy```

以显式指定的配置文件**运行**

```impersonate-proxy -config [config.yaml]```

通过代理并使用生成的 CA **发送 curl 请求**

```curl --proxy http://127.0.0.1:8080 --cacert [ca.crt] [https://example.com]```

**读取**实时管理 API

```curl http://127.0.0.1:8081/api/config```

运行时**切换** TLS 预设（仅对新连接生效）

```curl -X POST http://127.0.0.1:8081/api/config -H 'Content-Type: application/json' -d '{"tls_preset":"firefox"}'```

# SYNOPSIS

**impersonate-proxy** [**-config** _file_]

# PARAMETERS

**-config** _file_
> YAML 配置文件的路径。默认：`config.yaml`。

项目的 Makefile 还提供了以下目标：

**make build**
> 将 Go 源码编译为 `./impersonate-proxy`。需要 Go 1.22+。

**make run**
> 构建并结束占用端口 8080 的进程，然后启动 `./impersonate-proxy -config config.yaml`。

**make trust-ca**
> 在 macOS 上将生成的 `ca.crt` 添加到系统钥匙串（需要 sudo）。

**make clean**
> 删除二进制文件、`ca.crt` 和 `ca.key`。

# DESCRIPTION

**impersonate-proxy** 是一个用 Go 编写的本地中间人 HTTP 代理。它使用生成的 CA 解密客户端 TLS，然后建立新的上游连接，其 TLS ClientHello、HTTP/2 SETTINGS、头部顺序和 User-Agent 均取自 YAML 配置档案。其用途是对 WAF 和机器人检测系统进行经授权的测试：将 curl、浏览器或 Playwright 经由该代理路由，观察特定指纹会被如何分类。

首次启动时，进程会写入 `ca.crt` 和 `ca.key`（路径可配置），并默认监听 `127.0.0.1:8080`。客户端必须信任该 CA 或显式传入它（`curl --cacert`、`NODE_EXTRA_CA_CERTS`、Firefox 证书导入）。第二个监听器（`mgmt_listen`，默认 `127.0.0.1:8081`）提供 `GET`/`POST /api/config`，使随附的 Chrome 扩展——或 curl——能够在不重启的情况下更改 TLS 预设、自定义 JA3/JA4 `custom_hello`、伪造客户端 IP 头部以及 User-Agent。

内置的 TLS 预设包括 `chrome`、`firefox`、`safari`、`edge`、`ios`、`random`、`golang` 和 `custom`。HTTP/1.1 改写涵盖头部顺序、增删头部、User-Agent 以及可选的 `X-Forwarded-For` / `True-Client-IP`。当代理到服务器一端启用 HTTP/2 时，SETTINGS 顺序、`WINDOW_UPDATE` 和伪头部顺序也可配置。

支持的平台为 **macOS** 和 **Linux**（amd64 与 arm64）。没有包管理器二进制包；请克隆仓库并运行 `make build`。

# CONFIGURATION

**config.yaml**
> 启动时读取的单一 YAML 文件。所有键都有默认值；只需设置需要覆盖的部分。

**listen**
> 代理绑定地址。默认 `127.0.0.1:8080`。

**mgmt_listen**
> 管理 API 绑定地址。默认 `127.0.0.1:8081`。设为空则禁用。

**ca_cert** / **ca_key**
> 中间人 CA 的路径（默认 `ca.crt` / `ca.key`）。缺失时在首次运行时生成。

**tls.preset**
> `chrome` | `firefox` | `safari` | `edge` | `ios` | `random` | `golang` | `custom`。

**tls.custom_hello**
> 仅当 `preset` 为 `custom` 时使用。字段：`cipher_suites`、`curves`、`versions`、`extensions`。密码套件和扩展的顺序是 JA3/JA4 指纹的一部分。GREASE 占位值（`0x0a0a` 及其他 `0xXAXA` 值）会在每个连接中随机化。

**http.user_agent**
> 覆盖转发使用的 User-Agent。空字符串表示原样传递客户端的值。

**http.client_ip**
> 设置后覆盖 `X-Forwarded-For` 和 `True-Client-IP`。

**http.header_order** / **add_headers** / **remove_headers**
> 控制 HTTP/1.1 头部的顺序和成员关系。未列出的头部会追加在末尾。

**http2.enabled** / **settings** / **window_update** / **pseudo_header_order**
> 上游一端的 HTTP/2 指纹。SETTINGS 的 `id` 值遵循 RFC 7540 §11.3。

运行时 `POST /api/config` 接受 `tls_preset`、`custom_hello`、`client_ip` 和 `user_agent`。更改仅对新连接生效。

# CAVEATS

这是一个解密的中间人代理。客户端必须信任生成的 CA，且未经授权拦截流量可能违反法律和服务条款。客户端到代理一端仅支持 HTTP/1.1 CONNECT；自定义 HTTP/2 指纹仅应用于代理到服务器一端。不支持分块请求体。不支持 QUIC 和 HTTP/3。代理改写的是 HTTP `User-Agent` 头部，而非 JavaScript 的 `navigator.userAgent`。某些应用使用证书固定，会拒绝 MITM 证书。管理 API 没有身份验证——请将其保留在 localhost 上。

# HISTORY

由 **ytkoka** 用 **Go** 编写，是围绕 uTLS TLS 指纹库构建的独立本地代理。`go build -o impersonate-proxy .` 生成的二进制文件名为 **impersonate-proxy**。采用 MIT 许可证。

# SEE ALSO

[mitmproxy](/man/mitmproxy)(1), [curl](/man/curl)(1), [curl-impersonate](/man/curl-impersonate)(1), [tinyproxy](/man/tinyproxy)(1)

# RESOURCES

```[Source code](https://github.com/ytkoka/impersonate-proxy)```

<!-- verified: 2026-08-18 -->
