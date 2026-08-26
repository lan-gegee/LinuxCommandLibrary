# TAGLINE

对用户友好的命令行 HTTP 客户端

# TLDR

**简单的 GET 请求**

```http [https://api.example.com/users]```

**以 JSON 发送 POST**

```http POST [https://api.example.com/users] name=John age:=30```

**发送表单数据 POST**

```http -f POST [url] name=John email=john@example.com```

**添加自定义请求头**

```http [url] Authorization:"Bearer [token]"```

**下载文件**

```http --download [https://example.com/file.zip]```

**带认证的请求**

```http -a [user:password] [url]```

**跟随重定向**

```http --follow [url]```

**显示详细的请求和响应**

```http --verbose [url]```

**只显示响应头**

```http --headers [url]```

# SYNOPSIS

**http** [_options_] [_method_] _url_ [_items_...]

# PARAMETERS

_method_
> HTTP 方法（GET、POST、PUT、DELETE 等）。

**--json**, **-j**
> JSON 数据（默认）。

**--form**, **-f**
> 表单数据。

**--headers**, **-h**
> 只打印请求头。

**--body**, **-b**
> 只打印响应体。

**--download**, **-d**
> 下载文件。

**--follow**, **-F**
> 跟随重定向。

**--auth**, **-a** _user:pass_
> 基本认证。

**--auth-type**, **-A** _type_
> 认证类型：basic、digest、bearer。

**--verbose**, **-v**
> 打印完整的 HTTP 交互（请求和响应）。

**--print**, **-p** _what_
> 选择性打印：H（请求头）、B（请求体）、h（响应头）、b（响应体）、m（元数据）。

**--verify** _verify_
> SSL 证书校验。设为 "no" 可跳过。

**--timeout** _seconds_
> 连接超时时间（秒）（默认：30）。

**--proxy** _protocol:url_
> 设置代理（例如 http:http://proxy:8080）。

**--check-status**
> 遇到 HTTP 3xx/4xx/5xx 状态码时以错误状态退出。

**--output**, **-o** _file_
> 将响应体保存到文件。

**--session** _name_
> 命名会话，用于持久化 cookie/认证信息/请求头。

**--pretty** _mode_
> 输出格式化方式：all、colors、format、none。

**--offline**
> 离线构造请求而不发送。

# ITEM TYPES

```
key=value       String data (request body)
key:=value      Raw JSON value (request body)
key==value      URL query parameter
Header:value    HTTP header
@file           File upload (multipart)
key@file        File upload with field name
```

# DESCRIPTION

**HTTPie** 是一款对用户友好的命令行 HTTP 客户端。它提供直观的语法、彩色输出和合理的默认值，适合 API 测试与调试。

# CAVEATS

需要 Python。语法与 curl 不同。较大的响应着色渲染可能较慢。命令是 `http`（或 `https`），而不是 `httpie`。

# HISTORY

HTTPie 由 **Jakub Roztočil** 于 **2012 年**创建，旨在作为比 curl 更易用的 HTTP API 交互工具。

# INSTALL

```dnf: sudo dnf install httpie```

```pacman: sudo pacman -S httpie```

```apk: sudo apk add httpie```

```zypper: sudo zypper install httpie```

```brew: brew install httpie```

```nix: nix profile install nixpkgs#httpie```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[curl](/man/curl)(1), [wget](/man/wget)(1), [xh](/man/xh)(1)
