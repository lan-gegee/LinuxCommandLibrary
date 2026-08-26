# TAGLINE

通过公共 URL 将你的 localhost 暴露给外界

# TLDR

**暴露本地端口**

```lt --port [3000]```

**使用自定义子域名**

```lt --port [3000] --subdomain [myapp]```

**指定本地主机**

```lt --port [3000] --local-host [192.168.1.10]```

**使用自定义服务器**

```lt --port [3000] --host [https://tunnel.example.com]```

**打印传入请求的信息**

```lt --port [3000] --print-requests```

**隧道连接到本地 HTTPS 服务器**

```lt --port [443] --local-https```

# SYNOPSIS

**lt** [_options_]

# PARAMETERS

**--port** _port_
> 要暴露的本地端口。

**-s**, **--subdomain** _name_
> 请求特定的子域名。默认是随机字符。

**-l**, **--local-host** _host_
> 代理到 localhost 以外的主机名。同时会覆盖 Host 头部。

**--host** _url_
> 隧道服务器的 URL。

**--local-https**
> 启用到本地 HTTPS 服务器的隧道。

**--local-cert** _path_
> 本地 HTTPS 服务器的证书 PEM 文件路径。

**--local-key** _path_
> 本地 HTTPS 服务器的证书密钥文件路径。

**--local-ca** _path_
> 自签名证书所需的证书颁发机构文件路径。

**--allow-invalid-cert**
> 禁用对本地 HTTPS 服务器的证书检查。

**--print-requests**
> 为每个传入请求打印基本信息（方法和路径）。

**-o**, **--open**
> 在默认浏览器中打开隧道 URL。

# DESCRIPTION

**localtunnel** 通过公共 URL 将你的 localhost 暴露给外界。它在公共服务器与你的本地机器之间创建隧道，可用于测试 webhook、分享进行中的工作或移动端测试。

无需注册账户；隧道是临时的，客户端断开连接后即关闭。

# PROGRAMMATIC USE

```javascript
const localtunnel = require('localtunnel');
const tunnel = await localtunnel({ port: 3000 });
console.log(tunnel.url);
```

# CAVEATS

URL 是临时的。子域名不保证可用。免费版有速率限制。不适合生产环境使用。需要 Node.js。

# HISTORY

localtunnel 由 **Roman Shtylman** 创建，是 ngrok 的简易替代品，提供无需注册的免费隧道服务。

# INSTALL

```brew: brew install localtunnel```

```nix: nix profile install nixpkgs#localtunnel```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ngrok](/man/ngrok)(1), [cloudflared](/man/cloudflared)(1), [ssh](/man/ssh)(1)
