# TAGLINE

带浏览器同步功能的实时重载开发服务器

# TLDR

在当前目录**启动服务器**

```browser-sync start --server```

从指定目录**启动服务器**

```browser-sync start --server [app]```

启动服务器并监视所有文件

```browser-sync start --server --files "**/*"```

监视特定文件类型

```browser-sync start --server --files "*.html, css/*.css"```

代理现有服务器

```browser-sync start --proxy "[localhost:8080]"```

创建配置文件

```browser-sync init```

发送重载事件

```browser-sync reload```

以自定义端口启动

```browser-sync start --server --port [3000]```

# SYNOPSIS

**browser-sync** _command_ [_options_]

# DESCRIPTION

**browser-sync** 是一款开发工具，可在构建网站时保持多个浏览器和设备同步。它监视文件变化，或注入 CSS/图片，或触发整页重载。

它的工作方式是在初始请求时向 body 标签后注入一个异步脚本标签，从而实现所有已连接浏览器的实时同步。

# COMMANDS

**start**
> 启动 Browsersync 服务器。

**init**
> 创建配置文件。

**reload**
> 通过 HTTP 协议发送重载事件。

# PARAMETERS

**--server** _directory_
> 从指定目录提供文件服务。

**--proxy** _url_
> 代理一个现有服务器。

**--files** _pattern_
> 要监视变化的文件模式。

**--port** _number_
> 使用的端口（默认：3000）。

**--https**
> 为本地开发启用 HTTPS。

**--no-open**
> 启动时不打开浏览器。

**--browser** _name_
> 要打开的浏览器（chrome、firefox 等）。

**--config** _file_
> 配置文件的路径。

**--reload-delay** _ms_
> 重载前的等待毫秒数。

# CONFIGURATION

**bs-config.js**
> 由 `browser-sync init` 生成的配置文件。定义服务器设置、文件监视模式、代理目标和中间件选项。

# CAVEATS

要求 HTML 文件中存在 body 标签。代理 HTTPS 目标时会自动推断使用 HTTPS。CSS 和图片变化通过注入完成而无需整页重载；其他变化则触发整页重载。

# INSTALL

```nix: nix profile install nixpkgs#browser-sync```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[live-server](/man/live-server)(1), [webpack](/man/webpack)(1), [gulp](/man/gulp)(1)

# RESOURCES

```[Source code](https://github.com/BrowserSync/browser-sync)```

```[Homepage](https://browsersync.io)```

<!-- verified: 2026-06-22 -->
