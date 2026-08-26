# TAGLINE

面向本地开发的静态文件服务器

# TLDR

**托管当前目录**

```serve```

**托管指定目录**

```serve [path/to/directory]```

**自定义端口**

```serve -p [8080]```

**监听所有网络接口**

```serve -l [0.0.0.0]```

**单页应用模式**

```serve -s [path/to/spa]```

**启用 CORS**

```serve -C```

# SYNOPSIS

**serve** [_-p port_] [_-l address_] [_-s_] [_options_] [_path_]

# PARAMETERS

**-p** _PORT_
> 端口号。

**-l** _ADDRESS_
> 监听地址。

**-s**
> 单页应用模式。

**-C**
> 启用 CORS。

**-n**
> 禁用复制到剪贴板。

**-d**
> 调试模式。

**--ssl-cert** _FILE_
> SSL 证书。

# DESCRIPTION

**serve** 是一款零配置的本地开发静态文件服务器，由 Vercel 开发。它通过 HTTP 提供目录内容服务，无需任何设置——只需在任意目录运行 **serve** 即可开始托管文件。

单页应用（SPA）模式会将所有路由重定向到 **index.html**，适合测试客户端路由。CORS 可通过单个标志启用，便于跨源 API 测试。HTTPS 通过 SSL 证书和密钥文件支持，方便在本地测试安全连接。

# CAVEATS

仅用于开发。不是生产级服务器。需要 Node.js。

# HISTORY

**serve** 由 **Vercel**（前身为 ZEIT）开发，是一款简单的本地开发静态文件服务器。

# INSTALL

```brew: brew install serve```

```nix: nix profile install nixpkgs#serve```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[http-server](/man/http-server)(1), [python](/man/python)(1), [nginx](/man/nginx)(1)
