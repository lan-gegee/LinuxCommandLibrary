# TAGLINE

OAuth2 命令行客户端

# TLDR

**获取访问令牌**

```oauth2c [client_id] [client_secret] --token-url [url]```

**授权码流程**

```oauth2c --auth-url [url] --token-url [url] --redirect-uri [uri]```

**客户端凭据流程**

```oauth2c [client_id] [client_secret] --token-url [url] --grant-type client_credentials```

**带作用域请求**

```oauth2c [client_id] [client_secret] --token-url [url] --scope "[scope1 scope2]"```

# SYNOPSIS

**oauth2c** [_options_]

# PARAMETERS

**--auth-url** _URL_
> 授权端点。

**--token-url** _URL_
> 令牌端点。

**--redirect-uri** _URI_
> 重定向 URI。

**--grant-type** _TYPE_
> OAuth2 授权类型。

**--scope** _SCOPES_
> 请求的作用域。

**--help**
> 显示帮助信息。

# DESCRIPTION

**oauth2c** 是一款 OAuth2 命令行客户端，可使用多种 OAuth2 授权类型获取访问令牌。它支持授权码、客户端凭据、设备码及其他标准流程。

该工具适用于测试受 OAuth2 保护的 API、调试认证流程以及脚本化获取令牌。在授权码流程中它会打开浏览器，并将获取到的令牌输出到 stdout。

# CAVEATS

需要有效的 OAuth2 客户端凭据（client ID 和 secret）。授权码流程会打开浏览器并启动本地服务器作为重定向 URI。令牌会打印到 stdout，须妥善保管。某些授权类型要求重定向 URI 预先在授权服务器上注册。

# HISTORY

**oauth2c** 由 **Cloudentity** 创建，旨在简化从命令行获取 OAuth2 令牌的过程，支持全部 OAuth2 授权类型。

# INSTALL

```brew: brew install oauth2c```

```nix: nix profile install nixpkgs#oauth2c```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[curl](/man/curl)(1), [httpie](/man/httpie)(1)
