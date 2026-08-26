# TAGLINE

基于 HTTPS 的零配置远程终端共享

# TLDR

用二维码和加入链接**共享**当前终端会话

```reminal```

从另一个终端**连接**到远程会话

```reminal connect [session_id] [pin]```

显示本机上运行代理的**会话详情**

```reminal info```

对版本、中继可达性和 shell 设置**运行诊断**

```reminal doctor```

无需 sudo **安装**到 ~/.local/bin

```curl -fsSL https://raw.githubusercontent.com/harshalgajjar/Reminal/main/install.sh | sh```

# SYNOPSIS

**reminal** [_command_] [_options_]

# PARAMETERS

**connect** _id-or-url_ [_pin_]
> 连接到远程会话；省略 PIN 时会提示输入。

**info** [_--json_]
> 重新打印本地代理的会话 ID、PIN、URL 和二维码。

**qr**
> 只打印运行中代理的加入二维码。

**doctor**
> 检查版本、中继连通性、终端和 shell。

**upgrade**
> 下载并安装最新版本。

**relay** [_port_]
> 启动本地开发中继（默认端口 8080）。

**completion** _bash|zsh|fish_
> 将 shell 补全脚本输出到 stdout。

**version**
> 打印版本字符串。

**--connect** _id_ **--pin** _pin_
> 会话横幅中展示的另一种连接语法。

# DESCRIPTION

**reminal** 是一个 Go 编写的 CLI，通过加密的 WebSocket 中继共享你机器上的持久 PTY，让你可以从浏览器、手机或另一个 **reminal** 客户端重新连接，而无需开放入站端口或管理 SSH 密钥。

运行 **reminal** 会生成临时的会话 ID 和 PIN，显示二维码，并在查看者连接期间保持 shell 存活。中继只能看到密文；代理退出时会话凭据即失效。查看者可以使用中继 URL 上的内置 Web 终端，或使用 **reminal connect** 连接。

主机只发起出站 HTTPS/WSS 连接，因此可以在 NAT、酒店 Wi-Fi 以及其他阻止入站 SSH 的网络上工作。自动重连和回滚缓冲区重放有助于在短暂的网络中断后恢复。

# CAVEATS

reminal 依赖中继服务（默认为 Cloudflare Workers，也可自托管中继）。它**不是**任意远程管理的 SSH 直接替代品——它共享的是你已在本地启动的交互式 shell。根据项目的双许可条款，商业使用可能需要单独的许可证。

# HISTORY

**reminal** 由 **Harshal Gajjar** 创建并于 **2026 年**发布，是从移动设备和浏览器访问自己机器时零配置的 SSH 替代方案。

# SEE ALSO

[ssh](/man/ssh)(1), [tmux](/man/tmux)(1), [caffeinate](/man/caffeinate)(1)

# RESOURCES

```[Source code](https://github.com/harshalgajjar/Reminal)```

<!-- verified: 2026-07-11 -->
