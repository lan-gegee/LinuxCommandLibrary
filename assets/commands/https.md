# TAGLINE

HTTPie 用于 HTTPS 请求的别名或变体

# TLDR

**通过 HTTPS 发送 GET 请求**

```https [https://api.example.com/users]```

**以 JSON 发送 POST**

```https POST [url] name=value```

**跳过证书校验**

```https --verify no [url]```

**自定义请求头**

```https [url] Authorization:"Bearer token"```

**下载文件**

```https --download [url]```

# SYNOPSIS

**https** [_options_] [_method_] _url_ [_data_]

# PARAMETERS

_METHOD_
> HTTP 方法（GET、POST、PUT、DELETE 等）。若省略，则根据是否存在数据进行推断。

_URL_
> 请求 URL。未给出协议时默认使用 **https://**。

_DATA_
> 请求项：`key=value` 表示 JSON/表单字段，`key:value` 表示请求头，`key==value` 表示查询参数，`key@file` 表示文件上传。

**-j**, **--json**
> 将数据项编码为 JSON 对象（默认）。

**-f**, **--form**
> 将数据项编码为 `multipart/form-data` 或 `application/x-www-form-urlencoded`。

**-o**, **--output** _FILE_
> 将输出写入文件而不是标准输出。

**-d**, **--download**
> 将响应体下载为文件，类似支持断点续传的 wget。

**-v**, **--verbose**
> 同时打印完整的请求和响应。

**-p**, **--print** _FLAGS_
> 控制打印内容：`H`/`B` 对应请求头/请求体，`h`/`b` 对应响应头/响应体。

**-a**, **--auth** _USER[:PASS]_
> 基本认证或摘要认证凭据。

**--session** _NAME_
> 创建或复用命名会话，在多个请求之间持久化 cookie 和请求头。

**--verify** _yes|no|CA_BUNDLE_
> SSL 证书校验；设为 **no** 可跳过，或指向自定义 CA 证书包。

**--cert** _FILE_
> 客户端 SSL 证书。

**--cert-key** _FILE_
> 客户端证书对应的私钥文件（若未包含在 **--cert** 中）。

**--proxy** _PROTOCOL:URL_
> 为指定协议使用的代理。

**--follow**
> 跟随 HTTP 重定向（30x 响应）。

**--offline**
> 构造并打印请求而不通过网络发送。

**--help**
> 显示帮助信息。

# DESCRIPTION

**https** 是随 **HTTPie** 一起安装的配套可执行文件。它在功能上与 **http** 命令完全相同，只是默认 URL 协议为 **https://** 而非 **http://**，因此像 `https example.org` 这样只写主机名就会请求 `https://example.org`。所有其他行为、选项和输出格式均与 **http** 共享。

与整个 HTTPie 的风格一致，它提供彩色格式化输出、直观的 key=value/key:value 请求构造语法、默认的 JSON 支持，以及会话、下载和认证等特性。

# CAVEATS

它不是一个 shell 别名，而是 **httpie** Python 软件包附带的独立入口；安装 HTTPie 会同时安装 **http** 和 **https**。等同于运行 `http --default-scheme=https`。

# HISTORY

**https** 自早期版本起便随 **HTTPie** 一同提供。HTTPie 由 **Jakub Roztocil** 创建，旨在作为比 curl 更易用的命令行 HTTP/API 测试工具。

# INSTALL

```dnf: sudo dnf install httpie```

```pacman: sudo pacman -S httpie```

```apk: sudo apk add httpie```

```zypper: sudo zypper install httpie```

```brew: brew install httpie```

```nix: nix profile install nixpkgs#httpie```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[http](/man/http)(1), [curl](/man/curl)(1), [wget](/man/wget)(1)

# RESOURCES

```[Source code](https://github.com/httpie/cli)```

```[Homepage](https://httpie.io)```

```[Documentation](https://httpie.io/docs/cli)```

<!-- verified: 2026-07-19 -->
