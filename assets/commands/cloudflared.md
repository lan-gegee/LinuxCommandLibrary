# TAGLINE

用于安全连接的 Cloudflare Tunnel 客户端

# TLDR

**登录 Cloudflare**

```cloudflared tunnel login```

**创建隧道**

```cloudflared tunnel create [tunnel-name]```

**列出隧道**

```cloudflared tunnel list```

**运行隧道**

```cloudflared tunnel run [tunnel-name]```

**将 DNS 路由到隧道**

```cloudflared tunnel route dns [tunnel-name] [hostname]```

**快速隧道（临时）**

```cloudflared tunnel --url http://localhost:[8080]```

**删除隧道**

```cloudflared tunnel delete [tunnel-name]```

# SYNOPSIS

**cloudflared** tunnel _command_ [_options_]
**cloudflared** access _command_ [_options_]

# DESCRIPTION

**cloudflared** 是 Cloudflare Tunnel 客户端，用于创建从你的源站服务器到 Cloudflare 全球网络的仅出站（outbound-only）安全连接。这消除了暴露公网 IP 或开放入站防火墙端口的必要，因为所有流量都经由 Cloudflare 边缘网络路由。

该工具支持对 HTTP、SSH、RDP 和任意 TCP 协议建立隧道。命名隧道提供持久化配置，而快速隧道则为开发和测试提供临时公共 URL。可以通过 YAML 配置文件中定义的主机名和路径规则来配置隧道的流量路由。

cloudflared 还提供 Cloudflare Access 集成，可在用户访问源站之前对其进行身份验证，并可以作为系统服务在生产部署中运行。

# TUNNEL COMMANDS

**login**
> 向 Cloudflare 进行身份验证

**create** _name_
> 创建新隧道

**run** _name_
> 启动隧道

**list**
> 列出所有隧道

**delete** _name_
> 移除隧道

**route** dns/ip
> 配置路由

**info** _name_
> 显示隧道详情

**cleanup**
> 删除失效连接

# PARAMETERS

**--url** _url_
> 本地服务 URL

**--hostname** _host_
> 公共主机名

**--config** _file_
> 配置文件路径

**--credentials-file** _file_
> 隧道凭据

**--origincert** _file_
> 源站证书路径

**--no-autoupdate**
> 禁用自动更新

# CONFIGURATION

**~/.cloudflared/config.yml**
> 主隧道配置，定义隧道 ID、凭据路径和 ingress 路由规则。

**~/.cloudflared/cert.pem**
> 在 `cloudflared tunnel login` 期间获取的源站证书，用于验证隧道创建。

# CAVEATS

隧道凭据按隧道隔离。快速隧道是临时的。有免费层可用。此前名为 Argo Tunnel。

# INSTALL

```pacman: sudo pacman -S cloudflared```

```zypper: sudo zypper install cloudflared```

```brew: brew install cloudflared```

```nix: nix profile install nixpkgs#cloudflared```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ngrok](/man/ngrok)(1), [ssh](/man/ssh)(1)

# RESOURCES

```[Source code](https://github.com/cloudflare/cloudflared)```

```[Documentation](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/)```

<!-- verified: 2026-06-22 -->
