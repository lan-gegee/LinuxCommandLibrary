# TAGLINE

面向 AI 智能体的临时端到端加密命令隧道

# TLDR

**在远程机器上安装并启动主机（host）会话**

```curl -fsSL https://opentunnel.sh | sh```

**开启一个可供智能体连接的主机会话**

```opentunnel create```

**通过隧道在主机上执行命令**

```opentunnel exec [command]```

**运行自托管的中继服务器**

```opentunnel relay --public-url [https://relay.example.com]```

# SYNOPSIS

**opentunnel** _create_ | _exec_ | _relay_ [_options_]

# DESCRIPTION

**opentunnel** 在 AI 智能体与远程机器之间创建一条临时的、端到端加密的命令隧道。它让智能体无需 SSH 密钥、常驻凭据或永久基础设施即可在另一台主机上运行 shell 命令：主机会话会打印一次性邀请码，智能体用它执行命令，而命令的 stdout、stderr 和退出码会返回，就像命令在本地运行一样。

连接经过端到端加密，因此在双方之间撮合的中继服务器只会看到密文。系统不保留任何持久状态：会话、邀请码和载荷从不存储，也不涉及账户或长期令牌；在主机上按下 **Ctrl+C** 即可立即撤销访问。中继服务器支持自托管，可在 Docker 中以极少的依赖运行。

opentunnel 通常通过一行 shell 脚本安装，该脚本下载经校验和验证的二进制文件并开启单个前台会话。**create** 子命令启动主机会话，**exec** 通过已建立的隧道运行命令，**relay** 则负责运行中继服务器。

# PARAMETERS

**create**

> 在本地（相对于智能体为远端）机器上启动主机会话并打印邀请码。

**exec** _command_

> 通过隧道在主机上执行命令，返回 stdout、stderr 和退出码。

**relay**

> 运行中继服务器，在智能体与主机之间撮合加密流量。

**--public-url** _URL_

> 设置中继服务器的公开 URL。非 localhost 来源必须使用 HTTPS。

# CAVEAT

opentunnel 会在会话存续期间授予智能体在主机上运行任意命令的能力，因此只应把邀请码分享给你信任的智能体，并在工作完成后立即结束会话。虽然中继只能看到密文，但运行自己的中继可以对流量撮合位置拥有最大程度的控制。

# SEE ALSO

[ssh](/man/ssh)(1), [ngrok](/man/ngrok)(1), [cloudflared](/man/cloudflared)(1), [socat](/man/socat)(1)

# RESOURCES

```[Source code](https://github.com/akoenig/opentunnel)```

```[Homepage](https://opentunnel.sh)```

<!-- verified: 2026-06-23 -->
