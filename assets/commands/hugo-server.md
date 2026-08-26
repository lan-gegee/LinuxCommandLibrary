# TAGLINE

启动支持实时重载的本地开发服务器

# TLDR

**启动开发服务器**

```hugo server```

**包含草稿内容**

```hugo server -D```

**在自定义端口上启动**

```hugo server -p [8080]```

**绑定到所有网卡**（可从网络中的其他设备访问）

```hugo server --bind 0.0.0.0```

**禁用实时重载**

```hugo server --disableLiveReload```

**在浏览器中自动导航到变更的内容**

```hugo server --navigateToChanged```

**以指定的 base URL 构建并提供服务**

```hugo server --baseURL [http://example.com]```

# SYNOPSIS

**hugo server** [_options_]

# PARAMETERS

**-D**, **--buildDrafts**
> 包含草稿内容。

**-E**, **--buildExpired**
> 包含过期内容。

**-F**, **--buildFuture**
> 包含发布日期在未来的内容。

**-p**, **--port** _PORT_
> 服务器端口（默认：1313）。

**--bind** _ADDR_
> 监听地址（默认：127.0.0.1）。

**-b**, **--baseURL** _URL_
> 站点根路径的主机名和路径。

**--disableLiveReload**
> 禁用浏览器的自动实时刷新。

**--navigateToChanged**
> 实时重载时导航到发生变化的文件对应的页面。

**--poll** _DURATION_
> 以该周期轮询来检测文件变化（例如 700ms）。

**-w**, **--watch**
> 监视变化并重新构建（默认：true）。

**--noHTTPCache**
> 阻止 HTTP 缓存。

**--renderStaticToDisk**
> 静态文件从磁盘提供，动态文件从内存提供。

**--help**
> 显示帮助信息。

# DESCRIPTION

**hugo server** 启动一个支持实时重载的本地开发服务器。它会监视文件变化并自动重建站点，然后通过注入的 JavaScript 通知已连接的浏览器刷新。

为了提高速度，服务器默认将内容渲染到内存中。它默认监听 **localhost:1313**，并自动启用监视/实时重载功能。

# CAVEATS

仅用于开发，不适合生产环境。**--bind 0.0.0.0** 选项会将服务器暴露在所有网络接口上。由于内容渲染到内存中，大型站点的内存占用可能相当可观。在文件系统事件不可靠的环境中（例如 Docker、网络挂载），请使用 **--poll**。

# HISTORY

hugo server 是 **Hugo** 内置的开发服务器。Hugo 是用 Go 编写的开源静态站点生成器。

# INSTALL

```apt: sudo apt install hugo```

```dnf: sudo dnf install hugo```

```pacman: sudo pacman -S hugo```

```apk: sudo apk add hugo```

```zypper: sudo zypper install hugo```

```brew: brew install hugo```

```nix: nix profile install nixpkgs#hugo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hugo](/man/hugo)(1), [live-server](/man/live-server)(1)
