# TAGLINE

快速友好的 HTTP 客户端

# TLDR

**发送 GET 请求**

```xh [https://api.example.com/users]```

**发送带 JSON 数据的 POST 请求**

```xh POST [https://api.example.com/users] name=John email=john@example.com```

**发送带原始 JSON 的 POST 请求**

```xh POST [https://api.example.com/users] < [data.json]```

**设置自定义请求头**

```xh [https://api.example.com] Authorization:"Bearer [token]"```

**下载文件**

```xh --download [https://example.com/file.zip]```

**仅显示响应体**

```xh -b [https://api.example.com/users]```

**仅显示响应头**

```xh -h [https://api.example.com/users]```

**跟随重定向**

```xh --follow [https://example.com/redirect]```

# SYNOPSIS

**xh** [_method_] _URL_ [_items_] [_--json_] [_--download_] [_options_]

# PARAMETERS

**(method)**
> HTTP 方法：GET、POST、PUT、PATCH、DELETE、HEAD。

**-b**, **--body**
> 仅显示响应体。

**-h**, **--headers**
> 仅显示响应头。

**-d**, **--download**
> 下载文件。

**-c**, **--continue**
> 续传下载。

**-o** _FILE_, **--output** _FILE_
> 将响应保存到文件。

**-f**, **--form**
> 发送表单数据。

**-j**, **--json**
> 发送 JSON 数据（POST 的默认方式）。

**-F**, **--follow**
> 跟随重定向。

**--offline**
> 构造请求但不发送。

**-p** _WHAT_, **--print** _WHAT_
> 指定要打印的内容：H（请求头）、B（请求体）、h（响应头）、b（响应体）。

**-v**, **--verbose**
> 显示请求和响应。

**--timeout** _SECS_
> 请求超时时间。

**-A** _TYPE_, **--auth-type** _TYPE_
> 身份验证类型：basic、bearer、digest。

**-a** _USER:PASS_, **--auth** _USER:PASS_
> 身份验证凭据。

**--proxy** _PROTO:URL_
> 代理 URL。

**-I**, **--ignore-stdin**
> 忽略 stdin 数据。

# DESCRIPTION

**xh** 是一个友好的 HTTP 客户端，设计上是 HTTPie 更快的 Rust 重实现。它以语法高亮格式化输出，并提供直观的请求语法。

请求项使用特殊语法：key=value 表示 JSON/表单数据，key:=value 表示原始 JSON 值，key:value 表示请求头。这使得构造请求无需复杂的引号处理。

输出默认经过格式化并着色：JSON 会美化打印，请求头会高亮显示。-b 标志输出原始响应体，便于管道传给其他工具。

身份验证支持 basic、bearer 令牌和 digest。会话支持可在多个请求间持久保存 Cookie 和身份验证信息。

下载模式会将响应体保存到文件，支持中断后续传。下载过程中会显示进度。

离线模式会构造并显示请求但不发送，适用于调试或生成 curl 命令。

# CAVEATS

部分 HTTPie 功能尚未实现。对大型响应来说输出格式化会带来额外开销。会话处理与 HTTPie 不同。某些终端配色方案可能需要调整。

# HISTORY

**xh** 由 **ducaale** 于 **2020** 年前后创建，是 HTTPie 的 Rust 重实现。"xh" 这个名字是 HTTPie 中 h 的反转。它以性能和可移植性为目标编写，语法几乎完全一致，同时速度显著更快，并以单一二进制文件发布。

# INSTALL

```apt: sudo apt install xh```

```pacman: sudo pacman -S xh```

```apk: sudo apk add xh```

```zypper: sudo zypper install xh```

```brew: brew install xh```

```nix: nix profile install nixpkgs#xh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[curl](/man/curl)(1), [httpie](/man/httpie)(1), [wget](/man/wget)(1)
