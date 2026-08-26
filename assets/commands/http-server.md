# TAGLINE

简单的静态文件服务器

# TLDR

**启动服务器**

```http-server```

**指定端口**

```http-server -p [8080]```

**指定目录**

```http-server [./public]```

**启用 CORS**

```http-server --cors```

**启用 gzip**

```http-server -g```

**SSL 服务器**

```http-server -S -C [cert.pem] -K [key.pem]```

# SYNOPSIS

**http-server** [_options_] [_path_]

# PARAMETERS

_PATH_
> 要提供服务的目录。

**-p**, **--port** _PORT_
> 端口号（默认 8080）。

**-a** _ADDRESS_
> 监听地址。

**-c** _SECONDS_
> 缓存时间。

**--cors**
> 启用 CORS 头。

**-g**, **--gzip**
> 启用 gzip。

**-S**, **--ssl**
> 启用 SSL。

**-C** _FILE_
> SSL 证书文件（默认：cert.pem）。

**-K** _FILE_
> SSL 密钥文件（默认：key.pem）。

**-o**
> 启动后打开浏览器。

**-P**, **--proxy** _URL_
> 将无法解析的请求代理到此 URL。

**--no-dotfiles**
> 不提供点文件（dotfiles）服务。

# DESCRIPTION

**http-server** 是一个面向 Node.js 的简单零配置静态文件服务器。它通过 HTTP 从某个目录提供文件，非常适合快速测试前端构建产物、在局域网内共享文件或预览静态站点。

可通过 `npm install -g http-server` 安装。默认在 8080 端口上提供当前目录的服务。

# CAVEATS

需要 Node.js 和 npm。不适用于生产环境——没有身份验证、速率限制或强化的安全机制。生产环境的静态文件服务请使用 nginx 或 CDN。

# HISTORY

http-server 是一个流行的 **npm** 软件包，用于在开发过程中快速提供静态文件服务。

# INSTALL

```brew: brew install http-server```

```nix: nix profile install nixpkgs#http-server```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[serve](/man/serve)(1), [python](/man/python)(1), [live-server](/man/live-server)(1)
