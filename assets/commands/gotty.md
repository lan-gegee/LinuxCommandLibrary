# TAGLINE

将终端共享为 Web 应用

# TLDR

**将终端共享为网页**

```gotty [command]```

**以写入权限共享**

```gotty -w [bash]```

**指定端口**

```gotty -p [8080] [command]```

**启用身份验证**

```gotty -c [user:pass] [command]```

**随机 URL 路径**

```gotty --random-url [command]```

# SYNOPSIS

**gotty** [_options_] _command_

# PARAMETERS

_COMMAND_
> 要共享的命令。

**-w**, **--permit-write**
> 允许来自浏览器的输入。

**-p** _PORT_, **--port** _PORT_
> 服务器端口。

**-c** _CRED_, **--credential** _CRED_
> 基本认证凭据，格式为 user:pass。

**-r**, **--random-url**
> 在 URL 路径中添加随机字符串。

**-t**, **--tls**
> 启用 TLS/SSL。

**--tls-crt** _PATH_
> TLS 证书文件路径。

**--tls-key** _PATH_
> TLS 密钥文件路径。

**--reconnect**
> 允许客户端在连接关闭后重新连接。

**--once**
> 在第一个客户端断开后退出。

**--config** _FILE_
> 配置文件路径。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gotty** 将一个终端命令共享为可通过浏览器访问的 Web 应用。它运行一个命令并通过 HTTP 暴露该命令，从而实现远程终端访问、日志查看和协作调试。

支持身份验证和 TLS 以实现安全的部署。**-w** 标志允许浏览器用户向正在运行的命令发送输入。

# CONFIGURATION

**~/.gotty**
> 用于保存默认设置（如端口、TLS 证书和凭据选项）的配置文件。

# CAVEATS

使用 -w 标志时存在安全风险。生产环境中请启用身份验证。注意防火墙相关事项。

# HISTORY

gotty 由 **Iwasaki Yudai** 创建，用于通过 Web 浏览器共享终端会话。

# INSTALL

```nix: nix profile install nixpkgs#gotty```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ttyd](/man/ttyd)(1), [tmux](/man/tmux)(1)
