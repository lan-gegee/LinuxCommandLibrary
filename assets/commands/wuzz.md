# TAGLINE

交互式终端 HTTP 客户端

# TLDR

**启动交互式 HTTP 客户端**

```wuzz```

**启动时预填 URL**

```wuzz [https://api.example.com/users]```

**带自定义请求头启动**（cURL 兼容语法）

```wuzz -H "[Content-Type: application/json]" [https://api.example.com]```

**带 POST 数据启动**

```wuzz -X POST -d '{"key":"value"}' [https://api.example.com]```

**使用配置文件启动**

```wuzz -c [~/.wuzz/config.toml]```

# SYNOPSIS

**wuzz** [**-H** _header_]... [**-d** _data_] [**-X** _method_] [**-t** _msecs_] [**-c** _config_] [_URL_]

# PARAMETERS

**-H**, **--header** _HEADER_
> 设置请求头（可多次指定）。

**-d**, **--data** _DATA_
> 设置请求体数据。

**-X**, **--request** _METHOD_
> 设置 HTTP 方法（GET、POST、PUT 等）。

**-t**, **--timeout** _MSECS_
> 请求超时时间（毫秒）。

**-F**, **--form** _FIELD_
> 设置 multipart 表单数据。

**-c**, **--config** _FILE_
> 使用指定的配置文件。

**--insecure**
> 跳过 TLS 证书校验。

# DESCRIPTION

**wuzz** 是一个带终端用户界面的交互式 HTTP 调试工具。其命令行参数兼容 cURL 语法，因此可以从浏览器网络面板直接复制 "copy as cURL" 来发起请求。

界面分为多个面板：URL、方法、请求头、请求体、查询参数和响应。使用 **Tab**/**Shift+Tab** 在面板间导航，按 **Ctrl+R** 发送请求。**Ctrl+S** 保存响应，**Ctrl+E** 保存请求，**Ctrl+F** 加载已保存的请求，**Alt+H** 切换历史记录。**F2-F9** 可跳转到对应面板。

# CAVEATS

仅有终端 UI。配置文件采用 TOML 格式（Linux 上默认为 $XDG_CONFIG_HOME/wuzz/config.toml，其他平台为 ~/.wuzz/config.toml）。

# HISTORY

**wuzz** 由 **asciimoo** 创建，是一款交互式命令行 HTTP 调试工具，使用 Go 编写。项目地址：https://github.com/asciimoo/wuzz。

# INSTALL

```apt: sudo apt install wuzz```

```apk: sudo apk add wuzz```

```nix: nix profile install nixpkgs#wuzz```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[curl](/man/curl)(1), [httpie](/man/httpie)(1), [postman](/man/postman)(1)
