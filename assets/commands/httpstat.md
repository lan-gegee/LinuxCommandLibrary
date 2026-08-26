# TAGLINE

简单直观的 curl 统计可视化工具

# TLDR

**显示 URL 的 HTTP 请求统计**

```httpstat [https://example.com]```

**跟随重定向**

```httpstat -L [https://example.com]```

**发送 POST 请求**

```httpstat -X POST -d "[data]" [https://example.com/api]```

**使用自定义请求头**

```httpstat -H "Authorization: Bearer [token]" [https://example.com/api]```

# SYNOPSIS

**httpstat** [_curl_options_] _URL_

# DESCRIPTION

**httpstat** 以清晰美观的方式可视化 **curl** 的统计信息。它包装了 curl，捕获并显示 HTTP 请求各阶段花费的时间：**DNS 解析**、**TCP 连接**、**TLS 握手**、**服务器处理**和**内容传输**。这种分解有助于定位 Web 请求的性能瓶颈。

由于 httpstat 是 cURL 的一个包装器，你可以在 URL 之后传入任何 cURL 支持的选项（**-w**、**-D**、**-o**、**-s**、**-S** 除外，它们被内部使用）。

# CAVEATS

依赖系统上已安装的 curl。部分 curl 选项（-w、-D、-o、-s、-S）与 httpstat 的内部用法冲突，无法透传。Python 版本需要 Python 3。

# HISTORY

**httpstat** 由 **Reorx** 创建，使用 **Python** 编写，是一个没有任何依赖的单文件脚本。它迅速流行起来，并催生了 **Go**、**Rust** 和 **Nim** 语言的实现。**Dave Cheney** 编写的 Go 版本是一个独立二进制文件，不需要 curl。

# INSTALL

```brew: brew install httpstat```

```nix: nix profile install nixpkgs#httpstat```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[curl](/man/curl)(1), [wget](/man/wget)(1)
