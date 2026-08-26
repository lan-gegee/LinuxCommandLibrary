# TAGLINE

将本地服务器暴露为公网 URL 的隧道服务

# TLDR

**暴露本地服务器**

```expose share [http://localhost:8000]```

**使用自定义子域名**暴露

```expose share [http://localhost:3000] --subdomain [myapp]```

**使用基本认证**暴露

```expose share [http://localhost:8000] --auth [user:password]```

**设置**身份验证令牌

```expose token [your_auth_token]```

**使用自定义域名**暴露

```expose share [http://localhost:8000] --domain [example.com]```

# SYNOPSIS

**expose** _command_ [_options_]

# PARAMETERS

**share** _URL_
> 创建到本地服务器的隧道。

**token** _TOKEN_
> 设置身份验证令牌。

**--subdomain** _NAME_
> 使用自定义子域名。

**--auth** _USER:PASS_
> 为隧道添加 HTTP 基本认证。

**--domain** _DOMAIN_
> 使用自定义域名。

**--server** _SERVER_
> 连接到指定的 Expose 服务器。

**--server-host** _HOST_
> 指定服务器主机。

**--server-port** _PORT_
> 指定服务器端口。

**--dns** _DNS_
> 指定 DNS 服务器。

# DESCRIPTION

**Expose** 是一个用 PHP 编写的隧道服务，可创建安全的 HTTPS 隧道，把本地服务器暴露到互联网。它提供公共 URL，方便开发、测试和演示，无需部署。

自定义子域名和域名可以为演示或客户演示会生成易记的 URL。该工具是 ngrok 的开源替代品，由 BeyondCode 开发。

# CAVEATS

免费版对隧道时长和自定义子域名有限制。重连后隧道 URL 可能改变。不适合生产环境使用。使用托管服务需要身份验证令牌。

# HISTORY

Expose 是众多本地主机隧道服务之一，让开发者无需部署或配置防火墙即可共享本地开发服务器。

# SEE ALSO

[ngrok](/man/ngrok)(1), [localtunnel](/man/localtunnel)(1)
