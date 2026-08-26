# TAGLINE

具有 httpie 风格语法的 curl 前端

# TLDR

发送 **GET** 请求

```curlie [httpbin.org/get]```

发送带 JSON 数据的 **POST** 请求

```curlie post [httpbin.org/post] [name=john] [age:=25]```

发送带**查询参数**的 GET 请求

```curlie get [httpbin.org/get] [first_param==5] [second_param==true]```

发送带**自定义请求头**的请求

```curlie [httpbin.org/get] [X-Custom-Header:value]```

**上传文件**

```curlie post [httpbin.org/post] < [file.json]```

直接传递 **curl 选项**

```curlie -k https://[self-signed.example.com/api]```

# SYNOPSIS

**curlie** [_method_] _url_ [_items_...]

# DESCRIPTION

**curlie** 是 curl 的前端，结合了 httpie 的易用性与 curl 的强大功能。它把 httpie 风格的语法转换为 curl 命令，并以语法高亮的方式显示响应。

它使用与 httpie 相同的语法约定：= 表示字符串数据、:= 表示原始 JSON、== 表示查询参数、: 表示请求头。

# PARAMETERS

_method_
> HTTP 方法（GET、POST、PUT、DELETE 等）

_url_
> 目标 URL

**key=value**
> 字符串数据字段

**key:=value**
> 原始 JSON 数据字段

**key==value**
> 查询参数

**header:value**
> HTTP 请求头

**-v**
> 详细输出（显示请求头）。

**-I**, **--head**
> 发送 HEAD 请求。

支持所有 curl 选项并原样透传。

# CAVEATS

需要安装 curl。所有 curl 选项都可用，但会原样透传。Curlie 会自动格式化 JSON 输出。

# INSTALL

```pacman: sudo pacman -S curlie```

```apk: sudo apk add curlie```

```zypper: sudo zypper install curlie```

```brew: brew install curlie```

```nix: nix profile install nixpkgs#curlie```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[curl](/man/curl)(1), [httpie](/man/httpie)(1), [wget](/man/wget)(1)
