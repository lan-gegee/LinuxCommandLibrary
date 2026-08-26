# TAGLINE

用于检查和模拟 HTTP 请求的交互式 Web 服务器

# TLDR

**在默认端口上启动 httplab**

```httplab```

**在指定端口上启动**

```httplab -p [8080]```

**以初始响应状态码和响应体启动**

```httplab -s [200] -b "[Hello, World]"```

**以初始响应延迟启动**

```httplab -d [500]```

**启用 CORS**

```httplab --cors```

**指定自定义配置路径**

```httplab -c [path/to/.httplab]```

# SYNOPSIS

**httplab** [_options_]

# PARAMETERS

**-p**, **--port** _port_
> 要绑定的端口（默认：10080）。

**-s**, **--status** _code_
> 初始响应状态码（默认：200）。

**-b**, **--body** _string_
> 初始响应体（默认："Hello, World"）。

**-d**, **--delay** _ms_
> 初始响应延迟（毫秒）。

**-H**, **--headers** _strings_
> 初始响应头（默认：X-Server:HTTPLab）。

**-a**, **--auto-update**
> 字段变化时自动更新响应（默认：true）。

**--cors**
> 启用 CORS。

**--cors-display**
> 显示 CORS 请求（默认：true）。

**-c**, **--config** _path_
> 自定义配置路径。

**-v**, **--version**
> 打印版本信息。

# DESCRIPTION

**httplab** 是一个交互式 Web 服务器，让你可以通过终端 UI 实时检查传入的 HTTP 请求并伪造响应。它会运行一个本地 HTTP 服务器，显示每个请求的方法、路径、请求头和请求体，同时允许你以交互方式自定义响应的状态码、请求头和响应体。

预定义的响应可以保存到 **.httplab** 配置文件中，之后再加载使用。该工具适合 API 开发、webhook 测试以及调试 HTTP 客户端行为。

# CAVEATS

仅为开发和测试设计；不适合生产环境。默认端口为 10080，可能与其他服务冲突。

# HISTORY

**httplab** 由 **Gustavo Chaín**（qustavo）创建，使用 **Go** 编写。它的设计目标是为开发者提供一种快速检查和模拟 HTTP 交互的方式，无需配置完整的 mock 服务器。

# INSTALL

```nix: nix profile install nixpkgs#httplab```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[curl](/man/curl)(1), [nc](/man/nc)(1), [httpie](/man/httpie)(1)
