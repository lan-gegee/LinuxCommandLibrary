# TAGLINE

对用户友好的 HTTP 客户端

# TLDR

**GET 请求**

```http [https://api.example.com/users]```

**以 JSON 发送 POST**

```http POST [url] name=value```

**以表单数据发送 POST**

```http --form POST [url] field=value```

**自定义请求头**

```http [url] Authorization:"Bearer [token]"```

**下载文件**

```http --download [url]```

**带认证的请求**

```http --auth [user]:[password] [url]```

**详细输出**

```http --verbose [url]```

**使用命名会话**

```http --session=[name] [url]```

# SYNOPSIS

**http** [_options_] [_method_] _url_ [_data_]

# PARAMETERS

_METHOD_
> HTTP 方法（GET、POST、PUT、DELETE）。

_URL_
> 请求 URL。

_DATA_
> 请求数据（键值对）。

**-d**, **--download**
> 下载文件。

**-f**, **--form**
> 表单编码数据。

**-j**, **--json**
> JSON 数据。

**-v**, **--verbose**
> 详细输出。

**-o**, **--output** _FILE_
> 输出文件。

**-a**, **--auth** _USER:PASS_
> 基本认证或摘要认证凭据。

**-A**, **--auth-type** _TYPE_
> 认证类型：basic、digest、bearer。

**--session** _NAME_
> 创建或复用命名会话，用于保存 cookie 和请求头。

**-p**, **--print** _FLAGS_
> 控制输出内容：H（请求头）、B（请求体）、h（响应头）、b（响应体）。

**--pretty** _STYLE_
> 输出格式化方式：all、colors、format、none。

**--verify** _CERT_
> SSL 证书校验。使用 **no** 可跳过。

**--proxy** _PROTOCOL:URL_
> 为请求使用代理。

**--follow**
> 跟随 HTTP 重定向。

**--help**
> 显示帮助信息。

# DESCRIPTION

**HTTPie**（http）是一个对用户友好的 HTTP 客户端。它为 API 交互提供直观的语法、彩色输出和 JSON 支持。

该工具简化了从命令行发起 HTTP 请求的过程。它会自动格式化响应，并支持会话和认证。

# CAVEATS

Python 软件包。语法与 curl 不同。默认使用 JSON。

# HISTORY

HTTPie 由 **Jakub Roztocil** 创建，旨在作为比 curl 更易用的 API 测试工具。

# INSTALL

```dnf: sudo dnf install httpie```

```pacman: sudo pacman -S httpie```

```apk: sudo apk add httpie```

```zypper: sudo zypper install httpie```

```brew: brew install httpie```

```nix: nix profile install nixpkgs#httpie```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[curl](/man/curl)(1), [wget](/man/wget)(1), [https](/man/https)(1), [xh](/man/xh)(1), [curlie](/man/curlie)(1)
