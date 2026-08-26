# TAGLINE

使用 Twitter/X API 凭据授权 twurl

# TLDR

**授权**：使用 consumer key 与 secret（交互式 PIN 流程）

```twurl authorize --consumer-key [key] --consumer-secret [secret]```

**授权**：使用短选项名

```twurl authorize -c [key] -s [secret]```

**生成 bearer token**（仅应用认证）

```twurl authorize --bearer --consumer-key [key] --consumer-secret [secret]```

**对非默认主机授权**

```twurl authorize -c [key] -s [secret] -H [api.twitter.com]```

**为指定用户名授权**

```twurl authorize -c [key] -s [secret] -u [username]```

# SYNOPSIS

**twurl authorize** [**-c**|**--consumer-key** _key_] [**-s**|**--consumer-secret** _secret_] [_options_]

# PARAMETERS

**-c**, **--consumer-key** _key_
> OAuth consumer（API）key。必需。若省略该值，twurl 会交互式提示输入。

**-s**, **--consumer-secret** _secret_
> OAuth consumer（API）secret。必需。若省略该值，twurl 会交互式提示输入。

**-u**, **--username** _username_
> 被授权账户的用户名。

**--bearer**
> 使用仅应用认证，存储 bearer token 而不是用户 access token。

**-H**, **--host** _host_
> 授权过程中使用的 API 主机（默认：**api.twitter.com**）。若带协议前缀会被去除。

**-a**, **--access-token** _token_
> 提供已有的 access token，而不是执行完整的 PIN 握手流程。

**-S**, **--token-secret** _secret_
> 提供已有的 token secret，与 **--access-token** 搭配使用。

**-P**, **--proxy** _proxy_
> 授权请求所用的 HTTP 代理。

**-t**, **--trace**
> 跟踪握手过程中的请求与响应流量。

# DESCRIPTION

**twurl authorize** 是使用 **twurl** 的第一步。twurl 是 Twitter 面向 X (Twitter) API 的支持 OAuth 的 curl 替代工具。该命令将 consumer key 和 secret 注册到某个用户账户（或生成仅应用的 bearer token），然后保存生成的凭据，使后续的 **twurl** 请求自动完成签名。

对于用户上下文的 OAuth，该工具会打印一个授权 URL。在浏览器中打开它、登录 X，然后把返回的 PIN 码输入回终端。成功后凭据会写入 **~/.twurlrc**，如果此前没有默认配置文件，该配置将成为默认项。

使用 **--bearer** 时，**twurl authorize** 会获取并存储用于仅应用调用的 bearer token。后续请求可以传入 **--bearer**（可选 **-c**），在没有用户上下文的情况下使用该 token。

可以随时间授权多个账户和 consumer key。用 **twurl accounts** 列出它们，用 **twurl set default** 切换当前生效的配置。

# CAVEATS

需要开发者账户以及来自 X 开发者门户的应用凭据。授权流程需要交互式输入 PIN 码（或预先提供 token）。X API 的产品层级和端点访问权限会随时间变化；授权成功并不保证你的应用能访问所有端点。必须安装 Ruby 和 **twurl** gem。

# HISTORY

**twurl** 由 Twitter（现 X）创建，作为其 HTTP API 的开发辅助工具。**authorize** 子命令一直都是将 OAuth 凭据存入 **~/.twurlrc** 的入口。

# INSTALL

```nix: nix profile install nixpkgs#twurl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[twurl](/man/twurl)(1), [twurl-accounts](/man/twurl-accounts)(1), [curl](/man/curl)(1), [httpie](/man/httpie)(1)

# RESOURCES

```[Source code](https://github.com/twitter/twurl)```

```[Documentation](https://github.com/twitter/twurl#getting-started)```

<!-- verified: 2026-07-17 -->
