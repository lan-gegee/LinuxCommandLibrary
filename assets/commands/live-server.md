# TAGLINE

带实时重载的开发服务器

# TLDR

**在当前目录启动服务器**

```live-server```

**服务指定目录**

```live-server [public/]```

**自定义端口**

```live-server --port=[8080]```

**打开指定文件**

```live-server --open=[index.html]```

**监视指定路径**

```live-server --watch=[src/,public/]```

**禁用浏览器自动打开**

```live-server --no-browser```

**服务 SPA**（回退到 index.html）

```live-server --entry-file=[index.html]```

**启用 HTTPS 和 CORS**

```live-server --https=[https-config.js] --cors```

# SYNOPSIS

**live-server** [_options_] [_directory_]

# PARAMETERS

_DIRECTORY_
> 要服务的目录（默认为当前目录）。

**--port=**_PORT_
> 服务器端口（默认：8080，或 PORT 环境变量）。

**--host=**_HOST_
> 绑定的主机地址（默认：0.0.0.0，或 IP 环境变量）。

**--open=**_PATH_
> 启动时在浏览器中打开的路径。

**--watch=**_PATHS_
> 要监视变更的逗号分隔路径列表。

**--ignore=**_PATHS_
> 不予监视的逗号分隔路径列表。

**--no-browser**
> 不自动启动浏览器。

**--browser=**_BROWSER_
> 指定要打开的浏览器。

**--no-css-inject**
> CSS 变更时重新加载整页，而不是实时注入。

**--entry-file=**_PATH_
> 请求缺失时的回退文件（对 SPA 很有用）。

**--mount=**_ROUTE:PATH_
> 将 URL 路由映射到目录。

**--proxy=**_ROUTE:URL_
> 将匹配路由的请求代理到指定 URL。

**--https=**_PATH_
> HTTPS 配置模块的路径。

**--cors**
> 为所有请求启用 CORS。

**--wait=**_MS_
> 重载前的延迟（毫秒）（默认：100）。

**-q**, **--quiet**
> 抑制日志输出。

**-V**, **--verbose**
> 详细日志记录。

**-v**, **--version**
> 显示版本。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**live-server** 是一个基于 Node.js 的轻量级 HTTP 服务器，专为前端开发设计，只要被服务目录中的文件发生变化，它就会自动重新加载浏览器。其工作原理是向 HTML 页面注入一个小脚本，该脚本与服务器建立 WebSocket 连接；一旦检测到文件系统修改，就触发页面刷新。

服务器无需任何配置即可上手，默认服务当前目录并自动在浏览器中打开根页面。你可以自定义端口、主机绑定、监视目录以及要打开的初始页面。由于它严格面向开发用途，不应在生产环境中使用。

# CAVEATS

需要 Node.js。仅供开发使用。不可用于生产环境。

# HISTORY

live-server 的创建目的是通过文件变更时自动刷新浏览器来简化前端开发。

# INSTALL

```nix: nix profile install nixpkgs#live-server```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[http-server](/man/http-server)(1), [serve](/man/serve)(1), [browser-sync](/man/browser-sync)(1), [nodemon](/man/nodemon)(1), [python](/man/python)(1)
