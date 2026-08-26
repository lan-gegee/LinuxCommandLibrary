# TAGLINE

面向本地开发的简易静态文件服务器

# TLDR

以默认端口**伺服**当前目录

```sfz```

**伺服**某个路径，使用指定端口

```sfz -p [8080] [path]```

**启用 CORS** / 地址绑定（见帮助）

```sfz --help```

# SYNOPSIS

**sfz** [*options*] [*path*]

# DESCRIPTION

**sfz**（**S**tatic **F**ile **Z**erver）是一个小型 Rust CLI，通过 HTTP 伺服一个目录——适合快速本地预览。注意：原作者已表示维护有限；长期项目请考虑 crates.io 上的替代品。

# PARAMETERS

*path*

> 要伺服的目录（默认：当前目录）。

**-p**, **--port** *port*

> 监听端口。

其他标志控制地址、CORS 和缓存头——见 **sfz --help**。

# CAVEATS

未针对公网暴露进行加固。项目维护状态有限。生产环境请优先选用 **caddy**/**nginx**。

# INSTALL

```nix: nix profile install nixpkgs#sfz```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[python](/man/python)(1), [caddy](/man/caddy)(1), [miniserve](/man/miniserve)(1)

# RESOURCES

```[Source code](https://github.com/weihanglo/sfz)```

<!-- verified: 2026-07-19 -->
