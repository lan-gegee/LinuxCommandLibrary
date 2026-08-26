# TAGLINE

LWP 套件提供的命令行 HTTP 客户端

# TLDR

**GET 请求**

```lwp-request [https://example.com/]```

**带数据的 POST 请求**

```lwp-request -m POST -c 'application/json' -C '[{"key":"value"}]' [https://api.example.com/]```

**HEAD 请求**（仅响应头）

```lwp-request -m HEAD [https://example.com/]```

**显示响应头和内容**

```lwp-request -USed [https://example.com/]```

**跟随重定向**

```lwp-request -f [https://example.com/redirect]```

**使用指定方法**

```lwp-request -m [DELETE] [https://api.example.com/resource]```

**设置自定义请求头**

```lwp-request -H 'Authorization: Bearer [token]' [https://api.example.com/]```

**保存到文件**

```lwp-request [https://example.com/file] > [output]```

# SYNOPSIS

**lwp-request** [_-m method_] [_-f_] [_-H header_] [_-c content-type_] [_-C content_] [_options_] _url_

# PARAMETERS

**-m** _METHOD_
> HTTP 方法（GET、POST、HEAD、PUT、DELETE）。

**-f**
> 跟随重定向。

**-H** _HEADER_
> 添加自定义请求头。

**-c** _TYPE_
> 请求体的 Content-Type。

**-C** _CONTENT_
> 内容/请求体数据。

**-b** _URI_
> 相对 URL 的基准 URI。

**-o** _FORMAT_
> 输出格式。

**-d**
> 打印请求内容/请求体。

**-e**
> 打印响应头。

**-s**
> 打印响应状态。

**-S**
> 打印请求 URL。

**-U**
> 打印请求头。

**-t** _SECONDS_
> 超时时间。

**-a**
> 以文本模式处理内容。

# DESCRIPTION

**lwp-request** 是 LWP（Library for WWW in Perl）套件提供的命令行 HTTP 客户端。它发送 HTTP 请求并显示响应。

该工具还以 GET、POST 和 HEAD 命令的形式提供，它们是预设了方法的符号链接。这些快捷方式简化了常见操作。

输出选项控制打印的内容：请求详情（-U、-S、-d）和响应详情（-e、-s）。组合使用这些标志可以显示完整的请求事务，便于调试。

身份验证、Cookie 和代理设置来自环境变量或配置文件。它与 Perl LWP 生态系统集成。

对于简单的测试和脚本编写，除了 Perl 的 LWP 模块外，lwp-request 无需其他额外依赖即可提供 HTTP 访问能力。

# CAVEATS

需要 libwww-perl 软件包。功能不如 curl 或 httpie 丰富。错误处理较为简单。大文件下载可能较慢。

# HISTORY

**lwp-request** 是 **libwww-perl** 的一部分，由 **Gisle Aas** 自 **20 世纪 90 年代**起创建。LWP 成为 Perl 的标准 HTTP 库，而 lwp-request 则提供了对其功能的命令行访问。

# INSTALL

```pacman: sudo pacman -S perl-libwww```

```apk: sudo apk add perl-libwww```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[curl](/man/curl)(1), [wget](/man/wget)(1), [http](/man/http)(1), [httpie](/man/httpie)(1), [perl](/man/perl)(1)
