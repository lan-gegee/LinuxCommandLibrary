# TAGLINE

使用 TUI 发送美观的 HTTP 和 API 请求

# TLDR

**启动 HTTP 请求 TUI**

```resto```

**发送 GET 请求**

```resto get [https://api.example.com/endpoint]```

**发送 POST 请求**

```resto post [https://api.example.com/endpoint]```

# SYNOPSIS

**resto** [_command_] [_options_] [_url_]

# DESCRIPTION

**resto** 是一个用于发送 HTTP 和 API 请求的 CLI 与 TUI 工具，输出经过格式化。它支持 GET、POST、PUT、PATCH 和 DELETE 方法、Basic Auth 和 Bearer Token 认证，以及用于编写请求体的编辑器模式。TUI 面板可通过 Ctrl+P 打开。

# HISTORY

**resto** 由 **abdfnx** 创建，使用 **Go** 编写。

# INSTALL

```aur: yay -S resto```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[curl](/man/curl)(1), [httpie](/man/httpie)(1), [posting](/man/posting)(1)
