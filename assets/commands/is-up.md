# TAGLINE

检查网站是否可访问

# TLDR

**检查网站是否在线**

```is-up [example.com]```

**检查多个网站**

```is-up [site1.com] [site2.com]```

**只获取退出码**

```is-up -q [example.com]```

# SYNOPSIS

**is-up** [_options_] _url_...

# PARAMETERS

_URL_
> 要检查的网站 URL 或域名。

**-q**, **--quiet**
> 安静模式，仅返回退出码。

**--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# DESCRIPTION

**is-up** 用于检查网站是否可访问。它通过发送 HTTP 请求来验证网站的可用性。

如果网站有响应则返回成功。适用于快速的可用性检查和脚本编写。

# CAVEATS

仅从你所在的位置检查。网络问题会影响结果。只是简单的 HTTP 检查。

# HISTORY

is-up 的创建目的是提供一个简单的命令行工具，用于快速检查网站是否可达并有响应。

# SEE ALSO

[curl](/man/curl)(1), [wget](/man/wget)(1), [ping](/man/ping)(8), [httpie](/man/http)(1)
