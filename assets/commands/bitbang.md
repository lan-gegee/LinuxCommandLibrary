# TAGLINE

无需账号的点对点远程 shell、文件传输与代理

# TLDR

**提供** shell、文件和代理服务（输出 URL、二维码、配对码）

```bitbang serve```

**仅提供 shell 服务**

```bitbang serve shell```

**提供一个文件共享**（加 **-upload** 允许上传）

```bitbang serve files [~/share]```

**提供 HTTP 代理**指向固定的本地目标

```bitbang serve proxy [localhost:8080]```

从另一台机器**连接**交互式 shell

```bitbang connect [url-or-code-or-name]```

以非交互方式**运行远程命令**

```bitbang connect [url] -- [tail -f /var/log/syslog]```

以 scp 风格**复制文件**

```bitbang cp [url]:[/var/log/app.log] [./app.log]```

**配对一次**并保存一个简短的设备名

```bitbang connect [482731] -name [nas1]```

# SYNOPSIS

**bitbang** _command_ [_options_] [_args_...]

# PARAMETERS

**serve** [_mode_] [_args_]
> 启动一个监听器。模式：不带参数的 **serve**（shell + 文件 + 代理）、**shell**、**files** [_PATH_]、**proxy** [_HOST:PORT_]。

**connect** _target_ [**--** _command_...]
> 以客户端身份连接。_target_ 可以是 URL、6 位配对码或已保存的设备名。带 **--** _command_ 时，运行该命令后退出。

**cp** _src_ _dst_
> 复制文件；两侧必须恰好有一侧是远端，形式为 `url:/path`。**-** 表示标准输入/标准输出。

**version**
> 显示版本（也可用 **--version**）。

**help**
> 用法说明（也可用 **-h**、**--help**）。

**-server** _HOST_
> 信令服务器主机名（默认 **bitba.ng**）。

**-pin** _PIN_
> 要求（serve 模式）或发送（connect/cp 模式）一个 PIN 码。

**-ephemeral**
> 一次性身份：每次 serve 运行都生成新的 URL。

**-nocode**
> 在监听端禁用口述的 6 位配对方式（URL 仍可使用）。

**-name** _NAME_
> 将新配对/连接的主机以 _NAME_ 保存（仅首次有效）。

**-relay**
> 一开始就优先使用 TURN 中继（ICE 仍会尝试直连路径）。

**-timeout** _DUR_
> 连接超时时间（默认 **30s**）。

**-v**
> 详细日志输出。

# DESCRIPTION

**bitbang** 是一个静态编译的 Go 单二进制文件，通过 WebRTC 提供远程访问：打开 shell、浏览/传输文件，以及把 HTTP 反向代理到远程机器的网络——无需端口转发、无需配置 VPN、无需注册账号。

在你想访问的那台机器上运行 **bitbang serve**。它会打印一个 URL（以及二维码/配对码）。任何人在浏览器中打开该 URL 即可获得你启用的能力；另一个 **bitbang** 客户端也可以用同一凭证进行 **connect** 或 **cp**。

公共的 **bitba.ng** 主机只负责信令中转。数据经端到端加密（DTLS）。ICE 成功后，流量尽可能点对点直达；否则由 TURN 中继转发，但中继只能看到密文。设备身份是位于 **~/.bitbang/** 下的 RSA 密钥；成功连接过的主机会记录在 **~/.bitbang/devices.json** 中以便使用短名称。

# CAVEATS

serve 的 URL 是一种**持有即得的凭证**——任何拿到它的人都能使用所提供的能力（包括完整 shell）。对于长期运行的主机，建议使用短时/一次性监听器并启用 **-pin**。官方安装目标是通过 GitHub releases 提供 Linux（`amd64`/`arm64`/`armv7`）版本；macOS/Windows 构建可能滞后。除非你自建 BitBang 信令服务，否则需要能访问信令（以及可能的 TURN）服务器的出站连接。

# CONFIGURATION

身份与已知主机存放在 **~/.bitbang/** 下（文件权限受限）。密钥对路径为 **~/.bitbang/**_program_**/identity.pem**（默认程序名为 **bitbang**）。已保存的设备：**~/.bitbang/devices.json**。

# HISTORY

**bitbang** 是 **richlegrand** 发起的开源 **BitBang** 项目的一部分，采用 MIT 许可证。其 CLI 大致对应 **sshd**/**ssh**/**scp**，只是用 WebRTC 取代了 TCP，强调零配置穿透 NAT，并支持浏览器客户端而无需在连接方安装软件。

# SEE ALSO

[ssh](/man/ssh)(1), [scp](/man/scp)(1), [ngrok](/man/ngrok)(1), [tailscale](/man/tailscale)(1)

# RESOURCES

```[Source code](https://github.com/richlegrand/bitbang-cli)```

```[Homepage](https://bitba.ng)```

```[Documentation](https://github.com/richlegrand/bitbang-cli#readme)```

<!-- verified: 2026-08-01 -->
