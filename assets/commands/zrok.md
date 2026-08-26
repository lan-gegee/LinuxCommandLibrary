# TAGLINE

安全的隧道与共享平台

# TLDR

**公开共享本地 HTTP 服务**

```zrok share public localhost:[port]```

**以保留子域名共享**

```zrok reserve public localhost:[port] --unique-name [subdomain]```

**私密共享（需要 zrok access）**

```zrok share private localhost:[port]```

**访问私有共享**

```zrok access private [share_token]```

**复制文件到共享**

```zrok copy [file] [share_token]:[remote_path]```

# SYNOPSIS

**zrok** _command_ [_options_]

# SUBCOMMANDS

**enable**
> 启用 zrok 环境

**share** _mode_ _target_
> 共享本地资源

**reserve** _mode_ _target_
> 创建保留的共享

**release** _share_
> 释放保留的共享

**access** _mode_ _share_
> 访问共享资源

**copy**
> 向共享复制文件或从共享复制文件

**status**
> 显示环境状态

**disable**
> 禁用 zrok 环境

# 参数（share）

**public**
> 公开可访问的共享

**private**
> 仅凭令牌访问的共享

**--backend-mode** _mode_
> 后端类型（proxy、web、files）

**--unique-name** _name_
> 保留特定的子域名

**--headless**
> 不使用终端 UI 运行

# DESCRIPTION

**zrok** 是构建在 OpenZiti 之上的新一代共享平台，为 HTTP 服务、文件和任意 TCP/UDP 流量提供安全隧道。

公开共享会生成指向本地服务的互联网可访问 URL。私有共享则需要访问令牌，流量经由加密的 Ziti 叠加网络传输，提供零信任安全。

zrok 可以共享：
- HTTP/HTTPS 服务（Web 应用、API）
- 静态文件（文件服务器模式）
- 原始 TCP/UDP 端点

与简单的隧道不同，zrok 的私有共享绝不会把流量暴露给公共互联网——所有流量都留在零信任叠加网络内部。

# CAVEATS

公开共享会把你的本地服务暴露到互联网上。请确保有适当的身份验证/安全措施。

免费套餐有用量限制。重度使用可能需要付费账户或自行部署基础设施。

保留名称会持久存在，但共享不会——重启之后必须重新运行 share 命令。

需要 zrok 账户。运行 **zrok invite** 即可开始使用。

# INSTALL

```brew: brew install zrok```

```nix: nix profile install nixpkgs#zrok```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ngrok](/man/ngrok)(1), [cloudflared](/man/cloudflared)(1), [tailscale](/man/tailscale)(8)
