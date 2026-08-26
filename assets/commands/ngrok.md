# TAGLINE

创建通往 localhost 的安全隧道

# TLDR

**暴露本地端口**

```ngrok http [8080]```

**使用自定义域名暴露**

```ngrok http --domain=[myapp.ngrok-free.app] [8080]```

**TCP 隧道**

```ngrok tcp [22]```

**从配置启动命名隧道**

```ngrok start [tunnel-name]```

**从配置启动所有隧道**

```ngrok start --all```

**设置身份验证令牌**

```ngrok config add-authtoken [token]```

**TLS 隧道**

```ngrok tls [443]```

**带基本认证暴露**

```ngrok http --basic-auth="[user]:[password]" [8080]```

**检查配置文件是否有效**

```ngrok config check```

**诊断连通性**

```ngrok diagnose```

# SYNOPSIS

**ngrok** [_command_] [_options_]

# PARAMETERS

**http** _PORT_
> 创建指向本地端口的 HTTP 隧道。

**tcp** _PORT_
> 创建 TCP 隧道。

**tls** _PORT_
> 创建 TLS 隧道（不终止 TLS）。

**start** _name_
> 从配置文件启动命名隧道。

**config** _SUBCOMMAND_
> 管理 ngrok 配置（add-authtoken、check、edit）。

**diagnose**
> 对 ngrok 服务运行连通性诊断。

**service** _action_
> 将 ngrok 作为系统服务管理（install、start、stop、restart、uninstall）。

**--domain** _NAME_
> 隧道端点的自定义域名。

**--region** _REGION_
> 隧道所在区域（us、eu、ap、au、sa、jp、in）。

**--log** _path_
> 将日志写入文件或 "stdout"/"stderr"。

**--basic-auth** _USER:PASSWORD_
> 为隧道添加 HTTP 基本认证。

**api** _SUBCOMMAND_
> 访问 ngrok API（例如列出隧道、管理保留域名）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ngrok** 建立从公共端点通向本地运行服务的安全隧道。它使本地服务器无需部署或配置防火墙就能通过公共 URL 在互联网上访问。

常见用例包括 webhook 开发、现场演示、移动后端测试以及远程访问本地服务。Web 检查界面（默认位于 localhost:4040）支持对流量的实时查看与重放。

# CAVEATS

免费版有连接数限制，URL 随机分配且重启后会变化。多数功能需要账号和 authtoken。在较新的版本中，--subdomain 标志已被 --domain 取代。

# HISTORY

ngrok 由 **Alan Shreve** 创建，用于为本地开发提供安全隧道。

# INSTALL

```nix: nix profile install nixpkgs#ngrok```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[localtunnel](/man/localtunnel)(1), [ssh](/man/ssh)(1), [cloudflared](/man/cloudflared)(1)
