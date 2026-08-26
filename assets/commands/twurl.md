# TAGLINE

面向 Twitter API 的 OAuth 版 curl

# TLDR

**授权账户**

```twurl authorize --consumer-key [key] --consumer-secret [secret]```

**GET 请求**

```twurl [/2/users/me]```

**POST 请求**

```twurl -X POST [/2/tweets] -d '{"text":"Hello"}'```

**列出账户**

```twurl accounts```

**设置默认账户**

```twurl set default [username]```

# SYNOPSIS

**twurl** [_-X method_] [_-d data_] [_options_] _endpoint_

# PARAMETERS

**-X** _METHOD_
> HTTP 方法。

**-d** _DATA_
> 请求体。

**-H** _HEADER_
> 自定义请求头。

**authorize**
> 设置 OAuth。

**accounts**
> 列出账户。

# DESCRIPTION

**twurl** 是专为 Twitter (X) API 设计的 OAuth 版 curl 替代工具。它自动处理 OAuth 认证握手，让开发者无需在每个请求中手动管理 token 即可发起经过认证的 API 请求。

首次使用 consumer key 和 secret 完成授权后，twurl 会存储凭据并为之后的所有请求自动签名。可以授权多个账户并在其间切换，方便以不同用户身份测试 API 调用。所有 Twitter API 端点都可以通过标准 HTTP 方法访问。

请求支持自定义请求头以及 POST 操作的 JSON 请求体。该工具在 Twitter 应用开发过程中进行 API 探索和调试时特别有用。

# CAVEATS

Twitter API 会变动。需要开发者账户。需要 Ruby 环境。

# HISTORY

**twurl** 由 **Twitter** 创建，作为面向 Twitter API 的 OAuth 版 curl 替代品。

# INSTALL

```nix: nix profile install nixpkgs#twurl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[curl](/man/curl)(1), [httpie](/man/httpie)(1)
